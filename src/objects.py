import pygame
import constant
import image

import math
import random

pygame.font.init()

class Node:
    def __init__(self, _position = pygame.Vector2(0, 0), _image = image.CLOCK) -> None:
        self.position = _position
        self.image = _image
        self.velocity = pygame.Vector2(0,0)
        self.acceleration = pygame.Vector2(0,0)
    def update(self, deltaTime):
        self.velocity += self.acceleration * deltaTime
        self.position += self.velocity * deltaTime
    def draw(self, screen):
        screen.blit(self.image, self.position)  

class Hand(Node):
    def __init__(self, _position=pygame.Vector2(0, 0), _image=image.CLOCK, _size = 0, _rotspeed = 45) -> None:
        super().__init__(_position, _image)
        self.real_image = self.image
        self.original_rect = self.real_image.get_rect(center=(constant.WIDTH // 2, constant.HEIGHT // 2))
        self.rotation = 0
        self.rotation_speed = _rotspeed
        self.size = _size
        self.offset = pygame.Vector2(0,0)
    def update(self, deltaTime):
        super().update(deltaTime)
        # self.rotation += self.rotation_speed * deltaTime

        self.image = pygame.transform.rotate(self.real_image, self.rotation)
        self.rotated_rect = self.image.get_rect(center=(constant.WIDTH // 2, constant.HEIGHT // 2))
        
        if self.rotation < 90:
            self.offset.y = self.position.y - self.rotated_rect.bottom
            self.offset.x = self.position.x - self.rotated_rect.right
        elif self.rotation < 180:
            self.offset.y = (self.position.y - self.rotated_rect.top) - self.size
            self.offset.x = (self.position.x - self.rotated_rect.right)
        elif self.rotation < 270:
            self.offset.y = (self.position.y - self.rotated_rect.top) - self.size
            self.offset.x = (self.position.x - self.rotated_rect.left) - self.size
        elif self.rotation < 360:
            self.offset.y = (self.position.y - self.rotated_rect.bottom)
            self.offset.x = (self.position.x - self.rotated_rect.left) - self.size
        else:
            self.rotation = 0
    def draw(self, screen):
        screen.blit(self.image, self.rotated_rect.topleft + self.offset)
class Button(Node):
    def __init__(self,
                 _position=pygame.Vector2(0, 0),
                 _image=image.BTN,
                 _text = "no text given",
                 _imagehover=image.BTN_HOVER,
                 _imagepressed=image.BTN_PRESSED) -> None:
        super().__init__(_position, _image)
        self.text = Text(_text, _position + pygame.Vector2(25,56))
        self.get_pressed = False
        self.normal_image = self.image
        self.image_hover = _imagehover
        self.image_pressed = _imagepressed
    
    def update(self, deltaTime, mousepressed = False, mouseposX = 0, mouseposY = 0, fix=1, offset=pygame.Vector2(0,0)):
        super().update(deltaTime)
        self.rect = self.image.get_rect()
        self.rect.left += self.position.x
        self.rect.top += self.position.y
        mpx,mpy = pygame.mouse.get_pos()
        mouse_position_X = (mpx - offset.x) / fix
        mouse_position_Y =  (mpy - offset.y) / fix
        if (self.rect.left < mouse_position_X < self.rect.right) and (self.rect.top < mouse_position_Y < self.rect.bottom):
            self.image = self.image_hover
            if mousepressed:
                self.image = self.image_pressed
                self.get_pressed = True
        elif (self.rect.left < mouseposX < self.rect.right) and (self.rect.top < mouseposY < self.rect.bottom):
            self.image = self.image_hover
            if mousepressed:
                self.image = self.image_pressed
                self.get_pressed = True
        else:
            self.image = self.normal_image
    
    def draw(self, screen, fix: float = 1, xoffset = 0):
        super().draw(screen)
        self.text.draw(screen)

class Text():
    def __init__(self, 
        _text = "A",
        _position = pygame.Vector2(0,0),
        _color = constant.BLACK) -> None:
        self.text = _text
        self.position = _position
        self.font = image.NORMAL_FONT
        self.color = _color

    def draw(self, screen):
        text_surface = self.font.render(self.text, True, self.color)
        screen.blit(text_surface, self.position)
            


class Background(Node):
    def __init__(self) -> None:
        super().__init__(pygame.Vector2(-40,0), 
                         image.BACKGROUND)
        self.sin = MovementBySin()

    def update(self, deltaTime):
        self.sin.update(deltaTime)
        self.position.x += self.sin.sin / 2

class Timer:
    def __init__(self, _count_to) -> None:
        self.time = 0
        self.timing = False
        self.count_to = _count_to

    def update(self, deltaTime):
        if self.timing:
            if self.time > self.count_to:
                self.timing = False
                self.time = 0
            self.time += 1 * deltaTime
        else:
            self.time = 0

class MovementBySin:
    def __init__(self) -> None:
        self.angle = 0
        self.angle_in_radians = 0
        self.sin = 0

    def update(self, deltaTime):
        if self.angle >= 720:
            self.angle = 0
        self.angle += 90 * deltaTime
        self.angle_in_radians = self.angle * (math.pi / 180)
        self.sin = math.sin(self.angle_in_radians)

class Hour:
    def __init__(self) -> None:
        self.hour = random.randint(1,12)
        self.minutes = _minutes = random.randint(0,11) * 5
    def getTuple(self):
        return (self.hour, self.minutes)
    def newSet(self, rrandom = True, _hour = 2, _minutes=30):
        if rrandom:
            self.hour = random.randint(1,12)
            self.minutes = _minutes = random.randint(0,11) * 5
        else:
            self.hour = _hour
            self.minutes = _minutes 
    def getStrHour(self, language = "es"):
        
        
        texth = str(self.hour).zfill(2)
        mid = ":"

        if self.minutes == 0:
            texth = str(self.hour)
            mid = ""
            if language == "es":
                textm = " en punto"
            else:
                textm = " o'clock"
        elif self.minutes == 15:
            if language == "es":
                texth = str(self.hour)
                mid = ""
                textm = " y un cuarto"
            else:
                texth = "a quarter past "
                mid = ""
                textm = str(self.hour)

        elif self.minutes == 30:
            if language == "es":
                texth = str(self.hour)
                mid = ""
                textm = " y media"
            else:
                texth = "half past "
                mid = ""
                textm = str(self.hour)
                
                
        elif self.minutes == 45:
            if language == "es":
                texth = "un cuarto para "
                if self.hour == 12:
                    mid = "la "
                else:
                    mid = "las "
            else:
                texth = "a quarter to "
                mid = ""
            
            if self.hour == 12:
                textm = "1"
            else:
                textm = str(self.hour + 1)
        elif self.minutes == 50:
            if language == "es":
                texth = "10 minutos para "
                if self.hour == 12:
                    mid = "la "
                else:
                    mid = "las "
                if self.hour == 12:
                    textm = "1"
                else:
                    textm = str(self.hour + 1)
            else:
                textm = str(self.minutes).zfill(2)
        elif self.minutes == 55:
            if language == "es":
                texth = "5 minutos para "
                if (self.hour) == 12:
                    mid = "la "
                else:
                    mid = "las "
                if self.hour == 12:
                    textm = "1"
                else:
                    textm = str(self.hour + 1)
            else:
                textm = str(self.minutes).zfill(2)
        else:
            textm = str(self.minutes).zfill(2)
        return texth + mid + textm