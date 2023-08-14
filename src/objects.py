import pygame
import constant
import image

import math

class Node:
    def __init__(self, _position = pygame.Vector2(0, 0), _image = image.CLOCK) -> None:
        self.position = _position
        self.image = _image
        self.velocity = pygame.Vector2(0,0)
        self.acceleration = pygame.Vector2(0,0)
    def update(self, deltaTime):
        self.velocity += self.acceleration * deltaTime
        self.position += self.velocity * deltaTime
    def draw(self, screen, fix:float = 1.0):
        if fix == 1:
            screen.blit(self.image, self.position)
        else:
            self.timage = image.resize(self.image, int(self.image.get_width() * fix), int(self.image.get_height() * fix))
            screen.blit(self.timage, self.position * fix)    

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
    def draw(self, screen, fix:float = 1.0):
        if fix == 1:
            screen.blit(self.image, self.rotated_rect.topleft + self.offset)
        else:
            self.timage = image.resize(self.image, int(self.image.get_width() * fix), int(self.image.get_height() * fix))
            screen.blit(self.timage, (self.rotated_rect.topleft + self.offset) * fix)  
        

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
