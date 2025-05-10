from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, SHOT_RADIUS
import pygame
shots = pygame.sprite.Group()

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen,"white",self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and keys[pygame.K_d]:
            pass
        elif keys[pygame.K_a]:
            self.rotate(-dt)
        elif keys[pygame.K_d]:
            self.rotate(dt)
        else:
            pass

        if keys[pygame.K_w] and keys[pygame.K_s]:
            pass
        elif keys[pygame.K_s]:
            self.move(-dt)
        elif keys[pygame.K_w]:
            self.move(dt)
        else:
            pass
        
        if keys[pygame.K_SPACE]:
            self.shoot(dt)
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self,dt):
        velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS, velocity)
        
        shots.add(shot)
        

class Shot(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x,y,SHOT_RADIUS)
        self.velocity = velocity
        
    def draw(self, screen):
        
        pygame.draw.circle(screen,"white",(self.position.x,self.position.y), SHOT_RADIUS, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
        
    