from time import sleep
import pygame
from pyscroll import data
import pytmx
import pyscroll
import random

from perso import Player

class Game: #On crée la classe pour le jeu

    def __init__(self): #On définit la fonction qui s'éxécutera au lancement du jeu
        #On crée la fenètre
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Titre du jeu")

        #On charge la carte 
        tmx_data = pytmx.util_pygame.load_pygame('carte.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 3
        
        #On définit les points de sapwn du joueur
        spawn = ('player1_spawn', 'player2_spawn', 'player3_spawn')

        #On récupère la position du joueur initiale grâce aux point de spawn
        player_pos = tmx_data.get_object_by_name(spawn[random.randint(0, 2)])
        self.player = Player(player_pos.x, player_pos.y)
        
        #On définit le temps d'attente entre les frame
        self.ims = 0.09
        
        #On crée le groupe rassemblant les différents layer de la map
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        
        self.group.add(self.player)

        self.nom_bois = 0
        self.nom_pierre = 0

        self.suite_bois = 0
        self.stop_bois = False
        self.stop_stop_bois = 0


        self.suite_pierre = 0
        self.stop_pierre = False
        self.stop_stop_pierre = 0

        self.walls = []
        self.ress_bois = []
        self.ress_pierre = []

        for obj in tmx_data.objects:
            if obj.type == "collision" or obj.type == "collision_eau" or obj.type == "collision_panneau":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            elif obj.type == "collision_bois":
                self.ress_bois.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            elif obj.type == "collision_pierre":
                self.ress_pierre.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))


    def update(self):
        self.group.update()
        pressed = pygame.key.get_pressed()

        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.walls) > -1:
                sprite.move_back()

                
            elif sprite.feet.collidelist(self.ress_bois) > -1:
                sprite.move_back()
                if pressed[pygame.K_a] and self.stop_bois == False:
                    self.suite_bois += 1
                    self.nom_bois += 1
                    print("bois = ",self.nom_bois)
                if self.suite_bois >= 20:
                    self.stop_bois = True
                sleep(0.1)


            elif sprite.feet.collidelist(self.ress_pierre) > -1:
                sprite.move_back()
                if pressed[pygame.K_a] and self.stop_pierre == False:
                    self.suite_pierre += 1
                    self.nom_pierre += 1
                    print("pierre = ",self.nom_pierre)
                if self.suite_pierre >= 20:
                    self.stop_pierre = True
                sleep(0.1)


    def screen_update(self):
        self.group.update()
        self.group.center(self.player.rect.center)
        self.group.draw(self.screen)
        pygame.display.flip()

    def anim_compil(self, anim1, anim2, anim3):
        self.player.animations(anim1)
        self.screen_update()
        sleep(self.ims)
        self.player.animations(anim2)
        self.screen_update()
        sleep(self.ims)
        self.player.animations(anim3)
        self.screen_update()

    def handle_input(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP] or pressed[pygame.K_z]:
            self.player.move_up()
            self.anim_compil('haut1', 'haut3', 'haut2')
        elif pressed[pygame.K_DOWN] or pressed[pygame.K_s]:
            self.player.move_down()
            self.anim_compil('bas1', 'bas3', 'bas2')
        elif pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
            self.player.move_right()
            self.anim_compil('droite1', 'droite3', 'droite2')
        elif pressed[pygame.K_LEFT] or pressed[pygame.K_q]:
            self.player.move_left()
            self.anim_compil('gauche1', 'gauche3', 'gauche2')

    def run(self):

        clock = pygame.time.Clock()

        tourne = True

        while tourne:
            self.player.save_location()
            self.handle_input()
            self.update()
            self.screen_update()

            if self.stop_bois == True:
                self.stop_stop_bois += 1
                #print("bois ", self.stop_stop_bois, " / 500")
                if self.stop_stop_bois >= 500:
                    print("Lest go arbre")
                    self.stop_stop_bois = 0
                    self.suite_bois = 0
                    self.stop_bois = False

            if self.stop_pierre == True:
                self.stop_stop_pierre += 1
                #print("pierre ", self.stop_stop_pierre, " / 500")
                if self.stop_stop_pierre >= 500:
                    print("Lest go pierre")
                    self.stop_stop_pierre = 0
                    self.suite_pierre = 0
                    self.stop_pierre = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    tourne = False

            clock.tick(60)

        pygame.quit()
