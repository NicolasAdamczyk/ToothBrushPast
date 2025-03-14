import pygame
import sys

sys.path.append('class')
from projectile import Projectile
from pnj import *


class Monstre(pygame.sprite.Sprite):

    def __init__(self, x, y, espece, level, vie, attaque, exp, argent, item, boss):
        super().__init__()
        Hostile.__init__(self, espece, level, vie, attaque, exp, argent, item)
        self.espece = espece
        self.level = level
        self.vie = vie
        self.attaque = attaque
        self.exp = exp
        self.argent = argent
        self.item = item

        self.sprite_sheet = pygame.image.load(f"monstres/{self.espece}.png")
        self.image = self.get_image(0)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.images = [self.get_image(i) for i in range(40)]
        self.speed = 0.5
        if self.espece == "zombie":
            self.speed = 1
        self.step = 3
        self.feet = pygame.Rect(0, 0, 4, 16)
        self.old_position = self.position.copy()
        self.older_position = self.old_position.copy()
        self.ani = 28
        self.latence = 60
        self.latence_value = self.latence
        self.tqt = 3
        self.boss=boss
        if self.espece == 'witch':
            self.boule1 = Projectile(x, y, [1,0])
            self.boule2 = Projectile(x, y, [-1,0])
            self.boule3 = Projectile(x, y, [0,-1])
            self.boule4 = Projectile(x, y, [0,1])
            self.liste_projectiles = [self.boule1, self.boule2, self.boule3, self.boule4]
            if self.boss:
                self.boule5 = Projectile(x, y, [1,1])
                self.boule6 = Projectile(x, y, [-1,1])
                self.boule7 = Projectile(x, y, [1,-1])
                self.boule8 = Projectile(x, y, [-1,-1])
                self.liste_projectiles.append(self.boule5)
                self.liste_projectiles.append(self.boule6)
                self.liste_projectiles.append(self.boule7)
                self.liste_projectiles.append(self.boule8)
                self.image = pygame.image.load("monstres/dentv.png")
                x = self.image.get_width()
                y = self.image.get_height()
                self.image = pygame.transform.scale(self.image, (x // 14, y // 14))
                self.rect = self.image.get_rect()

    def get_image(self, x):
        x *= 32
        image = pygame.Surface([1280, 32])
        image.blit(self.sprite_sheet, (0, 0), (x, 0, 32, 32))
        return image

    def save_location(self):
        self.older_position = self.old_position.copy()
        self.old_position = self.position.copy()

    def change_animation(self, num):
        self.image = self.images[num]
        self.image.set_colorkey((0, 0, 0))

    def move_droite(self):
        self.position[0] += self.speed

    def move_gauche(self):
        self.position[0] -= self.speed

    def move_haut(self):
        self.position[1] -= self.speed

    def move_bas(self):
        self.position[1] += self.speed

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.bottomleft
        self.feet.x += 17
        self.feet.y -= 5
        if self.vie <= 0:
            self.position = [0, 0]
            self.rect.x = 0
            self.rect.y = 0
            self.feet.x = 0
            self.feet.y = 0

    def move_back(self):
        self.position = self.older_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.bottomleft
        self.feet.x += 17
        self.feet.y -= 5

    def move_back_moitie(self):
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.bottomleft
        self.feet.x += 17
        self.feet.y -= 5
