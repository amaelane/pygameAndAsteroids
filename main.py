# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import *
from shot import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    # initialize pygame
    pygame.init()

    # limit FPS
    clock = pygame.time.Clock()
    dt = 0

    # welcome message
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # initialize screen constants
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # define groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # define containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable

    # initialize player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    # screen refresh loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # update updatables
        updatable.update(dt)

        # collision check
        for asteroid in asteroids:
            if asteroid.collision(player) == True:
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.collision(asteroid) == True:
                    asteroid.split()
                    shot.kill()

        # black screen
        screen.fill("black")

        # draw refresh
        for obj in drawable:
            obj.draw(screen)

        # screen refresh
        pygame.display.flip()

        # tick the clock
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()