import pygame
import button
from game import Game
pygame.init()

size = width, height = 1280, 720
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Main Menu -- Island of Kingdoms")
background = pygame.image.load("background.png")

start_img = pygame.image.load('./menu_pics/start.png').convert_alpha()
exit_img = pygame.image.load('./menu_pics/exit.png').convert_alpha()
start_button = button.Button(100, 200, start_img, 0.8)
exit_button = button.Button(450, 200, exit_img, 0.8)

tourne = True

while tourne:
    screen.fill((202, 228, 241))

    start_button.clicked

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tourne = False

    start_button.draw(screen)

    screen.blit(background, (0, 0))
    screen.blit(start_img, (300, 400))
    screen.blit(exit_img, (0, 0))
    pygame.display.update()
    pygame.display.flip()


pygame.init
game = Game()
game.run()