# CS1210 Homework 1, Puzzle1
# Euysung Cha
# Section A07

# Puzzle : Write an expression that replaces the centermost element of L with that manycopies of 0.
#L = [1,2,3,4,5]
#L = [1,2,0,3]

L[:int(len(L)/2)]+([0]*L[int(len(L)/2)])+L[int(len(L)/2)+1:]

    
