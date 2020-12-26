import random
import matplotlib.pyplot as plt

class Disease:
    def __init__(self, name='influenza', t=0.95, E=2, I=7, r=0.0):
        self.name = name
        self.t = t
        self.E = E
        self.I = I
        self.r = r
    
class Agent:
    def __init__(self,s=0.99):
        self.s = s
        self.v = 1.0
        self.stateCounter = -1
        self.r = None

    def vaccinate(self,v):
        self.v = v

    def infect(self,other,disease):
        #If self  is susceptible and other is exposed or infected:
        if self.stateCounter == -1 and other.stateCounter > 0:
            r = random.random()
            #With this likelihood:
            if r <= self.s * self.v * disease.t:
                #Put self in an exposed state
                self.stateCounter = disease.I + disease.E
                self.r = disease.r
                
    def state(self):
        return self.stateCounter > 0

    def update(self):
        #If self is exposed or infected:
        if self.stateCounter > 0:
            #Decrement state counter
            self.stateCounter -= 1
        #Else if self is in recovery and the recovery probability is specified:
        elif self.stateCounter == 0 and self.r != None:
            r = random.random()
            #With likelihood r
            #Place in susceptible state
            if r > self.r:
                self.stateCounter = -1       
        
        
class Simulation:
    def __init__(self,D=500):
        self.D = D
        self.agents = []
        self.disease = None
        self.m = 0.01
        self.data = []
    
    def join(self,agent):
        self.agents.append(agent)
    
    def introduce(self,disease):
        self.disease = disease
    
    def run(self):
        result = []
        if self.disease == None:
            return result
        #For each day
        for d in range(self.D):
            #Copy the list of agents
            agentsCopy = self.agents
            #Iterate through all copied agents
            for i in range(len(agentsCopy)):
                #Iterate through all original agents
                for j in range(len(self.agents)):
                    #If we are comparing two agents and the other agent is exposed or infected: 
                    if i != j and self.agents[j].stateCounter>0:
                        r = random.random()
                        #With likelihood m, infect the agent
                        if r <= self.m:
                            agentsCopy[i].infect(self.agents[j],self.disease)
            #Iterate through all of the original agents
            for i in range(len(self.agents)):
                #If the agent has changed from original to copied agent
                if self.agents[i] != agentsCopy[i]:
                    #Overwrote the original agent with the copied agent
                    self.agents[i] = agentsCopy[i]
                #Otherwise update the unchanged agents
                else:
                    self.agents[i].update()
            #Go through all of the agents and count the exposed & the infected
            exposedCount = 0
            infectedCount = 0
            for agent in self.agents:
                if agent.stateCounter > self.disease.I:
                    exposedCount += 1
                elif agent.stateCounter > 0:
                    infectedCount += 1
            result.append((exposedCount, infectedCount))
            #If no more infected remain, terminate the simulation
            if infectedCount == 0:
                break
        self.data = result
        return result

    def populate(self,n,m=0.01):
        self.m = m;
        #Generate random set of n agents
        for i in range(n):
            self.join(Agent(random.random()))

    def seed(self,disease,k=1):
        self.introduce(disease)
        #Produce list of indices
        indices = list(range(len(self.agents)))
        #Pop off k random indices and use them to uniquely choose agents to infect
        for i in range(k):
            randomIndex = indices.pop(random.randint(0,len(indices)-1))
            self.agents[randomIndex].stateCounter = self.disease.I
            self.agents[randomIndex].r = self.disease.r

    #Use pyplot to plot the exposed and the infected
    def plot(self):
        exposed = []
        infected = []
        #Comb through the data and collect counts of the exposed and infected per day
        for datum in self.data:
            exposed.append(datum[0])
            infected.append(datum[1])
        #Plot the data provided that it is a nonzero dataset
        if len(self.data)>0:
            plt.plot(range(len(self.data)),exposed,range(len(self.data)),infected)
            plt.ylabel('N')
            plt.xlabel('Days')            
            plt.title('Simulation')

#Test function
def test(d=1000,n=1000,r=1.0,m=0.001):
    S = Simulation()
    S.populate(n,m)
    S.seed(Disease(r=r),1)
    S.run()
    S.plot()

test()
#test(1000,1000,0.2,0.001)