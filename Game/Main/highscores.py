import pygame, globals, text, menu, mysql, pymysql, time
pygame.init()

def show():
    show = True
    while show:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        mouse = pygame.mouse.get_pos()
        globals.gameDisplay.fill(globals.black)
    
        mysql_con = mysql.mysql()
        result = mysql_con.select("SELECT * FROM score ORDER BY points DESC LIMIT 10")
        font = pygame.font.SysFont("arial", 25)
        x = 125
        for player in result:
            score = str((player['points']))
            score_result= font.render(score, 1 ,(globals.white))
            score_position = score_result.get_rect()
            name = str((player['name']))
            name_result = font.render(name, 1, (globals.white))
            name_position = name_result.get_rect()
            globals.gameDisplay.blit(name_result, ((globals.display_width/2 - 100), x))
            globals.gameDisplay.blit(score_result, ((globals.display_width/2 + 65), x))
            x = x + 25
        TextSurf, TextRect = text.text_objects("Highscores", globals.largeText, globals.bright_grey)
        TextRect.center = ((400),(55)) 
        globals.gameDisplay.blit(TextSurf, TextRect)
        text.button("Back!",690,10,100,50,globals.grey,globals.bright_red,menu.game_intro)
        pygame.display.update()


def playerwon(winner):
        globals.gameDisplay.blit(globals.BackgroundBlur, (0,0))
        TextSurf, TextRect = text.text_objects(( str(winner)+ " wins"), globals.largeText)
        TextRect.center = ((400),(120))
        globals.gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        time.sleep(10)
