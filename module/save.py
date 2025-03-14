import sys
sys.path.append('../class')

import csv, os, pickle, shutil
import numpy as np
from personnage import *
from arme import *
from artefact import *

newpath = 'data'

def check_save():
    if os.path.exists(newpath):
        return True
    else:
        return False

def save(plr):
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    stats = np.array([plr.nom, plr.weapontype, plr.vie, plr.attaque, plr.dc, plr.tc])
    np.savetxt(newpath+'/data.csv', stats, fmt="%s", delimiter=",")
    return stats
    
def del_save():
    if os.path.exists(newpath+'/data.csv'):
        shutil.rmtree(newpath)
    else:
        return 'No data folder.'

def create_save(nom, weapontype, vie, attaque, dc, tc):
    arme = Arme(str(weapontype)+" de dev",weapontype,5,200,"ATK",20,"L'arme des developpeurs")
    fleur = Fleur("Fleur du dev", 2000, 5)
    plume = Plume("Plume du dev", 500, 5)
    sablier = Sablier("Sablier du dev", "ATK", 150, 5)
    coupe = Coupe("Coupe du dev", "TC", 30, 5)
    embleme = Embleme("Embleme du dev", "DC", 50, 5)
    player = Personnage(nom, weapontype, vie+fleur.valeur, attaque, dc, tc, arme, fleur, plume, sablier, coupe, embleme)
    save(player)
    with open(newpath+'/objects.pkl', 'wb') as objet:
        pickle.dump(arme, objet)
        pickle.dump(fleur, objet)
        pickle.dump(plume, objet)
        pickle.dump(sablier, objet)
        pickle.dump(coupe, objet)
        pickle.dump(embleme, objet)
    
    return player

def load_save():
    if os.path.exists(newpath+'/data.csv'):
        donnees = []
        with open(newpath+'/data.csv') as data:
            csv_reader = csv.reader(data, delimiter=';')
            for data in csv_reader:
                donnees.append(data[0])
        with open(newpath+'/objects.pkl', 'rb') as objet:
            arme = pickle.load(objet)
            fleur = pickle.load(objet)
            plume = pickle.load(objet)
            sablier = pickle.load(objet)
            coupe = pickle.load(objet)
            embleme = pickle.load(objet)
            
        return Personnage(donnees[0], donnees[1], donnees[2], donnees[3], donnees[4], donnees[5], arme, fleur, plume, sablier, coupe, embleme)