# A Leader has a :
# name, organization, and title
# Want to be able
# to set and retrieve these data0


def plotDistribution(D, title="Digit Distribution", xaxis="digit", yaxis="percent"):
    
    if D['total']==0:
        print("Empty dictionary; no plotting")
        return 
    
    plt.title(title)
    plt.xlabe(xaxis)
    plt.xlabel(yaxis)
    
    Xs = [ x for x in range(10) ]
    Ys= [ d[x] / D['total'] for x in range(10) ]
    
    plt.bar ( Xs, Ys)
    
    plt.show()





class Leader():
    valid_titles = ["Boss", "Pope", "TA", "no title"]
    
    # it is locate at outside, so it will use for whole function in Leader class
    
    def __init__(self, name="no name", org = 'no org', title = 'no title', age = -1):
        self.name = name
        self.org = org
        if title in Leader.valid_titles:
            self.title = title
        else:
            self.title = "Invalid title"
        self.age = age
        
        
# L = Leader("EUY", "UIOWA", "Student", 26)
# L.name / L.age, L.title . . . etc
    def have_birthday(self):
        self.age = self.age +1
        print("Happy {}th Birthday to you, dear {}".format(self.age, self.name))

# L = Leader("EUY", "UIOWA", "Student", 26)
# L.have_birthday()
# Happy 27th Birthday to you, dear EUY

# .format -> in order


    def __repr__(self):
        return "<Leader obj : name {}; title {}>".format(self.name, self.title)


    def __int__(self):
        return self.age
    
    def __eq__(self, other):
        return (self.name == other.name, self.org)
    
    # Skipping init and everything
        
    # A is B (figure out share same address) , A == B (value is same or not) are different. 
    # "A = [1,2,3,] / B = A / C = A[:] / A is B (True), A == B (True), C is A (False), C == A (True)"        
    
class Animal():
    def __init__(self, can_fly=False, n_legs=4, has_tail=True):
        self.can_fly = can_fly
        self.n_legs = n_legs
        self.has_tail = has_tail
        # obfurscated by Eagle
        def speak(self):
            return "Bow Woof caw meow, I am a generic animal"
        # obfurscated by Eagle
        def fly(self):
            return "I cannot fly, for my heart is heavy."
        # Inherited by Eagle
        def run(self):
            return "I run quickly with my {} legs".format(self.n_legs)
        # Inherited by Eagle
        def balance(self):
            if self.has_tail:
                return "Balancing is easy with a prehensile tail."
            else:
                return "Keeping upright is hard!"
            
class Eagle(Animal):
    
    def __init__(self):
        self.can_fly=True
        self.n_legs = 2
        self.has_tail =False
        
    def fly(self):
        return "Whooooosh! America! I'm an eagle!"
    
    def speak(self):
        return "C'CAW!"