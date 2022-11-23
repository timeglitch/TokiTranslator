from tokenize import String
import string
import json
from Word import Word

#create wordlist from jprogr's dataset
dictionaryFile = open("toki_pona_dictionary.json")
jsonin = json.load(dictionaryFile)
wordList = dict()
for i in jsonin:
    print(i, type(i))
    tempword = Word(i)
    wordList[tempword.name] = tempword.data
#print(wordList)
 
def nounPhrase(words: list[Word]) -> String:
    if len(words) == 0: 
        return ""
    output = ""
    output = words[0]
    for i in range(1, len(words)):
        #check for /pi/ and /anu/ phrases
        if words[i].name == "pi":
            output = output + " " + words[i].get() + " " + adjPhrase(words[i:])
            break
        elif words[i].name == "anu":
            output = output + " " + words[i] + " " + nounPhrase()
            break
        output = output + " " + i.adj()
    return output
    
#process adjective phrase, this only works if all words in the input are content words, ie. there are no preps or seps
def adjPhrase(words: list[Word]) -> String:
    output = ""
    for i, match in enumerate(words):
        output = match.adj() + " " + output


#loop to allow continued string inputs
while False:  #TODO loop changed to false for testing
    tpString = input("Enter a Toki Pona sentence: ")
    #tpString = str(tpString).lower()
    output = ""
    toneModifiers = "" #use this string to keep track of tone modifiers

    if tpString == "end":
        break

    tpString = tpString.strip()
    tpString = tpString.translate(str.maketrans('', '', string.punctuation))

    if(not tpString.isalpha()):
        print("Not valid string")
    
    tpWords = tpString.split(" ")

    
    for modifier in [["a", "emphasis, "],["o", "command"]]:
        for w in tpWords:
            if w == modifier[0]:
                toneModifiers = toneModifiers + modifier[1]
    output = output + toneModifiers
    
    print(output)
            



    








