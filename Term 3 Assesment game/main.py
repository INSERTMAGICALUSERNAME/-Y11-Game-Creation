# Fixing Boat game
# Creators Zach Hamilton and Johann Shotbolt
# Date: 15/07/2025 
# Version 1 

# imports
import pygame
from sys import exit
import random


class Player (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player_image = pygame.image.load("images/player_green.png").convert_alpha()

        self.image = self.player_image
        self.rect =  self.player_image.get_rect(midbottom = (600,400))


        self.gravity = 0 

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.y >= 400:
            self.rect.y = 400
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > 1130:
            self.rect.x = 1130

    
    
    def player_imput(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]:
            if self.rect.y >= 400:
                self.gravity = -20



        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.rect.y == 400:
                self.rect.x += 5
            else:
                self.rect.x += 8

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.rect.y == 400:
                self.rect.x -= 5
            else:
                self.rect.x -= 8

    def update(self):
        self.apply_gravity()
        self.player_imput()


class Button(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        self.type = type

        self.image = pygame.image.load("images/Wooden_plank.png").convert_alpha()
        

        self.x_pos = 600
        if type == 'top':
            self.y_pos = 280
            
        if type == 'middle':
            self.y_pos = 372
            
        if type == 'bottom':
            self.y_pos = 464
        
        
    
        # self.image = pygame.transform.scale(self.image,(360,65))
        self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))

    def check_click(self,mouse_pos,event):
        clicked = None
        if self.rect.collidepoint(mouse_pos):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if plank.type == 'top':
                    clicked = 1
                if plank.type == 'middle':
                    clicked = 2
                if plank.type == 'bottom':
                    clicked = 3       
        return clicked
            
        
        
        
        
            


    
    
    def update(self):
        self.draw(screen)
        self.check_click(pygame.mouse.get_pos())
        
    

# starts pygame
pygame.init() 

# Creates the play window
screen = pygame.display.set_mode((1200,675))

# sets the title for the game.
pygame.display.set_caption("Ultimate Pygame")

#creating font
pacific_font = pygame.font.Font('Font/Pacifico-regular.ttf',75)
pixel_font = pygame.font.Font('Font/Pixeltype.ttf',50)

# sets the frame rate of the game.
clock = pygame.time.Clock()

# set game display name
pygame.display.set_caption("Crossing the Deep")

FPS = 60

# Groups
# add player to group
player =  pygame.sprite.GroupSingle()
player.add(Player())

#Compass and wind
wind_strength = 0

wind_direction = random.randint(0, 1)  # 0 for left, 1 for right
if wind_direction == 0:
    wind_left = True
    wind_right = False
if wind_direction == 1:
    wind_right = True
    wind_left = False
tilt = (920 + wind_strength)


#title
title_surf = pacific_font.render('Pacific Pursuit', True,"#5fa8a9")
title_rec = title_surf.get_rect(center = (600,144))

plank_surf = pygame.image.load("images/Wooden_plank.png").convert_alpha()
plank_rect = plank_surf.get_rect(center = (600, 337))

hanging_sign = pygame.image.load("images/Hanging_Sign-removebg-preview.png").convert_alpha()
hanging_sign = pygame.transform.scale(hanging_sign,(500,700))
hanging_sign_rec = hanging_sign.get_rect(center = (600, 275))

#blurb

start_surf = pacific_font.render('START',True,("#342218"))
start_surf = pygame.transform.scale(start_surf,(200,50))
start_surf_rec = start_surf.get_rect(midbottom = (600, 305))

how_surf = pacific_font.render('How To Play',True,("#342218"))
how_surf = pygame.transform.scale(how_surf,(200,50))
how_surf_rec = how_surf.get_rect(midbottom = (600, 400))

quit_surf = pacific_font.render('QUIT',True,("#342218"))
quit_surf = pygame.transform.scale(quit_surf,(200,50))
quit_surf_rec = quit_surf.get_rect(midbottom = (600, 490))


#buttons
top = 'top'
middle = 'middle'
bottom = 'bottom'
button = pygame.sprite.Group()
button.add(Button(top))
button.add(Button(middle))
button.add(Button(bottom))


# images
background_surf = pygame.image.load("images/stormy_background.png").convert_alpha()
game_state = 2 

compass_direction = pygame.image.load("images/compass_direction.png").convert_alpha()
compass_direction = pygame.transform.scale2x(compass_direction)
compass_direction_rect = compass_direction.get_rect(center = (tilt, 100))

compass_bar = pygame.image.load("images/Compass_bar.png").convert_alpha()
compass_bar = pygame.transform.scale2x(compass_bar)
compass_bar_rect = compass_bar.get_rect(center = (1100,100))




while True:

    
    for event in pygame.event.get():
        # Closes the game if you click close
        if event.type == pygame.QUIT:
            pygame.quit() # oposite of pygame.init()
            exit()

        if game_state == 2:
            for plank in button:
                mouse_pos = pygame.mouse.get_pos()
                type_button_clicked = plank.check_click(mouse_pos,event)
                if type_button_clicked == 1:
                    game_state = 1
                if type_button_clicked == 2:
                    game_state = 3
                if type_button_clicked == 3:
                    pygame.quit()
                    exit()
            
            


       
            
            
            
            
            
                

    #main gameplay
    if game_state == 1:
        screen.blit(background_surf,(0,0))
        #compass and wind
        if wind_right:
            
            if tilt <= 840:
                wind_strength -= 0.2
            else:
                wind_strength -= 0.1
                
        if wind_left:
            
            if tilt >= 935:
                wind_strength += 0.2
            else:
                wind_strength += 0.1
        
        tilt = (890 + wind_strength/2)
        

        if tilt <= 800:
            tilt = 800
            
        if tilt >= 980:
            tilt = 980
        

        if wind_strength > 180:
            wind_strength = 180
        if wind_strength < -180:
            wind_strength = -180
        
            
        compass_direction_rect.x = tilt
        
        screen.blit(compass_direction,compass_direction_rect)
        screen.blit(compass_bar,compass_bar_rect)
        pygame.draw.rect(screen,"#000000FF",(772,90,250,20))
        pygame.draw.rect(screen,"#000000FF",(1178,90,22,20))




        # updates pygame display.
        player.draw(screen)
        player.update()
    
    #title and game over screen
    if game_state == 2:

        screen.blit(background_surf,(0,0))
        pygame.draw.rect(screen,"#c3dbdb",(title_rec.x-10 ,title_rec.y+10,title_rec.width + 30,title_rec.height))
        pygame.draw.rect(screen,"#6E6F71FF",(title_rec.x-10 ,title_rec.y+10,title_rec.width + 30,title_rec.height),10)
        
        screen.blit(title_surf,title_rec)
        screen.blit(hanging_sign,hanging_sign_rec)
        button.draw(screen)
        screen.blit(start_surf,start_surf_rec)
        screen.blit(how_surf,how_surf_rec)
        screen.blit(quit_surf,quit_surf_rec)
    if game_state == 3:
        screen.blit(background_surf,(0,-150))
        pygame.draw.rect(screen,"#673506FF",(50,25,1100,625))
        pygame.draw.rect(screen,"#2C2C2CCC",(50,25,1100,625),10,2)

        
        

        





            

   
    pygame.display.update()
    
    # While loop can only run at FPS speed per second. 
    clock.tick(FPS)



