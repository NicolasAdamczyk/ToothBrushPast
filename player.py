import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, weapontype):
        super().__init__()
        self.sprite_sheet = self.reduire_image(pygame.image.load('sprites/player_hand/bas.png'))
        self.position = [x, y]
        self.speed = 3
        self.step = 10
        self.ani = 0
        self.weapontype = weapontype
        self.images = {
            'bas': self.reduire_image(pygame.image.load('sprites/player_' + self.weapontype + '/bas.png')),
            'gauche': self.reduire_image(pygame.image.load('sprites/player_' + self.weapontype + '/gauche.png')),
            'droite': self.reduire_image(pygame.image.load('sprites/player_' + self.weapontype + '/droite.png')),
            'haut': self.reduire_image(pygame.image.load('sprites/player_' + self.weapontype + '/haut.png')),
            'bas1': self.reduire_image(pygame.image.load('sprites/player_' + self.weapontype + '/bas1.png')),
            'gauche1': self.reduire_image(pygame.image.load('sprites/player_' + self.weapontype + '/gauche1.png')),
            'droite1': self.reduire_image(pygame.image.load('sprites/player_' + self.weapontype + '/droite1.png')),
            'haut1': self.reduire_image(pygame.image.load('sprites/player_' + self.weapontype + '/haut1.png')),
            'bas2': self.reduire_image(pygame.image.load('sprites/player_' + self.weapontype + '/bas2.png')),
            'gauche2': self.reduire_image(pygame.image.load('sprites/player_' + self.weapontype + '/gauche2.png')),
            'droite2': self.reduire_image(pygame.image.load('sprites/player_' + self.weapontype + '/droite2.png')),
            'haut2': self.reduire_image(pygame.image.load('sprites/player_' + self.weapontype + '/haut2.png'))
        }
        self.image = self.images['bas']
        self.rect = self.image.get_rect()
        self.image.set_colorkey((255, 255, 255))

        self.feet = pygame.Rect(0, 0, 26, 16)
        self.old_position = self.position.copy()
        self.attaque_surf = pygame.Rect(0, 0, 64, 64)
        self.direction = [0, 1]
        self.latence = 60
        self.latence_value = self.latence

    def reduire_image(self, image):
        x = image.get_width()
        y = image.get_height()
        return pygame.transform.scale(image, (x // 2, y // 2))

    def save_location(self):
        self.old_position = self.position.copy()

    def change_animation(self, name):
        self.image = self.images[name]
        self.image.set_colorkey((255, 255, 255))

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
        self.feet.midbottom = self.rect.midbottom
        self.feet.y += 2
        if self.direction[0] == -1:
            self.attaque_surf.midright = self.rect.midleft
        if self.direction[0] == 1:
            self.attaque_surf.midleft = self.rect.midright
        if self.direction[1] == 1:
            self.attaque_surf.midtop = self.rect.midbottom
        if self.direction[1] == -1:
            self.attaque_surf.midbottom = self.rect.midleft
            self.attaque_surf.y -= 10
            self.attaque_surf.x += 7

        # self.attaque_surf[0] = 10 * self.direction[0] + self.rect[0]
        # self.attaque_surf[1] = 10 * self.direction[1] + self.rect[1]

    def move_back(self):
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom
