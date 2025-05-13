import pygame
import math
from physics_behaviours import Physics
pygame.init()
class Player:
    def __init__(self,x,y, physics):
        self.physics = physics
        self.body = pygame.Surface((50,50))
        self.rect = self.body.get_rect()
        self.body.fill((255,255,255))
        self.pos = pygame.Vector2(self.rect.topleft)
        self.velocity = pygame.Vector2(10,10)
        self.dx = 0
        self.dy = 0

        self.base_contact = False

    def key_input(self,keys):
        #expects: pygame.key.get_pressed()
        self.dx = 0
        self.dy = 0
        if keys[pygame.K_w]:
            self.dy = -1
        if keys[pygame.K_a]:
            self.dx = -1
        if keys[pygame.K_d]:
            self.dx = 1

        if self.dx != 0 and self.dy != 0:
            norm = math.sqrt(self.dx ** 2 + self.dy ** 2)
            self.dx /= norm
            self.dy /= norm

    def follow_cursor(self,MouseX, MouseY):
        self.pos= (MouseX, MouseY)

    def update(self):
        #apply gravity
        self.physics.gravity(self.velocity)
        if self.dy != -1:
            self.dy = 1
        self.pos.x += self.dx * self.velocity.x
        self.pos.y += self.dy * self.velocity.y

    def draw(self,screen):
        screen.blit(self.body,(self.pos.x,self.pos.y))