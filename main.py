#based on zach tomaszewski's paper and code
#http://zach.tomaszewski.name/uh/ics661/source/

from tokenize import String
import string
import json
from Word import Word
import cky
punctuation = string.punctuation

#create wordlist from jprogr's dataset
dictionaryFile = open("toki_pona_dictionary.json")
jsonin = json.load(dictionaryFile)
wordList = dict() #create wordlist from jprogr's dataset
cky("TPCNFgrammar.txt")


for i in jsonin:
    tempword = Word(i)
    wordList[tempword.name] = tempword
#wordlist is a dict with the word name as key and the word object as value


def nounPhrase(words: list[Word]) -> string:
    #catch empty strings
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
        output = output + " " + words[i].adj()
    return output
    
#process adjective phrase, this only works if all words in the input are content words, ie. there are no preps or seps
def adjPhrase(words: list[Word]) -> string:
    output = ""
    for i, match in enumerate(words):
        output = match.adj() + " " + output
    return output

#changes slightly processed input string to list of words. Ignores punctuation
def stringToWords(input: string) -> list[Word]:
    tpString = input
    tpString = tpString.strip()
    tpString = tpString.translate(str.maketrans('', '', punctuation))

    print(tpString)
    if(not tpString.isalpha()):
        print("Not valid string")
    tpWords = tpString.split(" ")
    tpout = [None] * len(tpWords)
    for index, string in enumerate(tpWords):
        tpout[index] = wordList[string]
    return tpout



    

#loop to allow continued string inputs
while False:  #TODO loop changed to false for testing
    tpString = input("Enter a Toki Pona sentence: ")
    #tpString = str(tpString).lower()
    output = ""
    toneModifiers = "" #use this string to keep track of tone modifiers
    if tpString == "end":
        break

    for modifier in [["a", "emphasis, "],["o", "command"]]:
        for w in tpWords:
            if w == modifier[0]:
                toneModifiers = toneModifiers + modifier[1]
    output = output + toneModifiers
    
    print(output)
            



    








