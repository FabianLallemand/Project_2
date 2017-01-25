import pygame
import globals
import text
pygame.init()
import playboard



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
                globals.gameDisplay.blit(pause_text,(300,300))
                pygame.display.flip()
                globals.clock.tick(60)  
                 

        globals.gameDisplay.fill(globals.black)
        bord  = playboard.Grid(globals.gameDisplay, globals.white , 1)
        bord.draw()


        
        pygame.display.update()
        globals.clock.tick(60)