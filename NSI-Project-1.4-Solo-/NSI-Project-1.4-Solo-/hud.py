from time import sleep
import pygame

class HUD:

    def __init__(self):
        self.shopinterface = pygame.image.load('shop interface.png')
        self.panneauimg = pygame.image.load("fond panneau.png").convert()
        self.panneauimg.set_alpha(158)
        self.questimg = pygame.image.load("quest.png")
        self.croix = pygame.image.load("croix rouge.png")
        self.fleche = pygame.image.load("fleche verte.png")
        self.popup_img = pygame.image.load("popup quest.png")

        self.heart1 = pygame.image.load("hearth1.png")
        self.heart2 = pygame.image.load("hearth2.png")
        self.heart3 = pygame.image.load("hearth3.png")
        self.heart4 = pygame.image.load("hearth4.png")
        self.heart5 = pygame.image.load("hearth5.png")
        self.vie = 0

        self.coin = pygame.image.load("coin.png")
        self.rock = pygame.image.load("rock.png")
        self.tree = pygame.image.load("tree.png")
        self.faitmal = pygame.image.load("degat.png")
        self.theend = pygame.image.load('theend.png')

        self.isPierre = False
        self.isBois = False
        self.anotherPopup = 0

        self.quest1_first = False
        self.quest2_first = False
        self.quest3_first = False
        self.quest4_first = False
        self.quest5_first = False

    ############
        self.textvie = "0000"
        self.textarbre = "0000" 
        self.textpierre = "0000"
        self.textmoney = "0000" 
        self.textdegats = "0000"
        self.textzombie = "0000"
        self.textmeilleur = "0000"

        self.vie = "Vie :"
        self.arbre = "Bois :"
        self.pierre = "Pierre :"
        self.money = "Argent :"
        self.degats = "Dégats :"
        self.zombie = "Nombre de zombie :"
        self.meilleur = "Meilleur score de zombie :"

        self.stoparbre = "Limite de récolte de bois !"
        self.stoppierre = "Limite de récolte de pierre !"

    ############
        self.achat_acheter = "Appuyer sur A pour acheter"
        self.achat_continuer = "Appuyer sur entrée pour"
        self.achat_continuer2 = "continuer"

        self.attack1_title = "Dégats + 5"
        self.attack1_desc = "Acheter cette amélioration"
        self.attack1_desc1 = "pour avoir 5 de dégats"
        self.attack1_desc2 = "supplémentaire en payant"
        self.attack1_desc3 = "7 d'argent"
        self.attack1 = False

        self.attack2_title = "Dégats + 10"
        self.attack2_desc = "Acheter cette amélioration"
        self.attack2_desc1 = "pour avoir 10 de dégats"
        self.attack2_desc2 = "supplémentaire en payant"
        self.attack2_desc3 = "22 d'argent"
        self.attack2 = False

        self.attack3_title = "Dégats + 50"
        self.attack3_desc = "Acheter cette amélioration"
        self.attack3_desc1 = "pour avoir 50 de dégats"
        self.attack3_desc2 = "supplémentaire en payant"
        self.attack3_desc3 = "102 d'argent"
        self.attack3 = False

        self.attack4_title = "Dégats + 100"
        self.attack4_desc = "Acheter cette amélioration"
        self.attack4_desc1 = "pour avoir 100 de dégats"
        self.attack4_desc2 = "supplémentaire en payant"
        self.attack4_desc3 = "202 d'argent"
        self.attack4 = False
        
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
        self.vie3_desc3 = "100 d'argent"
        self.vie3 = False

        self.vie4_title = "Vie + 100"
        self.vie4_desc = "Acheter cette amélioration"
        self.vie4_desc1 = "pour avoir 100 de vie"
        self.vie4_desc2 = "supplémentaire en payant"
        self.vie4_desc3 = "200 d'argent"
        self.vie4 = False

        self.buche1_title = "1 Buche"
        self.buche1_desc = "Vendez 1 de buche"
        self.buche1_desc1 = "pour avoir 5 d'argent"
        self.buche1_desc2 = "supplémentaire"
        self.buche1_desc3 = ""
        self.buche1 = False

        self.buche2_title = "10 Buche"
        self.buche2_desc = "Vendez 10 de buche"
        self.buche2_desc1 = "pour avoir 50 d'argent"
        self.buche2_desc2 = "supplémentaire"
        self.buche2_desc3 = ""
        self.buche2 = False

        self.pierre1_title = "1 Pierre"
        self.pierre1_desc = "Vendez 1 de piere"
        self.pierre1_desc1 = "pour avoir 7 d'argent"
        self.pierre1_desc2 = "supplémentaire"
        self.pierre1_desc3 = ""
        self.pierre1 = False

        self.pierre2_title = "10 Pierre"
        self.pierre2_desc = "Vendez 10 de pierre"
        self.pierre2_desc1 = "pour avoir 70 d'argent"
        self.pierre2_desc2 = "supplémentaire"
        self.pierre2_desc3 = ""
        self.pierre2 = False
    ############
        self.page = 1

        self.questbase_title = "Tuer 1 zombie"
        self.questbase_desc = "Afin de finir cette quête, vous"
        self.questbase_desc1 = "devrez tuer 1 zombie afin de"
        self.questbase_desc2 = "recevoir 10 d'argent"
        self.questbase_desc3 = ""
        self.questbase = False
        self.questbase_isDo = False

        self.popup_questbase_desc = "Vous avez reçu 10 d'argent"
        self.questbase_cond = False
        self.questbase_stop = 0
        ####
        self.quest2_title = "Couper 5 arbres"
        self.quest2_desc = "Afin de finir cette quête, vous"
        self.quest2_desc1 = "devrez abattre 5 arbres ou"
        self.quest2_desc2 = "tronc afin de recevoir"
        self.quest2_desc3 = "10 d'argent"
        self.quest2 = False
        self.quest2_isDo = False

        self.popup_quest2_desc = "Vous avez reçu 10 d'argent"
        self.quest2_cond = False
        self.quest2_stop = 0
        ####
        self.quest3_title = "De la vie en boite ?"
        self.quest3_desc = "Afin de finir cette quête, vous"
        self.quest3_desc1 = "devrez acheter de la vie dans"
        self.quest3_desc2 = "le shop afin de recevoir 5 de"
        self.quest3_desc3 = "vie en plus"
        self.quest3 = False
        self.quest3_isDo = False

        self.popup_quest3_desc = "Vous avez reçu 5 de vie"
        self.quest3_cond = False
        self.quest3_stop = 0
        ####
        self.quest4_title = "Une pioche !"
        self.quest4_desc = "Afin de finir cette quête, vous"
        self.quest4_desc1 = "devrez récupérez 2 de buches"
        self.quest4_desc2 = "et 3 de pierres afin de"
        self.quest4_desc3 = "recevoir une pioche"
        self.quest4 = False
        self.quest4_isDo = False

        self.popup_quest4_desc = "Vous avez reçu une pioche"
        self.quest4_cond = False
        self.quest4_stop = 0
        ####
        self.quest5_title = "Une hachette !"
        self.quest5_desc = "Afin de finir cette quête, vous"
        self.quest5_desc1 = "devrez récupérez 2 buches et 5"
        self.quest5_desc2 = "de pierres en ayant déjà la"
        self.quest5_desc3 = "pioche afin de recevoir la hache"
        self.quest5 = False
        self.quest5_isDo = False

        self.popup_quest5_desc = "Vous avez reçu une hache"
        self.quest5_cond = False
        self.quest5_stop = 0
        ####
        self.quest6_title = "The end ?"
        self.quest6_desc = "Afin de finir cette quête, vous"
        self.quest6_desc1 = "devrez débloquer le donjon"
        self.quest6_desc2 = "afin de recevoir 1000 d'argent"
        self.quest6_desc3 = ""
        self.quest6 = False
        self.quest6_isDo = False

        self.popup_quest6_desc = "Vous avez reçu 10000 d'argent"
        self.quest6_cond = False
        self.quest6_stop = 0
    ###########
        self.panneau_intro = "Bonjour voyageur,"
        self.panneau_desc1 = "Si vous êtes ici, ce n'est pas pour rien..."
        self.panneau_desc2 = "En effet, afin de finir ce jeu vous devrez libérer le monde d'un terrible"
        self.panneau_desc3 = "monstre ! Pour ce faire, il faudra vous aventurez dans le trou en haut à"
        self.panneau_desc4 = "droite de la map. Mais pour ce faire, vous devrez récolter plusieurs"
        self.panneau_desc5 = "ressources afin que de tuer nombreux de ses sbires."
        self.panneau_desc6 = "Afin de vous aider dans votre tâche, vous avez à disposition des quêtes"
        self.panneau_desc7 = "qui vous permetteront de progresser dans le jeu !"
        self.panneau_desc8 = "Aussi, un shop vous permettera d'acheter de la vie ou des dégats afin"
        self.panneau_desc9 = "de tuer vos ennemis ou de récupérer des ressources plus facilement !"
        self.panneau_desc10 = "Enfin, j'ai entendu dire que, dans le abs de la map, se situe une"
        self.panneau_desc11 = "maison abandonnée... Je pense que vous pourriez trouver quelque"
        self.panneau_desc12 = "petites chose afin de vous aider !"
        self.panneau_desc13= ""
        self.panneau_desc14 = "Bien cordialement,  uh  j l"

        self.font_achat = pygame.font.SysFont('Comic Sans MS', 18)
        self.font = pygame.font.SysFont('Comic Sans MS', 36)
        self.font_title_quest = pygame.font.SysFont('Comic Sans MS', 50)
        self.font_desc_quest = pygame.font.SysFont('Comic Sans MS', 24)
        self.font_desc_popup = pygame.font.SysFont('Comic Sans MS', 20)
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

    def quest(self, condition_quest, screen, fond, titre, description_1, description_2, description_3, description_4, isDo):
        if condition_quest == True:
            screen.blit(fond, (400, 0))

            quest = self.font_title_quest.render("Quêtes", False, (0, 0, 0))
            screen.blit(quest, (550, 42))

            quest_title = self.font_warning.render(titre, False, (0, 0, 0))
            screen.blit(quest_title, (560, 205))

            quest_desc = self.font_desc_quest.render(description_1, False, (0, 0, 0))
            screen.blit(quest_desc, (470, 300))

            quest_desc = self.font_desc_quest.render(description_2, False, (0, 0, 0))
            screen.blit(quest_desc, (470, 350))

            quest_desc = self.font_desc_quest.render(description_3, False, (0, 0, 0))
            screen.blit(quest_desc, (470, 400))

            quest_desc = self.font_desc_quest.render(description_4, False, (0, 0, 0))
            screen.blit(quest_desc, (470, 450))

            if isDo == False:
                screen.blit(self.croix, (479, 210))
            elif isDo == True:
                screen.blit(self.fleche, (790, 210))
    
    def popup_quest(self, condition, screen, fond, titre, desc):
        if condition == True:
            screen.blit(fond, (550, 20))

            quest_title = self.font_warning.render(titre, False, (0, 0, 0))
            screen.blit(quest_title, (570, 25))

            quest_desc = self.font_desc_popup.render(desc, False, (0, 0, 0))
            screen.blit(quest_desc, (570, 55))

    def popup_quest2(self, condition, screen, fond, titre, desc):
        if condition == True:
            screen.blit(fond, (550, 60))

            quest_title = self.font_warning.render(titre, False, (0, 0, 0))
            screen.blit(quest_title, (570, 65))

            quest_desc = self.font_desc_popup.render(desc, False, (0, 0, 0))
            screen.blit(quest_desc, (570, 95))

            pygame.display.flip()

    def render(self, screen, color):

        textvie = self.font.render(self.textvie, False, color)
        textarbre = self.font.render(self.textarbre, False, color)
        textpierre = self.font.render(self.textpierre, False, color)
        textmoney = self.font.render(self.textmoney, False, color)
        textdegats = self.font.render(self.textdegats, False, color)
        textzombie = self.font.render(self.textzombie, False, color)
        textmeilleur = self.font.render(self.textmeilleur, False, color)


        zombie = self.font.render(self.zombie, False, color)
        meilleur = self.font.render(self.meilleur, False, color)

        if self.vie >= 80:
            screen.blit(self.heart1, (1080, 10))
        elif self.vie <= 79 and self.vie >= 60:
            screen.blit(self.heart2, (1080, 10))
        elif self.vie <= 59 and self.vie >= 40:
            screen.blit(self.heart3, (1080, 10))
        elif self.vie <= 39 and self.vie >= 20:
            screen.blit(self.heart4, (1080, 10))
        elif self.vie <= 19 and self.vie >= 0:
            screen.blit(self.heart5, (1080, 10))

        screen.blit(self.coin, (1080, 600))
        screen.blit(self.faitmal, (950, 10))
        screen.blit(self.theend, (70, 650))

        if self.isPierre == False and self.isBois == False:
            screen.blit(self.rock, (10, 590))
            screen.blit(self.tree, (10, 650))

            screen.blit(textpierre, (70, 600))
            screen.blit(textarbre, (70, 650))

        elif self.isPierre == True and self.isBois == False:
            screen.blit(self.rock, (10, 540))
            screen.blit(self.tree, (10, 600))

            screen.blit(textpierre, (70, 550))
            screen.blit(textarbre, (70, 600))

        elif self.isPierre == False and self.isBois == True:
            screen.blit(self.rock, (10, 490))
            screen.blit(self.tree, (10, 550))

            screen.blit(textpierre, (70, 500))
            screen.blit(textarbre, (70, 550))

        elif self.isPierre == True and self.isBois == True:
            screen.blit(self.rock, (10, 490))
            screen.blit(self.tree, (10, 550))

            screen.blit(textpierre, (70, 500))
            screen.blit(textarbre, (70, 550))
        

        screen.blit(textmoney, (1145, 600))
        screen.blit(textdegats, (1000, 10))
        screen.blit(textvie, (1150, 40))
        screen.blit(textzombie, (400, 15))
        screen.blit(textmeilleur, (475, 70))


        screen.blit(zombie, (15, 15))
        screen.blit(meilleur, (15, 70))

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

        desc = self.font_panneau.render(self.panneau_desc1, False, (255, 255, 255))
        screen.blit(desc, (20, 150))
        desc = self.font_panneau.render(self.panneau_desc2, False, (255, 255, 255))
        screen.blit(desc, (20, 210))
        desc = self.font_panneau.render(self.panneau_desc3, False, (255, 255, 255))
        screen.blit(desc, (20, 270))
        desc = self.font_panneau.render(self.panneau_desc4, False, (255, 255, 255))
        screen.blit(desc, (20, 330))
        desc = self.font_panneau.render(self.panneau_desc5, False, (255, 255, 255))
        screen.blit(desc, (20, 390))
        desc = self.font_panneau.render(self.panneau_desc6, False, (255, 255, 255))
        screen.blit(desc, (20, 450))
        desc = self.font_panneau.render(self.panneau_desc7, False, (255, 255, 255))
        screen.blit(desc, (20, 510))
        desc = self.font_panneau.render(self.panneau_desc8, False, (255, 255, 255))
        screen.blit(desc, (20, 570))
        desc = self.font_panneau.render(self.panneau_desc9, False, (255, 255, 255))
        screen.blit(desc, (20, 630))
        desc = self.font_panneau.render(self.panneau_desc10, False, (255, 255, 255))
        screen.blit(desc, (20, 690))
        desc = self.font_panneau.render(self.panneau_desc11,  False, (255, 255, 255))
        screen.blit(desc, (20, 710))
        desc = self.font_panneau.render(self.panneau_desc12, False, (255, 255, 255))
        screen.blit(desc, (20, 770))
        desc = self.font_panneau.render(self.panneau_desc13, False, (255, 255, 255))
        screen.blit(desc, (20, 830))
        desc = self.font_panneau.render(self.panneau_desc14, False, (255, 255, 255))
        screen.blit(desc, (20, 890))

        pygame.mixer.music.load("Son panneau1.mp3")
        pygame.mixer.music.play(0)