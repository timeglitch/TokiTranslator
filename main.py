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
grammar = cky.main("testgrammar.txt", False) #TODO: check what grammar file you are using
for i in jsonin:
    tempword = Word(i)
    wordList[tempword.name] = tempword


#wordlist is a dict with the word name as key and the word object as value



def tupleisRoot(tup):
    if type(tup) != tuple:  return False
    if len(tup) != 2: 
        print("Error tuple doesnt have 2 elements")
        print(tup)
        return False
    return type(tup[1]) == str

def simpleRecursiveText(parsed):
    out = ""
    #print(parsed)
    #print(type(parsed))
    
    if type(parsed) is tuple:
        if tupleisRoot(parsed):
            out = out + " " + wordList[parsed[1]].get(parsed[0])
        else:
            out = simpleRecursiveText(parsed[0]) + " " + simpleRecursiveText(parsed[1])

        
    if type(parsed) is str and parsed in wordList:
        print("you shouldn't be able to get here, line 46 main")
        out = out + " " + wordList[parsed].name
    return out


    

#loop to allow continued string inputs
while True:
    #tpString = "suno la, mi wile toki e jan pona." 
    tpString = input("Enter a Toki Pona sentence: ") #TODO change this for testing

    tpString = str(tpString).lower()
    tpString = tpString.translate(str.maketrans('', '', string.punctuation))
    if (tpString == "exit"):
        break

    #parsedex is a a list of possible parses of the sentence.
    #Sentences may have multiple grammatical breakdowns and parsedex may contain duplicates
    parsedEx = cky.parse(grammar, tpString)

    for parseTree in parsedEx:
        try:

            #print(parseTree)
            out = simpleRecursiveText(parseTree)
            print(out)
        except Exception:
            pass
    #break #temporarily break out automatically for testingj