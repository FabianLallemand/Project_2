import pygame, webbrowser

pygame.init()
clock = pygame.time.Clock()

def openrules():
    url = "https://www.dropbox.com/sh/fqanfbkw8l5y0b6/AAA8PrSl17eJWV_1DkiRGvVoa?dl=0"
    webbrowser.open_new(url)

def quitgame():
    pygame.quit()
    quit()

shipdrawn = False

display_width = 800
display_height = 600
display_resolution = (display_width,display_height)
gameDisplay = pygame.display.set_mode((display_width,display_height))
#game colors 
black = (0,0,0)
white = (255,255,255)
grey = (105,105,105)
blue = (0,0,175)
blue2 = (0, 131, 195)
red2 =  (225,6,0)
red = (170,0,0)
green = (0,170,0)
green2 = (27,171,11)
orange = (200,50,0)
brown = (139,69,19)
purple = (124,70,145)


#bright game colors
bright_red = (255,0,0)
bright_green = (0,255,0)
bright_black = (1,1,1)
bright_grey = (211,211,211)
bright_blue = (0,0,255)
bright_orange = (200,100,0)

#texts
largeText = pygame.font.Font("assets/piraat.ttf",75)
smallText = pygame.font.SysFont("freesansbold.ttf",24)
infoText = pygame.font.SysFont("freesansbold.ttf",18)

#cardimages

#offensive
fmjupgrade = pygame.image.load('assets/FMJupgrade.png')
rifling = pygame.image.load('assets/Rifling.png')
advancedrifling = pygame.image.load('assets/advancedrifling.png')
navalmine = pygame.image.load('assets/navalmine.png')
emp = pygame.image.load('assets/emp.png')

#defensive
hull = pygame.image.load('assets/hull.png')
sonar = pygame.image.load('assets/sonar.png')
smokescreen = pygame.image.load('assets/smokescreen.png')
sabotage = pygame.image.load('assets/sabotage.png')

#help
backup = pygame.image.load('assets/backup.png')
extrafuel2 = pygame.image.load('assets/extrafuel2.png')
extrafuel = pygame.image.load('assets/extrafuel.png')
rally = pygame.image.load('assets/rally.png')
adrenalinerush = pygame.image.load('assets/adrenalinerush.png')

#sounds
Exploisionfx = pygame.mixer.Sound("assets/Explosion.ogg")
MenuSoundfx = pygame.mixer.Sound("assets/MenuSound.ogg")
Blopfx = pygame.mixer.Sound("assets/Blop.ogg")
