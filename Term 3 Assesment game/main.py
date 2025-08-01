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
        border_width = 4
        border_color = (255, 0, 0)

        
        breakage_image = pygame.image.load("images/breakage.png").convert_alpha()
        alpha_value = 50  # 50% transparency
        breakage_image.set_alpha(alpha_value)
        self.image = breakage_image
        
        # If type is sail, bow, floor_board or rope it sets the y and x position of the breakage
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



# breakage group
breakage = pygame.sprite.Group()


#text



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



# set breakages spawning lists
breakage_type_eligible_list = ['sail', 'bow', 'floor_board', 'rope']
breakage_type_ineligible_list = []

# images
background_surf = pygame.image.load("images/stormy_background(Medium).png").convert_alpha()

game_state = 2 

compass_direction = pygame.image.load("images/compass_direction.png").convert_alpha()
compass_direction = pygame.transform.scale2x(compass_direction)
compass_direction_rect = compass_direction.get_rect(center = (tilt, 100))

compass_bar = pygame.image.load("images/Compass_bar.png").convert_alpha()
compass_bar = pygame.transform.scale2x(compass_bar)
compass_bar_rect = compass_bar.get_rect(center = (1100,100))




# clocks
breakage_timer = pygame.USEREVENT + 1
pygame.time.set_timer(breakage_timer,2500)
 
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
            
            






        # if the game is in the main gameplay state
        if game_state == 1:

            # Breakages spawning. Gets a random item from a list. adds it to the breakages sprite class, removes from current list and than put on another list. 
            if event.type == breakage_timer:
                if breakage_type_eligible_list:
                    removed_breakage = breakage_type_eligible_list[random.randint(0, len(breakage_type_eligible_list) - 1)]
                    breakage.add(Breakage(removed_breakage))
                    breakage_type_eligible_list.remove(removed_breakage)
                    breakage_type_ineligible_list.append(removed_breakage) # might not be needed for use laster

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
                    pass_digit_1_rect = pass_digit_1_text.get_rect(center = (500,600 ))
                    
                    pass_digit_2_text = pacific_font.render(f"{pass_digit_2}", True, font_colour_2)
                    pass_digit_2_rect = pass_digit_2_text.get_rect(center = (600,600 ))

                    pass_digit_3_text = pacific_font.render(f"{pass_digit_3}", True, font_colour_3)
                    pass_digit_3_rect = pass_digit_3_text.get_rect(center = (700,600 ))

                    # display the input digits
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

            
                        
        # drawing the breakage
        breakage.draw(screen)
                
        # drawing and updates the player

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

        screen.blit(background_surf,(0,0))
        pygame.draw.rect(screen,"#673506FF",(50,25,1100,625))
        pygame.draw.rect(screen,"#2C2C2CCC",(50,25,1100,625),10,2)

   
    pygame.display.update()
    
    # While loop can only run at FPS speed per second. 
    clock.tick(FPS)