from circleshape import CircleShape
import pygame
import random
from constants import ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_MAX_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    def draw(self, screen):
        pygame.draw.circle(screen,"white",(self.position.x,self.position.y), self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            pass
        else:
            random_angle = random.uniform(20,50)
            asteroid1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            asteroid2=Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            asteroid1.velocity = pygame.math.Vector2.rotate(self.velocity, random_angle) * 1.2
            asteroid2.velocity = pygame.math.Vector2.rotate(self.velocity, -random_angle) * 1.2
    
