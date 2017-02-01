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


gameIcon = pygame.image.load('assets/Logo.png')

#backgrounds
Background = pygame.image.load('assets/background.jpg')
BackgroundBlur = pygame.image.load('assets/background_blur.jpg')

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


#shipimages
boot1off = pygame.image.load('assets/Ships/Ship1off.png')
boot1def = pygame.image.load('assets/Ships/Ship1def.png')
boot1offact = pygame.image.load('assets/Ships/Ship1offact.png')
boot1defact = pygame.image.load('assets/Ships/Ship1defact.png')
boot1offdead = pygame.image.load('assets/Ships/Ship1offdead.png')
boot1defdead = pygame.image.load('assets/Ships/Ship1defdead.png')

boot3off = pygame.image.load('assets/Ships/Ship3off.png')
boot3def = pygame.image.load('assets/Ships/Ship3def.png')
boot3offact = pygame.image.load('assets/Ships/Ship3offact.png')
boot3defact = pygame.image.load('assets/Ships/Ship3defact.png')
boot3offdead = pygame.image.load('assets/Ships/Ship3offdead.png')
boot3defdead = pygame.image.load('assets/Ships/Ship3defdead.png')

boot4off = pygame.image.load('assets/Ships/Ship4off.png')
boot4def = pygame.image.load('assets/Ships/Ship4def.png')
boot4offact = pygame.image.load('assets/Ships/Ship4offact.png')
boot4defact = pygame.image.load('assets/Ships/Ship4defact.png')
boot4offdead = pygame.image.load('assets/Ships/Ship4offdead.png')
boot4defdead = pygame.image.load('assets/Ships/Ship4defdead.png')

boot5off = pygame.image.load('assets/Ships/Ship5off.png')
boot5def = pygame.image.load('assets/Ships/Ship5def.png')
boot5offact = pygame.image.load('assets/Ships/Ship5offact.png')
boot5defact = pygame.image.load('assets/Ships/Ship5defact.png')
boot5offdead = pygame.image.load('assets/Ships/Ship5offdead.png')
boot5defdead = pygame.image.load('assets/Ships/Ship5defdead.png')

boot7off = pygame.image.load('assets/Ships/Ship7off.png')
boot7def = pygame.image.load('assets/Ships/Ship7def.png')
boot7offact = pygame.image.load('assets/Ships/Ship7offact.png')
boot7defact = pygame.image.load('assets/Ships/Ship7defact.png')
boot7offdead = pygame.image.load('assets/Ships/Ship7offdead.png')
boot7defdead = pygame.image.load('assets/Ships/Ship7defdead.png')

boot8off = pygame.image.load('assets/Ships/Ship8off.png')
boot8def = pygame.image.load('assets/Ships/Ship8def.png')
boot8offact = pygame.image.load('assets/Ships/Ship8offact.png')
boot8defact = pygame.image.load('assets/Ships/Ship8defact.png')
boot8offdead = pygame.image.load('assets/Ships/Ship8offdead.png')
boot8defdead = pygame.image.load('assets/Ships/Ship8defdead.png')

overlay = pygame.image.load('assets/overlay.png')
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
Canonfx = pygame.mixer.Sound("assets/Canon.ogg")
MenuSoundfx = pygame.mixer.Sound("assets/MenuSound.ogg")
Blopfx = pygame.mixer.Sound("assets/Blop.ogg")
Deadshipfx = pygame.mixer.Sound("assets/deadship.ogg")
music_playing = False