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


#�߿��Ѱ�
#L=[1,2,3,4,5]
#L.copy()
#L2=L


#Puzzle0
# [0]*5 
# (1,2)*5
# (1)*5 (���ڷ� ����)
# tuple(1,)*5 (Ʃ���� , �� ������ �־����)
#tuple([1]*5) (�̷����ص���)

#Puzzle1
#������ �� ���� ������ �ɰ��� �ذ�
# [1,2,3,4,5,] = [1,2] [3] [ 4,5]
