from constants import PLAYER_RADIUS
from circleshape import CircleShape
import pygame
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED
from constants import SHOT_RADIUS
from constants import PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN

class Player(CircleShape):
    def __init__(self, x, y, shots_group = None, updatable = None, drawable = None):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shots_group = shots_group
        self.updatable = updatable
        self.drawable = drawable
        self.shoot_timer = 0
        
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        # return self.rotation
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        if self.shoot_timer > 0:
            self.shoot_timer -= dt
            

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        
    def shoot(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot_position = self.triangle()[0]
        shot_velocity = forward * PLAYER_SHOOT_SPEED
        if self.shots_group is not None and self.updatable is not None and self.drawable is not None:
            if self.shoot_timer <= 0:
                self.shoot_timer = PLAYER_SHOOT_COOLDOWN
                new_shot = Shot(shot_position, shot_velocity)
                self.shots_group.add(new_shot)
                self.updatable.add(new_shot)
                self.drawable.add(new_shot)

        
class Shot(CircleShape):
    def __init__(self, position, velocity):
        x, y = position
        if isinstance(position, pygame.Vector2):
            x, y = position.x, position.y
        else:
            x, y = position
            
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity
        
    def update(self, dt):
        self.position += self.velocity * dt
        
    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "red",
            (int(self.position.x), int(self.position.y)),
            self.radius
        )