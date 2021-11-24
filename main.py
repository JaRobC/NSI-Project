import pygame, sys, time, tkinter       #
from pygame import draw                 #
from pygame.display import update       # On importe les bibliothèques / librairies
mainClock = pygame.time.Clock()         #
from pygame.locals import *             #
from pygame import mixer                #

class Main:

    def __init__(self):
        pygame.init()

        self.logo = pygame.image.load('logo.png')
        pygame.display.set_icon(self.logo)

        pygame.display.set_caption('Island of Kingdoms - Main Menu')      #
        self.screen = pygame.display.set_mode((1280, 720),0,32)    
        font = pygame.font.SysFont('Comic Sans MS', 50)              # 
        self.font = font  
        font2 = pygame.font.SysFont('Comic Sans MS', 30)   
        self.font2 = font2
        font_button = pygame.font.SysFont('Comic Sans MS', 30)               #
        self.font_button = font_button         # On se charge de la partie de déclaration des principale variable et
        self.background1 = pygame.image.load("./menu/background/bg1.jpg")    # de l'initialisation de base de Pygame.
        self.background2 = pygame.image.load("./menu/background/bg2.png")    #
        self.click = False                                                   #
        self.flag = False    
        self.isPlay = False                                                #
        self.lvl_sound = 0.2  
        
                                          #

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
        if self.isPlay == False:     
            self.play()
            self.isPlay = True

        while running:   
            
            self.soundlvl()

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
            button_ext = pygame.Rect(540, 435, 200, 50)
            
            # Déclaration des condition de ce qu'il va se passer pour chaque boutton si il est cliquer en faisant appelle à une autre fonction.
            if button_str.collidepoint((mx, my)):
                if click:
                    self.game()
            if button_opt.collidepoint((mx, my)):
                if click:
                    self.options()
            if button_ext.collidepoint((mx, my)):
                if click:
                    sys.exit()

            pygame.draw.rect(self.screen, (0, 255, 0), button_str)                       #
            self.draw_text('COMMENCER', self.font_button, (255, 255, 255), button_str, 545, 240)   #
            pygame.draw.rect(self.screen, (250, 250, 250), button_opt)                   # Ici c'est partie des dessins de chaqu'un des bttons et du text.
            self.draw_text('OPTIONS', self.font_button, (0, 0, 0), button_opt, 570, 340)       # [-]
            pygame.draw.rect(self.screen, (255, 0, 0), button_ext)                       #
            self.draw_text('QUITTER', self.font_button, (225, 255, 255), button_ext, 570, 440)   #
            
            # La variable clique est reset sur false.
            click = False

            for event in pygame.event.get():            #
                if event.type == QUIT:                  #
                    pygame.quit()                       #
                    sys.exit()                          #
                if event.type == KEYDOWN:               #
                    if event.key == K_ESCAPE:           # Déclaration des conditions utilisés pour chaque events (clique, exit...). [*]
                        pygame.quit()                   #
                        sys.exit()                      #
                if event.type == MOUSEBUTTONDOWN:       #
                    if event.button == 1:               #
                        click = True                    #

            # Mise à jour de l'affichage.
            pygame.display.update()

            # On définit les ticks de notre jeu (le temps pour éviter que cela soit trop rapide).
            mainClock.tick(60)


    # Creation de la fonction permettant de lancer le jeu à partir du Menu.
    def game(self):
        from game import Game       # 
        pygame.init                 # Importation de la class Game du script game.py permettant de lacer le jeu.
        game = Game()               #
        game.run()                  #

        for event in pygame.event.get():        #
            if event.type == QUIT:              #
                pygame.quit()                   #
                sys.exit()                      #      [*]
            if event.type == KEYDOWN:           #
                if event.key == K_ESCAPE:       #
                    pygame.quit()               #
                    sys.exit()                  #

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