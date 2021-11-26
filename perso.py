from time import sleep
import pygame

#On créer la classe joueur qui est un sprite (un personnage)
class Player(pygame.sprite.Sprite):

    #On créer la fonction qui s'effectuera au lancement du jeu
    def __init__(self, x, y):
        super().__init__()

        #On charge le perso
        self.sprite_sheet = pygame.image.load('perso.png')
        self.image = self.get_img(34, 0)
        self.image.set_colorkey([255, 255, 255])
        self.rect = self.image.get_rect()

        #On lui donne ses positions comme étant x et y (modifiable donc)
        self.position = [x, y]

        #On attribue les différentes images selon l'animation
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

        #On effectue la zone des pieds (zone de collision)
        self.feet = pygame.Rect(0,0, self.rect.width * 0.5, 12)

        #On retiens son ancienne positions
        self.old_position = self.position.copy()

        #On lui donne une vitesse
        self.speed = 10

    #On créer la fonction qui nous permet de récupérer les images pour ensuite les animer (les mettres de bout en bout en gros)
    def animations(self, anim_name):
        self.image = self.images_pos[anim_name]
        self.image.set_colorkey([255, 255, 255])
        self.rect = self.image.get_rect()
        self.update() #On update l'image du perso

    #On définit la vitesse selon le mouvement du perso
    def move_right(self): self.position[0] += self.speed
    def move_left(self): self.position[0] -= self.speed
    def move_up(self): self.position[1] -= self.speed
    def move_down(self): self.position[1] += self.speed

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
        image = pygame.Surface([32, 32])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32))
        return image