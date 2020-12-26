# CS1210 Homework 1, Puzzle 0
# Euysung Cha
# Section A07

# Puzzle : Write an expression that specifies a newtuple consisting of max copies of min followed by min copies of max.
L = [1, 3, 5, 4, 4, 6, 2, 3, 1, 1]

D = [min(L)]*int(max(L))+[max(L)]

print(D)



        

