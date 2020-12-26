def vowel(w,i):
    w = w.lower()
    print(w)
    if w[i] in 'aeio':
        return True
    elif w[i] in 'u' and w[i-1] in 'gq': 
        return True    
    elif w[i] in 'y' and i==int(0):
        return True
    elif w[i] in 'w' and i!=0 and vowel(w,i-1)==True:
        return True
    else:
        return False
