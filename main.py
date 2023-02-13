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





def simpleRecursiveText(parsed):
    out = ""
    #print(parsed)
    #print(type(parsed))
    if type(parsed) is tuple:
        out = simpleRecursiveText(parsed[0]) + " " + simpleRecursiveText(parsed[1])

        
    if type(parsed) is str and parsed in wordList:
        out = out + " " + str(wordList[parsed])
        return out
    return out


    

#loop to allow continued string inputs
while True:
    tpString = "tenpo pini la mi wile kama pona" #input("Enter a Toki Pona sentence: ") TODO change this for testing
    tpString = str(tpString).lower()
    if (tpString == "exit"):
        break

    #parsedex is a a list of possible parses of the sentence.
    #Sentences may have multiple grammatical breakdowns and parsedex may contain duplicates
    parsedEx = cky.parse(grammar, tpString)

    parseTree = parsedEx[0] #only take the first parse, we only need one but may want to show more later.
    print(parseTree)
    out = simpleRecursiveText(parseTree)
    print(out)
    break #temporarily break out automatically for testing
            



    








