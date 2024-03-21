import pygame
import math
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 1600, 900

class PowerUp(pygame.sprite.Sprite):
    def __init__(self,screen_width,screen_height,type,image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (60, 60))  # Adjust the size as needed
        self.rect = self.image.get_rect()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.type = type
        self.mask = pygame.mask.from_surface(self.image)

        self.spawn_position()
    
    def spawn_position(self):
        self.rect.x = random.randint(100, self.screen_width-100)
        self.rect.y = random.randint(100, self.screen_height-100)

        self.velocity = random.randint(-5, 5) 

    def update(self):
        # Update the position of the asteroid based on velocity
        self.rect.x += self.velocity * 0.2
        self.rect.y += self.velocity * 0.2


    
    

