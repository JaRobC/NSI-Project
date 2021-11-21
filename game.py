import sys
from time import sleep      #
import pygame
from pygame.constants import K_ESCAPE, KEYDOWN, MOUSEBUTTONDOWN, QUIT               #
from pyscroll import data   # On importe les bibliothèques / librairies
import pytmx                #
import pyscroll             #
import random
from hud import HUD
from mechant import Mechant               #
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

        self.spawn_mechant = ('mechant_spawn', 'mechant_spawn1', 'mechant_spawn2', 'mechant_spawn4', 'mechant_spawn5', 'mechant_spawn6', 'mechant_spawn7')
        self.mechant_pos = self.tmx_data.get_object_by_name(self.spawn_mechant[random.randint(0, 6)])
        self.mechant = Mechant(self.mechant_pos.x, self.mechant_pos.y)

        #On définit le temps d'attente entre les frame
        self.ims = 0.005
        
        #On crée le groupe rassemblant les différents layer de la map
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=7)
        
        #On ajoute le perso à ce groupe
        self.group.add(self.player)
        self.group.add(self.mechant)

    #################################################################################################

        self.font = pygame.font.SysFont('Comic Sans MS', 50)                 # 
        self.font2 = pygame.font.SysFont('Comic Sans MS', 30)                #
        self.font_button = pygame.font.SysFont('Comic Sans MS', 30)          # On se charge de la partie de déclaration des principale variable et
        self.background1 = pygame.image.load("./menu/background/bg1.jpg")    # de l'initialisation de base de Pygame.
        self.background2 = pygame.image.load("./menu/background/bg2.png")    #
        self.click = False                                                   #
        self.flag = False 
        self.lvl_sound = 0.5

    #################################################################################################

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

    #################################################################################################

        self.choice = False
        self.choice2 = False
        self.money = 0
        self.pv = 100
        self.attack = 10
        self.isMoney = 0

        self.isAchat = False

        self.nom_mechant = 0
        self.isKilling = False
    
    #################################################################################################

        #On créer les liste pour les collisions
        self.walls = []
        self.ress_bois = []
        self.ress_pierre = []
        self.shop = []
        self.cote_maison = []
        self.castle = []
        self.castle_enter = []
        self.escalier = []
        self.collision_panneau = []

        self.collision_attack1 = []
        self.collision_attack2 = []
        self.collision_attack3 = []
        self.collision_attack4 = []

        self.collision_vie1 = []
        self.collision_vie2 = []
        self.collision_vie3 = []
        self.collision_vie4 = []

        self.collision = []
        self.table = []
        self.biblio = []
        self.vendre_bois1 = []
        self.vendre_bois2 = []
        self.vendre_pierre1 = []
        self.vendre_pierre2 = []

    #################################################################################################

        #On initialise les collisions en créeant des "boites"
        for obj in self.tmx_data.objects:
            if obj.type == "collision" or obj.type == "collision_eau":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            elif obj.type == "collision_panneau":
                self.collision_panneau.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
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
            

###########################################################

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

            # La base de l'écran va être posé ici même, le fond d'écran mais aussi "l'entête" de l'onglet.                                                           
            self.screen.fill((202, 228, 241))                                            
            self.screen.blit(self.background1, (0, 0))                                        
            self.draw_text('Island of Kingdoms', self.font, (255,215,0), self.screen, 420, 40)      
            self.draw_text('Alpha 6.d', self.font2, (255, 255, 255), self.screen, 1120, 660)              
            
            # Creation de deux variables (mx et my) qui vont avoir la valeur du curseur de la souris. [**]
            mx , my = pygame.mouse.get_pos()  

            # Creation des variable button qui vont pemettre un echange de entre "page"/onglet de menu.
            button_str = pygame.Rect(540, 235, 200, 50)                  
            button_opt = pygame.Rect(540, 335, 200, 50)
            button_ext = pygame.Rect(520, 435, 240, 50)
            
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
            self.draw_text('REPRENDRE', self.font_button, (255, 255, 255), button_str, 550, 240)   #
            pygame.draw.rect(self.screen, (250, 250, 250), button_opt)                   # Ici c'est partie des dessins de chaqu'un des bttons et du text.
            self.draw_text('OPTIONS', self.font_button, (0, 0, 0), button_opt, 570, 340)       # [-]
            pygame.draw.rect(self.screen, (255, 0, 0), button_ext)                       #
            self.draw_text('RETOUR MENU', self.font_button, (225, 255, 255), button_ext, 530, 440)   #
            
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
            self.draw_text('Options', self.font, (255, 255, 255), self.screen, 551, 40)         #

            # Set du son ( voir le def soundlvl() plus haut).
            self.soundlvl()

            button_sound = pygame.Rect(540, 285, 200, 50)            #
            button_soundneg = pygame.Rect(503, 385, 50, 50)          # Création de chaque button utile aux options.
            button_soundpoz = pygame.Rect(721, 385, 50, 50)         #

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
            self.draw_text("-", self.font2, (0, 0, 0), button_soundneg, 521, 385)                      #
            pygame.draw.rect(self.screen, (255, 255, 255), button_soundpoz)                      #
            self.draw_text("+", self.font2, (0, 0, 0), button_soundpoz, 739, 385)                     #
            self.draw_text("Volume: ", self.font2, (0, 0, 0), self.screen, 558, 385)                        # [-]
            self.draw_numbers(int(self.lvl_sound * 100), (0, 0, 0), self.font2, self.screen, 665, 385)         #
            if self.flag == False:                                                               #
                self.draw_text('Pause', self.font2, (0, 0, 0), button_sound, 600, 290)           #
            elif self.flag == True:                                                              #
                self.draw_text('Reprendre', self.font2, (0, 0, 0), button_sound, 570, 290)         #

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

###########################################################

    def shop_world(self): #On définit le "switch" pour aller dans le monde du shop
        self.world = 'shop'

        #On charge la carte 
        self.tmx_data = pytmx.util_pygame.load_pygame('shop house.tmx')
        map_data = pyscroll.data.TiledMapData(self.tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 3

        if self.choice == True:
            #On donne les coordonées de spawn du joueur
            self.player = Player(265, 150)
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

            elif obj.type == "collision_attack1":
                self.collision_attack1.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            elif obj.type == "collision_attack2":
                self.collision_attack2.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            elif obj.type == "collision_attack3":
                self.collision_attack3.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            elif obj.type == "collision_attack4":
                self.collision_attack4.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

            elif obj.type == "collision_vie1":
                self.collision_vie1.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            elif obj.type == "collision_vie2":
                self.collision_vie2.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            elif obj.type == "collision_vie3":
                self.collision_vie3.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            elif obj.type == "collision_vie4":
                self.collision_vie4.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

    def chateau_world(self): #On définit le "switch" pour aller dans le monde du shop
        self.world = 'chateau'
        self.isAchat = False
        
        #On charge la carte 
        self.tmx_data = pytmx.util_pygame.load_pygame('chateau.tmx')
        map_data = pyscroll.data.TiledMapData(self.tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 3

        if self.choice == True:
            #On donne les coordonées de spawn du joueur
            self.player = Player(265, 150)
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
        self.collision = []

        #On initialise les collisions en créeant des "boites"
        for obj in self.tmx_data.objects:
            if obj.type == "collision_escalier":
                self.escalier.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            elif obj.type == "collision":
                self.collision.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            if obj.type == "collision_table":
                self.table.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            elif obj.type == "collision_book":
                self.biblio.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

            elif obj.type == "collision_vendre1":
                self.vendre_bois1.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            elif obj.type == "collision_vendre2":
                self.vendre_bois2.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            elif obj.type == "collision_vendre3":
                self.vendre_pierre1.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            elif obj.type == "collision_vendre4":
                self.vendre_pierre2.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

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
        elif self.choice == True:
            #self.spawn = ('player1_spawn', 'player2_spawn', 'player3_spawn')
            #On récupère la position du joueur initiale grâce aux point de spawn
            self.player_pos = self.player.old_position
            self.player = Player(self.player_pos[0], self.player_pos[1])
            self.choice = True
        elif self.choice2 == True:
            self.spawn = ('castle_exit_spawn', 'castle_exit_spawn', 'castle_exit_spawn')
            #On récupère la position du joueur initiale grâce aux point de spawn
            self.player_pos = self.tmx_data.get_object_by_name(self.spawn[random.randint(0, 2)])
            self.player = Player(self.player_pos.x, self.player_pos.y)
        
        
        #On crée le groupe rassemblant les différents layer de la map
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=7)
        
        self.spawn_mechant = ('mechant_spawn', 'mechant_spawn1', 'mechant_spawn2', 'mechant_spawn4', 'mechant_spawn5', 'mechant_spawn6', 'mechant_spawn7')
        self.mechant_pos = self.tmx_data.get_object_by_name(self.spawn_mechant[random.randint(0, 6)])
        self.mechant = Mechant(self.mechant_pos.x, self.mechant_pos.y)
        self.group.add(self.mechant)

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

###########################################################

    def render_hud(self):

        self.hud.textvie = str(self.pv)
        self.hud.textarbre = str(self.nom_bois)
        self.hud.textpierre = str(self.nom_pierre)
        self.hud.textmoney = str(self.money)
        self.hud.textdegats = str(self.attack)
        self.hud.textzombie = str(self.nom_mechant)
        if self.stop_bois == True:
            self.stoparbre = self.hud.font_warning.render(self.hud.stoparbre, False, (255,0,0))
            self.screen.blit(self.stoparbre, (10, 600))
        if self.stop_pierre == True:
            self.stoppierre = self.hud.font_warning.render(self.hud.stoppierre, False, (255, 0, 0))
            self.screen.blit(self.stoppierre, (10, 650))
        if self.world == 'world':
            self.hud.render(self.screen, (0, 0, 0))
        if self.world == 'shop':
            self.hud.render(self.screen, (255, 255, 255))
        if self.world == 'chateau':
            self.hud.render(self.screen, (255, 255, 255))
        pygame.display.flip()

###########################################################

    def shop_achat_attack(self, pressed, condition, prix, augmente, plus):

        if pressed[pygame.K_a] and self.money >= prix and condition == True:
            self.money = self.money - prix
            print("ton argent restant est:", self.money)
            self.attack = self.attack + plus
            print("les dégats sont augmenté de ", prix, ". Ils sont donc à :", self.attack)
            sleep(0.1)

    def shop_achat_pv(self, pressed, condition, prix, augmente, plus):

        if pressed[pygame.K_a] and self.money >= prix and condition == True:
            self.money = self.money - prix
            print("ton argent restant est:", self.money)
            self.pv = self.pv + plus
            print("les points de vie sont augmenté de ", prix, ". Ils sont donc à :", self.pv)
            sleep(0.1)

    def shop_vendre_buche(self, pressed, condition, nom_bois, augmente, plus):

        if pressed[pygame.K_a] and self.nom_bois >= nom_bois and condition == True:
            self.nom_bois = self.nom_bois - nom_bois
            print("ton nombre de buche restant est:", self.nom_bois)
            self.money = self.money + plus
            print("ton argent est augmenté ", plus, ". Ils sont donc à :", self.money)
            sleep(0.1)

    def shop_vendre_pierre(self, pressed, condition, nom_pierre, augmente, plus):

        if pressed[pygame.K_a] and self.nom_pierre >= nom_pierre and condition == True:
            self.nom_pierre = self.nom_pierre - nom_pierre
            print("ton nombre de pierre restant est:", self.nom_pierre)
            self.money = self.money + plus
            print("ton argent est augmenté ", plus, ". Ils sont donc à :", self.money)
            sleep(0.1)

    def isDead(self):
        if self.mechant.pv <= 0:
            self.nom_mechant += 1
            if random.randint(0, 2) == 0:
                if self.nom_mechant >= 0 and self.nom_mechant <= 20:
                    self.money += 15
                elif self.nom_mechant >= 21 and self.nom_mechant <= 50:
                    self.money += 30
                elif self.nom_mechant >= 51 and self.nom_mechant <= 100:
                    self.money += 60
            elif random.randint(0, 2) == 1:
                if self.nom_mechant >= 0 and self.nom_mechant <= 20:
                    self.nom_bois += 5
                elif self.nom_mechant >= 21 and self.nom_mechant <= 50:
                    self.nom_bois += 10
                elif self.nom_mechant >= 51 and self.nom_mechant <= 100:
                    self.nom_bois += 20
            elif random.randint(0, 2) == 2:
                if self.nom_mechant >= 0 and self.nom_mechant <= 20:
                    self.nom_pierre += 5
                elif self.nom_mechant >= 21 and self.nom_mechant <= 50:
                    self.nom_pierre += 10
                elif self.nom_mechant >= 51 and self.nom_mechant <= 100:
                    self.nom_pierre += 20
            self.isKilling = False
            self.mechant.kill()
            sleep(0.1)
            self.spawn_mechant = ('mechant_spawn', 'mechant_spawn1', 'mechant_spawn2', 'mechant_spawn4', 'mechant_spawn5', 'mechant_spawn6', 'mechant_spawn7')
            self.mechant_pos = self.tmx_data.get_object_by_name(self.spawn_mechant[random.randint(0, 6)])
            self.mechant = Mechant(self.mechant_pos.x, self.mechant_pos.y)
            self.group.add(self.mechant)


###########################################################

    def update(self): #On créer la fonction qui va gérer les collisions

        #On fait une mise à jour du groupe afin de récupérer les différentes coordonées etc..
        self.group.update()

        #On effectue une variable pour éviter à retaper plusieurs fois la même chose
        pressed = pygame.key.get_pressed()

    #################################################################################################

        for sprite in self.group.sprites():

            if sprite.feet.collidelist(self.walls) > -1 and self.world == 'world': #On vérifie les collisions
                sprite.move_back() #On effectue ce qu'il faut pour lorsqu'il y a collisions

            elif sprite.feet.collidelist(self.collision_panneau) > -1 and self.world == 'world':
                sprite.move_back()
                if pressed[pygame.K_a]:
                    self.pause()
                    self.hud.panneau(self.screen)
                    pygame.display.flip()
                    sleep(3)
                    self.play()

            elif sprite.feet.collidelist(self.ress_bois) > -1 and self.world == 'world': #On vérifie les collisions
                sprite.move_back() #On effectue ce qu'il faut pour lorsqu'il y a collisions
                if pressed[pygame.K_a] and self.stop_bois == False: #On effectue la récupération des items
                    self.isMoney = random.randint(0, 5)
                    if self.isMoney == 5:
                        self.money += random.randint(0, 5)
                        print(self.money)
                    if self.attack >= 0 and self.attack <= 20:
                        self.nom_bois += 1
                    elif self.attack >= 21 and self.attack <= 50:
                        self.nom_bois += 3
                    elif self.attack >= 51:
                        self.nom_bois += 5
                    self.pv = self.pv - 1
                    self.suite_bois += 1
                    print("bois = ",self.nom_bois)
                    self.render_hud()
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
                    if self.attack >= 0 and self.attack <= 20:
                        self.nom_pierre += 1
                    elif self.attack >= 21 and self.attack <= 50:
                        self.nom_pierre += 3
                    elif self.attack >= 51:
                        self.nom_pierre += 5
                    self.pv = self.pv - 2
                    self.suite_pierre += 1
                    print("pierre = ",self.nom_pierre)
                    self.render_hud()
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
                if pressed[pygame.K_a] and self.enter_castle == False:
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
                self.render_hud()
            
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
                    self.choice = True
                    self.chateau_world()
                self.render_hud()

    #################################################################################################

            elif sprite.feet.collidelist(self.walls) > -1 and self.world == 'shop': #On vérifie les collisions
                sprite.move_back() #On effectue ce qu'il faut pour lorsqu'il y a collisions

            elif sprite.feet.collidelist(self.escalier) > -1 and self.world == 'shop': #On vérifie les collisions
                self.choice = True

                self.isAchat = False

                self.hud.attack1 = False
                self.hud.attack2 = False
                self.hud.attack3 = False
                self.hud.attack4 = False

                self.hud.vie1 = False
                self.hud.vie2 = False
                self.hud.vie3 = False
                self.hud.vie4 = False
                self.world_world()

            elif sprite.feet.collidelist(self.collision) > -1 and self.world == 'chateau': #On vérifie les collisions
                sprite.move_back() #On effectue ce qu'il faut pour lorsqu'il y a collisions

            elif sprite.feet.collidelist(self.biblio) > -1 and self.world == 'chateau': #On vérifie les collisions
                sprite.move_back() #On effectue ce qu'il faut pour lorsqu'il y a collisions
            
            elif sprite.feet.collidelist(self.escalier) > -1 and self.world == 'chateau': #On vérifie les collisions
                self.choice2 = True
                self.choice = False
                self.world_world()

            elif sprite.feet.collidelist(self.table) > -1 and self.world == 'chateau': #On vérifie les collisions
                sprite.move_back() #On effectue ce qu'il faut pour lorsqu'il y a collisions

    #################################################################################################

            elif sprite.feet.collidelist(self.collision_attack1) > -1 and self.world == 'shop': #On vérifie les collisions  :
                if self.isAchat == False:
                    self.hud.attack1 = True
                    self.isAchat = True
                sprite.move_back()#On effectue ce qu'il faut pour lorsqu'il y a collisions

            elif sprite.feet.collidelist(self.collision_attack2) > -1 and self.world == 'shop': #On vérifie les collisions  :
                if self.isAchat == False:
                    self.hud.attack2 = True
                    self.isAchat = True
                sprite.move_back()#On effectue ce qu'il faut pour lorsqu'il y a collisions

            elif sprite.feet.collidelist(self.collision_attack3) > -1 and self.world == 'shop': #On vérifie les collisions  :
                if self.isAchat == False:
                    self.hud.attack3 = True
                    self.isAchat = True
                sprite.move_back()#On effectue ce qu'il faut pour lorsqu'il y a collisions

            elif sprite.feet.collidelist(self.collision_attack4) > -1 and self.world == 'shop': #On vérifie les collisions  :
                if self.isAchat == False:
                    self.hud.attack4 = True
                    self.isAchat = True
                sprite.move_back()#On effectue ce qu'il faut pour lorsqu'il y a collisions

            elif sprite.feet.collidelist(self.collision_vie1) > -1 and self.world == 'shop': #On vérifie les collisions  :
                if self.isAchat == False:
                    self.hud.vie1 = True
                    self.isAchat = True
                sprite.move_back()#On effectue ce qu'il faut pour lorsqu'il y a collisions

            elif sprite.feet.collidelist(self.collision_vie2) > -1 and self.world == 'shop': #On vérifie les collisions  :
                if self.isAchat == False:
                    self.hud.vie2 = True
                    self.isAchat = True
                sprite.move_back()#On effectue ce qu'il faut pour lorsqu'il y a collisions

            elif sprite.feet.collidelist(self.collision_vie3) > -1 and self.world == 'shop': #On vérifie les collisions  :
                if self.isAchat == False:
                    self.hud.vie3 = True
                    self.isAchat = True
                sprite.move_back()#On effectue ce qu'il faut pour lorsqu'il y a collisions

            elif sprite.feet.collidelist(self.collision_vie4) > -1 and self.world == 'shop': #On vérifie les collisions  :
                if self.isAchat == False:
                    self.hud.vie4 = True
                    self.isAchat = True
                sprite.move_back()#On effectue ce qu'il faut pour lorsqu'il y a collisions

            elif sprite.feet.collidelist(self.vendre_bois1) > -1 and self.world == 'chateau': #On vérifie les collisions  :
                if self.isAchat == False:
                    self.hud.buche1 = True
                    self.isAchat = True
                sprite.move_back()#On effectue ce qu'il faut pour lorsqu'il y a collisions
            
            elif sprite.feet.collidelist(self.vendre_bois2) > -1 and self.world == 'chateau': #On vérifie les collisions  :
                if self.isAchat == False:
                    self.hud.buche2 = True
                    self.isAchat = True
                sprite.move_back()#On effectue ce qu'il faut pour lorsqu'il y a collisions

            elif sprite.feet.collidelist(self.vendre_pierre1) > -1 and self.world == 'chateau': #On vérifie les collisions  :
                if self.isAchat == False:
                    self.hud.pierre1 = True
                    self.isAchat = True
                sprite.move_back()#On effectue ce qu'il faut pour lorsqu'il y a collisions

            elif sprite.feet.collidelist(self.vendre_pierre2) > -1 and self.world == 'chateau': #On vérifie les collisions  :
                if self.isAchat == False:
                    self.hud.pierre2 = True
                    self.isAchat = True
                sprite.move_back()#On effectue ce qu'il faut pour lorsqu'il y a collisions

        if pygame.sprite.collide_rect(self.player, self.mechant):
            if self.isKilling == False:
                if self.nom_mechant >= 0 and self.nom_mechant <= 20:
                    self.mechant.pv = 10
                    self.pv = self.pv - 1
                elif self.nom_mechant >= 21 and self.nom_mechant <= 50:
                    self.mechant.pv = 25
                    self.pv = self.pv - 3
                elif self.nom_mechant >= 51 and self.nom_mechant <= 100:
                    self.mechant.pv = 50
                    self.pv = self.pv - 5
            if self.nom_mechant >= 0 and self.nom_mechant <= 20:
                    self.pv = self.pv - 1
            elif self.nom_mechant >= 21 and self.nom_mechant <= 50:
                    self.pv = self.pv - 3
            elif self.nom_mechant >= 51 and self.nom_mechant <= 100:
                    self.pv = self.pv - 5
            sleep(0.1)
            if pressed[pygame.K_a] and (self.attack >= 0 and self.attack <= 20):
                self.mechant.pv = self.mechant.pv - 2
                self.isKilling = True
                self.isDead()
                print(self.mechant.pv)
                print(self.nom_mechant)
                sleep(0.1)
            elif pressed[pygame.K_a] and (self.attack >= 21 and self.attack <= 50):
                self.mechant.pv = self.mechant.pv - 5
                self.isKilling = True
                self.isDead()
                print(self.mechant.pv)
                print(self.nom_mechant)
                sleep(0.1)
            elif pressed[pygame.K_a] and (self.attack >= 51):
                self.mechant.pv = self.mechant.pv - 7
                self.isKilling = True
                self.isDead()
                print(self.mechant.pv)
                print(self.nom_mechant)
                sleep(0.1)
            self.player.move_back()

        if pressed[pygame.K_KP_ENTER] and self.hud.attack1 == True:
            self.hud.attack1 = False
            self.isAchat = False
        self.shop_achat_attack(pressed, self.hud.attack1, 5, self.attack, 5)

        if pressed[pygame.K_KP_ENTER] and self.hud.attack2 == True:
            self.hud.attack2 = False
            self.isAchat = False
        self.shop_achat_attack(pressed, self.hud.attack2, 20, self.attack, 10)

        if pressed[pygame.K_KP_ENTER] and self.hud.attack3 == True:
            self.hud.attack3 = False
            self.isAchat = False
        self.shop_achat_attack(pressed, self.hud.attack3, 75, self.attack, 50)

        if pressed[pygame.K_KP_ENTER] and self.hud.attack4 == True:
            self.hud.attack4 = False
            self.isAchat = False
        self.shop_achat_attack(pressed, self.hud.attack4, 200, self.attack, 100)

        if pressed[pygame.K_KP_ENTER] and self.hud.vie1 == True:
            self.hud.vie1 = False
            self.isAchat = False
        self.shop_achat_pv(pressed, self.hud.vie1, 5, self.pv, 5)

        if pressed[pygame.K_KP_ENTER] and self.hud.vie2 == True:
            self.hud.vie2 = False
            self.isAchat = False
        self.shop_achat_pv(pressed, self.hud.vie2, 20, self.pv, 10)

        if pressed[pygame.K_KP_ENTER] and self.hud.vie3 == True:
            self.hud.vie3 = False
            self.isAchat = False
        self.shop_achat_pv(pressed, self.hud.vie3, 75, self.pv, 50)

        if pressed[pygame.K_KP_ENTER] and self.hud.vie4 == True:
            self.hud.vie4 = False
            self.isAchat = False
        self.shop_achat_pv(pressed, self.hud.vie4, 200, self.pv, 100)

        if pressed[pygame.K_KP_ENTER] and self.hud.buche1 == True:
            self.hud.buche1 = False
            self.isAchat = False
        self.shop_vendre_buche(pressed, self.hud.buche1, 1, self.pv, 10)

        if pressed[pygame.K_KP_ENTER] and self.hud.buche2 == True:
            self.hud.buche2 = False
            self.isAchat = False
        self.shop_vendre_buche(pressed, self.hud.buche2, 10, self.pv, 100)

        if pressed[pygame.K_KP_ENTER] and self.hud.pierre1 == True:
            self.hud.pierre1 = False
            self.isAchat = False
        self.shop_vendre_pierre(pressed, self.hud.pierre1, 1, self.pv, 12)

        if pressed[pygame.K_KP_ENTER] and self.hud.pierre2 == True:
            self.hud.pierre2 = False
            self.isAchat = False
        self.shop_vendre_pierre(pressed, self.hud.pierre2, 10, self.pv, 120)

    #################################################################################################
        
        if pressed[pygame.K_ESCAPE]:
            self.main_menu()

        if pressed[pygame.K_LCTRL] and pressed[pygame.K_m] and pressed[pygame.K_LALT]:
            self.money += 10000
            sleep(0.1) 
        
        if pressed[pygame.K_LCTRL] and pressed[pygame.K_p] and pressed[pygame.K_LALT]:
            self.nom_pierre += 10000
            sleep(0.1) 

        if pressed[pygame.K_LCTRL] and pressed[pygame.K_b] and pressed[pygame.K_LALT]:
            self.nom_bois += 10000 
            sleep(0.1)

        if self.pv <= 0:
            main = Main()
            main.main_menu()

###########################################################

    def screen_update(self): #On créer une fonction qui vient mettre à jour l'écran
        self.group.update()
        self.group.center(self.player.rect.center)
        self.group.draw(self.screen)
        self.render_hud()

    def anim_compil(self, anim1, anim2, anim3): #On créer une fonction pour effectuer les différentes animations de marche
        self.player.animations(anim1)
        self.screen_update() #On met à jour l'écran
        sleep(self.ims)
        self.player.animations(anim2)
        self.screen_update() #On met à jour l'écran
        sleep(self.ims)
        self.player.animations(anim3)
        self.screen_update() #On met à jour l'écran
        self.render_hud()

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

            #################################################################################################

            self.player.save_location() #
            self.handle_input()         #   On effectue les différentes fonctions
            self.update()               #
            self.screen_update()        #
            self.render_hud()

            #################################################################################################

            if self.stop_bois == True: #On effectue le timer de la récolte des items
                self.stop_stop_bois += 1
                self.render_hud()
                if self.stop_stop_bois >= 500:
                    print("Lest go arbre")
                    self.stop_stop_bois = 0
                    self.suite_bois = 0
                    self.stop_bois = False

            if self.stop_pierre == True:  #On effectue le timer de la récolte des items
                self.stop_stop_pierre += 1
                self.render_hud()
                if self.stop_stop_pierre >= 500:
                    print("Lest go pierre")
                    self.stop_stop_pierre = 0
                    self.suite_pierre = 0
                    self.stop_pierre = False

            #################################################################################################

            for event in pygame.event.get():
                if event.type == pygame.QUIT: #On lance la condition si le joueur appuye sur la croix
                    tourne = False #Cela ferme la fenêtre

            clock.tick(60) #On définit les ticks de notre jeu (le temps pour éviter que cela soit trop rapide)

        pygame.quit()
