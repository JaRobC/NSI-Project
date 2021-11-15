import pygame, sys, time, tkinter       #
from pygame import draw                 #
from pygame.display import update       # On importe les bibliothèques / librairies
mainClock = pygame.time.Clock()         #
from pygame.locals import *             #
from pygame import mixer                #

pygame.init()
pygame.display.set_caption('Island of Kingdoms Main Menu')      #
screen = pygame.display.set_mode((500, 500),0,32)               # 
font = pygame.font.SysFont('Comic Sans MS', 50)                 # 
font2 = pygame.font.SysFont('Comic Sans MS', 30)                #
font_button = pygame.font.SysFont('Comic Sans MS', 30)          # On se charge de la partie de déclaration des principale variable et
background1 = pygame.image.load("./menu/background/bg1.jpg")    # de l'initialisation de base de Pygame.
background2 = pygame.image.load("./menu/background/bg2.png")    #
click = False                                                   #
flag = False                                                    #
lvl_sound = 0.5                                                 #

def play():
    pygame.mixer.music.load("./menu/sound/sound1.mp3")          #
    pygame.mixer.music.play(-1)                                 #
def pause():                                                    #
    pygame.mixer.music.pause()                                  #   Declartion est creation des fonctions de musique qui font nou permettre
def unpause():                                                  #   de pouvoir avoir un mixer music.
    pygame.mixer.music.unpause()                                #
def soundlvl():                                                 #
    pygame.mixer.music.set_volume(lvl_sound)                    #

def draw_text(text, font, color, suface, x, y):                 #
    textobj = font.render(text, 1, color)                       #   
    textrect = textobj.get_rect()                               #   Création de la fonction pour pouvoir afficher du text sur le Menu.
    textrect.topleft = (x, y)                                   #
    screen.blit(textobj, textrect)                              #

def numbers_draw(variable, color,font, surface, x, y):          #
    variableobj = font.render(str(variable), 1, color)          #
    variablerect = variableobj.get_rect()                       #   Création de la fonction pour pouvoir afficher des nombres sur le Menu.
    variablerect.topleft = (x, y)                               #
    screen.blit(variableobj, variablerect)                      #


# Simple lecture de la musique.
play()

# Creation de la feneître principal du Menu.
def main_menu():                                                                
    running = True                                                              
    click = False                                                               
    while running:   

        # La base de l'écran va être posé ici même, le fond d'écran mais aussi "l'entête" de l'onglet.                                                           
        screen.fill((202, 228, 241))                                            
        screen.blit(background1, (0, 0))                                        
        draw_text('Island of Kingdoms', font, (255,215,0), screen, 50, 40)      
        draw_text('Alpha 4.c', font2, (255, 255, 255), screen, 400, 450)        
        
        # Creation de deux variables (mx et my) qui vont avoir la valeur du curseur de la souris. [**]
        mx , my = pygame.mouse.get_pos()  

        # Creation des variable button qui vont pemettre un echange de entre "page"/onglet de menu.
        button_str = pygame.Rect(50, 100, 200, 50)                  
        button_opt = pygame.Rect(50, 200, 200, 50)
        button_ext = pygame.Rect(50, 300, 200, 50)
        
        # Déclaration des condition de ce qu'il va se passer pour chaque boutton si il est cliquer en faisant appelle à une autre fonction.
        if button_str.collidepoint((mx, my)):
            if click:
                game()
        if button_opt.collidepoint((mx, my)):
            if click:
                options()
        if button_ext.collidepoint((mx, my)):
            if click:
                sys.exit()

        pygame.draw.rect(screen, (0, 255, 0), button_str)                       #
        draw_text('START', font_button, (255, 255, 255), button_str, 92, 115)   #
        pygame.draw.rect(screen, (250, 250, 250), button_opt)                   # Ici c'est partie des dessins de chaqu'un des bttons et du text.
        draw_text('OPTIONS', font_button, (0, 0, 0), button_opt, 78, 215)       # [-]
        pygame.draw.rect(screen, (255, 0, 0), button_ext)                       #
        draw_text('EXIT', font_button, (225, 255, 255), button_ext, 105, 315)   #
        
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
def game():
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
def options():
    click = False       #
    running = True      # Importation de variable de base et reset de chaque booléean.
    global flag         #
    global lvl_sound    #

    while running:
        screen.fill((202, 228, 241))                                        #
        screen.blit(background2, (0, 0))                                    # Set de base pour la fenaître des options.
        draw_text('Options', font, (255, 255, 255), screen, 20, 20)         #

        # Set du son ( voir le def soundlvl() plus haut).
        soundlvl()

        button_sound = pygame.Rect(50, 100, 200, 50)            #
        button_soundneg = pygame.Rect(38, 200, 50, 50)          # Création de chaque button utile aux options.
        button_soundpoz = pygame.Rect(212, 200, 50, 50)         #

        # [**]
        mx , my = pygame.mouse.get_pos()

        if button_sound.collidepoint((mx, my)):
            if flag == False: # Utilisation d'un flag pour savoir quand est-ce que nous allons afficher pause sound est unpause sound + ce rappeller de comment était le text.
                if click:
                    pause()
                    flag = True
            elif flag == True:
                if click:
                    unpause()
                    flag = False
        elif button_soundneg.collidepoint((mx, my)):
            if click:
                lvl_sound += -0.1
                if lvl_sound <= 0.0:                        #
                    lvl_sound = 0.0                         #
                elif lvl_sound == 0.8999999999999999:       #
                    lvl_sound = 0.9                         # Conditions mis en place pour ne pas avoir de problème avec le float car il peut oublier un 0.0001 du à la mémoire alloqué.
                elif lvl_sound == 0.9999999999999999:       # [***]
                    lvl_sound = 1.0                         #
                soundlvl()                                  #
                
        elif button_soundpoz.collidepoint((mx, my)):        
            if click:                                       
                lvl_sound += +0.1                           
                if lvl_sound >= 1.0:                        #
                    lvl_sound = 1.0                         #
                elif lvl_sound == 0.8999999999999999:       #
                    lvl_sound = 0.9                         # [***]
                elif lvl_sound == 0.9999999999999999:       #
                    lvl_sound = 1.0                         #
                soundlvl()                                  #

        pygame.draw.rect(screen, (255, 255, 255), button_sound)                         #
        pygame.draw.rect(screen, (255, 255, 255), button_soundneg)                      #
        draw_text("-", font2, (0, 0, 0), button_soundneg, 60, 213)                      #
        pygame.draw.rect(screen, (255, 255, 255), button_soundpoz)                      #
        draw_text("+", font2, (0, 0, 0), button_soundpoz, 230, 213)                     #
        draw_text("Volume: ", font2, (0, 0, 0), screen, 92, 215)                        # [-]
        numbers_draw( int(lvl_sound * 100), (0, 0, 0), font2, screen, 175, 215)         #
        if flag == False:                                                               #
            draw_text('Pause Sound', font2, (0, 0, 0), button_sound, 86, 115)           #
        elif flag == True:                                                              #
            draw_text('Unpause Sound', font2, (0, 0, 0), button_sound, 76, 115)         #

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
                    main_menu()                        #

        pygame.display.update()
        mainClock.tick(60)

# Lancement du menu comme un run().
main_menu()