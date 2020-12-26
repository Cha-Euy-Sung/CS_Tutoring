def is_vowel (character):
    return(character in "aeiouAEIOU")
def is_alphabetic(character):
    code = ord(character)
    if ((97 <= code <= 122) or (65 <= code <= 90)):
        return(True)
    else:
        return(False)
def is_consonant(character):
    if is_alphabetic(character) and not(is_vowel(character)):
        return(True)
    else:
        return(False)
def generate_ubbi_dubbi(string):
## Ubbi Dubbi is a kid¡¯s language code in which "ub" is added before
## the first vowel
## in every sullable.
    output = ''
    found_vowel = False
    last = 'A'
    for character in string:
        if found_vowel:
            if (not is_vowel(character)):
                found_vowel = False
            elif (is_vowel(character) or ((character in 'yY') and (is_consonant(last)))):
                output=output+'ub'
                found_vowel=True
                output=output+character
                print('Output so far: ',output,'character: ', character, 'Last: ',last)
                last = character
        return(output)
