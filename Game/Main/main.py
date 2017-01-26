"""
PyGame Battleport
Fabian Lallemand, Tim van Leeuwen, Bob Verkaik & Damian van Vuuren
"""

import pygame, time, random, playboard, globals, menu

pygame.init()
pygame.display.set_caption('Battleport')
    
menu.game_intro()
menu.game_loop()
pygame.quit()
quit()
