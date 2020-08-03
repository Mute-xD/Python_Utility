"""
pyGame test module
"""
import sys
import pygame


def runGame():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    while True:
        checkEvent()
        updateScreen(screen)


def checkEvent():
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            sys.exit()


def updateScreen(screen):
    screen.fill((240, 240, 240))
    pygame.display.flip()


if __name__ == '__main__':
    runGame()
