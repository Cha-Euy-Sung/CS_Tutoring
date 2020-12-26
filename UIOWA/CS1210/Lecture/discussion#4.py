#key = shuffle
# made 13 = player win
# card number and round should be same 
# doing that 13 times
# round and card number match = dealer win. 
# use numerical value
# import package

import string
string.punctuation
import math
math.cos(1)
import random
random.random()


random.randint(5,10) #important for homework

from random import randint

random.random() #not work

#but

randint(1,3) # it work

from random import randint as r_i
r_i(1,3)

import random as ran

ran.random()
ran.randint(1,5)

#important
import random
random.choice
#give random thing in list
L=[1,2,3,4,5,6,7]
L=[1,1,1,2,3,4,]
random.choice(L)


L=list(range(10,100,6))


random.shuffle(L)

#build the deck




# regarding suffling



#goolgle suffle knuth (?)

# deck = [ (1,'hearts'),(2,'hearts')....,diamonds, clubs, spades) (1~5)

# deck = tidy_deck()
# deck = made it in order, and he is going to be suffle

# i can do swap in my way.

#1. build deck in order = tiny deck
#2. start counting from backward =random int between range
#3. swap thing # switch last one with one of card in range(0,i-1)
#    and switch (i-1)card with one of the card in range (0,i-2)...keep going until everthing is shuffle
    # if card choose itself, it is fixed in that order(trun).     
    
    
#4. 



def scopint():
    x=1000
    y-5
    def schoping2():
        return x+3
    return y_scoping2()  #what is this


# swap the values L[i] and L[j]
def swap(L,i,j):
    L[i]=j
    return None

# L=[1,3,5,7,9]
# swap(L,2,99)
# L=[1,3,99,7,9]


def test(x):
    x=99
    return None

# test(x)

def swap1(L,i,j): #use this helper function
    temp = L[j]
    L[j] = L[i]
    L[i] = temp
    
# len(deck)
# from random import randint
# randint(0,19)
# swap(deck,17,19)
# randint(0,18)
#>>.14
# swap(deck,14,18)
# randint(0,18) # keep doing this 

# for c in deck


#card = deck.pop()
# you can cut card in this way (Len of list is getting smaller)

import random
def example1(n=10,verbose=False):
    if verbose:
        print("Hello there!")
    L=[]
    for i in range(n):
        new_num=random.randint(1,100)
        if verbose:
            print("you draw a random", new_num)
        L.append(new_num)
        
    if verbose:
        print("Loop ended, returning list of numbers")
    return L


