import pygame
import globals
import text
pygame.init()
import ships
import time
import playboard



def game_loop():
    pygame.time.wait(50)
    pause_text = pygame.font.SysFont('freesansbold.ttf', 50).render('Paused', True, globals.white)
    RUNNING, PAUSE = 0, 1
    state = RUNNING

    gameExit = False
    gameExit2 = False
    globals.gameDisplay.fill(globals.black)
    shiplength = 5
    shipsplaced = 0
    while not gameExit and shipsplaced <1:
        
        board  = playboard.Grid(globals.gameDisplay, globals.white , 1)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #Pause key
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p: state = PAUSE
                if event.key == pygame.K_u: state = RUNNING

            click = pygame.mouse.get_pressed()
            
            if click[0] == 1:
                print("schip plaatsen")
                mouse = pygame.mouse.get_pos()
                mousex = int(mouse[0]/20)
                print(mousex)
                shipy = 21 - shiplength
                ship1  = ships.Ship(globals.green, shiplength, mousex,21-shipy, 2, 1, board, 1,3)
                ship1.draw()
                shipsplaced +=1
                time.sleep(0.2)              
                

            while state == PAUSE:
                globals.gameDisplay.blit(pause_text,(300,300))
                pygame.display.flip()
                globals.clock.tick(60)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_u: state = RUNNING

        board.draw()
        pygame.display.update()
        globals.clock.tick(60)


    while shipsplaced == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #Pause key
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    state = PAUSE
                if event.key == pygame.K_u:
                    state = RUNNING
                if event.key == pygame.K_LEFT:
                    if mousex == 1: 
                        mousex += 0
                    else:
                        mousex += -1
                if event.key == pygame.K_RIGHT:
                    if mousex == 20:
                        mousex += 0
                    else:
                        mousex += 1
                if event.key == pygame.K_UP:
                    if shipy == 1:
                        shipy += 0
                    else:
                       shipy += -1
                if event.key == pygame.K_DOWN:
                    if shipy == (21 -shiplength):
                        shipy += 0
                    else:
                        shipy += 1
                           


            while state == PAUSE:
                globals.gameDisplay.blit(pause_text,(300,300))
                pygame.display.flip()
                globals.clock.tick(60)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_u: state = RUNNING
                 
                 

        globals.gameDisplay.fill(globals.black)
        board  = playboard.Grid(globals.gameDisplay,globals.white , 1)

        ship1  = ships.Ship(globals.green, shiplength, mousex,shipy, 2, 1, board, 1,3)
        
        ship1.draw()
        board.draw()
        
        pygame.display.update()
        globals.clock.tick(60)
