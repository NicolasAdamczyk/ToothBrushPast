import random, math

class Personnage:
    """
    Un personnage est défini par:
    - son Nom
    - son Type d'arme
    - ses points de Vie
    - ses points d'Attaque
    - son pourcentage de Degats Critique
    - son pourcentage de Taux Critique
    - son Level
    - ses points d'Experience
    Un personnage peut s'equipper d'objets tel que:
    - une Arme
    - une Fleur de PV
    - une Plume d'Attaque
    - un Sablier de: Attaque ou PV
    - une Coupe de: Attaque, PV ou Degats Critique
    - un Embleme de: Attaque, PV, Degats Critique ou Taux Critique
    """
    def __init__(self, nom, weapontype, vie, attaque, dc, tc, arme, fleur, plume, sablier, coupe, embleme):
        self.nom = nom
        self.weapontype = weapontype
        self.viemax = int(vie)
        self.vie = int(vie)
        self.attaque = int(attaque)
        self.dc = int(dc)
        self.tc = int(tc)
        self.__level = 1
        self.__exp = 0
        
        self.arme = arme
        self.fleur = fleur
        self.plume = plume
        self.sablier = sablier
        self.coupe = coupe
        self.embleme = embleme
        
    def get_level(self):
        return print("Level: "+str(self.__level)+"\nExperience: "+str(self.__exp))
    
    def get(self):
        return print("Nom: "+self.nom+"\nType d'arme: "+self.weapontype+"\nVie: "+str(self.vie)+"\nAttaque: "+str(self.attaque)+"\nDegats Critique: "+str(self.dc)+"%"+"\nTaux Critique: "+str(self.tc)+"%")
    
    def __add__(self, valeur):
        self.__expup(valeur)
    
    def __sub__(self, valeur):
        self.vie -= valeur
    
    def __expup(self, newExp):
        cap = self.__level*1200
        maxlevel = 100
        
        self.__exp += newExp
        while self.__exp >= cap and self.__level < maxlevel:
            self.__exp -= cap
            self.__level+=1
        print(self.nom," a level up:",self.__level)
        print("Exp:",self.__exp)
        
    def equip(self, objet):
        if self.arme == objet or self.fleur == objet or self.plume == objet or self.coupe == objet or self.embleme == objet:
            return
        assert type(objet).__name__ == "Arme" or hasattr(objet, "atype"), "L'arme ou l'artefact n'est pas valide."
        
        
        if type(objet).__name__ == "Arme":
            self.arme = objet
        elif type(objet).__name__ == "Fleur":
            if self.fleur != "None":
                self.unequip(self.fleur)
            self.fleur = objet
        elif type(objet).__name__ == "Plume":
            self.plume = objet
        elif type(objet).__name__ == "Sablier":
            self.sablier = objet
        elif type(objet).__name__ == "Coupe":
            self.coupe = objet
        elif type(objet).__name__ == "Embleme":
            self.embleme = objet
        
        #Ajouter les PV
        if hasattr(objet, "substat") and objet.substat == "PV":
            self.vie += int(objet.valeur)
        
    def unequip(self, objet):
        assert self.arme == objet or self.fleur == objet or self.plume == objet or self.coupe == objet or self.embleme == objet, "L'arme ou l'artefact n'est pas equippe"
        if type(objet).__name__ == "Arme":
            self.arme = "None"
        elif type(objet).__name__ == "Fleur":
            self.fleur = "None"
        elif type(objet).__name__ == "Plume":
            self.plume = "None"
        elif type(objet).__name__ == "Sablier":
            self.sablier = "None"
        elif type(objet).__name__ == "Coupe":
            self.coupe = "None"
        elif type(objet).__name__ == "Embleme":
            self.embleme = "None"
        
        #Enleve les PV
        if hasattr(objet, "substat") and objet.substat == "PV":
            self.vie -= int(objet.valeur)
        
    def attack(self):
        tcrate = random.randint(0,100)
        
        attaque = self.attaque + self.arme.degats
        dc = self.dc
        tc = self.tc
        
        buffobj = [self.fleur, self.plume, self.sablier, self.coupe, self.embleme]
        
        if self.arme.substat == "ATK":
            attaque += self.arme.degats*(self.arme.pourcentage/100)
        elif self.arme.substat == "DC":
            dc += (self.arme.pourcentage/100)
        elif self.arme.substat == "TC":
            tc += (self.arme.pourcentage/100)
    
        for objet in buffobj:
            if objet.substat == "ATK":
                attaque += int(objet.valeur)
            elif objet.substat == "DC":
                dc += int(objet.valeur)
            elif objet.substat == "TC":
                tc += int(objet.valeur)
        
        if tc >= tcrate:
            print('coup crit!')
            attaque += attaque*(dc/100)
        
        return math.floor(attaque)