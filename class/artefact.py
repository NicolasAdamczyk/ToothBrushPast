class Artefact:
    def __init__(self, nom, valeur, rarete):
        assert type(rarete) == int and rarete >= 3 and rarete <= 5, "La rarete est un entier naturel compris entre 3 et 5"
        assert type(valeur) == int, "La valeur doit etre un entier naturel"
        self.nom = nom
        self.valeur = valeur
        self.rarete = rarete
        self.level = 1
        self.exp = 0
        
    def __add__(self, valeur):
        self.__proc(valeur)
        
    def __proc(self, newexp):
        cap = self.level*1200
        oldlevel = self.level
        maxproc = self.rarete*4
        
        if self.level < maxproc and self.exp <= cap:
            self.exp += newexp
            while self.exp >= cap:
                self.exp -= cap
                self.level+=1
            if self.level > oldlevel:
                print(self.nom," a level up:",self.level)
            return("Exp:"+str(self.exp))
        else:
            return("max")
        
    def stats(self):
        return self.nom
        
class Fleur(Artefact):
    def __init__(self, nom, valeur, rarete):
        Artefact.__init__(self, nom, valeur, rarete)
        self.substat = "PV"
        self.atype = "Fleur"

class Plume(Artefact):
    def __init__(self, nom, valeur, rarete):
        Artefact.__init__(self, nom, valeur, rarete)
        self.substat = "ATK"
        self.atype = "Plume"

class Sablier(Artefact):
    def __init__(self, nom, substat, valeur, rarete):
        Artefact.__init__(self, nom, valeur, rarete)
        self.substat = substat
        self.atype = "Sablier"
        
class Coupe(Artefact):
    def __init__(self, nom, substat, valeur, rarete):
        Artefact.__init__(self, nom, valeur, rarete)
        self.substat = substat
        self.atype = "Coupe"
        
class Embleme(Artefact):
    def __init__(self, nom, substat, valeur, rarete):
        Artefact.__init__(self, nom, valeur, rarete)
        self.substat = substat
        self.atype = "Embleme"