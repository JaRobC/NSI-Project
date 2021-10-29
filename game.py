import pygame
import pytmx
import pyscroll
import time

from perso import Player

class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Island of Kingdoms")
        tmx_data = pytmx.util_pygame.load_pygame('carte.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2
        
        player_pos = tmx_data.get_object_by_name("player_spawn")
        self.player = Player(player_pos.x, player_pos.y)

        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=4)
        
        self.group.add(self.player)
    
    def screen_update(self):
        self.group.update()
        self.group.center(self.player.rect.center)
        self.group.draw(self.screen)
        pygame.display.flip()

    def handle_input(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] or pressed[pygame.K_z]:
            self.player.move_up()
            self.player.animations('./b/b1.png')
            self.screen_update()
            time.sleep(0.07)
            self.player.move_up()
            self.player.animations('./b/b2.png')
            self.screen_update()
            time.sleep(0.07)
            self.player.move_up()
            self.player.animations('./b/b3.png')
            self.screen_update()
           
        elif pressed[pygame.K_DOWN] or pressed[pygame.K_s]:
            self.player.move_down()
            self.player.animations('./f/f1.png')
            self.screen_update()
            time.sleep(0.07)
            self.player.move_down()
            self.player.animations('./f/f2.png')
            self.screen_update()
            time.sleep(0.07)
            self.player.move_down()
            self.player.animations('./f/f3.png')
            self.screen_update()
            
        elif pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
            self.player.move_right()
            self.player.animations('./r/r1.png')
            self.screen_update()
            time.sleep(0.07)
            self.player.move_right()
            self.player.animations('./r/r2.png')
            self.screen_update()
            time.sleep(0.07)
            self.player.move_right()
            self.player.animations('./r/r3.png')
            self.screen_update()
            
        elif pressed[pygame.K_LEFT] or pressed[pygame.K_q]:
            self.player.move_left()
            self.player.animations('./l/l1.png')
            self.screen_update()
            time.sleep(0.07)
            self.player.move_left()
            self.player.animations('./l/l2.png')
            self.screen_update()
            time.sleep(0.07)
            self.player.move_left()
            self.player.animations('./l/l3.png')
            self.screen_update()

    def run(self):

        clock = pygame.time.Clock()

        tourne = True

        while tourne:
            
            self.handle_input()
            self.group.update()
            self.group.center(self.player.rect.center)
            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    tourne = False

            clock.tick(60)

        pygame.quit()

game = Game()
game.run()