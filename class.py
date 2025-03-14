import sys
sys.path.append('class')

from personnage import *
from arme import *
from artefact import *
import time, os, csv, pickle, shutil
import numpy as np
        
def save(plr):
    newpath = '../data' 
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    stats = np.array([plr.nom, plr.weapontype, plr.vie, plr.attaque, plr.dc, plr.tc])
    np.savetxt('../data/data.csv', stats, fmt="%s", delimiter=",")
    return stats
    
def delsave():
    shutil.rmtree('../data')
    return "Donnees supprimes!"

enablesave = True

if enablesave == True:
    if os.path.exists("../data/data.csv"):
        donnees = []
        with open('../data/data.csv') as data:
            csv_reader = csv.reader(data, delimiter=';')
            for data in csv_reader:
                donnees.append(data[0])
        with open('../data/objects.pkl', 'rb') as objet:
            arme = pickle.load(objet)
            fleur = pickle.load(objet)
            plume = pickle.load(objet)
            sablier = pickle.load(objet)
            coupe = pickle.load(objet)
            embleme = pickle.load(objet)
            
        player = Personnage(donnees[0], donnees[1], donnees[2], donnees[3], donnees[4], donnees[5], arme, fleur, plume, sablier, coupe, embleme)
    else:
        nom=input("Choisissez le nom de votre personnage ")
        wtype=False
        while wtype not in weaponlist:
            wtype=input("Choisissez la classe de votre personnage: "+str(weaponlist))
        vie=0
        attaque=0
        dc=0
        tc=0
        ptype=False
        plist=["DPS", "Support DPS", "Healer"]
        while ptype not in plist:
            ptype=input("Choisissez le type de votre personnage: 'DPS' ou 'Support DPS' ou 'Healer'. \nIl est vivement conseille de prendre un DPS pour le moment.")
        if ptype == "DPS":
            vie=300
            attaque=60
            dc=50
            tc=50
        elif ptype == "Support DPS":
            vie=200
            attaque=45
            dc=70
            tc=20
        elif ptype == "Healer":
            vie=1000
            attaque=10
            dc=0
            tc=0
        arme = Arme(str(wtype)+" de base",wtype,1,30,"ATK",5,"L'arme de base qui vous sert pour debuter")
        fleur = Fleur("Fleur du debutant", 10, 3)
        plume = Plume("Plume du debutant", 10, 3)
        sablier = Sablier("Sablier du debutant", "ATK", 10, 3)
        coupe = Coupe("Coupe du debutant", "TC", 10, 3)
        embleme = Embleme("Embleme du debutant", "DC", 10, 3)
        player = Personnage(nom, wtype, vie, attaque, dc, tc, arme, fleur, plume, sablier, coupe, embleme)
        save(player)
        with open('../data/objects.pkl', 'wb') as objet:
            pickle.dump(arme, objet)
            pickle.dump(fleur, objet)
            pickle.dump(plume, objet)
            pickle.dump(sablier, objet)
            pickle.dump(coupe, objet)
            pickle.dump(embleme, objet)

def Combat(P1, P2):
    if P1.vie > 0 and P2.vie > 0:
        P1.Attack(P2)
        P2.Attack(P1)
        time.sleep(0.5)
    print(P1.vie, P2.vie)
    if P1.vie <= 0:
        return P2
    elif P2.vie <= 0:
        P1.__expup(5000)
        return P1
    else:
        return(Combat(P1,P2))