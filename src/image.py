import pygame
BACKGROUND = pygame.image.load("img/back.png")

CLOCK = pygame.image.load("img/clock.png")

MINUTE = pygame.image.load("img/minute.png")
HOUR = pygame.image.load("img/hour.png")


def resize(image, width, height):
    return pygame.transform.scale(image, (width, height))