import pygame, sys                                 # uvoz knjiznice
from pygame.locals import *

pygame.init()                                      # inicializacija pygame 
DISPLAYSURF = pygame.display.set_mode((400, 300))  # nastavitev velikosti 
pygame.display.set_caption('Pozdravljen svet')     # naslov okna
while True:                                        # 
    for event in pygame.event.get():               # pregled dogodkov
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()                        # osvezevanje okna
