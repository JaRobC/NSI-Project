import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.sprite_sheet = pygame.image.load('./characters_model/char.png')
        self.image = self.get_img(31, 0)
        self.image.set_colorkey([255, 255, 255])
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.images_pos = {
            './f/f1.png' : self.get_img(0, 0),
            './f/f2.png' : self.get_img(32, 0),
            './f/f3.png' : self.get_img(64, 0),

            './l/l1.png' : self.get_img(0, 32),
            './l/l2.png' : self.get_img(32, 32),
            './l/l3.png' : self.get_img(64, 32),

            './r/r1.png' : self.get_img(0, 64),
            './r/r2.png' : self.get_img(32, 64),
            './r/r3.png' : self.get_img(64, 64),

            './b/b1.png' : self.get_img(0, 96),
            './b/b2.png' : self.get_img(32, 96),
            './b/b3.png' : self.get_img(64, 96),
        }
        self.speed = 4
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
        image = pygame.Surface([31, 31])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32))
        return image


    