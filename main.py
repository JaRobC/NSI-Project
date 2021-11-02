import pygame, sys, time
mainClock = pygame.time.Clock()
from pygame.locals import *
from pygame import mixer


pygame.init()
pygame.display.set_caption('Island of Kingdoms Main Menu')
screen = pygame.display.set_mode((500, 500),0,32)
font = pygame.font.SysFont('Comic Sans MS', 50)
font2 = pygame.font.SysFont('Comic Sans MS', 20)

font_button = pygame.font.SysFont('Comic Sans MS', 30)


mixer.init()
mixer.music.load("./menu/sound/sound1.wav")
mixer.music.set_volume(0.7)
mixer.music.play()

def music_pause():
    mixer.music.pause()


def draw_text(text, font, color, suface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    screen.blit(textobj, textrect)

background1 = pygame.image.load("./menu/background/bg1.jpg")
background2 = pygame.image.load("./menu/background/bg2.png")
click = False

def main_menu():
    while True:

        screen.fill((202, 228, 241))
        screen.blit(background1, (0, 0))
        draw_text('Island of Kingdoms', font, (255,215,0), screen, 50, 40)
        draw_text('Alpha 3.0', font2, (255, 255, 255), screen, 400, 450)

        mx , my = pygame.mouse.get_pos()
        button_str = pygame.Rect(50, 100, 200, 50)
        button_opt = pygame.Rect(50, 200, 200, 50)
        button_ext = pygame.Rect(50, 300, 200, 50)

        if button_str.collidepoint((mx, my)):
            if click:
                game()
        if button_opt.collidepoint((mx, my)):
            if click:
                options()
        if button_ext.collidepoint((mx, my)):
            if click:
                exit()

        pygame.draw.rect(screen, (0, 255, 0), button_str)

        draw_text('START', font_button, (255, 255, 255), button_str, 92, 108)
        
        pygame.draw.rect(screen, (250, 250, 250), button_opt)

        draw_text('OPTIONS', font_button, (0, 0, 0), button_opt, 78, 208)

        pygame.draw.rect(screen, (255, 0, 0), button_ext)
        draw_text('EXIT', font_button, (225, 255, 255), button_ext, 105, 308)
        

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

        

def game():
    from game import Game
    pygame.init
    game = Game()
    game.run()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

def options():
    running = True
    while running:
        screen.fill((202, 228, 241))
        screen.blit(background2, (0, 0))

        draw_text('Options', font, (255, 255, 255), screen, 20, 20)

        button_stopsound = pygame.Rect(50, 100, 200, 50)

        mx , my = pygame.mouse.get_pos()

        if button_stopsound.collidepoint((mx, my)):

            if click:
                pass
            elif click:
                pass

        pygame.draw.rect(screen, (255, 255, 255), button_stopsound)

        if mixer.music.play:
            draw_text('Stop Music', font_button, (0, 0, 0), button_stopsound, 55, 108)
        else:
            draw_text('Play Music', font_button, (0, 0, 0), button_stopsound, 55, 108)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)



def exit():
    running = True
    while running:
        exit()

main_menu()