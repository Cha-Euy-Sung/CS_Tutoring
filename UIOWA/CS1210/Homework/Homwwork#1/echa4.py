# CS1210 Homework 1, Puzzle 4
# Euysung Cha
# Section A07

# Puzzle : Write an expression that takes a string and returns a dictionary,where each key isalower case version of a word in the string and each value is the number of vowels in that word.
#S = "to be or not to be, that is the question"
 
{w.lower():sum(l.lower() in'aeiou'for l in w) for w in S.split()}