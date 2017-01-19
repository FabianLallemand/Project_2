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
crashed = False
carImg = pygame.image.load('container_schip.png')





def car(x,y):
    gameDisplay.blit(carImg, (x,y))

x =  (display_width * 0.45)
y = (display_height * 0.8)
x_change = 0
y_change = 0
car_speed = 0

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

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
