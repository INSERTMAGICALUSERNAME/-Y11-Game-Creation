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
screen = pygame.display.set_mode((1200,675))

# sets the title for the game.
pygame.display.set_caption("Ultimate Pygame")

#creating font
pacific_font = pygame.font.Font('Font/Pacifico-regular.ttf',50)

# sets the frame rate of the game.
clock = pygame.time.Clock()

# set game display name
pygame.display.set_caption("Crossing the Deep")

FPS = 60

# images
background_surf = pygame.image.load("images/stormy_background.png")

#text

#title
title_surf = pacific_font.render('Pacific Pursuit', True,"#006439")
title_rec = title_surf.get_rect(center = (600,373))

#blurb

info_surf = pacific_font.render('Press Space to Start, Press esacpe to quit, Press "h" for how to play',True,('#006439'))
info_surf = pygame.transform.scale(info_surf,(1000,50))
info_surf_rec = info_surf.get_rect(midbottom = (600, 500))

game_active = False 

while True:

    
    for event in pygame.event.get():
        # Closes the game if you click close
        if event.type == pygame.QUIT:
            pygame.quit() # oposite of pygame.init()
            exit()

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True   
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

    if game_active:
        screen.blit(background_surf,(0,-150))
    
    #title and game over screen
    else:
        screen.blit(background_surf,(0,-150))
        pygame.draw.rect(screen,(64,64,64),(50,300,1100,300))
        screen.blit(info_surf,info_surf_rec)
        screen.blit(title_surf,title_rec)

        


            

    # updates pygame display.
    pygame.display.update()

    # While loop can only run at FPS speed per second. 
    clock.tick(FPS)



