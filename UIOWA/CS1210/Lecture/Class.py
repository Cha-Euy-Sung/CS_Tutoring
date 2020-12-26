# Name
# Homework 1 for CS1210
# Section A07

#Problem -1:


# Given a list L of nonnegative int, write an expression that produces a tuple where the first elements divided by the smallest int, in is the sum of L divided by largest element

# Define a test list
L = [1,5,3,8,25]

# I need the sum, min, and max of L

sum(L)
min(L)
max(L)

# Use these to get the two numbers
first_item=sum(L)/min(L)
second_item=sum(L)/max(L)
# Combine those number into a tuple
(first_item, second_item)


#len("thisis").split.. 


#중요한거
#L=[1,2,3,4,5]
#L.copy()
#L2=L


#Puzzle0
# [0]*5 
# (1,2)*5
# (1)*5 (숫자로 계산됨)
# tuple(1,)*5 (튜플은 , 가 무조건 있어야함)
#tuple([1]*5) (이렇게해도됨)

#Puzzle1
#문제를 더 작은 문제로 쪼개서 해결
# [1,2,3,4,5,] = [1,2] [3] [ 4,5]
