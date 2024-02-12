import pygame
import random
import math

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, image_path, screen_width, screen_height,split,player_position):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.split = split
        if(split):
            if(image_path == "images/piece1.png"):
                self.image = pygame.transform.scale(self.image, (30, 40))  # Adjust the size as needed
            else:
                self.image = pygame.transform.scale(self.image, (35, 35))  # Adjust the size as needed
        else:
            self.image = pygame.transform.scale(self.image, (65, 65))  # Adjust the size as needed


        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.player_position = player_position
  
        self.spawn_position()


    def spawn_position(self):
        # Choose a random edge of the screen
        edge = random.choice(["top", "bottom", "left", "right"])
        # Set initial position for the asteroid just outside the chosen edge
        if edge == "top":
            self.rect.x = random.randint(0, self.screen_width - self.rect.width)
            self.rect.y = -self.rect.height
        elif edge == "bottom":
            self.rect.x = random.randint(0, self.screen_width - self.rect.width)
            self.rect.y = self.screen_height
        elif edge == "left":
            self.rect.x = -self.rect.width
            self.rect.y = random.randint(0, self.screen_height - self.rect.height)
        elif edge == "right":
            self.rect.x = self.screen_width
            self.rect.y = random.randint(0, self.screen_height - self.rect.height)

        # Calculate direction towards the player
        direction = pygame.math.Vector2(self.player_position) - pygame.math.Vector2(self.rect.center)
        if direction.length() > 0:  # Avoid division by zero
            direction = direction.normalize()

        # Set velocity based on direction
        speed = random.randint(3, 7) if not self.split else random.randint(1, 3)
        self.velocity = direction * speed
        
    def update(self):
        # Update the position of the asteroid based on velocity
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y
