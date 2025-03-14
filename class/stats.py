import pygame

class Stats:
    def __init__(self):
        self.image = pygame.image.load('images/menu.png')
        self.ouvert = False
            
    def draw(self, screen):
        screen.blit(pygame.transform.scale(self.image, screen.get_size()), (0,0))