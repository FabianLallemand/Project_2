import pygame
import globals
import text
pygame.init()
import ships
import playboard



def game_loop():

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

            while state == PAUSE:
                globals.gameDisplay.blit(pause_text,(300,300))
                pygame.display.flip()
                globals.clock.tick(60)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_u: state = RUNNING
                 
                 

        globals.gameDisplay.fill(globals.black)
        board  = playboard.Grid(globals.gameDisplay, globals.white , 1)
        board.draw()

        ship1  = ships.Ship(globals.green, 3, 10,10, 2, 1, board, 1,3)
        
        ship1.draw()
        board.draw()
        
        pygame.display.update()
        globals.clock.tick(60)