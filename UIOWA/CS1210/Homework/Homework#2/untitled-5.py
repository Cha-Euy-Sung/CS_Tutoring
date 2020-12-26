def vowel(w,i):
    w = w.lower()
  
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


def vowel2(w,i):
    w = w.lower()
  
    if w[i] in 'aeio':
        return True
    elif w[i] in 'u' and w[i-1] in 'gq': 
        return True    
    elif w[i] in 'y' and i==int(0):
        return True
    else:
        return False

def syllables(w):
    syllables = []
    current_syllable = ""
    for i in range(0, len(w)):
        #print(current_syllable)
        if vowel(w, i):
          
            syllables.append(current_syllable)
         
            current_syllable = w[i]
            #print(current_syllable)
        else:
            current_syllable = current_syllable + w[i]
   
    syllables.append(current_syllable)
    return syllables