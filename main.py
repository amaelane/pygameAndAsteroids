# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    # initialize pygame
    pygame.init()

    # welcome message
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # initialize screen constants
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # screen refresh loop
    while True:
        #print("looping") # debug message

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # black screen
        screen.fill("black")

        # screen refresh
        pygame.display.flip()


if __name__ == "__main__":
    main()