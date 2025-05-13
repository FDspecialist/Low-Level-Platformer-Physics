from operator import truediv

import pygame
import sys
from physics_behaviours import Physics
from configs import Configs
from player import Player

class Game:
    def __init__(self):
        self.Configs = Configs()
        self.Screen = pygame.display.set_mode((self.Configs.SCREEN_WIDTH, self.Configs.SCREEN_HEIGHT))
        self.Layout = pygame.Surface((self.Configs.SCREEN_WIDTH,self.Configs.SCREEN_HEIGHT))
        self.Screen.fill((0,0,0))
        pygame.display.set_caption("Low Level Platformer")
        self.clock = self.Configs.clock

        #game physics
        self.Physics = Physics(self.clock)
        #game structures
        self.Baseplate = pygame.Surface((1200,100))
        self.Baseplate.fill((125,125,125))
        self.BaseRect = self.Baseplate.get_rect()
        self.BaseRect.x = 0
        self.BaseRect.y = self.Configs.SCREEN_HEIGHT - 100

        self.Player = Player(250,250, self.Physics)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        print("Exit from escape key")
                        running = False
            player_keys = pygame.key.get_pressed()
            mouse_pos = pygame.mouse.get_pos()
            mx, my = mouse_pos
            self.Player.key_input(player_keys)
            #self.Player.follow_cursor(mx,my)
            self.Player.update()
            self.draw()
            self.clock.tick(60)
            pygame.display.flip()
        pygame.quit()
        sys.exit()
    def draw(self):
        self.Screen.fill((0,0,0))
        self.Screen.blit(self.Baseplate, (0,self.Configs.SCREEN_HEIGHT - 100))
        self.Player.draw(self.Screen)


if __name__ == '__main__':
    game = Game()
    game.run()
