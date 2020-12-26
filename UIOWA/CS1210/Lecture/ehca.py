# CS1210 Homework 3
# EUYSUNG CHA
# Section A07

import random


def predeck():
   # build deck in order using tuple
    deck = [ (1,'hearts'),(2,'hearts'),(3,'hearts'),(4,'hearts'),(5,'hearts'),(6,'hearts'),(7,'hearts'),(8,'hearts'),(9,'hearts'),(10,'hearts'),(11,'hearts'),(12,'hearts'),(13,'hearts'),(1,'diamonds'),(2,'diamonds'),(3,'diamonds'),(4,'diamonds'),(5,'diamonds'),(6,'diamonds'),(7,'diamonds'),(8,'diamonds'),(9,'diamonds'),(10,'diamonds'),(11,'diamonds'),(12,'diamonds'),(13,'diamonds'),(1,'clubs'),(2,'clubs'),(3,'clubs'),(4,'clubs'),(5,'clubs'),(6,'clubs'),(7,'clubs'),(8,'clubs'),(9,'clubs'),(10,'clubs'),(11,'clubs'),(12,'clubs'),(13,'clubs'),(1,'spades'),(2,'spades'),(3,'spades'),(4,'spades'),(5,'spades'),(6,'spades'),(7,'spades'),(8,'spades'),(9,'spades'),(10,'spades'),(11,'spades'),(12,'spades'),(13,'spades')]
    # Suffle and cutting deck by using randint
    for i in range(len(deck)-1,0,-1):
        # 'i' start from last value of deck (reverse)
        j=random.randint(0,i)
        temp = deck[j]
        deck[j] = deck[i]
        deck[i] = temp
    
    return deck


    
def treize(n,verbose=False):
    count=0
    used_deck=[]
    dealer_win=0
    total_game=n
    # decide how many times play the game ( n times)
    for times in range(0,n):
        # chage to new deck if exhausted.
        deck=predeck()
        for i in range(len(deck)):
            # reduce card to prevent duplicate
            used_deck.append(deck.pop())
            x,y=used_deck[i]
            count=count+1
            # give conditon for dealer win
            if x==count:
                print(str(count)+':','dealing',str(x) ,"of",str(y))
                print("Delaer wins!")
                count = 0
                n = n-1
                dealer_win=dealer_win+1
                if n==0:
                    # decide 'end  game' or keep going.
                    return (round(int(dealer_win)/int(total_game),2))
                
                    
            
             # give condition for dealer lose        
            elif count==13 and x != count:
                print(str(count)+':','dealing',str(x) ,"of",str(y))
                print("Dealer loses")
                count = 0
                n = n-1
                
                if n==0:
                    # decide 'end  game' or keep going.
                    return (round(int(dealer_win)/int(total_game),2))
                                
                
                
 
            else:
                print(str(count)+':','dealing',str(x) ,"of",str(y))
                # traking card   
                
       
                
            
import matplotlib.pyplot as plt

def simulate(n=10,m=10):
    plt.title('Dealer Win Percentage' )
    plt.xlabel('Replicate')
    plt.ylabel('Win %')
    plt.bar(range(n),[treize(m, False) for i in
    range (n)])
    plt.show( )
