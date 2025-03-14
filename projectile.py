import pygame
import sys

sys.path.append('images')


class Projectile(pygame.sprite.Sprite):

    def __init__(self, x, y, direction):
        super().__init__()
        self.image = pygame.image.load("images/boule.png")
        self.image.set_colorkey((255, 255, 255))
        x = self.image.get_width()
        y = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (x // 14, y // 14))
        self.rect = self.image.get_rect()
        self.position = [x,y]
        self.direction = list(direction)

    def update(self):
        self.position = [self.position[0]+self.direction[0],self.position[1]+self.direction[1]]
        self.rect.topleft = self.position




