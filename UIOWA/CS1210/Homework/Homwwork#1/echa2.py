
# CS1210 Homework 1, Puzzle 2
# Euysung Cha
# Section A07

# Puzzle : Write a comprehension that returns a list containing the length, in characters, of all the words in the input sentence that contain the letter ¡¯a¡¯.
S = "this is a test" 


C=[len(x) for x in S.split( ) if "a" in x.lower()]

print(C)