# CS1210 Homework 1, Puzzle 3
# Euysung Cha
# Section A07

# Puzzle : start from a string S, and produce a list of integers that correspond to the number of vowels
#S = "coffEE Tea LemOnade"


([sum(l.lower() in'aeiou'for l in w)for w in S.split()])