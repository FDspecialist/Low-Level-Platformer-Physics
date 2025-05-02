import pygame
import math
pygame.init()
class Player:
    def __init__(self,x,y):
        self.body = pygame.Surface((50,50))
        self.body.fill((255,255,255))
        self.x = x
        self.y = y
        self.velocity = 1
        self.dx = 0
        self.dy = 0

    def key_input(self,keys):
        #expects: pygame.key.get_pressed()
        self.dx = 0
        self.dy = 0
        if keys[pygame.K_w]:
            self.dy = -1
        if keys[pygame.K_s]:
            self.dy = 1
        if keys[pygame.K_a]:
            self.dx = -1
        if keys[pygame.K_d]:
            self.dx = 1

        if self.dx != 0 and self.dy != 0:
            norm = math.sqrt(self.dx ** 2 + self.dy ** 2)
            self.dx /= norm
            self.dy /= norm

    def follow_cursor(self,MouseX, MouseY):

        self.x, self.y = MouseX, MouseY



    def update(self):

        self.x += self.dx * self.velocity
        self.y += self.dy * self.velocity

    def draw(self,screen):
        screen.blit(self.body,(self.x,self.y))