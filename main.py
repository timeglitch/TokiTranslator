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
grammar = cky.main("TPCNFgrammar.txt", False)
for i in jsonin:
    tempword = Word(i)
    wordList[tempword.name] = tempword


#wordlist is a dict with the word name as key and the word object as value





def recursiveText(parsed):
    out = ""
    for i in parsed:
        if i is String:
            if i in wordList:
                pass

    return out

    

#loop to allow continued string inputs
while True:
    tpString = input("Enter a Toki Pona sentence: ")
    tpString = str(tpString).lower()
    if (tpString == "exit"):
        break

    #parsedex is a a list of possible parses of the sentence.
    #Sentences may have multiple grammatical breakdowns and parsedex may contain duplicates
    parsedEx = cky.parse(grammar, tpString)

    parseTree = parsedEx[0] #only take the first parse, we only need one but may want to show more later.
    print(parseTree)
    out = recursiveText(parseTree)

    break #temporarily break out automatically for testing
            



    








