# Fixing Boat game
# Creators Zach Hamilton and Johann Shotbolt
# Date: 15/07/2025 
# Version 1 

# imports
import pygame
from sys import exit

# starts pygame
pygame.init() 

# Creates the play window
screen = pygame.display.set_mode((800,400))

# sets the title for the game.
pygame.display.set_caption("Ultimate Pygame")

# sets the frame rate of the game.
clock = pygame.time.Clock()

FPS = 60

while True:

    
    for event in pygame.event.get():
        # Closes the game if you click close
        if event.type == pygame.QUIT:
            pygame.quit() # oposite of pygame.init()
            exit()


    # updates pygame display.
    pygame.display.update()

    # While loop can only run at FPS speed per second. 
    clock.tick(FPS)



