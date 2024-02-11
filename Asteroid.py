import pygame
import random

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, image_path, screen_width, screen_height,split):
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
  
        self.spawn_position()


    def spawn_position(self):
        # Choose a random edge of the screen
        edge = random.choice(["top", "bottom", "left", "right"])

        # Set initial position for the asteroid just outside the chosen edge
        if edge == "top":
            self.rect.x = random.randint(0, self.screen_width - self.rect.width)
            self.rect.y = 0
        elif edge == "bottom":
            self.rect.x = random.randint(0, self.screen_width - self.rect.width)
            self.rect.y = self.screen_height
        elif edge == "left":
            self.rect.x = 0
            self.rect.y = random.randint(0, self.screen_height - self.rect.height)
        elif edge == "right":
            self.rect.x = self.screen_width
            self.rect.y = random.randint(0, self.screen_height - self.rect.height)

        #set velocity
        if(self.split):
            self.velocity = pygame.Vector2(random.randint(-2, 2), random.randint(-2, 2))
        else:
            if edge == "top":
                self.velocity = pygame.Vector2(0, random.randint(3, 8))
            elif edge == "bottom":
                self.velocity = pygame.Vector2(0, -random.randint(3, 8))
            elif edge == "left":
                self.velocity = pygame.Vector2(random.randint(3, 8), 0)
            elif edge == "right":
                self.velocity = pygame.Vector2(-random.randint(3, 8), 0)

    def update(self):
        # Update the position of the asteroid based on velocity
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y
