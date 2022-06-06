#In This program we will replace vowel word with a letter

def translate(word):
    translation = ""
    letter1 = ""
    letter2 = ""
    for letter in word:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation  
        
    

print(translate("elephant"))

