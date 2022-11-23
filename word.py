from tokenize import String


class Word:
    def __init__(s, input: dict) -> None:
        s.name = input["word"]
        s.data = dict()
        for i in input["meanings"]:
            s.data[i[0]] = i[1]

    def __str__(s) -> str:
        return s.name  +  str(s.data)

    def get(s, type: String = ""):
        if type == "noun":
            return s.noun()
        elif type == "mod" or type == "adj":
            return s.adj()
        elif type == "v":
            return s.verb()
        else:
            #edge case catcher
            return list(s.data.values)[0]    

    def noun(s):
        return s.data["n"]
    
    def adj(s):
        return s.data["mod"]

    def verb(s, transitive = False):
        if transitive:
            return s.data["vt"]
        else:
            return s.data["vi"]
    
    def isPrep(s):
        return "prep" in s.data or "sep" in s.data