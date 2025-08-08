import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    updatable.add(player)
    drawable.add(player)
    Asteroid.containers = [updatable, drawable, asteroids]
    AsteroidField.containers = [updatable]
    asteroid_field = AsteroidField()
    updatable.add(asteroid_field)

    Shot.containers = [updatable, drawable, shots]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                pygame.quit()
                sys.exit()

            for shot in shots:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()

        for drawable_object in drawable:
            drawable_object.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
