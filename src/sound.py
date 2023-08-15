import pygame
import platformdetect
path = platformdetect.getPath()

pygame.mixer.init()

BAD = pygame.mixer.Sound(f"{path}sound/bad.mp3")
GOOD = pygame.mixer.Sound(f"{path}sound/good.mp3")
TIC1 = pygame.mixer.Sound(f"{path}sound/tic1.mp3")
TIC2 = pygame.mixer.Sound(f"{path}sound/tic2.mp3")