import pygame

import infoChicken
from infoChicken import ally_hp, ene_hp
from infoChicken import currentally_hp, currentenemy_hp

import rooster-file

pygame.init()
clock = pygame.time.Clock()
fps= 60

#game Window
Side_panel = 400
screen_width =400 + Side_panel
screen_height = 400

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Battle")

#load images

#back ground image
background_img = pygame.image.load("/Users/User/Desktop/sabong game/MainMenu.png").convert_alpha()
#Panel Image
panel_img = pygame.image.load("/Users/User/Desktop/sabong game/WoodPanel.png").convert_alpha()

#Function of drawing background
def draw_bg():
    screen.blit(background_img, (0,0))
#Function of drawing panel
def draw_panel():
    screen.blit(panel_img , (400,0))


run = True

while run:
    clock.tick(fps)
    
    draw_bg()
    draw_panel()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = True

    pygame.display.update()

            

pygame.quit()
    
