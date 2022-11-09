from tokenize import String


class Word:
    name = ""
    noun = []
    verb = []
    adj = []
    
    def __init__(self, name, noun: list[String], verb: list[String], adj: list[String]):
        self.name = name
        self.noun = noun
        self.verb = verb
        self.adj = adj
    
    
    
