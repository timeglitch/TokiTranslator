from cgi import test


from Word import Word
import main

"""testNoun = Word({"word": "akesi","meanings": [["n","non-cute animal, reptile, amphibian, dinosaur, monster"]]})
print(testNoun)
print(testNoun.noun())"""

input = main.stringToWords("mama sina")

print(input)

adjs = main.adjPhrase(input)
print(adjs)
