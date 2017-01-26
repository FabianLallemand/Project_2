import pygame
import globals
import text
pygame.init()
import ships
import playboard



def game_loop():
    globals.gameDisplay.fill(globals.black)
    pause_text = pygame.font.SysFont('freesansbold.ttf', 50).render('Paused', True, globals.white)
    RUNNING, PAUSE = 0, 1
    state = RUNNING

    gameExit = False

    shipposx = 10
    shipposy = 10
    shiplength = 3

    while not gameExit:
        board  = playboard.Grid(globals.gameDisplay,globals.white , 1)
        




        for event in pygame.event.get():
        #    if event.type == pygame.QUIT:
        #        pygame.quit()
        #        quit()
        #    click = pygame.mouse.get_pressed()
        #    if click[0] == 1:
        #        print("schip plaatsen")
        #        mouse = pygame.mouse.get_pos()
        #        mousex = int(mouse[0]/20)
        #        print(mousex)
        #        ship1  = ships.Ship(globals.green, shiplength, mousex,21-shiplength, 2, 1, board, 1,3)
        #        ship1.draw()
            

            #Pause key
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    state = PAUSE
                if event.key == pygame.K_u:
                    state = RUNNING
                if event.key == pygame.K_LEFT:
                    if shipposx == 1: 
                        shipposx += 0
                    else:
                        shipposx += -1
                if event.key == pygame.K_RIGHT:
                    if shipposx == 20:
                        shipposx += 0
                    else:
                        shipposx += 1
                if event.key == pygame.K_UP:
                    if shipposy == 1:
                        shipposy += 0
                    else:
                       shipposy += -1
                if event.key == pygame.K_DOWN:
                    if shipposy == (21 -shiplength):
                        shipposy += 0
                    else:
                        shipposy += 1
            
    
            ship1  = ships.Ship(globals.green, shiplength, shipposx,shipposy, 2, 1, board, 1,3)

            while state == PAUSE:
                globals.gameDisplay.blit(pause_text,(300,300))
                pygame.display.flip()
                globals.clock.tick(60)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_u: state = RUNNING
                 
      
        

        board.draw()
        ship.draw()
        pygame.display.update()
        globals.clock.tick(60)