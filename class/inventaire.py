import pygame
import math

class Inventaire:
    def __init__(self, objet_liste, stockage_max):
        self.__objet_liste = objet_liste
        self.__stockage_max = stockage_max
        self.image = pygame.image.load('images/inventaire.png')
        self.ouvert = False

    def get_stockage_max(self):
        return(self.__stockage_max)

    def afficher_inventaire(self):
        return(self.__objet_liste)

    def detruire_objet(self, objet):
        if objet in self.__objet_liste:
            del objet

    def ajouter_objet(self,objet):
        if objet not in self.__objet_liste:
            self.__objet_liste.append(objet)
            
    def draw(self, screen):
        center_x=screen.get_width()/2
        center_y=screen.get_height()/2
            
        x_size = math.floor(screen.get_width()*0.7)
        y_size = math.floor(screen.get_height()*0.7)
        
        screen.blit(pygame.transform.scale(self.image, (x_size, y_size)), (center_x - x_size // 2, center_y - y_size // 2))