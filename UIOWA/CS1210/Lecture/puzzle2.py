def puzzle2(S):
    L=S.split( )
    countA = [len(x) for x in L if "a" in x]
    return countA