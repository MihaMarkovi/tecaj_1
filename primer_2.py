import pygame, sys                                 # uvoz knjiznice
from pygame.locals import *

pygame.init()                                      # inicializacija pygame
DISPLAYSURF = pygame.display.set_mode((500, 400))  # nastavitev velikosti
pygame.display.set_caption('Risanje')              # naslov okna

# nastavitev barv
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)

# risanje
DISPLAYSURF.fill(WHITE)
pygame.draw.polygon(DISPLAYSURF, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
pygame.draw.line(DISPLAYSURF, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(DISPLAYSURF, BLUE, (120, 60), (60, 120))
pygame.draw.line(DISPLAYSURF, BLUE, (60, 120), (120, 120), 4)
pygame.draw.circle(DISPLAYSURF, BLUE, (300, 50), 20, 0)
pygame.draw.ellipse(DISPLAYSURF, GREEN, (300, 250, 40, 80), 1)
pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 100, 50))

while True:                                        #
    for event in pygame.event.get():               # pregled dogodkov
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()                        # osvezevanje okna
