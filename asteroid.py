from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.position.x, self.position.y), self.radius, 2)
        # pygame.draw.circle(screen, (255, 255, 255), (self.position_new.x, self.position_new.y), self.new_radius, 2)
        
    def update(self, dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt
        
    def split(self, radius, asteroids):
        self.kill()
        if radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            direction_1 = self.velocity.rotate(angle)
            direction_2 = self.velocity.rotate(-angle)
            radius_new = radius - ASTEROID_MIN_RADIUS
            if radius_new <= 0:
                return
            new_asteroid_1 = Asteroid(self.position.x, self.position.y, radius_new)
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, radius_new)
            new_asteroid_1.velocity = direction_1 * 1.2
            new_asteroid_2.velocity = direction_2 * 1.2
            asteroids.add(new_asteroid_1)
            asteroids.add(new_asteroid_2)
          