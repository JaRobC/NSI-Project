import pygame

class HUD:

    def __init__(self):
        self.box = pygame.image.load('hud.jpg')
        self.text1 = "0000" 
        self.font = pygame.font.SysFont('Comic Sans MS', 18)
          

    def render(self, screen):
        #screen.blit(self.box, (0, 0))
        text = self.font.render(self.text1, False, (0, 0, 0))
        screen.blit(text, (0, 0))
    