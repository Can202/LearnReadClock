import pygame
import platformdetect
path = platformdetect.getPath()

pygame.font.init()



BACKGROUND = pygame.image.load(f"{path}img/back.png")

CLOCK = pygame.image.load(f"{path}img/clock.png")

MINUTE = pygame.image.load(f"{path}img/minute.png")
HOUR = pygame.image.load(f"{path}img/hour.png")
BTN = pygame.image.load(f"{path}img/btn.png")
BTN_HOVER = pygame.image.load(f"{path}img/btnhover.png")
BTN_PRESSED = pygame.image.load(f"{path}img/btnpressed.png")

TICKET = pygame.image.load(f"{path}img/ticket.png")
ERROR = pygame.image.load(f"{path}img/error.png")

MENU = pygame.image.load(f"{path}img/menu.png")

ES = pygame.image.load(f"{path}img/es.png")
EN = pygame.image.load(f"{path}img/en.png")

HARDMODE = pygame.image.load(f"{path}img/hard.png")
MUSICMODE = pygame.image.load(f"{path}img/music.png")

NORMAL_FONT = pygame.font.Font(None, 36)




def resize(image, width, height):
    return pygame.transform.scale(image, (width, height))