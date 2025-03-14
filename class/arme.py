weaponlist = ["Sword", "Claymore", "Polearm", "Catalyst", "Bow"]
substatlist = ["PV", "ATK", "DC", "TC"]

class Arme:
    """
    Une arme est défini par:
    - son Nom
    - son Type d'arme
    - sa Rarete
    - ses Degats de base
    - sa Stat secondaire
    - les Pourcentages de la Stat secondaire
    - sa Description
    (La vitesse d'attaque et les dégats de base dépendront du type d'arme)
    """
    def __init__(self, nom, weapontype, rarete, degats, substat, pourcentage, description):
        vitessearme={"Sword":1,"Claymore":2,"Polearm":0.5,"Catalyst":0.5,"Bow":0.2}
        assert weapontype in weaponlist, ("Le type d'arme doit etre un des suivants:", str(weaponlist))
        assert substat in substatlist, ("La stat secondaire doit etre une des suivantes:", str(substatlist))
        assert type(rarete) == int and rarete >= 1 and rarete <= 5, "La rarete doit etre un nombre naturel compris entre 1 et 5"
        assert type(pourcentage) == int, "Le pourcentage doit etre un entier naturel"
        self.nom = nom
        self.weapontype = weapontype
        self.rarete = rarete
        self.degats = int(degats)
        self.substat = substat
        self.pourcentage = pourcentage
        self.description = description
        self.vitesse = vitessearme[weapontype]
        
    def get(self):
        return print("Nom: "+ self.nom+"\nType d'arme: "+ self.weapontype+"\nRarete: "+ str(self.rarete)+"*"+"\nDegats: "+ str(self.degats)+"\nStat secondaire: "+ self.substat+"\nPourcentage de Stat secondaire: "+ str(self.pourcentage)+"%"+"\nDescription: "+ self.description)