import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(
        x = SCREEN_WIDTH / 2,
        y = SCREEN_HEIGHT / 2,
        shots_group = shots,
        updatable = updatable,
        drawable = drawable
    )
    # updatable.add(player)
    # drawable.add(player)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        shots.update(dt)
        for asteroid in asteroids:
            if player.detectCollision(asteroid):
                print("Game Over")
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if shot.detectCollision(asteroid):
                    shot.kill()
                    asteroid.split(asteroid.radius, asteroids)
        screen.fill((0, 0, 0))
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        

# welcome_message = welcome()
# print(welcome_message)    

if __name__ == "__main__":
    main()
    
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}") 
    