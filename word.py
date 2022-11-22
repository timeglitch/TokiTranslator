class Word:
    def __init__(s, input: dict) -> None:
        s.name = input["word"]
        s.data = dict()
        for i in input["meanings"]:
            s.data[i[0]] = i[1]

    def __str__(s) -> str:
        return s.name, s.data

word1 = Word({'word': 'a', 'meanings': [['interj', 'ah! ha! oh! ooh! aw! (emotion word)']]})
print(word1)