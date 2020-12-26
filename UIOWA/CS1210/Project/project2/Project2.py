from random import random, sample
import matplotlib.pyplot as plt

# Function to roll a weighted die. Returns True with probability p.
# else False.
def rolldie (p):
    '''Returns True with probability p.'''
    return(random() <= p)

# Our infection model is quite simple (see Carrat et al, 2008). People
# are exposed for E days (the incubation period), then infected for I
# additional days (the symptomatic period). Individuals are infectious
# as either E or I.  

# Recall status[] starts at E+I and counts down to REC=0.
#
# If I=7, E=2:
#   SUS REC                   I    E+I
#     |  |                    |     | 
#    -1  0  1  2  3  4  5  6  7  8  9
#          |===================||====|

# Disease model. Each disease has a name, transmissivity coefficient,
# recovery coefficient, and exposure and infection times.
class Disease():
    def __init__(self, name='influenza', t=0.95, E=2, I=7, r=0.0): 
        self.name=name
        self.t=t         # Transmissivity: how easy is it to pass on?
        self.E=E         # Length of exposure (in days)
        self.I=I         # Length of infection (in days)
        self.r=r         # Probability of lifelong immunity at recovery
        self.Q = 0
    
    # Quarantine function to enable quarantining of a disease
    def quarantine(self,Q):
        if Q <= self.I:
            self.Q = Q
        
# Agent model. Each agent has a susceptibility value, a vaccination
# state, and a counter that is used to model their current E, I, R or
# S status.
class Agent():
    def __init__(self, s=0.99,q=0.7,type=0,cp=[1.0]):
        self.s = s       # Susceptibility: how frail is my immune system?
        self.v = 1.0     # Vaccination state
        self.c = -1      # Current state S=-1, R=0, E,I > 0
        self.disease = None
        self.q = q
        # Quarantined boolean for state
        self.quarantined = False
        # Contact probability matrix
        self.cp = cp
        # Type specification for agent types
        self.type = type

    # Return True if infectious (i.e., in I or E state), False
    # otherwise.
    def state(self):
        '''Returns True if agent is infectious.'''
        return(self.c > 0 and not self.quarantined)

    # Set the agent's vaccination value to whatever value you give.
    def vaccinate(self, v):
        '''Models vaccination; v=0 denotes full immunity; v=1 denotes no immunity.'''
        self.v = v

    # Susceptible: if other is infected, roll the dice and update your
    # state. No real need to check other.state() here, since it is
    # checked prior to invoking the method, but it is included as per
    # spec. Note also that I add 1 to I+E, because my first step in
    # run() is to update state: your code may differ. Finally, it's
    # important to "remember" which disease you have so that you can
    # handle recovery and susceptibility correctly when the disease
    # finally runs its course.
    def infect(self, other, disease):
        '''Other tries to infects self with disease.'''
        if rolldie(self.cp[other.type]):
            if other.state() and self.c < 0 and rolldie(self.s*self.v*disease.t):
                self.c = disease.E + disease.I + 1
                self.disease = disease
                return(True)
        return(False)

    # Update the status of the agent. This involves decrementing your
    # internal counter if you are actively infected. When you get to
    # 0, you need to flip a (weighted) coin to decide if the agent
    # goes to state R (c=0) or back to state S (c=-1).
    def update(self):
        '''Daily status update.'''
        if self.c == 1:
            if not rolldie(self.disease.r):
                # Revert to susceptible, c=-1.
                self.c = -1
            else:
                # Lifelong immunity at recovery, c=0.
                self.c = 0
            # Clear your internal disease value.
            self.disease = None
        elif self.c > 1:
            #If making transition from I to E, check for possibility of quarantining
            if (self.c == self.disease.I + 1) and rolldie(self.q):
                self.quarantined = True
            #Check for end of quarantine
            if self.quarantined and (self.c == self.disease.I + 1 - self.disease.Q):
                self.quarantined = False
            # One day closer to recovery.
            self.c = self.c - 1
            return(True)
        return(False)

# Simulation model. Each simulation runs for at most a certain
# duration, D, expressed in terms of days.
class Simulation():
    def __init__(self, D=500,m=0.001,cpMatrix=[1.0]):
        self.steps = D		# Maximum number of timesteps
        self.agents = []      # List of agents in the simulation
        # Disctionary to keep track of known diseases for Simulation.cmd()
        self.d = {}
        # List of actual enacted diseases        
        self.diseases = []      # Diseases being simulated
        # list of disease events
        self.diseaseEvents = []     
        self.history = {}       # Dictionary of (E, I, R) tuples based on disease
        self.m = m          # Mixing parameter for this simulation
        # Agent matrix of contact probability
        self.cpMatrix = cpMatrix
        # List of events (for quarantine and campaigns)
        self.events = []

    # Populates the simulation with n agents and sets the mixing
    # parameter to m.
    def populate(self, n, agentType):
        '''Populate simulation with n agents, having mixing probability m.'''
        for i in range(n):
            self.join(Agent(0.99,0.7,agentType,self.cpMatrix[agentType]))

    # Add agent to current simulation.
    def join(self, agent):
        '''Add specified agent to current simulation.'''
        self.agents.append(agent)
        
    # Simply store a record of a vaccine campaign event
    def campaign(self, time, disease, coverage, v):
        self.events.append((time, disease, coverage, v))
    
    # Simply store a record of a quarantine event
    def quarantine(self, time, disease, Q):
        self.events.append((time,disease,Q))

    # Add disease to current simulation. For now, you can only model
    # one disease at a time.
    def introduce(self, diseaseEvent):
        '''Add specified disease to current simulation.'''
        self.diseaseEvents.append(diseaseEvent)

    # Seed the simulation with k agents having the specified disease.
    def seed(self, disease, k=1, time=0):
        '''Seed a certain number of agents with a particular disease.'''
        # Add the disease to the simulation.
        self.diseases.append(disease)
        self.history[disease] = []
        self.introduce((disease,k,time))

    # This is where the simulation actually happens. The run() method
    # performs at most self.steps iterations, where each iteration
    # updates the agents, counts how many are in E and I states,
    # checks if there is an early termination (i.e., no contagious
    # agents left) and then propagates the infection as per the mixing
    # parameter, m.
    def run(self):
        '''Run the simulation.'''
        for i in range(self.steps):
            for event in self.events:
                # Process quarantine
                if len(event) == 3:
                    time, disease, Q = event
                    if time == i:
                        for a in self.agents:
                            if a.disease == disease:
                                a.disease.quarantine(Q)
                # Process vaccination campaign
                elif len(event) == 4:
                    time, disease, coverage, v = event
                    if time == i:
                        for a in self.agents:
                            if a.disease != disease:
                                if rolldie(coverage):
                                    a.vaccinate(v)
            # Introduce a disease if the time is right
            for diseaseEvent in self.diseaseEvents:
                disease, k, time = diseaseEvent
                if time == i:
                    # I+E+1, because my first step in run() is to update
                    # state. Also, remember what disease you have.
                    for agent in sample(self.agents, k):
                        agent.c = disease.E + disease.I + 1
                        agent.disease = disease
            
            # Update each agent, counting how many are still exposed
            # or infected.  Finding infected agents first avoids
            # letting the infection infect a friend's friend in one
            # pass.
            # Change: keep track of both contagious AND susceptible
            contagious = []
            susceptible = []
            for a in self.agents:
                state = a.update()
                if state == True:
                    contagious.append(a)
                else:
                    susceptible.append(a)
            # Update the history with exposed and infected counts.
            # History is categorized based on disease for easy plotting
            for disease in self.diseases:
                self.history[disease].append((len([ a for a in contagious if (a.c > a.disease.I and a.disease == disease) ]), 
                                              len([ a for a in contagious if (a.c <= a.disease.I and a.disease == disease) ]),
                                              sum([ a.v for a in susceptible ])))
            # Exit early if there are no infected agents left.
            if len([ a for a in contagious if (a.c > a.disease.I) ]) == 0:
                if len([ a for a in contagious if (a.c <= a.disease.I) ]) == 0:
                    return(i)
            for a1 in contagious:
                # Let's see who a1 can infect. No need to check
                # a2.state() here, as a2.infect() will check it for
                # you. Note the use of the mixing parameter to
                # determine if a1 and a2 have been in contact with
                # each other today.
                for a2 in self.agents:
                    if rolldie(self.m):
                        a2.infect(a1, a1.disease)
        # Return the history of (E, I) tuples.
        return(self.history)

    # This method plots the pandemic curve from the self.history variable.
    # The plot is produced for a single disease type
    def plot(self, disease):
        '''Produce a pandemic curve for the simulation.'''
        plt.title('Disease: '+disease.name)
        plt.axis( [0, len(self.history[disease]), 0, len(self.agents)] )
        plt.xlabel('Days')
        plt.ylabel('N')
        plt.plot( [ i for i in range(len(self.history[disease])) ], [ e for (e, i, s) in self.history[disease] ], 'g-', label='Exposed' )
        plt.plot( [ i for i in range(len(self.history[disease])) ], [ i for (e, i, s) in self.history[disease] ], 'r-', label='Infected' )
        plt.plot( [ i for i in range(len(self.history[disease])) ], [ s for (e, i, s) in self.history[disease] ], 'b-', label='Susceptible' )
        plt.show()
        
    #Text command function which takes in a single line of text and enacts a command
    def cmd(self, line):
        inp = line.split()
        cmd = inp[0]
        if cmd == "add":
            n = eval(inp[1])
            agentType = eval(inp[2])
            self.populate(n,agentType)
        elif cmd == "disease":
            diseaseName = inp[1]
            t = eval(inp[2])
            E = eval(inp[3])
            I = eval(inp[4])
            r = eval(inp[5])
            disease = Disease(diseaseName,t,E,I,r)
            self.d[diseaseName] = disease
        elif cmd == "seed":
            time = eval(inp[1])
            diseaseName = inp[2]
            k = eval(inp[3])
            if diseaseName in self.d:
                self.seed(self.d[diseaseName],k,time)
        elif cmd == "quarantine":
            time = eval(inp[1])
            diseaseName = inp[2]
            Q = eval(inp[3])
            if diseaseName in self.d:
                self.quarantine(time,self.d[diseaseName],Q)
        elif cmd == "campaign":
            time = eval(inp[1])
            diseaseName = inp[2]
            coverage = eval(inp[3])
            v = eval(inp[4])
            if diseaseName in self.d:
                self.campaign(time,self.d[diseaseName],coverage,v)
        elif cmd == "run":
            self.run()
        elif cmd == "plot":
            diseaseName = inp[1]
            if diseaseName in self.d:
                self.plot(self.d[diseaseName])
    
    #config function which reads a full text file and feeds commands to Simulation.cmd()
    def config(self, filename):
        f = open(filename)
        lines = f.readlines()
        for line in lines:
            self.cmd(line)
        f.close()

#Simulate function which handles new and bye and delegates rest to Simulation.cmd()
def simulate():
    s = Simulation()
    while True:
        line = input("sim> ")
        inp =  line.split()
        cmd = inp[0]
        if cmd == "new":
            D = eval(inp[1])
            m = eval(inp[2])
            cpMatrix = eval(inp[3])
            s = Simulation(D,m,cpMatrix)
        elif cmd == "bye":
            break
        else:
            s.cmd(line)
 
#Demonstrate effective parsing of text file       
s = Simulation(500,0.001,[[1.0,0.5,0.5],[0.5,1.0,0.5],[0.5,0.5,1.0]])
s.config("config.txt")

