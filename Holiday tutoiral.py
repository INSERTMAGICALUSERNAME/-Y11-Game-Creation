import pygame
from sys import exit

pygame.init() #starting pygame
screen = pygame.display.set_mode((800,400)) # setting the display window
pygame.display.set_caption('Tutorial game') # the caption of the window
clock = pygame.time.Clock() # creating a frame rate timer
test_font = pygame.font.Font('KWS Onedrive/OneDrive - KingsWay School/Y11/11DGT/Game Proposal/Game/Holiday pygame game/Font/Pixeltype.ttf',50)

#getting images
sky_surface = pygame.image.load('KWS Onedrive/OneDrive - KingsWay School/Y11/11DGT/Game Proposal/Game/Holiday pygame game/graphics/Sky.png').convert() #convolutedly getting the image from the file
ground_surface = pygame.image.load('KWS Onedrive/OneDrive - KingsWay School/Y11/11DGT/Game Proposal/Game/Holiday pygame game/graphics/ground.png').convert()
text_surface = test_font.render('score',False,'Orange')
text_box = text_surface.get_rect(midleft = (25, 25))


snail_surface = pygame.image.load('KWS Onedrive/OneDrive - KingsWay School/Y11/11DGT/Game Proposal/Game/Holiday pygame game/graphics/Snail/snail1.png').convert_alpha()
snail_hitbox = snail_surface.get_rect(bottomleft = (600,300))

player_surf = pygame.image.load('KWS Onedrive/OneDrive - KingsWay School/Y11/11DGT/Game Proposal/Game/Holiday pygame game/graphics/Player/player_walk_1.png').convert_alpha()
player_hitbox = player_surf.get_rect(midbottom = (80,300) )

#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # Looking for an event, which pygame can receive. If this event is the pygame 'QUIT' it quits
            exit()
        
    # static backdrops
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    
    pygame.draw.rect(screen,'pink', text_box)
    pygame.draw.rect(screen,'pink', text_box, 10)
    screen.blit(text_surface,text_box)
    '''
    pygame.draw.line(screen,'gold',(0,0),pygame.mouse.get_pos(),10)
    pygame.draw.line(screen,'gold',(800,400),pygame.mouse.get_pos(),10)
    pygame.draw.line(screen,'purple',(0,400),pygame.mouse.get_pos(),10)
    pygame.draw.line(screen,'purple',(800,0),pygame.mouse.get_pos(),10)
    pygame.draw.line(screen,'green',(400,400),pygame.mouse.get_pos(),10)
    pygame.draw.line(screen,'green',(400,0),pygame.mouse.get_pos(),10)
    pygame.draw.line(screen,'blue',(0,200),pygame.mouse.get_pos(),10)
    pygame.draw.line(screen,'blue',(800,200),pygame.mouse.get_pos(),10)
    '''
    #snail movement
    snail_hitbox.right -= 4
    if snail_hitbox.right <= 0:
        snail_hitbox.left = 800
    screen.blit(snail_surface,snail_hitbox)

    #player
    player_hitbox.left += 4
    if player_hitbox.left >= 800:
        player_hitbox.right = 0
    screen.blit(player_surf,player_hitbox)

    #if player_hitbox.colliderect(snail_hitbox):
     #   print('ouch!')
    mouse_pos = pygame.mouse.get_pos()
    if player_hitbox.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
        print('-1 health')
     


    #updating display
    pygame.display.update()
    clock.tick(60)

