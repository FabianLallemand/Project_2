"""
PyGame Battleship
Fabian Lallemand, Tim van Leeuwen, Bob Verkaik & Damian van Vuuren
"""

import pygame
import time
import random
import playboard
import globals

pygame.init()
 
gameDisplay = pygame.display.set_mode((globals.display_width,globals.display_height))
pygame.display.set_caption('Battleport')
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
    textSurface = font.render(text, True, globals.black)
    #titleSurface = font.render(text, True, globals.white)
    return textSurface, textSurface.get_rect()
    
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/display_width))
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
    smallText = pygame.font.SysFont("freesansbold.ttf",22)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def game_loop():
    x = (globals.display_width * 0.45)
    y = (globals.display_height * 0.8)
    
    x_change = 0
    y_change = 0
    #Pause
    pause_text = pygame.font.SysFont('freesansbold.ttf', 50).render('Paused', True, globals.white)
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
                 

        gameDisplay.fill(globals.black)
        bord  = playboard.Grid(gameDisplay, globals.white , 1)
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
            click = pygame.mouse.get_pressed()
            print(event)
            print(click)     

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #Background code
        BackGround = Background('assets/background.jpg', [0,0])        
        gameDisplay.fill(globals.white)
        gameDisplay.blit(BackGround.image, BackGround.rect)

        #Title
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("Battleport", largeText)
        TextRect.center = ((300),(150))
        gameDisplay.blit(TextSurf, TextRect)
        
        mouse = pygame.mouse.get_pos()

        button("Start Game!",150,450,100,50,globals.green,globals.bright_green,game_loop)
        button("Quit Game!",350,450,100,50,globals.red,globals.bright_red,quitgame)
        button("Settings",250,450,100,50,globals.grey,globals.bright_grey,"game_settings")   
        button("Game Rules",450,450,100,50,globals.blue,globals.bright_blue,instructions)

        pygame.display.update()
        clock.tick(15)

def instructions():

    instr = True
    gameDisplay.fill(globals.white)
    
            
    gamerules = pygame.image.load('assets/gamerules.png')
    gameDisplay.blit(gamerules, (0,0))


    pygame.display.update()

    
    while instr:
        for event in pygame.event.get():
            print(event)     

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
              
        mouse = pygame.mouse.get_pos()
   
        button("Back!",650,450,100,50,globals.orange,globals.bright_red,game_intro)
       

        pygame.display.update()
        clock.tick(60)
  

game_intro()
game_loop()
pygame.quit()
quit()

