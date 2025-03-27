import pygame
from circleshape import CircleShape
from constants import *

class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen): #overrides draw func in circleshape.py
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]: # turn left
            self.rotate(-dt)
        if keys[pygame.K_RIGHT]: # turn right
            self.rotate(dt)
        if keys[pygame.K_UP]: # move forward
            self.move(dt)
        if keys[pygame.K_DOWN]: # move backwards
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        if self.shoot_timer > 0:
            self.shoot_timer -= dt # decrease shot timer
    
    def shoot(self):
        if self.shoot_timer <= 0: # only shoots if timer is at or below 0
            shot = Shot(int(self.position.x), int(self.position.y))
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN # reset timer to the cooldown period
            return shot
        return None # if can't shoot yet

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        
    def draw(self, screen): # overrides draw func in circleshape.py
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt