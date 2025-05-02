from operator import truediv

import pygame
import sys
from configs import Configs
from player import Player

class Game:
    def __init__(self):
        self.Configs = Configs()
        self.Screen = pygame.display.set_mode((self.Configs.SCREEN_WIDTH, self.Configs.SCREEN_HEIGHT))
        self.Layout = pygame.Surface((self.Configs.SCREEN_WIDTH,self.Configs.SCREEN_HEIGHT))
        self.Layout.fill((0,0,0))
        self.Screen.fill((0,0,0))
        pygame.display.set_caption("Low Level Platformer")
        self.clock = self.Configs.clock
        self.clock.tick(60)
        #game structures
        self.Baseplate = pygame.Surface((1200,100))
        self.Baseplate.fill((125,125,125))
        self.BaseRect = self.Baseplate.get_rect()
        self.BaseRect.x = 0
        self.BaseRect.y = self.Configs.SCREEN_HEIGHT - 100

        self.Player = Player(250,250)

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
            self.Player.check_base_collisions(self.BaseRect)
            self.Player.update()
            print(self.Player.rect)
            self.draw()
            pygame.display.flip()
        pygame.quit()
        sys.exit()
    def draw(self):
        FinalDisplay = self.Layout.copy()
        FinalDisplay.blit(self.Baseplate, (0,self.Configs.SCREEN_HEIGHT - 100))

        self.Player.draw(FinalDisplay)
        self.Screen.blit(FinalDisplay,(0,0))


if __name__ == '__main__':
    game = Game()
    game.run()
