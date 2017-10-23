import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Fonti')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

fontObj = pygame.font.Font('freesansbold.ttf', 32)  # nalaganje fontov
textSurfaceObj = fontObj.render('Pozdravljen svet!', True, GREEN, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150)

while True:
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

# Primer 5: predvajanje zvokov
import pygame, sys
from pygame.locals import *
import time

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Zvoki')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

pygame.mixer.music.load('beep-10.wav') # nalaganje zvocne datoteke
pygame.mixer.music.play(0)   # predvaja enkrat

time.sleep(5)

pygame.mixer.music.load('cautious-path-01.mp3') # nalaganje zvocne datoteke
pygame.mixer.music.play(-1)  # predvaja neskoncno

while True:
    DISPLAYSURF.fill(WHITE)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.mixer.music.stop() # ustavi predvajanje zvocne datoteke
            pygame.quit()
            sys.exit()
    pygame.display.update()