import pygame, globals, text, menu, mysql, pymysql, time, settings
pygame.init()
pygame.mixer.init()

def show():
    show = True
    while show:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        mouse = pygame.mouse.get_pos()
        globals.gameDisplay.blit(globals.BackgroundBlur,(0,0))
    
        mysql_con = mysql.mysql()
        result = mysql_con.select("SELECT * FROM score ORDER BY points DESC LIMIT 10")
        font = pygame.font.SysFont("arial", 25)
        x = 125
        for player in result:
            score = str((player['points']))
            score_result= font.render(score, 1 ,(globals.bright_black))
            score_position = score_result.get_rect()
            name = str((player['name']))
            name_result = font.render(name, 1, (globals.bright_black))
            name_position = name_result.get_rect()
            globals.gameDisplay.blit(name_result, ((globals.display_width/2 - 100), x))
            globals.gameDisplay.blit(score_result, ((globals.display_width/2 + 65), x))
            x = x + 25
        TextSurf, TextRect = text.text_objects("Highscores", globals.largeText, globals.bright_grey)
        TextRect.center = ((400),(55)) 
        globals.gameDisplay.blit(TextSurf, TextRect)
        text.button("Back!",690,10,100,50,globals.grey,globals.bright_red,menu.game_intro)
        pygame.display.update()

def playerwon(winner, loser):
    intro = True        
    if globals.music_playing == True:        
        globals.MenuSoundfx.stop()
        globals.Winfx.play()
    
    while intro:
        for event in pygame.event.get():
            click = pygame.mouse.get_pressed()

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            #Background code
            BackGround = pygame.image.load('assets/background.jpg')

            globals.gameDisplay.blit(globals.BackgroundBlur, (0,0))
            TextSurf, TextRect = text.text_objects(( str(winner)+ " wins"), globals.largeText, globals.bright_black)
            TextRect.center = ((400),(120))
            globals.gameDisplay.blit(TextSurf, TextRect)
            TextSurf, TextRect = text.text_objects(( str(loser)+ " loses"), globals.mediumText, globals.bright_black)
            TextRect.center = ((400),(250))
            globals.gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
          
            text.button("Back to Menu!",325,500,150,50,globals.red,globals.bright_red,backtomenu)

            mouse = pygame.mouse.get_pos()
            pygame.display.update()
            globals.clock.tick(60)

def backtomenu():
    globals.Winfx.stop()
    if globals.music_playing == True:
        globals.MenuSoundfx.play(-1)  
        menu.game_intro()
    elif globals.music_playing == False:
        menu.game_intro()