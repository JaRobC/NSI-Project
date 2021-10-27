import pygame
import sys
import button
pygame.init()


size = width, height = 600, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Main Menu -- Island of Kingdoms")
background = pygame.image.load("./menu_pics/menu_background.png")

start_img = pygame.image.load('./menu_pics/start.png').convert_alpha()
exit_img = pygame.image.load('./menu_pics/exit.png').convert_alpha()
start_button = button.Button(100, 200, start_img, 0.8)
exit_button = button.Button(450, 200, exit_img, 0.8)

while True:
    screen.fill((202, 228, 241))

    if start_button.draw(screen):
        print("START")
    if exit_button.draw(screen):
        print("EXIT")

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit(0)
    
    screen.blit(background, (0, 0))
    screen.blit(start_img, (300, 400))
    screen.blit(exit_img, (0, 0))
    pygame.display.update()
    pygame.display.flip()

pygame.quit()