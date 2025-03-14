import math

import pygame.draw
import pyscroll
import pytmx
import sys

# Ajouter les dossiers comme chemins
sys.path.append('class')
sys.path.append('module')
sys.path.append('map')

from pygame.locals import *
from inventaire import *
from stats import *
from player import *
from monstre import *
from personnage import *
from arme import *
from artefact import *
from save import *
from textbox import *

# Recuperer la resolution de lecran
# user32 = ctypes.windll.user32
# screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

# Horloge pygame
clock = pygame.time.Clock()


# Classe de la fenetre de jeu
class Game:
    def __init__(self):
        """
        init du jeu, après le
        """
        self.ouvert = True
        self.screen = pygame.display.set_mode((800, 600), RESIZABLE)
        pygame.display.set_caption("ToothPast")
        self.map = "maison"
        self.inventaire = False
        self.walls = []

        self.bvbg = pygame.image.load("images/vievide.png")
        self.bvbg.set_colorkey((255, 255, 255))
        self.bvfg = pygame.image.load("images/viefull.png")
        self.bvfg.set_colorkey((255, 255, 255))

        self.zombie1 = Monstre(0, 0, "zombie", 10, 5000, 200, 2000, 200, ["a", "b"],False)
        self.zombie2 = Monstre(0, 0, "zombie", 10, 5000, 200, 2000, 200, ["a", "b"],False)
        self.zombie3 = Monstre(0, 0, "zombie", 10, 5000, 200, 2000, 200, ["a", "b"],False)
        self.zombie4 = Monstre(0, 0, "zombie", 10, 5000, 200, 2000, 200, ["a", "b"],False)
        self.zombie5 = Monstre(0, 0, "zombie", 10, 5000, 200, 2000, 200, ["a", "b"],False)
        self.zombie6 = Monstre(0, 0, "zombie", 10, 5000, 200, 2000, 200, ["a", "b"],False)
        self.zombie7 = Monstre(0, 0, "zombie", 10, 5000, 200, 2000, 200, ["a", "b"],False)
        self.zombie8 = Monstre(0, 0, "zombie", 10, 5000, 200, 2000, 200, ["a", "b"],False)
        self.zombie9 = Monstre(0, 0, "zombie", 10, 5000, 200, 2000, 200, ["a", "b"],False)
        self.zombie10 = Monstre(0, 0, "zombie", 10, 5000, 200, 2000, 200, ["a", "b"],False)
        self.sorciere1 = Monstre(0, 0, "witch", 10, 3000, 400, 2000, 200, ["a", "b"],False)
        self.sorciere2 = Monstre(0, 0, "witch", 10, 3000, 400, 2000, 200, ["a", "b"],False)
        self.sorciere3 = Monstre(0, 0, "witch", 10, 10000, 750, 2000, 200, ["a", "b"],True)
        self.squelette1 = Monstre(0, 0, "skeleton", 10, 6000, 300, 2000, 200, ["a", "b"],False)
        self.squelette2 = Monstre(0, 0, "skeleton", 10, 6000, 300, 2000, 200, ["a", "b"],False)

        tmx_data = pytmx.util_pygame.load_pygame('map/carte.tmx')
        monstre_position = tmx_data.get_object_by_name("spawn2")
        self.zombie1.position = [monstre_position.x, monstre_position.y]

        tmx_data = pytmx.util_pygame.load_pygame('map/foret_maudite.tmx')
        monstre_position = tmx_data.get_object_by_name("spawn1")
        self.zombie2.position = [monstre_position.x, monstre_position.y]
        monstre_position = tmx_data.get_object_by_name("spawn2")
        self.zombie3.position = [monstre_position.x, monstre_position.y]
        monstre_position = tmx_data.get_object_by_name("spawn3")
        self.zombie4.position = [monstre_position.x, monstre_position.y]

        tmx_data = pytmx.util_pygame.load_pygame('map/catacombes1.tmx')
        monstre_position = tmx_data.get_object_by_name("spawn4")
        self.zombie5.position = [monstre_position.x, monstre_position.y]
        monstre_position = tmx_data.get_object_by_name("spawn5")
        self.zombie8.position = [monstre_position.x, monstre_position.y]
        monstre_position = tmx_data.get_object_by_name("spawn6")
        self.zombie9.position = [monstre_position.x, monstre_position.y]
        monstre_position = tmx_data.get_object_by_name("spawn7")
        self.zombie7.position = [monstre_position.x, monstre_position.y]
        monstre_position = tmx_data.get_object_by_name("spawn8")
        self.zombie6.position = [monstre_position.x, monstre_position.y]
        monstre_position = tmx_data.get_object_by_name("spawn9")
        self.zombie10.position = [monstre_position.x, monstre_position.y]

        monstre_position = tmx_data.get_object_by_name("spawn_sorciere1")
        self.sorciere1.position = [monstre_position.x, monstre_position.y]
        monstre_position = tmx_data.get_object_by_name("spawn_sorciere2")
        self.sorciere2.position = [monstre_position.x, monstre_position.y]


        tmx_data = pytmx.util_pygame.load_pygame('map/catacombes1.tmx')
        monstre_position = tmx_data.get_object_by_name("spawn10")
        self.squelette1.position = [monstre_position.x, monstre_position.y]

        tmx_data = pytmx.util_pygame.load_pygame('map/catacombes3.tmx')
        monstre_position = tmx_data.get_object_by_name("spawn_boss")
        self.sorciere3.position = [monstre_position.x, monstre_position.y]

        tmx_data = pytmx.util_pygame.load_pygame('map/maison.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=4)
        self.sortir_rect1 = pygame.Rect(0, 0, 0, 0)
        self.sortir_rect2 = pygame.Rect(0, 0, 0, 0)
        self.sortir_rect3 = pygame.Rect(0, 0, 0, 0)
        self.sortir_rect4 = pygame.Rect(0, 0, 0, 0)

        # Inventaire
        self.inventaire = Inventaire([], 100)
        self.stats = Stats()

        # Sons
        self.son_menu = pygame.mixer.Sound('sons/menu.ogg')
        self.son_inventaire = pygame.mixer.Sound('sons/inventaire.ogg')
        self.son_stats = pygame.mixer.Sound('sons/inventaire.ogg')
        self.cata1_son = pygame.mixer.Sound('sons/cata1.ogg')
        self.surfaceterre = pygame.mixer.Sound('sons/surface.ogg')
        self.coup_touche = pygame.mixer.Sound('sons/attack.ogg')

        self.son_menu.play(-1)

    def load_map(self, maps, spawn):
        tmx_data = pytmx.util_pygame.load_pygame(f'map/{maps}.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        player_position = tmx_data.get_object_by_name(spawn)
        self.player.position = [player_position.x, player_position.y]

        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == 'collision':
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=4)
        self.group.add(self.player)

        if maps == "maison":
            sortir = tmx_data.get_object_by_name('tp_outside')
            self.sortir_rect1 = pygame.Rect(sortir.x, sortir.y, sortir.width, sortir.height)
            self.sortir_rect2 = pygame.Rect(0, 0, 0, 0)
            self.sortir_rect3 = pygame.Rect(0, 0, 0, 0)
            self.sortir_rect4 = pygame.Rect(0, 0, 0, 0)

        if maps == "foret_maudite":
            sortir = tmx_data.get_object_by_name('tp_carte1')
            self.sortir_rect3 = pygame.Rect(sortir.x, sortir.y, sortir.width, sortir.height)
            sortir = tmx_data.get_object_by_name('tp_catacombe1')
            self.sortir_rect4 = pygame.Rect(sortir.x, sortir.y, sortir.width, sortir.height)
            self.sortir_rect1 = pygame.Rect(0, 0, 0, 0)
            self.sortir_rect2 = pygame.Rect(0, 0, 0, 0)
            self.cata1_son.stop()
            self.group.add(self.zombie2)
            self.group.add(self.zombie3)
            self.group.add(self.zombie4)
        else:
            self.group.remove(self.zombie2)
            self.group.remove(self.zombie3)
            self.group.remove(self.zombie4)

        if maps == "catacombes1":
            sortir = tmx_data.get_object_by_name('tp_foretmalefique')
            self.sortir_rect1 = pygame.Rect(sortir.x, sortir.y, sortir.width, sortir.height)
            sortir = tmx_data.get_object_by_name('tp_catacombe2')
            self.sortir_rect2 = pygame.Rect(sortir.x, sortir.y, sortir.width, sortir.height)
            self.sortir_rect4 = pygame.Rect(0, 0, 0, 0)
            self.sortir_rect3 = pygame.Rect(0, 0, 0, 0)
            self.surfaceterre.stop()
            self.group.add(self.zombie5)
            self.group.add(self.zombie6)
            self.group.add(self.zombie7)
            self.group.add(self.zombie8)
            self.group.add(self.zombie9)
            self.group.add(self.zombie10)
            self.group.add(self.squelette1)
            self.group.add(self.sorciere1)
            for i in self.sorciere1.liste_projectiles:
                self.group.add(i)
                i.position = self.sorciere1.position
            self.group.add(self.sorciere2)
            for i in self.sorciere2.liste_projectiles:
                self.group.add(i)
                i.position = self.sorciere2.position

        else:
            self.group.remove(self.zombie5)
            self.group.remove(self.zombie6)
            self.group.remove(self.zombie7)
            self.group.remove(self.zombie8)
            self.group.remove(self.zombie9)
            self.group.remove(self.zombie10)
            self.group.remove(self.squelette1)
            self.group.remove(self.zombie1)
            self.group.remove(self.sorciere1)
            for i in self.sorciere1.liste_projectiles:
                self.group.remove(i)
                i.position = self.sorciere1.position
            self.group.remove(self.sorciere2)
            for i in self.sorciere2.liste_projectiles:
                self.group.remove(i)
                i.position = self.sorciere2.position



        if maps == "catacombes2":
            sortir = tmx_data.get_object_by_name('tp_catacombe1')
            self.sortir_rect3 = pygame.Rect(sortir.x, sortir.y, sortir.width, sortir.height)
            sortir = tmx_data.get_object_by_name('tp_catacombe3')
            self.sortir_rect4 = pygame.Rect(sortir.x, sortir.y, sortir.width, sortir.height)
            sortir = tmx_data.get_object_by_name('tp_catacombe_false1')
            self.sortir_rect1 = pygame.Rect(sortir.x, sortir.y, sortir.width, sortir.height)
            sortir = tmx_data.get_object_by_name('tp_catacombe_false2')
            self.sortir_rect2 = pygame.Rect(sortir.x, sortir.y, sortir.width, sortir.height)

        if maps == "catacombes3":
            sortir = tmx_data.get_object_by_name('tp_catacombe2')
            self.sortir_rect1 = pygame.Rect(sortir.x, sortir.y, sortir.width, sortir.height)
            self.sortir_rect2 = pygame.Rect(0, 0, 0, 0)
            self.sortir_rect3 = pygame.Rect(0, 0, 0, 0)
            self.sortir_rect4 = pygame.Rect(0, 0, 0, 0)
            self.group.add(self.sorciere3)
            for i in self.sorciere3.liste_projectiles:
                self.group.add(i)
                i.position = self.sorciere3.position
        else:
            self.group.remove(self.sorciere3)
            for i in self.sorciere3.liste_projectiles:
                self.group.remove(i)
                i.position = self.sorciere3.position


        if maps == "shop":
            sortir = tmx_data.get_object_by_name('tp_carte')
            self.sortir_rect1 = pygame.Rect(sortir.x, sortir.y, sortir.width, sortir.height)
            sortir = tmx_data.get_object_by_name('tp_shop2')
            self.sortir_rect2 = pygame.Rect(sortir.x, sortir.y, sortir.width, sortir.height)
            self.sortir_rect3 = pygame.Rect(0, 0, 0, 0)
            self.sortir_rect4 = pygame.Rect(0, 0, 0, 0)
        if maps == "shop2":
            sortir = tmx_data.get_object_by_name('tp_shop')
            self.sortir_rect1 = pygame.Rect(sortir.x, sortir.y, sortir.width, sortir.height)
            self.sortir_rect2 = pygame.Rect(0, 0, 0, 0)
            self.sortir_rect3 = pygame.Rect(0, 0, 0, 0)
            self.sortir_rect4 = pygame.Rect(0, 0, 0, 0)

        if maps == "carte":
            sortir = tmx_data.get_object_by_name('tp_maison')
            self.sortir_rect1 = pygame.Rect(sortir.x, sortir.y, sortir.width, sortir.height)
            sortir = tmx_data.get_object_by_name('tp_foret_maudite')
            self.sortir_rect2 = pygame.Rect(sortir.x, sortir.y, sortir.width, sortir.height)
            sortir = tmx_data.get_object_by_name('tp_shop')
            self.sortir_rect3 = pygame.Rect(sortir.x, sortir.y, sortir.width, sortir.height)
            self.sortir_rect4 = pygame.Rect(0, 0, 0, 0)
            self.group.add(self.zombie1)

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.ouvert = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_i and not self.stats.ouvert:
                    self.inventaire.ouvert = not self.inventaire.ouvert
                    if self.inventaire.ouvert:
                        self.son_inventaire.play(-1)
                    else:
                        self.son_inventaire.stop()
                if event.key == pygame.K_COMMA and not self.inventaire.ouvert:
                    self.stats.ouvert = not self.stats.ouvert
                    if self.stats.ouvert:
                        self.son_stats.play(-1)
                    else:
                        self.son_stats.stop()
                if not self.inventaire.ouvert == True or not self.stats.ouvert == True:
                    if event.key == pygame.K_z:
                        self.player.change_animation('haut')
                        self.player.direction = [0, -1]
                    if event.key == pygame.K_s:
                        self.player.change_animation('bas')
                        self.player.direction = [0, 1]
                    if event.key == pygame.K_q:
                        self.player.change_animation('gauche')
                        self.player.direction = [-1, 0]
                    if event.key == pygame.K_d:
                        self.player.change_animation('droite')
                        self.player.direction = [1, 0]
        if self.inventaire.ouvert == True or self.stats.ouvert == True:
            return
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_k]:
            if self.player.latence_value == self.player.latence:
                degats = self.playerstats.attack()
                if self.map == "carte":
                    liste_monstre = [self.zombie1]
                    for monstr in liste_monstre:
                        if self.player.attaque_surf.colliderect(monstr.feet):
                            monstr.vie -= degats
                            self.coup_touche.play(1)
                            print("bien joué" + str(monstr))
                            self.player.latence_value = 0
                if self.map == 'foret_maudite':
                    liste_monstre = [self.zombie2, self.zombie3, self.zombie4]
                    for monstr in liste_monstre:
                        if self.player.attaque_surf.colliderect(monstr.feet):
                            monstr.vie -= degats
                            self.coup_touche.play(1)
                            print("bien joué" + str(monstr))
                            self.player.latence_value = 0

                if self.map == 'catacombes1':
                    liste_monstre = [self.zombie5, self.zombie6, self.zombie7, self.zombie8, self.zombie9,
                                     self.squelette1,self.sorciere1,self.sorciere2]
                    for monstr in liste_monstre:
                        if self.player.attaque_surf.colliderect(monstr.feet):
                            monstr.vie -= degats
                            self.coup_touche.play(1)
                            print("bien joué" + str(monstr))
                            self.player.latence_value = 0
                if self.map == 'catacombes3':
                    if self.player.attaque_surf.colliderect(self.sorciere3.feet):
                        self.sorciere3.vie -= degats
                        self.coup_touche.play(1)
                        print("bien joué,ta hit le boss !")
                        self.player.latence_value = 0


        if pressed[pygame.K_z]:
            self.player.direction[1] = -1
            self.player.ani += 1
            self.player.move_haut()
            if self.player.ani == self.player.step:
                self.player.change_animation('haut1')
            if self.player.ani == self.player.step * 2:
                self.player.change_animation('haut')
            if self.player.ani == self.player.step * 3:
                self.player.change_animation('haut2')
            if self.player.ani == self.player.step * 4:
                self.player.change_animation('haut')
                self.player.ani = 0
        if pressed[pygame.K_s]:
            self.player.direction[1] = 1
            self.player.move_bas()
            self.player.ani += 1
            if self.player.ani == self.player.step:
                self.player.change_animation('bas1')
            if self.player.ani == self.player.step * 2:
                self.player.change_animation('bas')
            if self.player.ani == self.player.step * 3:
                self.player.change_animation('bas2')
            if self.player.ani == self.player.step * 4:
                self.player.change_animation('bas')
                self.player.ani = 0
        if pressed[pygame.K_q]:
            self.player.direction[0] = -1
            self.player.move_gauche()
            self.player.ani += 1
            if self.player.ani == self.player.step:
                self.player.change_animation('gauche1')
            if self.player.ani == self.player.step * 2:
                self.player.change_animation('gauche')
            if self.player.ani == self.player.step * 3:
                self.player.change_animation('gauche2')
            if self.player.ani == self.player.step * 4:
                self.player.change_animation('gauche')
                self.player.ani = 0
        if pressed[pygame.K_d]:
            self.player.direction[0] = 1
            self.player.move_droite()
            self.player.ani += 1
            if self.player.ani == self.player.step:
                self.player.change_animation('droite1')
            if self.player.ani == self.player.step * 2:
                self.player.change_animation('droite')
            if self.player.ani == self.player.step * 3:
                self.player.change_animation('droite2')
            if self.player.ani == self.player.step * 4:
                self.player.change_animation('droite')
                self.player.ani = 0

    def monstres_interaction(self):
        liste_monstre = []
        if self.map == 'carte':
            liste_monstre = [self.zombie1]
        elif self.map == 'catacombes1':
            liste_monstre = [self.zombie5, self.zombie6, self.zombie7, self.zombie8, self.zombie9, self.zombie10,
                             self.squelette1,self.sorciere1,self.sorciere2]
        elif self.map == 'foret_maudite':
            liste_monstre = [self.zombie2, self.zombie3, self.zombie4]
        elif self.map=="catacombes3":
            liste_monstre=[self.sorciere3]
        for monstr in liste_monstre:
            if monstr.vie <= 0:
                self.group.remove(monstr)
                monstr.position = [0, 0]
                monstr.rect.x = 0
                monstr.rect.y = 0
                if monstr.espece=="witch":
                    for i in monstr.liste_projectiles:
                        self.group.remove(i)
                        i.position = monstr.position
            if monstr.latence_value < monstr.latence:
                monstr.latence_value += 1
            monstr.ani += 1
            if monstr.boss ==False:
                monstr.change_animation(monstr.ani)
            if monstr.espece != "witch":
                if self.player.position[0] < monstr.position[0] + 13:
                    monstr.move_gauche()
                if self.player.position[0] > monstr.position[0] + 13:
                    monstr.move_droite()
                if self.player.position[1] > monstr.position[1]:
                    monstr.move_bas()
                if self.player.position[1] < monstr.position[1]:
                    monstr.move_haut()
            else:
                for i in monstr.liste_projectiles :
                    if i.rect.colliderect(self.player.feet) and monstr.latence_value == monstr.latence:
                        i.position = monstr.position
                        self.playerstats.vie -= monstr.attaque
                        print(str(self.playerstats.vie) + " / " + str(self.playerstats.viemax))
                        monstr.latence_value = 0
                    if i.rect.collidelist(self.walls) > -1:
                        i.position = monstr.position
            if monstr.boss:
                if self.player.position[0] < monstr.position[0] + 13:
                    monstr.move_gauche()
                if self.player.position[0] > monstr.position[0] + 13:
                    monstr.move_droite()
                if self.player.position[1] > monstr.position[1]:
                    monstr.move_bas()
                if self.player.position[1] < monstr.position[1]:
                    monstr.move_haut()
                for i in monstr.liste_projectiles :
                    if i.rect.colliderect(self.player.feet) and monstr.latence_value == monstr.latence:
                        i.position = monstr.position
                        self.playerstats.vie -= monstr.attaque
                        print(str(self.playerstats.vie) + " / " + str(self.playerstats.viemax))
                        monstr.latence_value = 0
                    if i.rect.collidelist(self.walls) > -1:
                        i.position = monstr.position




            if monstr.ani == 39:
                monstr.ani = 28
            if monstr.feet.collidelist(self.walls) > -1:
                monstr.move_back()
            if self.player.feet.colliderect(monstr.feet):
                monstr.move_back()
                if monstr.espece == "witch":
                    self.player.move_back()
                if monstr.latence_value == monstr.latence and monstr.vie > 0:
                    monstr.latence_value = 0
                    self.playerstats.vie -= monstr.attaque
                    print(str(self.playerstats.vie) + " / " + str(self.playerstats.viemax))
            for monstr2 in liste_monstre:
                if monstr2.feet.colliderect(monstr.feet) and monstr != monstr2:
                    monstr2.move_back_moitie()
                    monstr.move_back_moitie()

    def update(self):
        self.group.update()
        self.monstres_interaction()
        if self.player.latence_value < self.player.latence:
            self.player.latence_value += 1

        if self.map == "maison" and self.player.feet.colliderect(self.sortir_rect1):
            self.load_map('carte', 'spawn_maison')
            self.map = "carte"
            self.player.change_animation('bas')
            return

        if self.map == "carte" and self.player.feet.colliderect(self.sortir_rect3):
            self.load_map('shop', 'spawn_carte')
            self.map = "shop"
            self.player.change_animation('haut')
            return

        if self.map == "carte" and self.player.feet.colliderect(self.sortir_rect1):
            self.load_map('maison', 'spawn_inside')
            self.map = "maison"
            self.player.change_animation('haut')

        if self.player.feet.collidelist(self.walls) > -1:
            self.player.move_back()

        if self.map == "carte" and self.player.feet.colliderect(self.sortir_rect2):
            self.load_map('foret_maudite', 'spawn_carte1')
            self.map = "foret_maudite"
            self.player.change_animation('haut')
            return
        if self.map == "shop" and self.player.feet.colliderect(self.sortir_rect1):
            self.load_map('carte', 'spawn_shop')
            self.map = "carte"
            self.player.change_animation('bas')

        if self.map == "shop" and self.player.feet.colliderect(self.sortir_rect2):
            self.load_map('shop2', 'spawn_shop')
            self.map = "shop2"
            self.player.change_animation('gauche')
        if self.map == "shop2" and self.player.feet.colliderect(self.sortir_rect1):
            self.load_map('shop', 'spawn_shop2')
            self.map = "shop"
            self.player.change_animation('gauche')

        if self.map == "foret_maudite" and self.player.feet.colliderect(self.sortir_rect3):
            self.load_map('carte', 'spawn_foret_maudite')
            self.map = "carte"

        if self.map == "foret_maudite" and self.player.feet.colliderect(self.sortir_rect4):
            self.load_map('catacombes1', 'spawn_foretmalefique')
            self.map = "catacombes1"
            self.cata1_son.play(-1)

        if self.map == "catacombes1" and self.player.feet.colliderect(self.sortir_rect1):
            self.load_map('foret_maudite', 'spawn_catacombe')
            self.map = "foret_maudite"
            self.surfaceterre.play(-1)

        if self.map == "catacombes1" and self.player.feet.colliderect(self.sortir_rect2):
            self.load_map('catacombes2', 'spawn_catacombe1')
            self.map = "catacombes2"

        if self.map == "catacombes2" and self.player.feet.colliderect(self.sortir_rect3):
            self.load_map('catacombes1', 'spawn_catacombe2')
            self.map = "catacombes1"

        if self.map == "catacombes2" and self.player.feet.colliderect(self.sortir_rect4):
            self.load_map('catacombes3', 'spawn_catacombe2')
            self.map = "catacombes3"

        if self.map == "catacombes2" and self.player.feet.colliderect(
                self.sortir_rect1) or self.player.feet.colliderect(self.sortir_rect2):
            pygame.display.set_caption('PRANKED')
            # self.screamer.preview()
            pygame.display.set_caption('miskine mdr change ton fut')
            self.load_map('catacombes2', 'spawn_catacombe1')
            self.cata1_son.play(-1)

        if self.map == "catacombes3" and self.player.feet.colliderect(self.sortir_rect1):
            self.load_map('catacombes2', 'spawn_catacombe3')
            self.map = "catacombes2"

    # Menu

    def draw_text(self, text, font, size, color):
        if font == "Default":
            font = pygame.font.Font('font/alagard.ttf', size)
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        return textobj

    def create_save(self):
        namebox = TextInputBox(self.screen.get_width() / 2 - self.screen.get_width() * 0.4 // 2,
                               math.floor(self.screen.get_height() * 0.3), math.floor(self.screen.get_width() * 0.4),
                               pygame.font.Font('font/alagard.ttf', 100), 10)
        txtbox = pygame.sprite.Group(namebox)
        click = False
        weaponselected = "Sword"
        classselected = "DPS"
        while True:
            center_x = self.screen.get_width() / 2
            center_y = self.screen.get_height() / 2

            mx, my = pygame.mouse.get_pos()

            self.screen.fill((0, 0, 0))

            texte = self.draw_text('CREATE SAVE', "Default", math.floor(self.screen.get_height() * 0.1),
                                   (255, 255, 255))
            self.screen.blit(texte, (center_x - texte.get_width() // 2, math.floor(self.screen.get_height() * 0.1)))

            backbutton = pygame.Rect(0, center_y * 2 - self.screen.get_height() * 0.1, self.screen.get_width() * 0.3,
                                     self.screen.get_height() * 0.1)
            txtbackbutton = self.draw_text('Back', "Default", math.floor(self.screen.get_height() * 0.1),
                                           (255, 255, 255))
            self.screen.blit(txtbackbutton, (0, center_y * 2 - txtbackbutton.get_height()))

            namelabel = self.draw_text('Name: (Less than 10 caracters)', "Default",
                                       math.floor(self.screen.get_height() * 0.05), (255, 255, 255))
            self.screen.blit(namelabel,
                             (center_x - namelabel.get_width() // 2, math.floor(self.screen.get_height() * 0.2)))

            wtypelabel = self.draw_text('Weapon type:', "Default", math.floor(self.screen.get_height() * 0.05),
                                        (255, 255, 255))
            self.screen.blit(wtypelabel,
                             (center_x - wtypelabel.get_width() // 2, math.floor(self.screen.get_height() * 0.5)))

            # Toutes les armes avec boutton
            armehauteur = 0.6

            swordbutton = pygame.Rect(center_x - self.screen.get_width() * 0.8 // 2,
                                      math.floor(self.screen.get_height() * armehauteur),
                                      self.screen.get_width() * 0.15, self.screen.get_height() * 0.05)
            if weaponselected == "Sword":
                txtswordbutton = self.draw_text('Sword', "Default", math.floor(self.screen.get_height() * 0.05),
                                                (200, 200, 200))
            else:
                txtswordbutton = self.draw_text('Sword', "Default", math.floor(self.screen.get_height() * 0.05),
                                                (255, 255, 255))
            self.screen.blit(txtswordbutton, (
                center_x - self.screen.get_width() * 0.8 // 2, math.floor(self.screen.get_height() * 0.6)))

            claymorebutton = pygame.Rect(center_x - self.screen.get_width() * 0.4 // 2,
                                         math.floor(self.screen.get_height() * armehauteur),
                                         self.screen.get_width() * 0.15, self.screen.get_height() * 0.05)
            if weaponselected == "Claymore":
                txtclaymorebutton = self.draw_text('Claymore', "Default", math.floor(self.screen.get_height() * 0.05),
                                                   (200, 200, 200))
            else:
                txtclaymorebutton = self.draw_text('Claymore', "Default", math.floor(self.screen.get_height() * 0.05),
                                                   (255, 255, 255))
            self.screen.blit(txtclaymorebutton, (
                center_x - self.screen.get_width() * 0.4 // 2, math.floor(self.screen.get_height() * 0.6)))

            polearmbutton = pygame.Rect(center_x, math.floor(self.screen.get_height() * armehauteur),
                                        self.screen.get_width() * 0.15, self.screen.get_height() * 0.05)
            if weaponselected == "Polearm":
                txtpolearmbutton = self.draw_text('Polearm', "Default", math.floor(self.screen.get_height() * 0.05),
                                                  (200, 200, 200))
            else:
                txtpolearmbutton = self.draw_text('Polearm', "Default", math.floor(self.screen.get_height() * 0.05),
                                                  (255, 255, 255))
            self.screen.blit(txtpolearmbutton, (center_x, math.floor(self.screen.get_height() * 0.6)))

            catalystbutton = pygame.Rect(center_x + self.screen.get_width() * 0.4 // 2,
                                         math.floor(self.screen.get_height() * armehauteur),
                                         self.screen.get_width() * 0.15, self.screen.get_height() * 0.05)
            if weaponselected == "Catalyst":
                txtcatalystbutton = self.draw_text('Catalyst', "Default", math.floor(self.screen.get_height() * 0.05),
                                                   (200, 200, 200))
            else:
                txtcatalystbutton = self.draw_text('Catalyst', "Default", math.floor(self.screen.get_height() * 0.05),
                                                   (255, 255, 255))
            self.screen.blit(txtcatalystbutton, (
                center_x + self.screen.get_width() * 0.4 // 2, math.floor(self.screen.get_height() * 0.6)))

            bowbutton = pygame.Rect(center_x + self.screen.get_width() * 0.8 // 2,
                                    math.floor(self.screen.get_height() * armehauteur), self.screen.get_width() * 0.15,
                                    self.screen.get_height() * 0.05)
            if weaponselected == "Bow":
                txtbowbutton = self.draw_text('Bow', "Default", math.floor(self.screen.get_height() * 0.05),
                                              (200, 200, 200))
            else:
                txtbowbutton = self.draw_text('Bow', "Default", math.floor(self.screen.get_height() * 0.05),
                                              (255, 255, 255))
            self.screen.blit(txtbowbutton, (
                center_x + self.screen.get_width() * 0.8 // 2, math.floor(self.screen.get_height() * 0.6)))

            classlabel = self.draw_text('Class:', "Default", math.floor(self.screen.get_height() * 0.05),
                                        (255, 255, 255))
            self.screen.blit(classlabel,
                             (center_x - classlabel.get_width() // 2, math.floor(self.screen.get_height() * 0.7)))

            # Toutes les classes avec boutton
            classhauteur = 0.8

            dpsbutton = pygame.Rect(center_x - self.screen.get_width() * 0.7 // 2,
                                    math.floor(self.screen.get_height() * classhauteur), self.screen.get_width() * 0.2,
                                    self.screen.get_height() * 0.05)
            if classselected == "DPS":
                txtdpsbutton = self.draw_text('DPS', "Default", math.floor(self.screen.get_height() * 0.05),
                                              (200, 200, 200))
            else:
                txtdpsbutton = self.draw_text('DPS', "Default", math.floor(self.screen.get_height() * 0.05),
                                              (255, 255, 255))
            self.screen.blit(txtdpsbutton, (
                center_x - self.screen.get_width() * 0.5 // 2, math.floor(self.screen.get_height() * classhauteur)))

            supportbutton = pygame.Rect(center_x - self.screen.get_width() * 0.1,
                                        math.floor(self.screen.get_height() * classhauteur),
                                        self.screen.get_width() * 0.2, self.screen.get_height() * 0.05)
            if classselected == "Support DPS":
                txtsupportbutton = self.draw_text('Support DPS', "Default", math.floor(self.screen.get_height() * 0.05),
                                                  (200, 200, 200))
            else:
                txtsupportbutton = self.draw_text('Support DPS', "Default", math.floor(self.screen.get_height() * 0.05),
                                                  (255, 255, 255))
            self.screen.blit(txtsupportbutton, (center_x, math.floor(self.screen.get_height() * classhauteur)))

            healerbutton = pygame.Rect(center_x + self.screen.get_width() * 0.3 // 2,
                                       math.floor(self.screen.get_height() * classhauteur),
                                       self.screen.get_width() * 0.2, self.screen.get_height() * 0.05)
            if classselected == "Healer":
                txthealerbutton = self.draw_text('Healer', "Default", math.floor(self.screen.get_height() * 0.05),
                                                 (200, 200, 200))
            else:
                txthealerbutton = self.draw_text('Healer', "Default", math.floor(self.screen.get_height() * 0.05),
                                                 (255, 255, 255))
            self.screen.blit(txthealerbutton, (
                center_x + self.screen.get_width() * 0.5 // 2, math.floor(self.screen.get_height() * classhauteur)))

            event_list = pygame.event.get()

            createbutton = pygame.Rect(center_x - self.screen.get_width() * 0.3 // 2,
                                       math.floor(center_y * 2 - self.screen.get_height() * 0.1),
                                       self.screen.get_width() * 0.3, self.screen.get_height() * 0.05)
            txtcreatebutton = self.draw_text('Create', "Default", math.floor(self.screen.get_height() * 0.05),
                                             (255, 255, 255))
            self.screen.blit(txtcreatebutton, (
                center_x - txtcreatebutton.get_width() // 2, center_y * 2 - txtcreatebutton.get_height() * 2))

            if swordbutton.collidepoint((mx, my)):
                if click:
                    weaponselected = "Sword"
            if claymorebutton.collidepoint((mx, my)):
                if click:
                    weaponselected = "Claymore"
            if polearmbutton.collidepoint((mx, my)):
                if click:
                    weaponselected = "Polearm"
            if catalystbutton.collidepoint((mx, my)):
                if click:
                    weaponselected = "Catalyst"
            if bowbutton.collidepoint((mx, my)):
                if click:
                    weaponselected = "Bow"

            if dpsbutton.collidepoint((mx, my)):
                if click:
                    classselected = "DPS"
            if supportbutton.collidepoint((mx, my)):
                if click:
                    classselected = "Support DPS"
            if healerbutton.collidepoint((mx, my)):
                if click:
                    classselected = "Healer"

            if backbutton.collidepoint((mx, my)):
                if click:
                    self.save()
                    break

            if createbutton.collidepoint((mx, my)):
                if click:
                    if classselected == "DPS":
                        vie = 400
                        attaque = 60
                        dc = 50
                        tc = 50
                    elif classselected == "Support DPS":
                        vie = 200
                        attaque = 45
                        dc = 70
                        tc = 20
                    elif classselected == "Healer":
                        vie = 1000
                        attaque = 10
                        dc = 0
                        tc = 0
                    create_save(str(namebox.text), weaponselected, vie, attaque, dc, tc)
                    self.playerstats = load_save()
                    self.run()
                    break

            click = False
            for event in event_list:
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            txtbox.update(event_list)
            txtbox.draw(self.screen)

            pygame.display.update()
            clock.tick(60)

    def save(self):
        click = False
        while True:
            center_x = self.screen.get_width() / 2
            center_y = self.screen.get_height() / 2

            mx, my = pygame.mouse.get_pos()

            self.screen.fill((0, 0, 0))

            texte = self.draw_text('SAVE', "Default", math.floor(self.screen.get_height() * 0.1), (255, 255, 255))
            self.screen.blit(texte, (center_x - texte.get_width() // 2, math.floor(self.screen.get_height() * 0.1)))

            loadbutton = pygame.Rect(center_x - self.screen.get_width() * 0.3 // 2,
                                     math.floor(self.screen.get_height() * 0.3), self.screen.get_width() * 0.3,
                                     self.screen.get_height() * 0.1)
            createbutton = pygame.Rect(center_x - self.screen.get_width() * 0.3 // 2,
                                       math.floor(self.screen.get_height() * 0.45), self.screen.get_width() * 0.3,
                                       self.screen.get_height() * 0.1)
            backbutton = pygame.Rect(0, center_y * 2 - self.screen.get_height() * 0.1, self.screen.get_width() * 0.3,
                                     self.screen.get_height() * 0.1)

            if check_save():
                txtbutton_1 = self.draw_text('Load current save', "Default", math.floor(self.screen.get_height() * 0.1),
                                             (255, 255, 255))
            else:
                txtbutton_1 = self.draw_text('Load current save', "Default", math.floor(self.screen.get_height() * 0.1),
                                             (255, 0, 0))
            self.screen.blit(txtbutton_1,
                             (center_x - txtbutton_1.get_width() // 2, math.floor(self.screen.get_height() * 0.3)))
            txtbutton_2 = self.draw_text('Create a new save', "Default", math.floor(self.screen.get_height() * 0.1),
                                         (255, 255, 255))
            self.screen.blit(txtbutton_2,
                             (center_x - txtbutton_2.get_width() // 2, math.floor(self.screen.get_height() * 0.45)))
            txtbackbutton = self.draw_text('Back', "Default", math.floor(self.screen.get_height() * 0.1),
                                           (255, 255, 255))
            self.screen.blit(txtbackbutton, (0, center_y * 2 - txtbackbutton.get_height()))

            if loadbutton.collidepoint((mx, my)):
                if click and check_save():
                    self.playerstats = load_save()
                    self.run()
                    break
            if createbutton.collidepoint((mx, my)):
                if click:
                    self.create_save()
                    break
            if backbutton.collidepoint((mx, my)):
                if click:
                    self.main_menu()
                    break

            click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            pygame.display.update()
            clock.tick(60)

    def options(self):
        click = False
        while True:
            center_x = self.screen.get_width() / 2
            center_y = self.screen.get_height() / 2

            mx, my = pygame.mouse.get_pos()

            self.screen.fill((0, 0, 0))

            texte = self.draw_text('OPTIONS', "Default", math.floor(self.screen.get_height() * 0.1), (255, 255, 255))
            self.screen.blit(texte, (center_x - texte.get_width() // 2, math.floor(self.screen.get_height() * 0.1)))

            backbutton = pygame.Rect(0, center_y * 2 - self.screen.get_height() * 0.1, self.screen.get_width() * 0.3,
                                     self.screen.get_height() * 0.1)
            txtbackbutton = self.draw_text('Back', "Default", math.floor(self.screen.get_height() * 0.1),
                                           (255, 255, 255))
            self.screen.blit(txtbackbutton, (0, center_y * 2 - txtbackbutton.get_height()))

            if backbutton.collidepoint((mx, my)):
                if click:
                    self.main_menu()
                    break

            click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            pygame.display.update()
            clock.tick(60)

    def main_menu(self):
        click = False
        while True:
            center_x = self.screen.get_width() / 2
            center_y = self.screen.get_height() / 2

            self.screen.blit(pygame.transform.scale(pygame.image.load('images/mainmenu.jpg'), self.screen.get_size()),
                             (0, 0))
            self.screen.blit(pygame.transform.scale(pygame.image.load('images/logo.png'), (
                math.floor(self.screen.get_width() * 0.3), math.floor(self.screen.get_height() * 0.4))),
                             (center_x - self.screen.get_width() * 0.3 // 2, 20))

            mx, my = pygame.mouse.get_pos()

            playbutton = pygame.Rect(center_x - self.screen.get_width() * 0.3 // 2,
                                     math.floor(self.screen.get_height() * 0.4), self.screen.get_width() * 0.3,
                                     self.screen.get_height() * 0.1)
            optionbutton = pygame.Rect(center_x - self.screen.get_width() * 0.3 // 2,
                                       math.floor(self.screen.get_height() * 0.4) + 100, self.screen.get_width() * 0.3,
                                       self.screen.get_height() * 0.1)
            exitbutton = pygame.Rect(center_x - self.screen.get_width() * 0.3 // 2,
                                     math.floor(self.screen.get_height() * 0.4) + 200, self.screen.get_width() * 0.3,
                                     self.screen.get_height() * 0.1)

            txtbutton_1 = self.draw_text('Play', "Default", math.floor(self.screen.get_height() * 0.1), (255, 255, 255))
            self.screen.blit(txtbutton_1,
                             (center_x - txtbutton_1.get_width() // 2, math.floor(self.screen.get_height() * 0.4)))
            txtbutton_2 = self.draw_text('Options', "Default", math.floor(self.screen.get_height() * 0.1),
                                         (255, 255, 255))
            self.screen.blit(txtbutton_2, (
                center_x - txtbutton_2.get_width() // 2, math.floor(self.screen.get_height() * 0.4) + 100))
            txtbutton_3 = self.draw_text('Exit', "Default", math.floor(self.screen.get_height() * 0.1), (255, 255, 255))
            self.screen.blit(txtbutton_3, (
                center_x - txtbutton_3.get_width() // 2, math.floor(self.screen.get_height() * 0.4) + 200))

            if playbutton.collidepoint((mx, my)):
                if click:
                    self.save()
                    break
            if optionbutton.collidepoint((mx, my)):
                if click:
                    self.options()
                    break
            if exitbutton.collidepoint((mx, my)):
                if click:
                    pygame.quit()
                    sys.exit()

            click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            pygame.display.update()
            clock.tick(60)

    # Methode d'affichage par dessus pyscroll
    def draw(self):
        if self.inventaire.ouvert:
            self.inventaire.draw(self.screen)
        if self.stats.ouvert == True:
            self.stats.draw(self.screen)
        self.screen.blit(self.bvbg, (200, self.screen.get_height()-self.bvbg.get_height()))
        imag = pygame.Surface([319, 60])
        imag.blit(self.bvfg, (0, 0), (0, 0, 290 * self.playerstats.vie / self.playerstats.viemax + 29, 60))
        imag.set_colorkey((0, 0, 0))
        self.screen.blit(imag, (200, self.screen.get_height()-imag.get_height()))
        #pygame.draw.rect(self.screen, (255, 0, 0), self.player.attaque_surf)
        #pygame.draw.rect(self.screen, (0, 255, 0), self.player.rect)
        if self.map =="catacombes3":
            pygame.draw.rect(self.screen, (255,0, 0), pygame.Rect(20,40,self.sorciere3.vie*100,75))

    # Boucle principale

    def run(self):
        self.player = Player(0, 0, self.playerstats.weapontype)
        self.load_map("maison", "spawn")
        self.son_menu.stop()
        self.surfaceterre.play(-1)
        while self.ouvert:
            self.player.save_location()
            self.zombie1.save_location()
            self.zombie2.save_location()
            self.zombie3.save_location()
            self.zombie4.save_location()
            self.zombie5.save_location()
            self.zombie6.save_location()
            self.zombie7.save_location()
            self.zombie8.save_location()
            self.zombie9.save_location()
            self.zombie10.save_location()
            self.sorciere1.save_location()
            self.sorciere2.save_location()
            self.sorciere3.save_location()
            self.squelette1.save_location()
            self.squelette2.save_location()

            self.handle_input()
            self.update()
            self.group.center(self.player.rect)
            self.group.draw(self.screen)
            self.draw()
            pygame.display.flip()
            clock.tick(60)
            if self.playerstats.vie <= 0:
                self.sortir_rect1= pygame.Rect(0,0,0,0)
                self.sortir_rect1= pygame.Rect(0,0,0,0)
                self.sortir_rect1= pygame.Rect(0,0,0,0)
                self.sortir_rect1= pygame.Rect(0,0,0,0)
                self.surfaceterre.stop()
                self.cata1_son.stop()
                self.__init__()
                self.main_menu()

        pygame.quit()
