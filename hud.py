import pygame

class HUD:

    def __init__(self):
        self.box = pygame.image.load('hud.jpg')
        self.textarbre = "0000" 
        self.textpierre = "0000" 
        self.arbre = "Bois :"
        self.pierre = "Pierre :"
        self.stoparbre = "Vous ne pouvez plus récupérer de bois !"
        self.stoppierre = "Vous ne pouvez plus récupérez de pierre !"
        self.font = pygame.font.SysFont('Comic Sans MS', 36)
          
    def render(self, screen):
        #screen.blit(self.box, (0, 0))
        textarbre = self.font.render(self.textarbre, False, (0, 0, 0))
        textpierre = self.font.render(self.textpierre, False, (0, 0, 0))
        arbre = self.font.render(self.arbre, False, (0, 0, 0))
        pierre = self.font.render(self.pierre, False, (0, 0, 0))
        screen.blit(textpierre, (1180, 660))
        screen.blit(textarbre, (1180, 620))
        screen.blit(arbre, (1000, 620))
        screen.blit(pierre, (1000, 660))
        
    