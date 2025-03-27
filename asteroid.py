import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen): #overrides draw func in circleshape.py
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else: 
            angle = random.uniform(20, 50)
            Asteroid1 = Asteroid(self.position.x, self.position. y, (self.radius - ASTEROID_MIN_RADIUS))
            Asteroid2 = Asteroid(self.position.x, self.position. y, (self.radius - ASTEROID_MIN_RADIUS))
            velocity1 = pygame.math.Vector2(self.velocity)
            velocity2 = pygame.math.Vector2(self.velocity)
            Asteroid1.velocity = velocity1.rotate(angle) * 1.2
            Asteroid2.velocity = velocity2.rotate(-angle) * 1.2