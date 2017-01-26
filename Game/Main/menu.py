import pygame
import globals
import text #
import game

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
        BackGround = pygame.image.load('assets/background.jpg')
        globals.gameDisplay.blit(BackGround, (0,0))
        
 

        #Title
        
        TextSurf, TextRect = text.text_objects("Battleport", globals.largeText)
        TextRect.center = ((300),(150))
        globals.gameDisplay.blit(TextSurf, TextRect)
        
        mouse = pygame.mouse.get_pos()

        text.button("Start Game!",150,450,100,50,globals.green,globals.bright_green,game.game_loop)
        text.button("Quit Game!",350,450,100,50,globals.red,globals.bright_red,globals.quitgame)
        text.button("Settings",250,450,100,50,globals.grey,globals.bright_grey,"game_settings")   
        text.button("Game Rules",450,450,100,50,globals.blue,globals.bright_blue,instructions)

        pygame.display.update()
        globals.clock.tick(15)

def instructions():

    instr = True
    globals.gameDisplay.fill(globals.white)
    
            
    gamerules = pygame.image.load('assets/gamerules.png')
    globals.gameDisplay.blit(gamerules, (0,0))


    pygame.display.update()

    
    while instr:
        for event in pygame.event.get():
            print(event)     

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
              
        mouse = pygame.mouse.get_pos()
   
        text.button("Back!",650,450,100,50,globals.orange,globals.bright_red,game_intro)
       

        pygame.display.update()
        globals.clock.tick(60)