from time import sleep
import pygame
from pyscroll import data
import pytmx
import pyscroll
import random

from perso import Player

class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Titre du jeu")

        tmx_data = pytmx.util_pygame.load_pygame('carte.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 3

        spawn = ('player1_spawn', 'player2_spawn', 'player3_spawn')

        player_pos = tmx_data.get_object_by_name(spawn[random.randint(0, 2)])
        self.player = Player(player_pos.x, player_pos.y)

        self.ims = 0.09

        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)
        
        self.group.add(self.player)

        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision" or obj.type == "collision_eau":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

    def update(self):
        self.group.update()

        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.walls) > -1:
                sprite.move_back()

    def screen_update(self):
        self.group.update()
        self.group.center(self.player.rect.center)
        self.group.draw(self.screen)
        pygame.display.flip()

    def anim_compil(self, anim1, anim2, anim3):
        self.player.animations(anim1)
        self.screen_update()
        sleep(self.ims)
        self.player.animations(anim2)
        self.screen_update()
        sleep(self.ims)
        self.player.animations(anim3)
        self.screen_update()

    def handle_input(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP] or pressed[pygame.K_z]:
            self.player.move_up()
            self.anim_compil('haut1', 'haut3', 'haut2')
        elif pressed[pygame.K_DOWN] or pressed[pygame.K_s]:
            self.player.move_down()
            self.anim_compil('bas1', 'bas3', 'bas2')
        elif pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
            self.player.move_right()
            self.anim_compil('droite1', 'droite3', 'droite2')
        elif pressed[pygame.K_LEFT] or pressed[pygame.K_q]:
            self.player.move_left()
            self.anim_compil('gauche1', 'gauche3', 'gauche2')

    def run(self):

        clock = pygame.time.Clock()

        tourne = True

        while tourne:
            self.player.save_location()
            self.handle_input()
            self.update()
            self.screen_update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    tourne = False

            clock.tick(60)

        pygame.quit()