def vowel(w,i):
    w = w.lower()
    #print(w)
    if w[i] in 'aeio':
        return True
    elif w[i] in 'u' and w[i-1] in 'gq': 
        return True    
    elif w[i] in 'y' and i==int(0):
        return True
    elif w[i] in 'w' and vowel(w,i-1)==True:
        return True
    else:
        return False
    
def cluster(w):
    clist = [] 
    cluster = "" 
    for i in range(0,len(w)):
        if vowel(w[i],i)!=True:
           if vowel(w,i+1)!=True
           cluster = w[i] + w[i+1]
        elif 