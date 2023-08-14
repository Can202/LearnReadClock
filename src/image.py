import pygame

pygame.font.init()
BACKGROUND = pygame.image.load("img/back.png")

CLOCK = pygame.image.load("img/clock.png")

MINUTE = pygame.image.load("img/minute.png")
HOUR = pygame.image.load("img/hour.png")
BTN = pygame.image.load("img/btn.png")
BTN_HOVER = pygame.image.load("img/btnhover.png")
BTN_PRESSED = pygame.image.load("img/btnpressed.png")


NORMAL_FONT = pygame.font.Font(None, 36)


def resize(image, width, height):
    return pygame.transform.scale(image, (width, height))