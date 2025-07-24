# Fixing Boat game
# Creators Zach Hamilton and Johann Shotbolt
# Date: 15/07/2025 
# Version 1 

# imports
import pygame
from sys import exit
import random

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
        global player_x_pos
        player_x_pos = self.rect.x
        
        



class Breakage(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        self.type = type

        breakage_image = pygame.image.load("images/breakage.png").convert_alpha()
        self.image = breakage_image
        
        # If type is sail, bow, floor_board or rope it sets the y and x position of the breakage
        # and generates 3 random numbers between 0 and 9 for the passcode.
        if type == 'sail':
            self.y_pos = 301
            self.x_pos = 600

        elif type == 'bow':
            self.y_pos = 499
            self.x_pos = 1050

        elif type == 'floor_board':
            self.y_pos = 499
            self.x_pos = 400

        elif type == 'rope':
            self.y_pos = 499
            self.x_pos = 800

        self.pass_1 = random.randint(0,9)
        self.pass_2 = random.randint(0,9)
        self.pass_3 = random.randint(0,9)
        
        self.rect = self.image.get_rect(midtop = (self.x_pos, self.y_pos))
      

    # this is used to get the passcode when the player collides with the breakage based on the type of breakage
    def collition_passcode(self):
        collided_breakage = pygame.sprite.spritecollide(player.sprite, breakage, False)
        # b mean 'one Breakage object from the breakage group'
        for b in collided_breakage:
            if isinstance(b, Breakage):

                return [b.pass_1, b.pass_2, b.pass_3]
                # reference for later
                # if b.type == 'sail':
               
        
                    



# starts pygame
pygame.init() 

# Creates the play window
screen = pygame.display.set_mode((1200,675))

# sets the title for the game.
pygame.display.set_caption("Ultimate Pygame")

#creating font
pacific_font = pygame.font.Font('Font/Pacifico-regular.ttf',50)

# set up passcode variables
passcode = []
pass_digit_1 = 0
pass_digit_2 = 0
pass_digit_3 = 0


# sets the frame rate of the game.
clock = pygame.time.Clock()

# set game display name
pygame.display.set_caption("Crossing the Deep")

FPS = 60

# Groups
# add player to group
player =  pygame.sprite.GroupSingle()
player.add(Player())

# breakage group
breakage = pygame.sprite.Group()


#title
title_surf = pacific_font.render('Pacific Pursuit', True,"#006439")
title_rec = title_surf.get_rect(center = (600,373))

#blurb
info_surf = pacific_font.render('Press Space to Start, Press esacpe to quit, Press "h" for how to play',True,('#006439'))
info_surf = pygame.transform.scale(info_surf,(1000,50))
info_surf_rec = info_surf.get_rect(midbottom = (600, 500))

# set breakages spawning lists
breakage_type_eligible_list = ['sail', 'bow', 'floor_board', 'rope']
breakage_type_ineligible_list = []

# images
background_surf = pygame.image.load("images/stormy_background(Medium).png").convert_alpha()
game_state = 2 


# clocks
breakage_timer = pygame.USEREVENT + 1
pygame.time.set_timer(breakage_timer,1000)

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
        if game_state == 1:

            # Breakages spawning. Gets a random item from a list. adds it to the breakages sprite class, removes from current list and than put on another list. 
            if event.type == breakage_timer:
                if breakage_type_eligible_list:
                    removed_breakage = breakage_type_eligible_list[random.randint(0, len(breakage_type_eligible_list) - 1)]
                    breakage.add(Breakage(removed_breakage))
                    breakage_type_eligible_list.remove(removed_breakage)
                    breakage_type_ineligible_list.append(removed_breakage) # might not be needed for use laster

            
                


                    

       

    #main gameplay
    if game_state == 1:
        screen.blit(background_surf,(0,0))
        
       
        # updates pygame display.
        # drawing the breakage
        breakage.draw(screen)
                
        # drawing the player
        player.draw(screen)
        player.update()

        # getting the passcode from the breakage class
        for b in breakage:
            passcode = b.collition_passcode()
            if passcode:
                
                pass_digit_1 = passcode[0]
                pass_digit_2 = passcode[1]
                pass_digit_3 = passcode[2]

                font_colour = (255,0,0)
                
                # display the passcode digits
                pass_digit_1_text = pacific_font.render(f"{pass_digit_1}", True, font_colour)
                pass_digit_1_rect = pass_digit_1_text.get_rect(center = (500,500 ))

                pass_digit_2_text = pacific_font.render(f"{pass_digit_2}", True, font_colour)
                pass_digit_2_rect = pass_digit_2_text.get_rect(center = (600,500 ))

                pass_digit_3_text = pacific_font.render(f"{pass_digit_3}", True, font_colour)
                pass_digit_3_rect = pass_digit_3_text.get_rect(center = (700,500 ))

                screen.blit(pass_digit_1_text, pass_digit_1_rect)
                screen.blit(pass_digit_2_text, pass_digit_2_rect)
                screen.blit(pass_digit_3_text, pass_digit_3_rect)
            
        
        
    
    #title and game over screen
    if game_state == 2:

        screen.blit(background_surf,(0,0))
        pygame.draw.rect(screen,"#673506FF",(50,300,1100,300))
        pygame.draw.rect(screen,"#2C2C2CCC",(50,300,1100,300),10,2)
        screen.blit(info_surf,info_surf_rec)
        screen.blit(title_surf,title_rec)
        
    if game_state == 3:
        screen.blit(background_surf,(0,0))
        pygame.draw.rect(screen,"#673506FF",(50,25,1100,625))
        pygame.draw.rect(screen,"#2C2C2CCC",(50,25,1100,625),10,2)
        

   
    pygame.display.update()
    
    # While loop can only run at FPS speed per second. 
    clock.tick(FPS)



    




