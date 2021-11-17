import pygame


class HUD:

    def __init__(self):
        self.box = pygame.image.load('hud.jpg')

    def render(self, screen):
        screen.blit(self.box, (0, 0))
    