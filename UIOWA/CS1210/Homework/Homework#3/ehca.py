# CS1210 Homework 3
# EUYSUNG CHA
# Section A07

import random


def predeck():
   # build deck in order using tuple
    deck = [ (1,'hearts'),(2,'hearts'),(3,'hearts'),(4,'hearts'),(5,'hearts'),(6,'hearts'),(7,'hearts'),(8,'hearts'),(9,'hearts'),(10,'hearts'),(11,'hearts'),(12,'hearts'),(13,'hearts'),(1,'diamonds'),(2,'diamonds'),(3,'diamonds'),(4,'diamonds'),(5,'diamonds'),(6,'diamonds'),(7,'diamonds'),(8,'diamonds'),(9,'diamonds'),(10,'diamonds'),(11,'diamonds'),(12,'diamonds'),(13,'diamonds'),(1,'clubs'),(2,'clubs'),(3,'clubs'),(4,'clubs'),(5,'clubs'),(6,'clubs'),(7,'clubs'),(8,'clubs'),(9,'clubs'),(10,'clubs'),(11,'clubs'),(12,'clubs'),(13,'clubs'),(1,'spades'),(2,'spades'),(3,'spades'),(4,'spades'),(5,'spades'),(6,'spades'),(7,'spades'),(8,'spades'),(9,'spades'),(10,'spades'),(11,'spades'),(12,'spades'),(13,'spades')]
    # Suffle deck by using randint
    for i in range(len(deck)-1,0,-1):
        # 'i' start from last value of deck (reverse)
        j=random.randint(0,i)
        temp = deck[j]
        deck[j] = deck[i]
        deck[i] = temp
    
    return deck

def treize(n,verbose=False):
    count=0
    deck = predeck()
    countt=1
    while (n>0):
            for i in range(len(deck)-1,0,-1):
                    if count==13:
                        break
                    x,y=deck[i]
                  
                    
                    
                    deck.pop(i)
                    print(str(countt)+':','dealing',str(x) ,"of",str(y))
                    count=count+1
                    countt=countt+1
                    if int(countt) == int(x):
                        print(str(countt)+':','dealing',str(x) ,"of",str(y))
                        break                    
                
                
                
            
            
            n=n-1
# how to break when count became 13 or count number equal to card number
# and how to make it continue
# how to change new deck 
# how to make my fucntion repeat n times 