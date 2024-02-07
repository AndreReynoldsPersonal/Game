import pygame
import sys
import math
from Player import Player  # Import the Player class from Player.py

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 650
GRAVITY = 0.75  # Acceleration due to gravity
FRICTION = 0.95  # Friction coefficient (adjust as needed)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rotating Player")

# Load the background image
background_image = pygame.image.load("space.jpg")
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Load the player sprite image
player_image = pygame.image.load("ship2.png")  # Replace with your image file name
player_image = pygame.transform.scale(player_image, (130, 100))  # Adjust the size as needed

player = Player(player_image)
player.rect.center = (100, 100)  # Initial position of the player
player.angle = 0  # Initial angle of the player (in degrees)

# Rotation speed (adjust as needed)
rotation_speed = 5

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Apply friction to slow down the player
    player.velocity *= FRICTION

    if keys[pygame.K_w]:
        speed_multiplier = 0.75
        angle_in_radians = math.radians(player.angle)
        player.velocity.y -= speed_multiplier * math.sin(angle_in_radians)  # Negate the Y-component
        player.velocity.x += speed_multiplier * math.cos(angle_in_radians)

    # Update the player's position based on velocity
    player.rect.x += player.velocity.x
    player.rect.y += player.velocity.y

    # Rotate the player based on arrow key inputs
    if keys[pygame.K_LEFT]:
        player.angle += rotation_speed
    if keys[pygame.K_RIGHT]:
        player.angle -= rotation_speed
    
    print(math.cos(player.angle))

    # Rotate the player sprite
    rotated_player_image = pygame.transform.rotate(player.image, player.angle)
    rotated_rect = rotated_player_image.get_rect(center=player.rect.center)

    # Clear the screen
    screen.fill((0, 0, 0))
    screen.blit(background_image, (0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), 2)

    # Draw the rotated player sprite
    screen.blit(rotated_player_image, rotated_rect)

    pygame.display.flip()
    pygame.time.delay(20)

    
    
