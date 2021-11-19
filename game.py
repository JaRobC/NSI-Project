import sys
from time import sleep      #
import pygame
from pygame.constants import K_ESCAPE, KEYDOWN, MOUSEBUTTONDOWN, QUIT               #
from pyscroll import data   # On importe les bibliothèques / librairies
import pytmx                #
import pyscroll             #
import random
from hud import HUD               #
mainClock = pygame.time.Clock()   
                            #
from perso import Player    #
from main import Main

class Game: #On crée la classe pour le jeu

    def __init__(self): #On définit la fonction qui s'éxécutera au lancement du jeu

        self.world = 'world'
        self.hud = HUD()

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
        self.ims = 0.005
        
        #On crée le groupe rassemblant les différents layer de la map
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=7)
        
        #On ajoute le perso à ce groupe
        self.group.add(self.player)
             # 
        self.font = pygame.font.SysFont('Comic Sans MS', 50)                 # 
        self.font2 = pygame.font.SysFont('Comic Sans MS', 30)                #
        self.font_button = pygame.font.SysFont('Comic Sans MS', 30)          # On se charge de la partie de déclaration des principale variable et
        self.background1 = pygame.image.load("./menu/background/bg1.jpg")    # de l'initialisation de base de Pygame.
        self.background2 = pygame.image.load("./menu/background/bg2.png")    #
        self.click = False                                                   #
        self.flag = False 
        self.lvl_sound = 0.5

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

        self.choice = False
        self.money = 0
        self.pv = 100
        self.attack = 10
        self.isMoney = 0
        
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

    def play(self):
            pygame.mixer.music.load("./menu/sound/sound1.mp3")          #
            pygame.mixer.music.play(-1)                                 #
    def pause(self):                                                    #
            pygame.mixer.music.pause()                                  #   Declartion est creation des fonctions de musique qui font nou permettre
    def unpause(self):                                                  #   de pouvoir avoir un mixer music.
            pygame.mixer.music.unpause()                                #
    def soundlvl(self):                                                 #
            pygame.mixer.music.set_volume(self.lvl_sound)                    #

    def draw_text(self, text, font, color, suface, x, y):                 #
            self.textobj = font.render(text, 1, color)                       #   
            self.textrect = self.textobj.get_rect()                               #   Création de la fonction pour pouvoir afficher du text sur le Menu.
            self.textrect.topleft = (x, y)                                   #
            self.screen.blit(self.textobj, self.textrect)                              #

    def draw_numbers(self, variable, color,font, surface, x, y):          #
            self.variableobj = font.render(str(variable), 1, color)          #
            self.variablerect = self.variableobj.get_rect()                       #   Création de la fonction pour pouvoir afficher des nombres sur le Menu.
            self.variablerect.topleft = (x, y)                               #
            self.screen.blit(self.variableobj, self.variablerect)                      #

    # Creation de la feneître principal du Menu.
    def main_menu(self):                                                                
        running = True                                                              
        click = False     

        while running:   

            print(self.lvl_sound)

            # La base de l'écran va être posé ici même, le fond d'écran mais aussi "l'entête" de l'onglet.                                                           
            self.screen.fill((202, 228, 241))                                            
            self.screen.blit(self.background1, (0, 0))                                        
            self.draw_text('Island of Kingdoms', self.font, (255,215,0), self.screen, 50, 40)      
            self.draw_text('Alpha 4.c', self.font2, (255, 255, 255), self.screen, 400, 450)        
            
            # Creation de deux variables (mx et my) qui vont avoir la valeur du curseur de la souris. [**]
            mx , my = pygame.mouse.get_pos()  

            # Creation des variable button qui vont pemettre un echange de entre "page"/onglet de menu.
            button_str = pygame.Rect(50, 100, 200, 50)                  
            button_opt = pygame.Rect(50, 200, 200, 50)
            button_ext = pygame.Rect(50, 300, 200, 50)
            
            # Déclaration des condition de ce qu'il va se passer pour chaque boutton si il est cliquer en faisant appelle à une autre fonction.
            if button_str.collidepoint((mx, my)):
                if click:
                    if self.world == 'shop':
                        self.shop_world()
                    else:
                        self.world_world()
                    running = False
                    self.choice = False
            if button_opt.collidepoint((mx, my)):
                if click:
                    self.options()
            if button_ext.collidepoint((mx, my)):
                if click:
                    main = Main()
                    main.main_menu()

            pygame.draw.rect(self.screen, (0, 255, 0), button_str)                       #
            self.draw_text('RESUME', self.font_button, (255, 255, 255), button_str, 92, 115)   #
            pygame.draw.rect(self.screen, (250, 250, 250), button_opt)                   # Ici c'est partie des dessins de chaqu'un des buttons et du text.
            self.draw_text('OPTIONS', self.font_button, (0, 0, 0), button_opt, 78, 215)       # [-]
            pygame.draw.rect(self.screen, (255, 0, 0), button_ext)                       #
            self.draw_text('EXIT', self.font_button, (225, 255, 255), button_ext, 105, 315)   #
            
            # La variable clique est reset sur false.
            click = False

            for event in pygame.event.get():            #
                if event.type == QUIT:                  #
                    pygame.quit()                       #
                    sys.exit()                          #
                if event.type == KEYDOWN:               #
                    if event.key == K_ESCAPE:           # Déclaration des conditions utilisés pour chaque events (clique, exit...). [*]
                        if self.world == 'shop':
                            self.shop_world()
                        else:
                            self.world_world()
                        running = False
                        self.choice == False                  #
                if event.type == MOUSEBUTTONDOWN:       #
                    if event.button == 1:               #
                        click = True                    #

            # Mise à jour de l'affichage.
            pygame.display.update()

            # On définit les ticks de notre jeu (le temps pour éviter que cela soit trop rapide).
            mainClock.tick(60)

    # Création de la fonction "options" permettant de lancer la feneître d'options.
    def options(self):
        click = False       #
        running = True      # Importation de variable de base et reset de chaque booléean.
        global flag         #
        global lvl_sound    #

        while running:
            self.screen.fill((202, 228, 241))                                        #
            self.screen.blit(self.background2, (0, 0))                                    # Set de base pour la fenaître des options.
            self.draw_text('Options', self.font, (255, 255, 255), self.screen, 20, 20)         #

            # Set du son ( voir le def soundlvl() plus haut).
            self.soundlvl()

            button_sound = pygame.Rect(50, 100, 200, 50)            #
            button_soundneg = pygame.Rect(38, 200, 50, 50)          # Création de chaque button utile aux options.
            button_soundpoz = pygame.Rect(212, 200, 50, 50)         #

            # [**]
            mx , my = pygame.mouse.get_pos()

            if button_sound.collidepoint((mx, my)):
                if self.flag == False: # Utilisation d'un flag pour savoir quand est-ce que nous allons afficher pause sound est unpause sound + ce rappeller de comment était le text.
                    if click:
                        self.pause()
                        self.flag = True
                elif self.flag == True:
                    if click:
                        self.unpause()
                        self.flag = False
            elif button_soundneg.collidepoint((mx, my)):
                if click:
                    self.lvl_sound += -0.1
                    if self.lvl_sound <= 0.0:                        #
                        self.lvl_sound = 0.0                         #
                    elif self.lvl_sound == 0.8999999999999999:       #
                        self.lvl_sound = 0.9                         # Conditions mis en place pour ne pas avoir de problème avec le float car il peut oublier un 0.0001 du à la mémoire alloqué.
                    elif self.lvl_sound == 0.9999999999999999:       # [***]
                        self.lvl_sound = 1.0                         #
                    self.soundlvl()                                  #
                    
            elif button_soundpoz.collidepoint((mx, my)):        
                if click:                                       
                    self.lvl_sound += +0.1                           
                    if self.lvl_sound >= 1.0:                        #
                        self.lvl_sound = 1.0                         #
                    elif self.lvl_sound == 0.8999999999999999:       #
                        self.lvl_sound = 0.9                         # [***]
                    elif self.lvl_sound == 0.9999999999999999:       #
                        self.lvl_sound = 1.0                         #
                    self.soundlvl()                                  #

            pygame.draw.rect(self.screen, (255, 255, 255), button_sound)                         #
            pygame.draw.rect(self.screen, (255, 255, 255), button_soundneg)                      #
            self.draw_text("-", self.font2, (0, 0, 0), button_soundneg, 60, 213)                      #
            pygame.draw.rect(self.screen, (255, 255, 255), button_soundpoz)                      #
            self.draw_text("+", self.font2, (0, 0, 0), button_soundpoz, 230, 213)                     #
            self.draw_text("Volume: ", self.font2, (0, 0, 0), self.screen, 92, 215)                        # [-]
            self.draw_numbers( int(self.lvl_sound * 100), (0, 0, 0), self.font2, self.screen, 175, 215)         #
            if self.flag == False:                                                               #
                self.draw_text('Pause Sound', self.font2, (0, 0, 0), button_sound, 86, 115)           #
            elif self.flag == True:                                                              #
                self.draw_text('Unpause Sound', self.font2, (0, 0, 0), button_sound, 76, 115)         #

            click = False

            for event in pygame.event.get():               #
                if event.type == QUIT:                     #
                    pygame.quit()                          #
                    sys.exit()                             #
                if event.type == MOUSEBUTTONDOWN:          #
                    if event.button == 1:                  #  [*]
                        click = True                       #
                if event.type == KEYDOWN:                  #
                    if event.key == K_ESCAPE:              #
                        running = False                    #
                        self.main_menu()                        #

            pygame.display.update()
            mainClock.tick(60)

    def shop_world(self): #On définit le "switch" pour aller dans le monde du shop
        self.world = 'shop'

        #On charge la carte 
        self.tmx_data = pytmx.util_pygame.load_pygame('shop house.tmx')
        map_data = pyscroll.data.TiledMapData(self.tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 3

        if self.choice == True:
            #On donne les coordonées de spawn du joueur
            self.player = Player(100, 100)
        else:
            #self.spawn = ('player1_spawn', 'player2_spawn', 'player3_spawn')
            #On récupère la position du joueur initiale grâce aux point de spawn
            self.player_pos = self.player.old_position
            self.player = Player(self.player_pos[0], self.player_pos[1])
        
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

    def world_world(self): #On définit le "switch" pour aller dans le monde principale
        self.world = 'world'
        print("ok")
        self.player.save_location()

        #On charge la carte 
        self.tmx_data = pytmx.util_pygame.load_pygame('carte.tmx')
        map_data = pyscroll.data.TiledMapData(self.tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 3


        #On définit les points de sapwn du joueur
        if self.choice == True:
            self.spawn = ('house_exit_spawn', 'house_exit_spawn', 'house_exit_spawn')
            #On récupère la position du joueur initiale grâce aux point de spawn
            self.player_pos = self.tmx_data.get_object_by_name(self.spawn[random.randint(0, 2)])
            self.player = Player(self.player_pos.x, self.player_pos.y)
        else:
            #self.spawn = ('player1_spawn', 'player2_spawn', 'player3_spawn')
            #On récupère la position du joueur initiale grâce aux point de spawn
            self.player_pos = self.player.old_position
            self.player = Player(self.player_pos[0], self.player_pos[1])
            self.choice = True
        
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
                    self.isMoney = random.randint(0, 5)
                    if self.isMoney == 5:
                        self.money += random.randint(0, 5)
                        print(self.money)
                    self.suite_bois += 1
                    self.nom_bois += 1
                    print("bois = ",self.nom_bois)
                    self.hud.textarbre = str(self.nom_bois)
                    self.hud.textpierre = str(self.nom_pierre)
                    self.hud.render(self.screen)
                    pygame.display.flip()
                if self.suite_bois >= 20: #On lance le "timer" pour éviter que la récolte soit infini
                    print("Vous avez atteint votre limite de récolte de bois")
                    self.stop_bois = True
                sleep(0.1)

            elif sprite.feet.collidelist(self.ress_pierre) > -1 and self.world == 'world': #On vérifie les collisions
                sprite.move_back() #On effectue ce qu'il faut pour lorsqu'il y a collisions
                if pressed[pygame.K_a] and self.stop_pierre == False: #On effectue la récupération des items
                    self.isMoney = random.randint(0, 5)
                    if self.isMoney == 5:
                        self.money += random.randint(0, 5)
                        print(self.money)
                    self.suite_pierre += 1
                    self.nom_pierre += 1
                    print("pierre = ",self.nom_pierre)
                    self.hud.textarbre = str(self.nom_bois)
                    self.hud.textpierre = str(self.nom_pierre)
                    self.hud.render(self.screen)
                    pygame.display.flip()
                if self.suite_pierre >= 20: #On lance le "timer" pour éviter que la récolte soit infini
                    print("Vous avez atteint votre limite de récolte de pierres")
                    self.stop_pierre = True
                sleep(0.1)

            elif sprite.feet.collidelist(self.shop) > -1 and self.world == 'world': #On vérifie les collisions
                #maison = Shop() #On effectue ce qu'il faut pour lorsqu'il y a collisions
                #maison.run()
                self.choice = True
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
                        self.nom_bois = self.nom_bois - 40
                    elif self.enter_castle == False:
                        print("Vous ne pouvez pas avoir accès au château")
                        self.manque_pierre = 40 - self.nom_pierre
                        self.manque_bois = 40 - self.nom_bois
                        print("Il vous manque ", self.manque_bois, " de bois")
                        print("Il vous manque ", self.manque_pierre, " de pierre")
                self.hud.textarbre = str(self.nom_bois)
                self.hud.textpierre = str(self.nom_pierre)
                self.hud.render(self.screen)
                pygame.display.flip()
            
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
                self.hud.textarbre = str(self.nom_bois)
                self.hud.textpierre = str(self.nom_pierre)
                self.hud.render(self.screen)
                pygame.display.flip()

            if sprite.feet.collidelist(self.walls) > -1 and self.world == 'shop': #On vérifie les collisions
                sprite.move_back() #On effectue ce qu'il faut pour lorsqu'il y a collisions

            elif sprite.feet.collidelist(self.escalier) > -1 and self.world == 'shop': #On vérifie les collisions
                self.choice = True
                self.world_world()
        
        if pressed[pygame.K_ESCAPE]:
            self.main_menu()

    def screen_update(self): #On créer une fonction qui vient mettre à jour l'écran
        self.group.update()
        self.group.center(self.player.rect.center)
        self.group.draw(self.screen)
        self.hud.textarbre = str(self.nom_bois)
        self.hud.textpierre = str(self.nom_pierre)
        self.hud.render(self.screen)
        if self.stop_bois == True:
            self.stoparbre = self.font.render(self.hud.stoparbre, False, (255,0,0))
            self.screen.blit(self.stoparbre, (200, 260))
        elif self.stop_pierre == True:
            self.stoppierre = self.font.render(self.hud.stoppierre, False, (255, 0, 0))
            self.screen.blit(self.stoppierre, (200, 360))
        pygame.display.flip()

    def anim_compil(self, anim1, anim2, anim3): #On créer une fonction pour effectuer les différentes animations de marche
        self.player.animations(anim1)
        self.screen_update() #On met à jour l'écran
        sleep(self.ims)
        self.player.animations(anim2)
        self.screen_update() #On met à jour l'écran
        sleep(self.ims)
        self.player.animations(anim3)
        self.screen_update() #On met à jour l'écran
        self.hud.textarbre = str(self.nom_bois)
        self.hud.textpierre = str(self.nom_pierre)
        self.hud.render(self.screen)
        if self.stop_bois == True:
            self.stoparbre = self.font.render(self.hud.stoparbre, False, (255,0,0))
            self.screen.blit(self.stoparbre, (200, 260))
        elif self.stop_pierre == True:
            self.stoppierre = self.font.render(self.hud.stoppierre, False, (255, 0, 0))
            self.screen.blit(self.stoppierre, (200, 360))
        pygame.display.flip()

    def handle_input(self): #On créer une fonction afin de déplacer le joueur avec les animations

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

    def run(self): #On créer la fonction qui va faire la boucle de notre jeu

        clock = pygame.time.Clock() #On définit la variable clock pour éviter de retaper plusieurs fois la même chose

        tourne = True

        while tourne: #On lance la boucle

            self.player.save_location() #
            self.handle_input()         #   On effectue les différentes fonctions
            self.update()               #
            self.screen_update()        #
            self.hud.textarbre = str(self.nom_bois)
            self.hud.textpierre = str(self.nom_pierre)
            self.hud.render(self.screen)
            pygame.display.flip()

            if self.stop_bois == True: #On effectue le timer de la récolte des items
                self.stop_stop_bois += 1
                self.stoparbre = self.font.render(self.hud.stoparbre, False, (255,0,0))
                self.screen.blit(self.stoparbre, (200, 260))
                pygame.display.flip()
                if self.stop_stop_bois >= 500:
                    print("Lest go arbre")
                    self.stop_stop_bois = 0
                    self.suite_bois = 0
                    self.stop_bois = False
                    

            if self.stop_pierre == True:  #On effectue le timer de la récolte des items
                self.stop_stop_pierre += 1
                self.stoppierre = self.font.render(self.hud.stoppierre, False, (255, 0, 0))
                self.screen.blit(self.stoppierre, (200, 360))
                pygame.display.flip()
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
