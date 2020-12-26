# CS1210 Homework 2
# Euysung Cha
# Section A07

#function1
def vowel(w,i):
    w = w.lower()
    if w[i] in 'aeio':
        return True
    elif w[i] in 'u' and w[i-1] not in 'gq': 
        return True    
    elif w[i] in 'y' and i!=int(0):
        return True
    elif w[i] in 'w' and i!=0 and vowel(w,i-1)==True:
        return True
    else:
        return False



#function2
def syllables(w):
        L = []
        S = w[0]
        for i in range(1,len(w)):

                if vowel(w,i)==vowel(w,i-1)==True and i-1 != 0:
                        S=w[i-1]+w[i]
                elif vowel(w,i)==True:
                        L.append(S)
                        S = w[i]
                else:
                        S = S + w[i]
        L.append(S)
        return L       
    
    
    
#function3
def encode(S,ub):
    S=S.split()
    L=[]
    for i in range(0,len(S)):
        L.append(str(ub).join(syllables(S[i])))
    return ' '.join(L)



#function4
def decode(S,ub):
    S=S.split()
    L=[]
    for i in range(0,len(S)):
        L.append(S[i].replace(str(ub),""))
    return ' '.join(L)

