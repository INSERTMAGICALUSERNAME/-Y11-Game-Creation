# Fixing Boat game
# Creators Zach Hamilton and Johann Shotbolt
# Date: 15/07/2025 
# Version 1 

# test



# imports
import pygame
from sys import exit

# starts pygame
pygame.init() 

# Creates the play window
screen = pygame.display.set_mode((1200,600))

# sets the title for the game.
pygame.display.set_caption("Ultimate Pygame")

# sets the frame rate of the game.
clock = pygame.time.Clock()

# set game display name
pygame.display.set_caption("Crossing the Deep")

FPS = 60

# images
background_surf = pygame.image.load("images/stormy_background.png")



while True:

    
    for event in pygame.event.get():
        # Closes the game if you click close
        if event.type == pygame.QUIT:
            pygame.quit() # oposite of pygame.init()
            exit()


    screen.blit(background_surf,(0,-150))
    


    # updates pygame display.
    pygame.display.update()

    # While loop can only run at FPS speed per second. 
    clock.tick(FPS)



