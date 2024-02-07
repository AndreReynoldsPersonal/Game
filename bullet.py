import pygame
import math

SCREEN_WIDTH, SCREEN_HEIGHT = 1600, 900

class Bullet(pygame.sprite.Sprite):
    def __init__(self, start_pos, angle):
        super().__init__()
        self.image = pygame.Surface((7, 7))  # Replace with your bullet image or use a rectangle
        self.image.fill((255, 0, 0))  # Red color
        self.rect = self.image.get_rect()
        self.rect.center = start_pos
        self.angle = angle
        self.speed = 10  # Adjust the speed as needed
    
    def update(self):
        # Calculate the velocity components based on the angle
        velocity_x = self.speed * math.cos(math.radians(self.angle))
        velocity_y = -self.speed * math.sin(math.radians(self.angle))  # Negate the Y component for Pygame's coordinate system
        
        # Update the bullet's position based on velocity
        self.rect.x += velocity_x
        self.rect.y += velocity_y
        
        # Check if the bullet is out of bounds
        if not pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT).colliderect(self.rect):
            self.kill()  # Remove the bullet if it's out of bounds

