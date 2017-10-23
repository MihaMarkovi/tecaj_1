import pygame, sys
from pygame.locals import *

pygame.init()
FPS = 30  # FPS = frames per second; nastavitev frekvence osvezevanja
fpsClock = pygame.time.Clock()

# nastavitev okna
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animacija')

# nastavitve: barve, nalaganje slike, zacetna pozicija, zacetna usmeritev
WHITE = (255, 255, 255)
ballImg = pygame.image.load('balloon_4.png')   # nalaganje slike;
ballx = 10
bally = 10
direction = 'right'

while True: # the main game loop
    DISPLAYSURF.fill(WHITE)

    if direction == 'right':
        ballx += 2
        if ballx == 280:
            direction = 'down'
    elif direction == 'down':
        bally += 2
        if bally == 220:
            direction = 'left'
    elif direction == 'left':
        ballx -= 2
        if ballx == 10:
            direction = 'up'
    elif direction == 'up':
        bally -= 2
        if bally == 10:
            direction = 'right'

    DISPLAYSURF.blit(ballImg, (ballx, bally))  # osvezitev slike na zaslonu

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)  # preizkusiti delovanje brez te vrstice!
