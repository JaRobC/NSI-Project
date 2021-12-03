from time import sleep
import pygame

#On créer la classe joueur qui est un sprite (un personnage)
class Mechant(pygame.sprite.Sprite):

    #On créer la fonction qui s'effectuera au lancement du jeu
    def __init__(self, x, y):
        super().__init__()

        #On charge le perso
        self.sprite_sheet = pygame.image.load('./img/mechant.png')
        self.image = self.get_img(0, 0)
        self.image.set_colorkey([255, 255, 255])
        self.rect = self.image.get_rect()

        #On lui donne ses positions comme étant x et y (modifiable donc)
        self.position = [x, y]

        #On effectue la zone des pieds (zone de collision)
        self.feet = pygame.Rect(0,0, self.rect.width * 0.5, 12)

        #On retiens son ancienne positions
        self.old_position = self.position.copy()

        #On lui donne une vitesse
        self.speed = 8

        self.pv = 10

    #On sauvegarde l'ancienne position
    def save_location(self): self.old_position = self.position.copy()

    #On créer la fonction qui permet de mettre à jour les images du perso
    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    #On créer une fonction qui permet de rétablir l'ancienne pos du joueur
    def move_back(self):
        self.position = self.old_position
        self.update()

    #On créer une fonction pour récup une image
    def get_img(self, x, y):
        image = pygame.Surface([27, 42])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 27, 42))
        return image