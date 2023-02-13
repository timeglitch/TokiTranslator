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



parsedEx = cky.parse(grammar, "ni li seme")
for item in parsedEx:
    print(item)

def recursiveText(parsed):
    out = ""
    for i in parsed:
        if i is String:
            if i in wordList:
                pass

    

#loop to allow continued string inputs
while False:  #TODO loop changed to false for testing
    tpString = input("Enter a Toki Pona sentence: ")
    #tpString = str(tpString).lower()
    output = ""
    #do work here
    
    print(output)
            



    








