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
        globals.gameDisplay.blit(globals.BackgroundBlur,(0,0))
        
        TextSurf, TextRect = text.text_objects("Credits", globals.largeText, globals.bright_grey)
        TextRect.center = ((400),(55)) 
        globals.gameDisplay.blit(TextSurf, TextRect)
        

        text.button("Back!",690,10,100,50,globals.grey,globals.bright_red,menu.game_intro)
        text.button("Music",350,100,100,50,globals.grey,globals.bright_red,lambda: music("start"))
        text.button("Music",350,175,100,50,globals.grey,globals.bright_red, lambda: music("stop"))

        mouse = pygame.mouse.get_pos()
        pygame.display.update()
        globals.clock.tick(60)

def music(state):
    if state == "start":
        globals.MenuSoundfx.play()
    elif state == "stop":
        globals.MenuSoundfx.stop()