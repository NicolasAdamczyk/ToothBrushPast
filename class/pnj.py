import random

class PNJ:
    def __init__(self, nom):
        self.nom = nom
        
class Hostile(PNJ):
    def __init__(self, nom, level, vie, attaque, exp, argent, item):
        assert type(item) == list, "Le drop doit être une liste d'objets"
        PNJ.__init__(self, nom)
        self.level = int(level)
        self.vie = int(vie)
        self.attaque = int(attaque)
        
        self.exp = random.randint(exp-exp/10, exp+exp/10)
        self.argent = random.randint(argent-argent/10, argent+argent/10)
        self.item = random.choice(item)
    
class Friendly(PNJ):
    def __init__(self, nom, texte):
        PNJ.__init__(self, nom)
        self.texte = "texte"
    
    def chat(self):
        return(self.texte)