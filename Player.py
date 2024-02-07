import pygame
import math

class Player(pygame.sprite.Sprite):
    def __init__(self,player_image, screen_width, screen_height):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.rect.center = (600, 500)  # Initial position of the player
        self.velocity = pygame.Vector2(0, 0)

    def update(self):
        # Update the player's position based on velocity
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y
        
        # Keep the player within the screen bounds
        self.rect.x = max(0, min(self.rect.x, self.screen_width - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, self.screen_height - self.rect.height))

        # self.rotate()
    
    # def rotate(self):
    #     # Get angle between player position and mouse position
    #     mouse_x, mouse_y = pygame.mouse.get_pos()
    #     rel_x, rel_y = mouse_x - self.rect.centerx, mouse_y - self.rect.centery
    #     self.angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
    #     self.image = pygame.transform.rotate(pygame.Surface((50, 50), pygame.SRCALPHA), int(self.angle))
    #     self.rect = self.image.get_rect(center=self.rect.center)