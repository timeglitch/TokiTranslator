from tokenize import String
import string
import json
import word

words = {
    "li" :
}

#loop to allow continued string inputs
while True:
    tpString = input("Enter a Toki Pona sentence: ")
    #tpString = str(tpString).lower()

    if tpString == "end":
        break


    tpString = tpString.strip()
    tpString = tpString.translate(str.maketrans('', '', string.punctuation))

    if(not tpString.isalpha()):
        print("Not valid string")
    
    tpWords = tpString.split(" ")

    toneModifiers = "" #use this string to keep track of tone modifiers
    
    for modifier in [["a", "emphasis"],["o", "command"]]:
        for w in tpWords:
            if w == modifier[0]:
                toneModifiers = toneModifiers + modifier[1]
            



    








