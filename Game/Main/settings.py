import pygame, globals, text, menu

def settings():
    intro = True

    while intro:
        for event in pygame.event.get():
            click = pygame.mouse.get_pressed()


            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #Background code
        BackGround = pygame.image.load('assets/background.jpg')
        
        TextSurf, TextRect = text.text_objects("Credits", globals.largeText, globals.bright_grey)
        TextRect.center = ((400),(55)) 
        globals.gameDisplay.blit(TextSurf, TextRect)
        
        globals.gameDisplay.blit(BackGround, (0,0))

        text.button("Back!",690,10,100,50,globals.grey,globals.bright_red,menu.game_intro)
        text.button("Music",350,50,100,50,globals.grey,globals.bright_red,None)

        mouse = pygame.mouse.get_pos()
        pygame.display.update()
        globals.clock.tick(60)
