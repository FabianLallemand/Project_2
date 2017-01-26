import pygame
import globals
import text
pygame.init()
import ships
import time
import playboard



def game_loop():

    pause_text = pygame.font.SysFont('freesansbold.ttf', 50).render('Paused', True, globals.white)
    RUNNING, PAUSE = 0, 1
    state = RUNNING

    gameExit = False
    globals.gameDisplay.fill(globals.black)
    shiplength = 3
    while not gameExit:
        
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
                ship1  = ships.Ship(globals.green, shiplength, mousex,21-shiplength, 2, 1, board, 1,3)
                ship1.draw()
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