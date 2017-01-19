"""
PyGame Battleship
Fabian Lallemand, Tim van Leeuwen, Bob Verkaik & Damian van Vuuren
"""
import pygame

pygame.init()

display_width = 1000
display_height = 800

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Battleship')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
quit = False
carImg = pygame.image.load('container_schip.png')





def car(x,y):
    gameDisplay.blit(carImg, (x,y))

x =  (display_width * 0.45)
y = (display_height * 0.8)
x_change = 0
y_change = 0
car_speed = 0

while not quit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True

        ############################
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_change = -5
            elif event.key == pygame.K_DOWN:
                y_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change = 0

        ######################
    ##
    x += x_change
    x_change = 0
    y += y_change
    y_change = 0
   ##         
    gameDisplay.fill(black)
    car(x,y)
        
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()

#import pygame
#import time
#import random
 
#pygame.init()
 
#display_width = 800
#display_height = 600

##game colors 
#black = (0,0,0)
#white = (255,255,255)
#grey = (105,105,105)

#red = (200,0,0)
#green = (0,200,0)

##bright game colors
#bright_red = (255,0,0)
#bright_green = (0,255,0)
#bright_black = (1,1,1)
#bright_grey = (211,211,211)

#block_color = (53,115,255)
 
#car_width = 73
 
#gameDisplay = pygame.display.set_mode((display_width,display_height))
#pygame.display.set_caption('A bit Racey')
#clock = pygame.time.Clock()
 
#carImg = pygame.image.load('racecar.png')
 
 
#def things_dodged(count):
#    font = pygame.font.SysFont(None, 25)
#    text = font.render("Dodged: "+str(count), True, black)
#    gameDisplay.blit(text,(0,0))
 
#def things(thingx, thingy, thingw, thingh, color):
#    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
 
#def car(x,y):
#    gameDisplay.blit(carImg,(x,y))
 
#def text_objects(text, font):
#    textSurface = font.render(text, True, black)
#    return textSurface, textSurface.get_rect()
 
#def message_display(text):
#    largeText = pygame.font.Font('freesansbold.ttf',115)
#    TextSurf, TextRect = text_objects(text, largeText)
#    TextRect.center = ((display_width/2),(display_height/2))
#    gameDisplay.blit(TextSurf, TextRect)
 
#    pygame.display.update()
 
#    time.sleep(2)
 
#    game_loop()
    
    
 
#def crash():
#    message_display('You Crashed')

#    #msg = text x= location y = location w = width h = height ic = green ac = bright green
#def button(msg,x,y,w,h,ic,ac):
#    mouse = pygame.mouse.get_pos()

#    #button interaction
#    if x+w > mouse[0] > x and y+h > mouse[1] > y:
#        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
#    else:
#        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
        
    
        
#    #button text
#    smallText = pygame.font.Font("freesansbold.ttf",16)
#    textSurf, textRect = text_objects(msg, smallText)
#    textRect.center = ( (x+w/2)), (y+(h/2) )
#    gameDisplay.blit(textSurf, textRect)

##game intro and button's
#def game_intro():

#    intro = True

#    while intro:
#        for event in pygame.event.get():
#            print(event)
#            if event.type == pygame.QUIT:
#                pygame.quit()
#                quit()
                
#        gameDisplay.fill(white)
#        largeText = pygame.font.Font('freesansbold.ttf',115)
#        TextSurf, TextRect = text_objects("Battleport", largeText)
#        TextRect.center = ((display_width/2),(display_height/2))
#        gameDisplay.blit(TextSurf, TextRect)
        
#        button("Start Game!",150,450,100,50,green,bright_green)
#        button("Quit Game!",550,450,100,50,red,bright_red)
#        button("Settings",350,450,100,50,grey,bright_grey)

#        mouse = pygame.mouse.get_pos()

        

       
       
       
       
       
#        pygame.display.update()
#        clock.tick(15)
        
        
    
    

    
#def game_loop():
#    x = (display_width * 0.45)
#    y = (display_height * 0.8)
 
#    x_change = 0
 
#    thing_startx = random.randrange(0, display_width)
#    thing_starty = -600
#    thing_speed = 4
#    thing_width = 100
#    thing_height = 100
 
#    thingCount = 1
 
#    dodged = 0
 
#    gameExit = False
 
#    while not gameExit:
 
#        for event in pygame.event.get():
#            if event.type == pygame.QUIT:
#                pygame.quit()
#                quit()
 
#            if event.type == pygame.KEYDOWN:
#                if event.key == pygame.K_LEFT:
#                    x_change = -5
#                if event.key == pygame.K_RIGHT:
#                    x_change = 5
 
#            if event.type == pygame.KEYUP:
#                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
#                    x_change = 0
 
#        x += x_change
#        gameDisplay.fill(white)
 
#        things(thing_startx, thing_starty, thing_width, thing_height, block_color)
 
 
        
#        thing_starty += thing_speed
#        car(x,y)
#        things_dodged(dodged)
 
#        if x > display_width - car_width or x < 0:
#            crash()
 
#        if thing_starty > display_height:
#            thing_starty = 0 - thing_height
#            thing_startx = random.randrange(0,display_width)
#            dodged += 1
#            thing_speed += 1
#            thing_width += (dodged * 1.2)
 
#        if y < thing_starty+thing_height:
#            print('y crossover')
 
#            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
#                print('x crossover')
#                crash()
        
#        pygame.display.update()
#        clock.tick(60)

#game_intro()
#game_loop()
#pygame.quit()
#quit()