from cgi import test


from Word import Word

testNoun = Word({"word": "akesi","meanings": [["n","non-cute animal, reptile, amphibian, dinosaur, monster"]]})

print(testNoun)

print(testNoun.noun())

for i in range(3,3):
    print(i)