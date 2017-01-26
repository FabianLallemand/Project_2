import pygame
pygame.init()
clock = pygame.time.Clock()


def quitgame():
    pygame.quit()
    quit()



display_width = 800
display_height = 600
display_resolution = (display_width,display_height)
gameDisplay = pygame.display.set_mode((display_width,display_height))
#game colors 
black = (0,0,0)
white = (255,255,255)
grey = (105,105,105)
blue = (0,0,175)
red = (200,0,0)
green = (0,200,0)
orange = (200,50,0)
brown = (139,69,19)

#bright game colors
bright_red = (255,0,0)
bright_green = (0,255,0)
bright_black = (1,1,1)
bright_grey = (211,211,211)
bright_blue = (0,0,255)
bright_orange = (200,100,0)

#texts
largeText = pygame.font.Font('freesansbold.ttf',115)
smallText = pygame.font.SysFont("freesansbold.ttf",22)