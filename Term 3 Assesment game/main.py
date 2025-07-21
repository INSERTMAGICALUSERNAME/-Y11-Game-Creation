# Fixing Boat game
# Creators Zach Hamilton and Johann Shotbolt
# Date: 15/07/2025 
# Version 1 

# imports
import pygame
from sys import exit

# player class
class Player (pygame.sprite.Sprite):
    # inicailizes the class and sets thing like image, rect and gravity
    def __init__(self):
        super().__init__()
        self.player_image = pygame.image.load("images/player_green.png").convert_alpha()

        self.image = self.player_image
        self.rect =  self.player_image.get_rect(midbottom = (600,400))


        self.gravity = 0 
        # sets up gravity for jumping
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.y >= 400:
            self.rect.y = 400
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > 1130:
            self.rect.x = 1130

    
        # player movment
    def player_imput(self):
        # get keys pressed
        keys = pygame.key.get_pressed()
        # jump
        if keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]:
            if self.rect.y >= 400:
                self.gravity = -20


        # moving right
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.rect.y == 400:
                self.rect.x += 5
            # if the player is jumping they go faster
            else:
                self.rect.x += 8
        # moving left
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.rect.y == 400:
                self.rect.x -= 5
            # if the player is jumping they go faster
            else:
                self.rect.x -= 8
    # calls of the defs for the class
    def update(self):
        self.apply_gravity()
        self.player_imput()


        

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

# Groups
# add player to group
player =  pygame.sprite.GroupSingle()
player.add(Player())

#text

#title
title_surf = pacific_font.render('Pacific Pursuit', True,"#006439")
title_rec = title_surf.get_rect(center = (600,373))

#blurb

info_surf = pacific_font.render('Press Space to Start, Press esacpe to quit, Press "h" for how to play',True,('#006439'))
info_surf = pygame.transform.scale(info_surf,(1000,50))
info_surf_rec = info_surf.get_rect(midbottom = (600, 500))




# images
background_surf = pygame.image.load("images/background_frame_5(copy)(Medium).png").convert_alpha()
game_state = 2 


while True:

    
    for event in pygame.event.get():
        # Closes the game if you click close
        if event.type == pygame.QUIT:
            pygame.quit() # oposite of pygame.init()
            exit()
        if game_state == 2:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_state = 1   
            if event.type == pygame.KEYDOWN and event.key == pygame.K_h :
             game_state = 3
                
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

       
            
            
            
            
            
                

    #main gameplay
    if game_state == 1:
        screen.blit(background_surf,(0,-150))
        # updates pygame display.
        player.draw(screen)
        player.update()
    
    #title and game over screen
    if game_state == 2:

        screen.blit(background_surf,(0,-150))
        pygame.draw.rect(screen,"#673506FF",(50,300,1100,300))
        pygame.draw.rect(screen,"#2C2C2CCC",(50,300,1100,300),10,2)
        screen.blit(info_surf,info_surf_rec)
        screen.blit(title_surf,title_rec)
        
    if game_state == 3:
        screen.blit(background_surf,(0,-150))
        pygame.draw.rect(screen,"#673506FF",(50,25,1100,625))
        pygame.draw.rect(screen,"#2C2C2CCC",(50,25,1100,625),10,2)
        

        





            

   
    pygame.display.update()
    
    # While loop can only run at FPS speed per second. 
    clock.tick(FPS)



