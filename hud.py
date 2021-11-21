from time import sleep
import pygame

class HUD:

    def __init__(self):
        self.shopinterface = pygame.image.load('shop interface.png')
        self.panneauimg = pygame.image.load("fond panneau.png").convert()
        self.panneauimg.set_alpha(158)


        self.textvie = "0000"
        self.textarbre = "0000" 
        self.textpierre = "0000"
        self.textmoney = "0000" 
        self.textdegats = "0000"
        self.textzombie = "0000"

        self.vie = "Vie :"
        self.arbre = "Bois :"
        self.pierre = "Pierre :"
        self.money = "Argent :"
        self.degats = "Dégats :"
        self.zombie = "Nombre de zombie :"

        self.stoparbre = "Limite de récolte de bois !"
        self.stoppierre = "Limite de récolte de pierre !"

        self.achat_acheter = "Appuyer sur A pour acheter"
        self.achat_continuer = "Appuyer sur entrée pour"
        self.achat_continuer2 = "continuer"

        self.attack1_title = "Dégats + 5"
        self.attack1_desc = "Acheter cette amélioration"
        self.attack1_desc1 = "pour avoir 5 de dégats"
        self.attack1_desc2 = "supplémentaire en payant"
        self.attack1_desc3 = "5 d'argent"
        self.attack1 = False

        self.attack2_title = "Dégats + 10"
        self.attack2_desc = "Acheter cette amélioration"
        self.attack2_desc1 = "pour avoir 10 de dégats"
        self.attack2_desc2 = "supplémentaire en payant"
        self.attack2_desc3 = "20 d'argent"
        self.attack2 = False

        self.attack3_title = "Dégats + 50"
        self.attack3_desc = "Acheter cette amélioration"
        self.attack3_desc1 = "pour avoir 50 de dégats"
        self.attack3_desc2 = "supplémentaire en payant"
        self.attack3_desc3 = "75 d'argent"
        self.attack3 = False

        self.attack4_title = "Dégats + 100"
        self.attack4_desc = "Acheter cette amélioration"
        self.attack4_desc1 = "pour avoir 100 de dégats"
        self.attack4_desc2 = "supplémentaire en payant"
        self.attack4_desc3 = "200 d'argent"
        self.attack4 = False
        ######
        self.vie1_title = "Vie + 5"
        self.vie1_desc = "Acheter cette amélioration"
        self.vie1_desc1 = "pour avoir 5 de vie"
        self.vie1_desc2 = "supplémentaire en payant"
        self.vie1_desc3 = "5 d'argent"
        self.vie1 = False

        self.vie2_title = "Vie + 10"
        self.vie2_desc = "Acheter cette amélioration"
        self.vie2_desc1 = "pour avoir 10 de vie"
        self.vie2_desc2 = "supplémentaire en payant"
        self.vie2_desc3 = "20 d'argent"
        self.vie2 = False

        self.vie3_title = "Vie + 50"
        self.vie3_desc = "Acheter cette amélioration"
        self.vie3_desc1 = "pour avoir 50 de vie"
        self.vie3_desc2 = "supplémentaire en payant"
        self.vie3_desc3 = "75 d'argent"
        self.vie3 = False

        self.vie4_title = "Vie + 100"
        self.vie4_desc = "Acheter cette amélioration"
        self.vie4_desc1 = "pour avoir 100 de vie"
        self.vie4_desc2 = "supplémentaire en payant"
        self.vie4_desc3 = "200 d'argent"
        self.vie4 = False

        self.buche1_title = "1 Buche"
        self.buche1_desc = "Vendez 1 de buche"
        self.buche1_desc1 = "pour avoir 10 d'argent"
        self.buche1_desc2 = "supplémentaire"
        self.buche1_desc3 = ""
        self.buche1 = False

        self.buche2_title = "10 Buche"
        self.buche2_desc = "Vendez 10 de buche"
        self.buche2_desc1 = "pour avoir 100 d'argent"
        self.buche2_desc2 = "supplémentaire"
        self.buche2_desc3 = ""
        self.buche2 = False

        self.pierre1_title = "1 Pierre"
        self.pierre1_desc = "Vendez 1 de piere"
        self.pierre1_desc1 = "pour avoir 12 d'argent"
        self.pierre1_desc2 = "supplémentaire"
        self.pierre1_desc3 = ""
        self.pierre1 = False

        self.pierre2_title = "10 Pierre"
        self.pierre2_desc = "Vendez 10 de pierre"
        self.pierre2_desc1 = "pour avoir 120 d'argent"
        self.pierre2_desc2 = "supplémentaire"
        self.pierre2_desc3 = ""
        self.pierre2 = False
        
        self.panneau_intro = "Bonjour voyageur,"

        self.font_achat = pygame.font.SysFont('Comic Sans MS', 18)
        self.font = pygame.font.SysFont('Comic Sans MS', 36)
        self.font_warning = pygame.font.SysFont('Comic Sans MS', 28)
        self.font_panneau = pygame.font.SysFont('Comics Sans MS', 50)
          
    def achat(self, condition_achat, screen, fond, titre, description_1, description_2, description_3, description_4):
        if condition_achat == True:
            screen.blit(fond, (950, 10))

            achat_title = self.font_warning.render(titre, False, (0, 0, 0))
            screen.blit(achat_title, (1020, 37))

            achat_desc = self.font_achat.render(description_1, False, (0, 0, 0))
            screen.blit(achat_desc, (990, 120))

            achat_desc = self.font_achat.render(description_2, False, (0, 0, 0))
            screen.blit(achat_desc, (990, 150))

            achat_desc = self.font_achat.render(description_3, False, (0, 0, 0))
            screen.blit(achat_desc, (990, 180))

            achat_desc = self.font_achat.render(description_4, False, (0, 0, 0))
            screen.blit(achat_desc, (990, 210))

            achat_desc = self.font_achat.render(self.achat_acheter, False, (0, 0, 0))
            screen.blit(achat_desc, (990, 260))

            achat_desc = self.font_achat.render(self.achat_continuer, False, (0, 0, 0))
            screen.blit(achat_desc, (990, 290))

            achat_desc = self.font_achat.render(self.achat_continuer2, False, (0, 0, 0))
            screen.blit(achat_desc, (990, 320))

    def render(self, screen, color):

        textvie = self.font.render(self.textvie, False, color)
        textarbre = self.font.render(self.textarbre, False, color)
        textpierre = self.font.render(self.textpierre, False, color)
        textmoney = self.font.render(self.textmoney, False, color)
        textdegats = self.font.render(self.textdegats, False, color)
        textzombie = self.font.render(self.textzombie, False, color)

        vie = self.font.render(self.vie, False, color)
        arbre = self.font.render(self.arbre, False, color)
        pierre = self.font.render(self.pierre, False, color)
        money = self.font.render(self.money, False, color)
        degats = self.font.render(self.degats, False, color)
        zombie = self.font.render(self.zombie, False, color)

        screen.blit(textpierre, (1145, 660))
        screen.blit(textarbre, (1145, 620))
        screen.blit(textmoney, (1145, 580))
        screen.blit(textdegats, (1145, 540))
        screen.blit(textvie, (1145, 500))
        screen.blit(textzombie, (400, 15))
 
        screen.blit(arbre, (1000, 620))
        screen.blit(pierre, (1000, 660))
        screen.blit(money, (1000, 580))
        screen.blit(degats, (1000, 540))
        screen.blit(vie, (1000, 500))
        screen.blit(zombie, (15, 15))

        self.achat(self.attack1, screen, self.shopinterface, self.attack1_title, self.attack1_desc, self.attack1_desc1, self.attack1_desc2, self.attack1_desc3)
        self.achat(self.attack2, screen, self.shopinterface, self.attack2_title, self.attack2_desc, self.attack2_desc1, self.attack2_desc2, self.attack2_desc3)
        self.achat(self.attack3, screen, self.shopinterface, self.attack3_title, self.attack3_desc, self.attack3_desc1, self.attack3_desc2, self.attack3_desc3)
        self.achat(self.attack4, screen, self.shopinterface, self.attack4_title, self.attack4_desc, self.attack4_desc1, self.attack4_desc2, self.attack4_desc3)

        self.achat(self.vie1, screen, self.shopinterface, self.vie1_title, self.vie1_desc, self.vie1_desc1, self.vie1_desc2, self.vie1_desc3)
        self.achat(self.vie2, screen, self.shopinterface, self.vie2_title, self.vie2_desc, self.vie2_desc1, self.vie2_desc2, self.vie2_desc3)
        self.achat(self.vie3, screen, self.shopinterface, self.vie3_title, self.vie3_desc, self.vie3_desc1, self.vie3_desc2, self.vie3_desc3)
        self.achat(self.vie4, screen, self.shopinterface, self.vie4_title, self.vie4_desc, self.vie4_desc1, self.vie4_desc2, self.vie4_desc3)

        self.achat(self.buche1, screen, self.shopinterface, self.buche1_title, self.buche1_desc, self.buche1_desc1, self.buche1_desc2, self.buche1_desc3)
        self.achat(self.buche2, screen, self.shopinterface, self.buche2_title, self.buche2_desc, self.buche2_desc1, self.buche2_desc2, self.buche2_desc3)
        self.achat(self.pierre1, screen, self.shopinterface, self.pierre1_title, self.pierre1_desc, self.pierre1_desc1, self.pierre1_desc2, self.pierre1_desc3)
        self.achat(self.pierre2, screen, self.shopinterface, self.pierre2_title, self.pierre2_desc, self.pierre2_desc1, self.pierre2_desc2, self.pierre2_desc3)

    def panneau(self, screen):
        screen.blit(self.panneauimg, (0, 0))
        intro = self.font_panneau.render(self.panneau_intro, False, (255, 255, 255))
        screen.blit(intro, (20, 20))

        pygame.mixer.music.load("Son panneau1.mp3")
        pygame.mixer.music.play(0)