import pygame

class HUD:

    def __init__(self):
        self.box = pygame.image.load('hud.jpg')
        self.textarbre = "0000" 
        self.textpierre = "0000"
        self.textmoney = "0000" 
        self.arbre = "Bois :"
        self.pierre = "Pierre :"
        self.money = "money :"
        self.stoparbre = "Vous ne pouvez plus récupérer de bois !"
        self.stoppierre = "Vous ne pouvez plus récupérez de pierre !"
        self.font = pygame.font.SysFont('Comic Sans MS', 36)
          
    def render(self, screen):
        #screen.blit(self.box, (0, 0))
        textarbre = self.font.render(self.textarbre, False, (0, 0, 0))
        textpierre = self.font.render(self.textpierre, False, (0, 0, 0))
        textmoney = self.font.render(self.textmoney, False, (0, 0, 0))
        arbre = self.font.render(self.arbre, False, (0, 0, 0))
        pierre = self.font.render(self.pierre, False, (0, 0, 0))
        money = self.font.render(self.money, False, (0, 0, 0))
        screen.blit(textpierre, (1180, 660))
        screen.blit(textarbre, (1180, 620))
        screen.blit(textmoney, (1180, 580))
        screen.blit(arbre, (1000, 620))
        screen.blit(pierre, (1000, 660))
        screen.blit(money, (1000, 580))
        
    