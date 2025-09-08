# Fixing Boat game
# Creators Zach Hamilton and Johann Shotbolt
# Date: 15/07/2025 
# Version 1 

# imports all the librarys of code that we need for the game
import pygame
from sys import exit
import random

# the player class, where all the compenents of the player can be condensed and called easily. 
class Player (pygame.sprite.Sprite):
    # initializes the class and sets thing like image, rect and gravity. 
    def __init__(self):
        super().__init__()
         
        
        # loads all the different frames for the player
        self.player_frame_0 = pygame.image.load("images/player.png").convert_alpha()
        self.player_frame_0 = pygame.transform.scale(self.player_frame_0, (50, 100))

        self.player_frame_1 = pygame.image.load("images/player_frame_1.png").convert_alpha()
        self.player_frame_1 = pygame.transform.scale(self.player_frame_1, (50, 100))

        self.player_frame_2 = pygame.image.load("images/player_frame_2.png").convert_alpha()
        self.player_frame_2 = pygame.transform.scale(self.player_frame_2, (50, 100))

        self.player_frame_3 = pygame.image.load("images/player_frame_3.png").convert_alpha()
        self.player_frame_3 = pygame.transform.scale(self.player_frame_3, (50, 100))

        self.player_frame_4 = pygame.image.load("images/player_frame_4.png").convert_alpha()
        self.player_frame_4 = pygame.transform.scale(self.player_frame_4, (100, 100))

        self.player_frame_5 = pygame.image.load("images/player_frame_5.png").convert_alpha()
        self.player_frame_5 = pygame.transform.scale(self.player_frame_5, (100, 100))

        self.player_frame_6 = pygame.image.load("images/player_frame_6.png").convert_alpha()
        self.player_frame_6 = pygame.transform.scale(self.player_frame_6, (100, 100))

        self.player_frame_7 = pygame.image.load("images/player_frame_7.png").convert_alpha()
        self.player_frame_7 = pygame.transform.scale(self.player_frame_7, (100, 100))

        self.player_frame_8 = pygame.image.load("images/player_frame_8.png").convert_alpha()
        self.player_frame_8 = pygame.transform.scale(self.player_frame_8, (100, 100))
        
        self.player_frame_9 = pygame.image.load("images/player_frame_9.png").convert_alpha()
        self.player_frame_9 = pygame.transform.scale(self.player_frame_9, (100, 100))

        self.player_frame_10 = pygame.image.load("images/player_frame_10.png").convert_alpha()
        self.player_frame_10 = pygame.transform.scale(self.player_frame_10, (100, 100))

        #setting up the variables required for animation
        self.player_frames = [self.player_frame_0,self.player_frame_1,self.player_frame_2,self.player_frame_3,self.player_frame_4,self.player_frame_5,self.player_frame_6,self.player_frame_7,self.player_frame_8,self.player_frame_9,self.player_frame_10]
        self.player_frame_index = 0

        self.image = self.player_frames[self.player_frame_index]
        self.rect =  self.image.get_rect(midbottom = (600,570))

        #setting the player gravity to 0
        self.gravity = 0

    # player jump. and player collitions with sides of player area and raised deck
    def apply_gravity_and_jump(self):
        global ship_damage
        

        keys = pygame.key.get_pressed()
        
        # if the user click the jump button while the player is touching the groung then gravity will be set to -20. 
        # else if the player is touching the the raised floor than there gravity is set to zero. 


        if keys[pygame.K_LSHIFT] or keys[pygame.K_s] or keys[pygame.K_DOWN]:

            if self.rect.colliderect(raised_deck):
                self.gravity = 5
                
        elif keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]:
            if self.rect.y >= 470:
                self.gravity = -20
                
            elif self.rect.colliderect(raised_deck):
                if raised_deck.bottom > self.rect.bottom >= raised_deck.top:
                    self.gravity = -20
                    
        else:
            if self.rect.colliderect(raised_deck):
                if raised_deck.bottom > self.rect.bottom >= raised_deck.top:
                    self.rect.bottom = raised_deck.top
                    self.gravity = 0 
                    

        if keys[pygame.KMOD_SHIFT]:
            if self.rect.colliderect(raised_deck):
                self.gravity = -10
                
  
        
        self.gravity += 1
        self.rect.y += self.gravity

        
        # makes the player stay in the play area 
        if self.rect.y >= 470 and not self.rect.left > 1050 and not self.rect.right < 30 :
            self.rect.y = 470
            self.gravity = 0

        
        if (self.rect.right < 10 and self.rect.y >= 470) or (self.rect.left > 1150 and self.rect.y >= 470) or self.rect.y > 600:
            ship_damage = 250

            


    
    # player left and right movement
    def player_movement(self):

        # get keys pressed
        keys = pygame.key.get_pressed()

        # moving right
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.rect.y == 470:
                self.rect.x += 5
                
            elif self.rect.colliderect(raised_deck):
                
                self.rect.x += 5
            # if the player is jumping they go faster
            else:
                self.rect.x += 8
            self.player_frame_index = 0
                
        # moving left
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.rect.y == 470:
                
                self.rect.x -= 5
            elif self.rect.colliderect(raised_deck):
                
                self.rect.x -= 5
            # if the player is jumping they go faster
            else:
                self.rect.x -= 8
            self.player_frame_index = 0
        
    
   





    # calls of the defs for the class
    def update(self):
        self.apply_gravity_and_jump()
        self.player_movement()
        global player_x_pos
        global fixing
        player_x_pos = self.rect.x
        self.image = self.player_frames[self.player_frame_index]
        
        
            
        if game_state == 4:
            self.rect.midbottom = (600, 570)
            

        

class Breakage(pygame.sprite.Sprite):
    # inicailizes the class and sets thing like image and rect
    def __init__(self, type):
        super().__init__()
        self.type = type
        border_width = 4
        border_color = (255, 0, 0)

        
        breakage_image = pygame.image.load("images/breakage.png").convert_alpha()
        alpha_value = 50  # 50% transparency
        breakage_image.set_alpha(alpha_value)
        self.image = breakage_image
        
        # If type is sail, bow, floor_board or rope it sets the y and x position of the breakage
        if type == 'sail':
            self.y_pos = 335
            self.x_pos = 690

        elif type == 'bow':
            self.y_pos = 499
            self.x_pos = 950

        elif type == 'rope':
            self.y_pos = 450
            self.x_pos = 380

        elif type == 'floor_board':
            self.y_pos = 550
            self.x_pos = 735

        # generates 3 random numbers between 0 and 9 for the passcode.
        self.pass_1 = random.randint(0,9)
        self.pass_2 = random.randint(0,9)
        self.pass_3 = random.randint(0,9)
        
        self.rect = self.image.get_rect(midtop = (self.x_pos, self.y_pos))
        w, h = breakage_image.get_size()
        self.image = pygame.Surface((w + border_width, h + border_width), pygame.SRCALPHA)
        pygame.draw.rect(self.image, border_color, self.image.get_rect(), border_width)

      

    # this is used to get the passcode when the player collides with the breakage based on the type of breakage
    def collition_passcode(self):
        collided_breakage = pygame.sprite.spritecollide(player.sprite, breakage, False)
        # b mean 'one Breakage object from the breakage group'
        for b in collided_breakage:
            if isinstance(b, Breakage):
                return [b.pass_1, b.pass_2, b.pass_3]

              
class Main_buttons(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        self.object_type = type

        self.image = pygame.image.load("images/Wooden_plank.png").convert_alpha()
        self.x_pos = 600
        if type == 'top':
            self.y_pos = 278
        if type == "middle":
            self.y_pos = 372
        if type == "bottom":
            self.y_pos = 466
        if type == "top_5":
            self.y_pos = 278
            self.image = pygame.transform.scale(self.image, (360, 65))
        if type == "middle_5":
            self.y_pos = 372
            self.image = pygame.transform.scale(self.image, (360, 65))
        if type == "bottom_5":
            self.y_pos = 466
            self.image = pygame.transform.scale(self.image, (360, 65))

        self.rect = self.image.get_rect(center = (self.x_pos,self.y_pos))

   # checks if the user clicks on a button and return a result based on the button pressed
    def check_click(self):
        global difficulty
        clicked = None
        if self.rect.collidepoint(pygame.mouse.get_pos()):

            if event.type == pygame.MOUSEBUTTONDOWN and game_state_2_timer > 15:

                if  self.object_type == 'top':
                    clicked = 5
                elif self.object_type == 'middle':
                    clicked = 2
                elif self.object_type == 'bottom':
                    clicked = 3


            elif event.type == pygame.MOUSEBUTTONDOWN and game_state_5_timer > 15:

                if self.object_type == 'top_5':
                    difficulty = 1
                    clicked = 1
                if self.object_type == 'middle_5':
                    difficulty = 2
                    clicked = 1
                if self.object_type == 'bottom_5':
                    difficulty = 3
                    clicked = 1
        return clicked
    
    def check_hover(self):
        
    # if the mouse is hovering over the game over buttom the text will change colour
        if self.object_type == "top":
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.main_start_surf= pacific_font.render('START',True,("#A9FFF8"))
                self.main_start_surf = pygame.transform.scale(self.main_start_surf,(200,50))
            else: 
                self.main_start_surf = pacific_font.render('START',True,("#342218"))
                self.main_start_surf = pygame.transform.scale(self.main_start_surf,(200,50))

        if self.object_type == "middle":
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.main_help_surf = pacific_font.render('HOW TO PLAY',True,("#A9FFF8"))
                self.main_help_surf = pygame.transform.scale(self.main_help_surf,(200,50))
            else: 
                self.main_help_surf = pacific_font.render('HOW TO PLAY',True,("#342218"))
                self.main_help_surf = pygame.transform.scale(self.main_help_surf,(200,50))


        
        if self.object_type == "bottom":
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.main_quit_surf = pacific_font.render('QUIT',True,("#A9FFF8"))
                self.main_quit_surf = pygame.transform.scale(self.main_quit_surf,(200,50))
            else:
                self.main_quit_surf = pacific_font.render('QUIT',True,("#342218"))
                self.main_quit_surf = pygame.transform.scale(self.main_quit_surf,(200,50))
        
        if self.object_type == "top_5":
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.main_start_surf= pacific_font.render('Easy',True,("#A9FFF8"))
                self.main_start_surf = pygame.transform.scale(self.main_start_surf,(200,50))
            else: 
                self.main_start_surf = pacific_font.render('Easy',True,("#342218"))
                self.main_start_surf = pygame.transform.scale(self.main_start_surf,(200,50))

        if self.object_type == "middle_5":
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.main_help_surf = pacific_font.render('Medium',True,("#A9FFF8"))
                self.main_help_surf = pygame.transform.scale(self.main_help_surf,(200,50))
            else: 
                self.main_help_surf = pacific_font.render('Medium',True,("#342218"))
                self.main_help_surf = pygame.transform.scale(self.main_help_surf,(200,50))


        
        if self.object_type == "bottom_5":
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.main_quit_surf = pacific_font.render('Hard',True,("#A9FFF8"))
                self.main_quit_surf = pygame.transform.scale(self.main_quit_surf,(200,50))
            else:
                self.main_quit_surf = pacific_font.render('Hard',True,("#342218"))
                self.main_quit_surf = pygame.transform.scale(self.main_quit_surf,(200,50))
        

        
    def update(self):
        global game_state

        self.check_hover()

        
        clicked = self.check_click()
        if clicked == 5:
            game_state = 5
        if clicked == 2:
            game_state = 3
        if clicked == 3:
            pygame.quit()
            exit()
        if clicked == 1:
            game_state = 1
        

        if self.object_type == 'top':
            self.main_start_rect = self.main_start_surf.get_rect(center = (600, self.y_pos))
            screen.blit(self.main_start_surf,self.main_start_rect)

        if self.object_type == 'middle':
            self.main_help_rect = self.main_help_surf.get_rect(center = (600, self.y_pos))
            screen.blit(self.main_help_surf,self.main_help_rect )

        if self.object_type == 'bottom':
            self.main_quit_rect = self.main_quit_surf.get_rect(center = (600, self.y_pos))
            screen.blit(self.main_quit_surf,self.main_quit_rect)

        if self.object_type == 'top_5':
            self.main_start_rect = self.main_start_surf.get_rect(center = (600, self.y_pos))
            screen.blit(self.main_start_surf, self.main_start_rect)

        if self.object_type == 'middle_5':
            self.main_help_rect = self.main_help_surf.get_rect(center = (600, self.y_pos))
            screen.blit(self.main_help_surf, self.main_help_rect)

        if self.object_type == 'bottom_5':
            self.main_quit_rect = self.main_quit_surf.get_rect(center = (600, self.y_pos))
            screen.blit(self.main_quit_surf, self.main_quit_rect)
           

class Game_over_buttons(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        self.object_type = type

        self.image = pygame.image.load("images/Wooden_plank.png").convert_alpha()
        self.x_pos = 600
        if type == 'top':
            self.y_pos = 325
        if type == "bottom":
            self.y_pos = 418
        




        self.rect = self.image.get_rect(center = (self.x_pos,self.y_pos))

    def check_click(self):
        clicked = None

        if self.rect.collidepoint(pygame.mouse.get_pos()) and game_state_4_timer > 15:

            if event.type == pygame.MOUSEBUTTONDOWN:
                if  self.object_type == 'top':
                    clicked = 1
                if self.object_type == 'bottom':
                    clicked = 2     
        return clicked
    
    def check_hover(self):
          
    # if the mouse is hovering over the game over buttom the text will change colour
        if self.object_type == "top":
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.restart_game_over_surf = pacific_font.render('RESTART',True,("#A9FFF8"))
                self.restart_game_over_surf = pygame.transform.scale(self.restart_game_over_surf,(200,50))
            else: 
                self.restart_game_over_surf = pacific_font.render('RESTART',True,("#342218"))
                self.restart_game_over_surf = pygame.transform.scale(self.restart_game_over_surf,(200,50))


        
        if self.object_type == "bottom":
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.home_game_over_surf = pacific_font.render('HOME',True,("#A9FFF8"))
                self.home_game_over_surf = pygame.transform.scale(self.home_game_over_surf,(200,50))
            else:
                self.home_game_over_surf = pacific_font.render('HOME',True,("#342218"))
                self.home_game_over_surf = pygame.transform.scale(self.home_game_over_surf,(200,50))
        
      


        
    def update(self):
        global game_state

        self.check_hover()

        
        clicked = self.check_click()
        if clicked == 1:
            game_state = 1
            
        if clicked == 2:
            game_state = 2
            
        

        if self.object_type == 'top':
            restart_surf_rect = self.restart_game_over_surf.get_rect(center = (600, self.y_pos))
            screen.blit(self.restart_game_over_surf,restart_surf_rect)

        if self.object_type == 'bottom':
            home_game_over_rect = self.home_game_over_surf.get_rect(center = (600, self.y_pos))
            screen.blit(self.home_game_over_surf, home_game_over_rect)


class Button_how(pygame.sprite.Sprite):
    # inicailizes the class and sets thing like image and rect
    def __init__(self, type):
        super().__init__()
        self.type = type

  
        self.image = pygame.image.load("images/Wooden_plank.png").convert_alpha()
        

        self.x_pos = 600
        if type == 'top_left':
            self.y_pos = 70
            self.x_pos = 190
            self.image = pygame.transform.scale(self.image,(250,50))

      
        # self.image = pygame.transform.scale(self.image,(360,65))
        self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))

    def check_click(self,mouse_pos,event):
        clicked = None
        if self.rect.collidepoint(mouse_pos):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.type == 'top_left':
                    clicked = 1
                
        return clicked
    def check_hover(self):
          
    # if the mouse is hovering over the game over buttom the text will change colour
        if self.type == "top_left":
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.restart_game_over_surf = pacific_font.render('HOME',True,("#A9FFF8"))
                self.restart_game_over_surf = pygame.transform.scale(self.restart_game_over_surf,(200,50))
            else: 
                self.restart_game_over_surf = pacific_font.render('RESTART',True,("#342218"))
                self.restart_game_over_surf = pygame.transform.scale(self.restart_game_over_surf,(200,50))        
        
        
        
        
            


    
    
    def update(self):
        self.draw(screen)
        self.check_click(pygame.mouse.get_pos())




def display_score():
    global score
    global wind_score_weight
    if score <= 1:
        score = 1
    if score > 900:
        score = 900
    score += wind_score_weight # Calculate score based on elapsed time and wind strength
    #drawing score bar
    pygame.draw.rect(screen,(0,255,125),(50,15,score,45))
    

                  
# pygame set up code
pygame.init() 
screen = pygame.display.set_mode((1200,675))
pygame.display.set_caption("Ultimate Pygame")
pacific_font = pygame.font.Font('Font/Pacifico-regular.ttf',75)
pixel_font = pygame.font.Font('Font/Pixeltype.ttf',50)
clock = pygame.time.Clock()
pygame.display.set_caption("Crossing the Deep")






# variable set up
FPS = 60
game_state_2_timer = 0
game_state_4_timer = 0
game_state_5_timer = 0 

game_state = 2 # 1 = main gameplay, 2 = title screen, 3 = how to play screen, 4 = game over screen 5 = difficulty selection Screen. 
keys = None

score = 0
restart_screen_score = 0
game_timer = 0 
game_timer_score = 0

win = False
lose = True

ship_damage = 0

# set up passcode variables
passcode = []
pass_digit_1 = 0
pass_digit_2 = 0
pass_digit_3 = 0


input_digit_1 = None
input_digit_2 = None
input_digit_3 = None

breakage_colide_type = None
wrong_text = 0
fixing = False
changing= False
outline = False
wind_score_weight = 0

water_outline = False
difficulty = 1
# Groups

#player group
player =  pygame.sprite.GroupSingle()
player.add(Player())


#buttons

# home screen buttons
top = 'top'
middle = 'middle'
bottom = 'bottom'

top_5 = 'top_5'
middle_5 = 'middle_5'
bottom_5 = 'bottom_5'

main_button = pygame.sprite.Group()
main_button.add(Main_buttons(top))
main_button.add(Main_buttons(middle))
main_button.add(Main_buttons(bottom))

difficulty_buttons = pygame.sprite.Group()
difficulty_buttons.add(Main_buttons(top_5))
difficulty_buttons.add(Main_buttons(middle_5))
difficulty_buttons.add(Main_buttons(bottom_5))


# game over screen buttons
game_over_button = pygame.sprite.Group()
game_over_button.add(Game_over_buttons(top))
game_over_button.add(Game_over_buttons(bottom))

# breakage group
breakage = pygame.sprite.Group()
button_how = pygame.sprite.Group()
button_how.add(Button_how('top_left'))









#Compass and wind
wind_strength = 0
tilt = (920 + wind_strength)

wind_direction = random.randint(0, 1)  # 0 for left, 1 for right
if wind_direction == 0:
    wind_strength -= 0.1
if wind_direction == 1:
    wind_strength += 0.1
tilt = (920 + wind_strength)






#title screen
title_surf = pacific_font.render('Pacific Pursuit', True,"#5fa8a9")
title_rec = title_surf.get_rect(center = (600,144))

plank_surf = pygame.image.load("images/Wooden_plank.png").convert_alpha()
plank_rect = plank_surf.get_rect(center = (600, 337))

hanging_sign = pygame.image.load("images/Hanging_Sign-removebg-preview.png").convert_alpha()
hanging_sign = pygame.transform.scale(hanging_sign,(500,700))
hanging_sign_rec = hanging_sign.get_rect(center = (600, 275))







#breakages spawning lists

breakage_type_eligible_list = ['sail', 'bow', 'floor_board', 'rope']
breakage_type_ineligible_list = []






# images
# background
background_surf = pygame.image.load("images/stormy_background(Medium).png").convert_alpha()
# sunny_background_surf = pygame.image.load('images/new_sunny_background(Custom).png')

# play
dead_player_surf = pygame.image.load("images/player.png").convert_alpha()
dead_player_surf = pygame.transform.scale(dead_player_surf, (50, 100))
dead_player_rect = dead_player_surf.get_rect(midbottom = (1050,410))
alive_player_rect = dead_player_surf.get_rect(midbottom = (925,610))
# compass_direction surfs and rects
compass_direction = pygame.image.load("images/compass_direction.png").convert_alpha()
compass_direction = pygame.transform.scale2x(compass_direction)
compass_direction_rect = compass_direction.get_rect(center = (tilt, 100))

hide_compass_direction_left_surf = pygame.image.load("images/hide_compass_direction_right.png").convert_alpha()
hide_compass_direction_left_rect = hide_compass_direction_left_surf.get_rect(topleft = (1178,90))

hide_compass_direction_right_surf = pygame.image.load("images/hide_compass_direction_left.png").convert_alpha()
hide_compass_direction_right_rect = hide_compass_direction_right_surf.get_rect(topleft = (772,90))

compass_bar = pygame.image.load("images/Compass_bar.png").convert_alpha()
compass_bar = pygame.transform.scale2x(compass_bar)
compass_bar_rect = compass_bar.get_rect(center = (1100,100))

score_bar = pygame.image.load("images/score_frame.png").convert_alpha()
score_bar_rect = score_bar.get_rect(topleft=(50,15))

score_island_surf = pygame.image.load("images/Score_island.png").convert_alpha()
score_island_surf = pygame.transform.scale(score_island_surf,(150,150))
score_island_rect = score_island_surf.get_rect(center=(950, 35))

win_island_surf = pygame.image.load("images/island.png").convert_alpha()
win_island_rect = win_island_surf.get_rect(bottomright =(1400,675))

# rain frames and animations.
rain_frame_1 = pygame.image.load("images/rain_frame_1.png").convert_alpha()
rain_surf_1 = pygame.transform.scale(rain_frame_1,(1200,675))
rain_frame_2 = pygame.image.load("images/rain_frame_2.png").convert_alpha()
rain_surf_2 = pygame.transform.scale(rain_frame_2,(1200,675))
rain_frames = [rain_surf_1,rain_surf_2]
rain_frame_index = 0
rain_surf = rain_frames[rain_frame_index]
rain_rect = rain_surf.get_rect(topleft = (0,0))

broken_boat_surf = pygame.image.load("images/broken_boat.png").convert_alpha()
broken_boat_surf = pygame.transform.scale(broken_boat_surf,(1200,675))
broken_boat_rect = broken_boat_surf.get_rect(center = (500, 475))


# ship damage
ship_damage_meter_surf = pygame.image.load("images/damage_bar.xcf").convert_alpha()
ship_damage_meter_surf = pygame.transform.scale2x(ship_damage_meter_surf)
ship_damage_meter_surf = pygame.transform.rotate(ship_damage_meter_surf, 90)
ship_damage_meter_rect = ship_damage_meter_surf.get_rect(topleft=(50,82))



# ship 
boat_surf = pygame.image.load("images/pixel_boat_fixed_boarder_real.xcf").convert_alpha()
boat_surf= pygame.transform.scale(boat_surf,(1200,675))
boat_rect = boat_surf.get_rect(center = (600, 375))

win_boat_rect = boat_surf.get_rect(bottomright = (1000, 775))


raised_deck = pygame.Rect(310, 530, 510, 20)
rudder_rect = pygame.Rect(330, 450, 100, 50)

# Game Over screen text



traveled_safly_surf = pacific_font.render('You Succsesfuly Traveled Through the Storm',True,(0,255,0))
traveled_safly_surf = pygame.transform.scale(traveled_safly_surf,(1100,100))
traveled_safly_rect = traveled_safly_surf.get_rect(center = (600,100))



not_traveled_safly_surf = pacific_font.render('You Perished While Trying to Travel Through the Storm',True,(255,0,0))
not_traveled_safly_surf = pygame.transform.scale(not_traveled_safly_surf,(1100,100))
not_traveled_safly_rect = not_traveled_safly_surf.get_rect(center = (600,100))

#how to screen 
how_to_play_surf = pygame.image.load("images/how to play.png").convert_alpha()
how_to_play_surf = pygame.transform.scale(how_to_play_surf,(1100,625))
how_to_play_rect = how_to_play_surf.get_rect(center = (600, 337))


# clocks
breakage_timer_e = pygame.USEREVENT + 1
pygame.time.set_timer(breakage_timer_e,7000)

breakage_timer_m = pygame.USEREVENT + 4
pygame.time.set_timer(breakage_timer_m,5000)

breakage_timer_h = pygame.USEREVENT + 5
pygame.time.set_timer(breakage_timer_h,4000)

damage_timer = pygame.USEREVENT + 2
pygame.time.set_timer(damage_timer,200)

second_timer = pygame.USEREVENT + 3
pygame.time.set_timer(second_timer,1000)

rain_anamation_timer = pygame.USEREVENT + 6
pygame.time.set_timer(rain_anamation_timer,100)
 
while True:

    
    for event in pygame.event.get():
        # Closes the game if you click close
        if event.type == pygame.QUIT:
            pygame.quit() # oposite of pygame.init()
            exit()
        
        if game_state == 3 or game_state == 5:
            for plank in button_how:
                mouse_pos = pygame.mouse.get_pos()
                type_button_clicked = plank.check_click(mouse_pos,event)
                if type_button_clicked == 1:
                    game_state = 2
        
           


        # if the game is in the main gameplay state
        if game_state == 1:
            
            # rain animation cycling through the rain frames
            if event.type == rain_anamation_timer:
                if rain_frame_index == 0:
                    rain_frame_index = 1
                else:
                    rain_frame_index = 0
                rain_surf = rain_frames[rain_frame_index]
                rain_rect = rain_surf.get_rect(topleft = (0,0))
                
            # Breakages spawning. Gets a random item from a list. adds it to the breakages sprite class, removes from current list and than put on another list. \
            # spawns at differant rates based on difficulty 
            if difficulty == 1:
                if event.type == breakage_timer_e:
                    if breakage_type_eligible_list:
                        removed_breakage = breakage_type_eligible_list[random.randint(0, len(breakage_type_eligible_list) - 1)]
                        breakage.add(Breakage(removed_breakage))
                        breakage_type_eligible_list.remove(removed_breakage)
                        breakage_type_ineligible_list.append(removed_breakage) 

            elif difficulty == 2:
                if event.type == breakage_timer_m:
                    if breakage_type_eligible_list:
                        removed_breakage = breakage_type_eligible_list[random.randint(0, len(breakage_type_eligible_list) - 1)]
                        breakage.add(Breakage(removed_breakage))
                        breakage_type_eligible_list.remove(removed_breakage)
                        breakage_type_ineligible_list.append(removed_breakage) 

            elif difficulty == 3:
                if event.type == breakage_timer_h:
                    if breakage_type_eligible_list:
                        removed_breakage = breakage_type_eligible_list[random.randint(0, len(breakage_type_eligible_list) - 1)]
                        breakage.add(Breakage(removed_breakage))
                        breakage_type_eligible_list.remove(removed_breakage)
                        breakage_type_ineligible_list.append(removed_breakage) 

            # damage the ship based on the amount of breakages and difficulty
            if event.type == damage_timer:
                breakage_count = len(breakage_type_ineligible_list)
                
                if difficulty == 1:
                    if breakage_count <=0:
                        None
                    elif breakage_count  <=1:
                        ship_damage +=0.25
                        
                    elif breakage_count  <=2:
                        ship_damage +=0.5
                        
                    elif breakage_count  <=3:
                        ship_damage +=1.5
                        
                    elif breakage_count  <=4:
                        ship_damage += 3.5

                
                elif difficulty == 2:
                    if breakage_count <=0:
                        None
                    elif breakage_count  <=1:
                        ship_damage +=1
                        
                    elif breakage_count  <=2:
                        ship_damage +=2
                        
                    elif breakage_count  <=3:
                        ship_damage +=3.5
                        
                    elif breakage_count  <=4:
                        ship_damage += 5
                        
                elif difficulty == 3:
                    if breakage_count <=0:
                        None
                    elif breakage_count  <=1:
                        ship_damage +=1.5
                        
                    elif breakage_count  <=2:
                        ship_damage +=2.5
                        
                    elif breakage_count  <=3:
                        ship_damage +=4.5
                        
                    elif breakage_count  <=4:
                        ship_damage += 6


                #debug mode
                # ship_damage = 0

                



                keys = pygame.key.get_pressed()
                if (
                    not fixing and
                    not changing and
                    player.sprite.rect.y == 470 and
                    not keys[pygame.K_a] and
                    not keys[pygame.K_d] and
                    not keys[pygame.K_RIGHT] and
                    not keys[pygame.K_LEFT]
                ):
                    if keys[pygame.K_r] or keys[pygame.K_KP_MINUS]:

                        ship_damage -= 3
                        water_outline = True
                        if ship_damage <= 0:
                            ship_damage = 0
                            water_outline = False

                        
                    else:
                        water_outline = False
                else:
                    water_outline = False

  
                
                    


            # increase timer by 1 every second
            if event.type == second_timer:
                game_timer +=1

            

            # if user presses 'f' key, it will set fixing to True, allowing the player to input digits.
            # if user presses 'r' key, it will set fixing to False, resetting the input digits to None.
            # if user input is the correct digit game moves to the next digit, if not resets all digits to None.
            elif event.type == pygame.KEYDOWN:

                if pygame.sprite.spritecollide(player.sprite, breakage, False):

                    if event.key == pygame.K_f or event.key == pygame.K_KP_PLUS or event.key == pygame.K_KP_ENTER:
                        fixing = True
                
                    if fixing:
                        if event.unicode.isdigit():
                            digit = int(event.unicode)
                            

                            

                            
                            #animating the player depending on what key is pressed
                            if 1 <= digit <= 9:
                                player.sprite.player_frame_index = digit
                                
                            elif digit == 0:
                                player.sprite.player_frame_index = 10
                                
                            
                            

                            if input_digit_1 == pass_digit_1 and input_digit_2 == pass_digit_2:
                                input_digit_3 = digit
                                if input_digit_3 != pass_digit_3:
                                    input_digit_1 = None
                                    input_digit_2 = None
                                    input_digit_3 = None
                                    wrong_text = 60

                            elif input_digit_1 == pass_digit_1:
                                input_digit_2 = digit
                                if input_digit_2 != pass_digit_2:
                                    input_digit_1 = None
                                    input_digit_2 = None
                                    wrong_text = 60
                            

                            elif input_digit_1 == None:
                                input_digit_1 = digit
                                if input_digit_1 != pass_digit_1:
                                    input_digit_1 = None
                                    wrong_text = 60

                            else:
                                input_digit_1 = None
                                input_digit_2 = None
                                input_digit_3 = None
                    if event.key == pygame.K_r:
                        fixing = False
                        input_digit_1 = None
                        input_digit_2 = None
                        input_digit_3 = None
                        
                            
                            
                        
                else:
                        input_digit_1 = None
                        input_digit_2 = None
                        input_digit_3 = None
                        fixing = False
        
        # Restart game
        if game_state == 4:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_state = 1





    #main gameplay
    if game_state == 1:
        pygame.draw.rect(screen, (0,0,255), raised_deck)
        screen.blit(background_surf,(0,0))
        
        screen.blit(boat_surf,boat_rect)
        screen.blit(rain_surf,rain_rect)
        #compass and wind
        if wind_strength <= 0:
            
            if tilt <= 840:
                wind_strength -= 0.2
            else:
                wind_strength -= 0.1
                
        if wind_strength > 0:
            
            if tilt >= 935:
                wind_strength += 0.2
            else:
                wind_strength += 0.1
        
        tilt = (890 + wind_strength/2)

        if wind_strength > 180:
            wind_strength = 180
        if wind_strength < -180:
            wind_strength = -180

        press = pygame.key.get_pressed()
        



        if rudder_rect.colliderect(player.sprite):
            if press[pygame.K_f] or press[pygame.K_KP_PLUS] or press[pygame.K_KP_ENTER]:
                changing = True
                outline = True 
                
        else:
                changing = False  
                outline = False  


        if changing:
            
            if rudder_rect.colliderect(player.sprite.rect) and not pygame.sprite.spritecollide(player.sprite, breakage, False):
                outline = True
                if press[pygame.K_q]:
                    wind_strength += 1
                if press[pygame.K_e]:
                    wind_strength -= 1
            
            else:
                outline = False
                changing = False

        # sets the wind score weight based on the difficulty and directon the ship is facing. 

        if difficulty == 1:  
            if 20 > wind_strength > -20: #inside the green zone
                wind_score_weight = 0.25
            elif 60 > wind_strength > -60:#inside the yellow zone
                wind_score_weight = 0.2
            elif 100 > wind_strength > -100:#inside the orange zone
                wind_score_weight = 0.15
            else:
                wind_score_weight = 0.07#inside the red zone
            
        
        elif difficulty == 2:
            if 20 > wind_strength > -20:#inside the green zone
                wind_score_weight = 0.2
            elif 60 > wind_strength > -60:#inside the yellow zone
                wind_score_weight = 0.1
            elif 100 > wind_strength > -100:#inside the orange zone
                wind_score_weight = 0.05
            else:
                wind_score_weight = -0.03#inside the red zone
            
        elif difficulty == 3:
            if 20 > wind_strength > -20:#inside the green zone
                wind_score_weight = 0.2
            elif 60 > wind_strength > -60:#inside the yellow zone
                wind_score_weight = 0.075
            elif 100 > wind_strength > -100:#inside the orange zone
                wind_score_weight = 0.05
            else:
                wind_score_weight = -0.1#inside the red zone

        if press[pygame.K_x]or press[pygame.K_LSHIFT]:
            fixing = False
            changing = False
            outline = False
        
        
        
        #drawing everything on the screen
        pygame.draw.rect(screen, (0,255,255), rudder_rect,2)
        compass_direction_rect.x = tilt
        
        screen.blit(compass_direction,compass_direction_rect)
        screen.blit(compass_bar,compass_bar_rect)

        screen.blit(hide_compass_direction_right_surf,hide_compass_direction_right_rect)
        screen.blit(hide_compass_direction_left_surf,hide_compass_direction_left_rect)
        if outline:
            pygame.draw.rect(screen, (0, 255, 0), compass_bar_rect, 2)  # Draw the outline of the rudder
        
        display_score()
        screen.blit(score_bar, score_bar_rect)
        screen.blit(score_island_surf, score_island_rect)
        
        # draws ship_damage_indecator_height based on ship_damage
        ship_damage_indecator_height = ship_damage/1.7857142857142858 + 5
        ship_damage_indecator_left_top_y = 232 - ship_damage_indecator_height
        pygame.draw.rect(screen,(0,0,255), (55,ship_damage_indecator_left_top_y,25,ship_damage_indecator_height ))
        screen.blit(ship_damage_meter_surf,ship_damage_meter_rect )
        if water_outline:
            pygame.draw.rect(screen, (0, 255, 0), ship_damage_meter_rect, 2)
        
        



        # updates pygame display.

        # if the player is not colliding with a breakage, it will set fixing to False
        if not pygame.sprite.spritecollide(player.sprite, breakage, False):
            fixing = False
            


        # getting the passcode from the breakage class
        for b in breakage:
            if fixing:
                passcode = b.collition_passcode()
                if passcode:
                    

                    pass_digit_1 = passcode[0]
                    pass_digit_2 = passcode[1]
                    pass_digit_3 = passcode[2]


                    # if the input digit is equal to the passcode digit, it will change the font colour to green
                    # if the input digit is not equal to the passcode digit, it will change the font colour to orange for 60 frames, then red.
                
                    if input_digit_1 == pass_digit_1:
                        font_colour_1 = (0,255,0)
                    elif wrong_text > 0:
                        wrong_text -= 1
                        font_colour_1 = (255, 165, 0)
                        font_colour_2 = (255, 165, 0)
                        font_colour_3 = (255, 165, 0)
                    else:
                        font_colour_1 = (255,0,0)
                    

                    if input_digit_2 == pass_digit_2:
                        font_colour_2 = (0,255,0)
                    elif wrong_text > 0:
                        wrong_text -= 1
                        font_colour_1 = (255, 165, 0)
                        font_colour_2 = (255, 165, 0)
                        font_colour_3 = (255, 165, 0)
                    else:
                        font_colour_2 = (255,0,0)


                        
                    if input_digit_3 == pass_digit_3:
                        font_colour_3 = (0,255,0)
                    elif wrong_text > 0:
                        wrong_text -= 1
                        font_colour_1 = (255, 165, 0)
                        font_colour_2 = (255, 165, 0)
                        font_colour_3 = (255, 165, 0)
                    else:
                        font_colour_3 = (255,0,0)
                
                
                    
                    # display the passcode digits
                    pass_digit_1_text = pacific_font.render(f"{pass_digit_1}", True, font_colour_1)
                    pass_digit_1_rect = pass_digit_1_text.get_rect(center = (500,615 ))
                    
                    pass_digit_2_text = pacific_font.render(f"{pass_digit_2}", True, font_colour_2)
                    pass_digit_2_rect = pass_digit_2_text.get_rect(center = (600,615 ))

                    pass_digit_3_text = pacific_font.render(f"{pass_digit_3}", True, font_colour_3)
                    pass_digit_3_rect = pass_digit_3_text.get_rect(center = (700,615 ))

                    
                    screen.blit(pass_digit_1_text, pass_digit_1_rect)
                    screen.blit(pass_digit_2_text, pass_digit_2_rect)
                    screen.blit(pass_digit_3_text, pass_digit_3_rect)

        # if player is colliding with breakage, and the passcode is correct, it will remove the breakage from the group and add it to the eligible list.
        # it will also reset the input digits to None.
        collided_breakage_2 = pygame.sprite.spritecollide(player.sprite, breakage, False)

        for b in collided_breakage_2:
            if isinstance(b, Breakage):
                
                if pass_digit_1 == input_digit_1 and pass_digit_2 == input_digit_2 and pass_digit_3 == input_digit_3:
                    
                    if b.type == 'sail':
                        
                        if 'sail' in breakage_type_ineligible_list:
                            breakage_type_ineligible_list.remove('sail')
                            breakage_type_eligible_list.append('sail')
                            breakage.remove(b)

                    elif b.type == 'bow':
                        if 'bow' in breakage_type_ineligible_list:
                            breakage_type_ineligible_list.remove('bow')
                            breakage_type_eligible_list.append('bow')
                            breakage.remove(b)
                        
                        breakage.remove(b)

                    elif b.type == 'floor_board':
                        if 'floor_board' in breakage_type_ineligible_list:
                            breakage_type_ineligible_list.remove('floor_board')
                            breakage_type_eligible_list.append('floor_board')
                            breakage.remove(b)

                    elif b.type == 'rope':
                        if 'rope' in breakage_type_ineligible_list:
                            breakage_type_ineligible_list.remove('rope')
                            breakage_type_eligible_list.append('rope')
                            breakage.remove(b)
                                    

                    input_digit_1 = None
                    input_digit_2 = None
                    input_digit_3 = None


        # end of game resets
        if ship_damage >= 250:
            for b in breakage:
                b.kill()
            ship_damage = 0 
            wind_strength = 0 
            restart_screen_score = score
            score = 0
            breakage_type_eligible_list = ['sail', 'bow', 'floor_board', 'rope']
            breakage_type_ineligible_list = []
            game_state = 4
            win = False
            lose = True

        if score >= 900:
            for b in breakage:
                b.kill()
            ship_damage = 0 
            wind_strength = 0 
            restart_screen_score = score
            score = 0
            game_timer_score = game_timer
            game_timer = 0 
            breakage_type_eligible_list = ['sail', 'bow', 'floor_board', 'rope']
            breakage_type_ineligible_list = []

            game_state = 4

            win = True
            lose = False


        time_score_surf_2 = pacific_font.render(f'Time: {game_timer} Seconds',True,(0,255,0))
        time_score_surf_2 = pygame.transform.scale(time_score_surf_2,(400,60))
        time_score_rect_2 = time_score_surf_2.get_rect(center =(600, 85))
        screen.blit(time_score_surf_2,time_score_rect_2 )
        

            

                        
        # drawing the breakage
        breakage.draw(screen)
                
        # drawing and updates the player
        player.update()
        player.draw(screen)
       
        
            
        
        # home screen
    if game_state == 2:
        
        screen.blit(background_surf,(0,0))

        pygame.draw.rect(screen,"#c3dbdb",(title_rec.x-10 ,title_rec.y+10,title_rec.width + 30,title_rec.height))
        pygame.draw.rect(screen,"#6E6F71FF",(title_rec.x-10 ,title_rec.y+10,title_rec.width + 30,title_rec.height),10)


        
        
        screen.blit(title_surf,title_rec)
        screen.blit(hanging_sign,hanging_sign_rec)

        
        main_button.draw(screen)
        main_button.update()
        game_state_2_timer +=1 
        
       
    else:   
        game_state_2_timer = 0
        
      
    # help screen what is on screen
    if game_state == 3:
        
        screen.blit(background_surf,(0,0))
        pygame.draw.rect(screen,"#673506FF",(50,25,1100,625))
        pygame.draw.rect(screen,"#2C2C2CCC",(50,25,1100,625),10,2)
        button_how.draw(screen)
        screen.blit(how_to_play_surf,how_to_play_rect)
        

    
    if game_state == 4:
        game_state_4_timer += 1
        
        if lose:
            # get the scroe and make the text
            player_score_surf = pacific_font.render(f'Distance Traveled: { int(restart_screen_score*5)}m',True,(255,0,0))
            player_score_surf = pygame.transform.scale(player_score_surf,(400,60))
            player_score_rect = player_score_surf.get_rect(center = (600, 210))

            screen.blit(background_surf,(0,0))
            screen.blit(broken_boat_surf,broken_boat_rect)
            screen.blit(dead_player_surf, dead_player_rect)
            # Draw a dark grey transparent overlay over the whole screen
            overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
            # Only cover the text area with the overlay
            overlay.fill((0, 0, 0, 0))  # Fully transparent
            overlay_rect = pygame.Rect(50, 50, 1100, 200)
            # Add padding to the overlay rectangle
            padding = -20
            padded_rect = overlay_rect.inflate(-padding * 2, -padding * 2)
            pygame.draw.rect(overlay, (30, 30, 40, 180), padded_rect)
            screen.blit(overlay, (0, 0))
            # screen.blit(you_win_surf, you_win_rect)
            # Draw a navy blue outline around the padded overlay area
            pygame.draw.rect(screen, (35, 41, 67), padded_rect,10)

            screen.blit(player_score_surf, player_score_rect)
            screen.blit(not_traveled_safly_surf,not_traveled_safly_rect)
        
        
        if win:
            time_score_surf = pacific_font.render(f'Time: {game_timer_score} Seconds',True,(0,255,0))
            time_score_surf = pygame.transform.scale(time_score_surf,(400,60))
            time_score_rect = time_score_surf.get_rect(center =(600, 210))

            
            screen.blit(background_surf, (0,0))
            screen.blit(win_island_surf, win_island_rect)
            screen.blit(dead_player_surf, alive_player_rect)
            screen.blit(boat_surf, win_boat_rect)
            
            
            # Draw a dark grey transparent overlay over the whole screen
            overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
            
            # Only cover the text area with the overlay
            overlay.fill((0, 0, 0, 0))  # Fully transparent
            overlay_rect = pygame.Rect(50, 50, 1100, 200)
            # Add padding to the overlay rectangle
            padding = -20
            padded_rect = overlay_rect.inflate(-padding * 2, -padding * 2)
            pygame.draw.rect(overlay, (30, 30, 40, 180), padded_rect)
            screen.blit(overlay, (0, 0))
            # screen.blit(you_win_surf, you_win_rect)
            # Draw a navy blue outline around the padded overlay area
            pygame.draw.rect(screen, (35, 41, 67), padded_rect,10)
            
            screen.blit(traveled_safly_surf,traveled_safly_rect)
            screen.blit(time_score_surf,time_score_rect)

        
        game_over_button.draw(screen)
        game_over_button.update()


        
    else:
        game_state_4_timer = 0

    if game_state == 5:
        game_state_5_timer += 1
        screen.blit(background_surf, (0,0))
        pygame.draw.rect(screen,"#673506FF",(350,210,490,350))
        pygame.draw.rect(screen,"#2C2C2CCC",(350,210,490,350),10,2)
        difficulty_buttons.draw(screen)
        difficulty_buttons.update()
        button_how.draw(screen)
        
        
    else:
        game_state_5_timer = 0 

   
    pygame.display.update()
    # While loop can only run at FPS speed per second. 
    clock.tick(FPS)