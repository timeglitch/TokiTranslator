from tokenize import String

class Word:
    def __init__(s, input: dict) -> None:
        s.name = input["word"]
        s.data = dict()
        for i in input["meanings"]:
            s.data[i[0]] = i[1]

    def __str__(s) -> str:
        return s.name  +  str(s.data)

    def get(s, typeIn: String = ""):
        print(s)
        type = typeIn
        if typeIn[0:2] == "ZZ":
            type = typeIn[6:]

        dictionaryType = ""
        
        if type == "noun" or type == "N_NoMiSina" or type == "NP_NoMiSina" or type == "N" or type == "SubjPred":
            return s.noun()
        elif type == "Mod" or type == "Modifier":
            return s.mod()
        elif type == "V" or type == "Pred":
            return s.verb()
        elif type == "Prep":
            return s.prep()
        elif type == "Interjection":
            return s.inter()
        else:
            #edge case catcher
            return s.other(type)

    def noun(s):
        return s.data["n"].split(",")[0]
    
    def mod(s):
        return s.data["mod"].split(",")[0]

    def verb(s, transitive = True):
        if transitive and "vt" in s.data:
            return s.data["vt"].split(",")[0]
        else:
            return s.data["vi"].split(",")[0]
    
    def prep(s):
        return s.data["prep"]

    def inter(s):
        return s.data["interj"]

    def other(s, forError = ""):
        try:
            out = list(s.data.values())[0].split(",")[0]
        except Exception:
            out = "ERROR"
            print("Word failure with type: " + forError)
            print(str(s))

        return out
