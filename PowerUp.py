import pygame
import math
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 1600, 900

class PowerUp(pygame.sprite.Sprite):
    def __init__(self,screen_width,screen_height,type):
        super().__init__()
        self.image = pygame.Surface((15, 15))  # Replace with your bullet image or use a rectangle
        self.image.fill((255, 0, 0))  # Red color
        self.rect = self.image.get_rect()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.type = type
        self.mask = pygame.mask.from_surface(self.image)

        self.spawn_position()
    
    def spawn_position(self):
        self.rect.x = random.randint(100, self.screen_width-100)
        self.rect.y = random.randint(100, self.screen_height-100)


    
    

