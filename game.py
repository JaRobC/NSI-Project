from time import sleep      #
import pygame               #
from pyscroll import data   # On importe les bibliothèques / librairies
import pytmx                #
import pyscroll             #
import random               #

from perso import Player

class Game: #On crée la classe pour le jeu

    def __init__(self): #On définit la fonction qui s'éxécutera au lancement du jeu

        self.world = 'world'

        #On crée la fenètre
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Island of Kingdoms")

        #On charge la carte 
        self.tmx_data = pytmx.util_pygame.load_pygame('carte.tmx')
        map_data = pyscroll.data.TiledMapData(self.tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 3

        #On définit les points de sapwn du joueur
        self.spawn = ('player1_spawn', 'player2_spawn', 'player3_spawn')
        #On récupère la position du joueur initiale grâce aux point de spawn
        self.player_pos = self.tmx_data.get_object_by_name(self.spawn[random.randint(0, 2)])
        self.player = Player(self.player_pos.x, self.player_pos.y)
        
        #On définit le temps d'attente entre les frame
        self.ims = 0.001
        
        #On crée le groupe rassemblant les différents layer de la map
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=7)
        
        #On ajoute le perso à ce groupe
        self.group.add(self.player)

        #On créer les varaibles pour la récupération d'items
        self.nom_bois = 0
        self.nom_pierre = 0

        self.suite_bois = 0
        self.stop_bois = False
        self.stop_stop_bois = 0

        self.suite_pierre = 0
        self.stop_pierre = False
        self.stop_stop_pierre = 0

        self.enter_castle = False

        #On créer les liste pour les collisions
        self.walls = []
        self.ress_bois = []
        self.ress_pierre = []
        self.shop = []
        self.cote_maison = []
        self.castle = []
        self.castle_enter = []
        self.escalier = []

        #On initialise les collisions en créeant des "boites"
        for obj in self.tmx_data.objects:
            if obj.type == "collision" or obj.type == "collision_eau" or obj.type == "collision_panneau":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            elif obj.type == "collision_bois":
                self.ress_bois.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            elif obj.type == "collision_pierre":
                self.ress_pierre.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            elif obj.type == "collision_maison":
                self.shop.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            elif obj.type == "collision_cote_maison":
                self.cote_maison.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            elif obj.type == "collision_castle":
                self.castle.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            elif obj.type == "collision_castle_enter":
                self.castle_enter.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

    def shop_world(self):
        self.world = 'shop'

        #On charge la carte 
        self.tmx_data = pytmx.util_pygame.load_pygame('shop house.tmx')
        map_data = pyscroll.data.TiledMapData(self.tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 3

        #On donne les coordonées de spawn du joueur
        self.player = Player(100, 100)
        
        #On crée le groupe rassemblant les différents layer de la map
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=4)
        
        #On ajoute le perso à ce groupe
        self.group.add(self.player)

        #On créer les liste pour les collisions
        self.escalier = []
        self.walls = []

        #On initialise les collisions en créeant des "boites"
        for obj in self.tmx_data.objects:
            if obj.type == "collision_escalier":
                self.escalier.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            elif obj.type == "collision_walls":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

    def world_world(self):
        self.world = 'world'

        #On charge la carte 
        self.tmx_data = pytmx.util_pygame.load_pygame('carte.tmx')
        map_data = pyscroll.data.TiledMapData(self.tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 3

        #On définit les points de sapwn du joueur
        self.spawn = ('house_exit_spawn', 'house_exit_spawn', 'house_exit_spawn')
        #On récupère la position du joueur initiale grâce aux point de spawn
        self.player_pos = self.tmx_data.get_object_by_name(self.spawn[random.randint(0, 2)])
        self.player = Player(self.player_pos.x, self.player_pos.y)
        
        #On crée le groupe rassemblant les différents layer de la map
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=7)
        
        #On ajoute le perso à ce groupe
        self.group.add(self.player)

        #On créer les liste pour les collisions
        self.walls = []
        self.ress_bois = []
        self.ress_pierre = []
        self.shop = []
        self.cote_maison = []
        self.castle = []
        self.castle_enter = []

        #On initialise les collisions en créeant des "boites"
        for obj in self.tmx_data.objects:
            if obj.type == "collision" or obj.type == "collision_eau" or obj.type == "collision_panneau":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            elif obj.type == "collision_bois":
                self.ress_bois.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            elif obj.type == "collision_pierre":
                self.ress_pierre.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            elif obj.type == "collision_maison":
                self.shop.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            elif obj.type == "collision_cote_maison":
                self.cote_maison.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            elif obj.type == "collision_castle":
                self.castle.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            elif obj.type == "collision_castle_enter":
                self.castle_enter.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

    def update(self): #On créer la fonction qui va gérer les collisions

        #On fait une mise à jour du groupe afin de récupérer les différentes coordonées etc..
        self.group.update()

        #On effectue une variable pour éviter à retaper plusieurs fois la même chose
        pressed = pygame.key.get_pressed()

        for sprite in self.group.sprites():

            if sprite.feet.collidelist(self.walls) > -1 and self.world == 'world': #On vérifie les collisions
                sprite.move_back() #On effectue ce qu'il faut pour lorsqu'il y a collisions

            elif sprite.feet.collidelist(self.ress_bois) > -1 and self.world == 'world': #On vérifie les collisions
                sprite.move_back() #On effectue ce qu'il faut pour lorsqu'il y a collisions
                if pressed[pygame.K_a] and self.stop_bois == False: #On effectue la récupération des items
                    self.suite_bois += 1
                    self.nom_bois += 1
                    print("bois = ",self.nom_bois)
                if self.suite_bois >= 20: #On lance le "timer" pour éviter que la récolte soit infini
                    print("Vous avez atteint votre limite de récolte de bois")
                    self.stop_bois = True
                sleep(0.1)

            elif sprite.feet.collidelist(self.ress_pierre) > -1 and self.world == 'world': #On vérifie les collisions
                sprite.move_back() #On effectue ce qu'il faut pour lorsqu'il y a collisions
                if pressed[pygame.K_a] and self.stop_pierre == False: #On effectue la récupération des items
                    self.suite_pierre += 1
                    self.nom_pierre += 1
                    print("pierre = ",self.nom_pierre)
                if self.suite_pierre >= 20: #On lance le "timer" pour éviter que la récolte soit infini
                    print("Vous avez atteint votre limite de récolte de pierres")
                    self.stop_pierre = True
                sleep(0.1)

            elif sprite.feet.collidelist(self.shop) > -1 and self.world == 'world': #On vérifie les collisions
                #maison = Shop() #On effectue ce qu'il faut pour lorsqu'il y a collisions
                #maison.run()
                self.shop_world()
            
            elif sprite.feet.collidelist(self.cote_maison) > -1 and self.world == 'world': #On vérifie les collisions
                sprite.move_back() #On effectue ce qu'il faut pour lorsqu'il y a collisions

            elif sprite.feet.collidelist(self.castle) > -1 and self.world == 'world': #On vérifie les collisions
                sprite.move_back()
                if pressed[pygame.K_a]:
                    if self.nom_bois >= 40 and self.nom_pierre >= 40:
                        self.enter_castle = True
                        print("Vous avez accès au chateau")
                        self.nom_pierre = self.nom_pierre - 40
                        self.nom_bois = self.nom_pierre - 40
                    else:
                        print("Vous ne pouvez pas avoir accès au château")
                        self.manque_pierre = 40 - self.nom_pierre
                        self.manque_bois = 40 - self.nom_bois
                        print("Il vous manque ", self.manque_bois, " de bois")
                        print("Il vous manque ", self.manque_pierre, " de pierre")
            
            elif sprite.feet.collidelist(self.castle_enter) > -1 and self.world == 'world': #On vérifie les collisions
                if self.enter_castle == False:
                    sprite.move_back()
                    print("Vous n'avez pas accès au chateau")
                    self.manque_pierre = 40 - self.nom_pierre
                    self.manque_bois = 40 - self.nom_bois
                    print("Il vous manque ", self.manque_bois, " de bois")
                    print("Il vous manque ", self.manque_pierre, " de pierre")
                elif self.enter_castle == True:
                    print("ok")

            if sprite.feet.collidelist(self.walls) > -1 and self.world == 'shop': #On vérifie les collisions
                sprite.move_back() #On effectue ce qu'il faut pour lorsqu'il y a collisions

            elif sprite.feet.collidelist(self.escalier) > -1 and self.world == 'shop': #On vérifie les collisions
                self.world_world()

    #On créer une focntion qui vient mettre à jour l'écran
    def screen_update(self):
        self.group.update()
        self.group.center(self.player.rect.center)
        self.group.draw(self.screen)
        pygame.display.flip()

    #On créer une fonction pour effectuer les différentes animations de marche
    def anim_compil(self, anim1, anim2, anim3):
        self.player.animations(anim1)
        self.screen_update() #On met à jour l'écran
        sleep(self.ims)
        self.player.animations(anim2)
        self.screen_update() #On met à jour l'écran
        sleep(self.ims)
        self.player.animations(anim3)
        self.screen_update() #On met à jour l'écran

    #On créer une fonction afin de déplacer le joueur avec les animations
    def handle_input(self):

        pressed = pygame.key.get_pressed() #On effectue une variable pour éviter à retaper plusieurs fois la même chose

        if pressed[pygame.K_UP] or pressed[pygame.K_z]: #Si telles touche préssés....
            self.player.move_up()                       #....Aller dans une direction....
            self.anim_compil('haut1', 'haut3', 'haut2') #....Et effectuer les animations
        elif pressed[pygame.K_DOWN] or pressed[pygame.K_s]: #Si telles touche préssés....
            self.player.move_down()                         #....Aller dans une direction....
            self.anim_compil('bas1', 'bas3', 'bas2')        #....Et effectuer les animations
        elif pressed[pygame.K_RIGHT] or pressed[pygame.K_d]: #Si telles touche préssés....
            self.player.move_right()                         #....Aller dans une direction....
            self.anim_compil('droite1', 'droite3', 'droite2')#....Et effectuer les animations
        elif pressed[pygame.K_LEFT] or pressed[pygame.K_q]:   #Si telles touche préssés....
            self.player.move_left()                           #....Aller dans une direction....
            self.anim_compil('gauche1', 'gauche3', 'gauche2') #....Et effectuer les animations

    #On créer la fonction qui va faire la boucle de notre jeu
    def run(self):

        clock = pygame.time.Clock() #On définit la variable clock pour éviter de retaper plusieurs fois la même chose

        tourne = True

        while tourne: #On lance la boucle

            self.player.save_location() #
            self.handle_input()         #   On effectue les différentes fonctions
            self.update()               #
            self.screen_update()        #

            if self.stop_bois == True: #On effectue le timer de la récolte des items
                self.stop_stop_bois += 1
                if self.stop_stop_bois >= 500:
                    print("Lest go arbre")
                    self.stop_stop_bois = 0
                    self.suite_bois = 0
                    self.stop_bois = False

            if self.stop_pierre == True:  #On effectue le timer de la récolte des items
                self.stop_stop_pierre += 1
                if self.stop_stop_pierre >= 500:
                    print("Lest go pierre")
                    self.stop_stop_pierre = 0
                    self.suite_pierre = 0
                    self.stop_pierre = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT: #On lance la condition si le joueur appuye sur la croix
                    tourne = False #Cela ferme la fenêtre

            clock.tick(60) #On définit les ticks de notre jeu (le temps pour éviter que cela soit trop rapide)

        pygame.quit()