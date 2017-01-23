"""
PyGame Battleship
Fabian Lallemand, Tim van Leeuwen, Bob Verkaik & Damian van Vuuren
"""

import pygame
import time
import random
import playboard

pygame.init()

display_width = 800
display_height = 600
display_resolution = (display_width,display_height)

#game colors 
black = (0,0,0)
white = (255,255,255)
grey = (105,105,105)

red = (200,0,0)
green = (0,200,0)

#bright game colors
bright_red = (255,0,0)
bright_green = (0,255,0)
bright_black = (1,1,1)
bright_grey = (211,211,211)

 
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Battleship')
clock = pygame.time.Clock()
 
shipimg = pygame.image.load('assets/container_schip.png')

#Background class
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

def ship(x,y):
    gameDisplay.blit(shipimg,(x,y))
 
def text_objects(text, font):
    textSurface = font.render(text, True, grey)
    return textSurface, textSurface.get_rect()
    
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
 
    pygame.display.update()
 
    time.sleep(2)

    
def quitgame():
    pygame.quit()
    quit()
    
    #msg = text x=   location y = location w = width h = height ic = green ac = bright green
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))       
    #button text
    smallText = pygame.font.SysFont("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    
    x_change = 0
    y_change = 0
    #Pause
    pause_text = pygame.font.SysFont('freesansbold.ttf', 50).render('Paused', True, white)
    RUNNING, PAUSE = 0, 1
    state = RUNNING

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #Pause key
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p: state = PAUSE
                if event.key == pygame.K_u: state = RUNNING
       
      
            if state == RUNNING:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change = -50
                    elif event.key == pygame.K_RIGHT:
                        x_change = 50
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        y_change = -50
                    elif event.key == pygame.K_DOWN:
                        y_change = 50
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0
                    elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        y_change = 0
 
                x += x_change
                y += y_change
                x_change = 0
                y_change = 0
            elif state == PAUSE:
                gameDisplay.blit(pause_text,(300,300))
                pygame.display.flip()
                clock.tick(60)  
                 

        gameDisplay.fill(black)
        bord  = playboard.Grid(gameDisplay, white , 1)
        bord.draw()
        #location ship
        ship(x,y)   

        
        pygame.display.update()
        clock.tick(60)


#game intro and button's
def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)     

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #Background code
        BackGround = Background('assets/background.jpg', [0,0])        
        gameDisplay.fill(white)
        gameDisplay.blit(BackGround.image, BackGround.rect)

        #Title
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("Battleport", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        
        mouse = pygame.mouse.get_pos()

        button("Start Game!",150,450,100,50,green,bright_green,game_loop)
        button("Quit Game!",550,450,100,50,red,bright_red,quitgame)
        button("Settings",350,450,100,50,grey,bright_grey,"game_settings")   
       
        pygame.display.update()
        clock.tick(15)
           

game_intro()
game_loop()
pygame.quit()
quit()