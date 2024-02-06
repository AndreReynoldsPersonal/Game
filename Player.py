import pygame


    
SCREEN_WIDTH, SCREEN_HEIGHT = 1400, 750

class Player(pygame.sprite.Sprite):
    def __init__(self,player_image):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)  # Initial position of the player
        self.velocity = pygame.Vector2(0, 0)