from time import sleep
import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.sprite_sheet = pygame.image.load('perso.png')
        self.image = self.get_img(34, 0)
        self.image.set_colorkey([255, 255, 255])
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.images_pos = {
            'bas1' : self.get_img(0, 0),
            'bas2' : self.get_img(32, 0), 
            'bas3' : self.get_img(64, 0),

            'gauche1' : self.get_img(0, 32),
            'gauche2' : self.get_img(32, 32), 
            'gauche3' : self.get_img(64, 32),

            'droite1' : self.get_img(0, 64),
            'droite2' : self.get_img(32, 64), 
            'droite3' : self.get_img(64, 64),

            'haut1' : self.get_img(0, 96),
            'haut2' : self.get_img(32, 96), 
            'haut3' : self.get_img(64, 96),
        }
        self.speed = 8

    def animations(self, anim_name):
        self.image = self.images_pos[anim_name]
        self.image.set_colorkey([255, 255, 255])
        self.rect = self.image.get_rect()
        self.update()

    def move_right(self): self.position[0] += self.speed
    def move_left(self): self.position[0] -= self.speed
    def move_up(self): self.position[1] -= self.speed
    def move_down(self): self.position[1] += self.speed

    def update(self):
        self.rect.topleft = self.position

    def get_img(self, x, y):
        image = pygame.Surface([32, 32])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32))
        return image