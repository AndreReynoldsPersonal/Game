import pygame
import sys
import time
import math

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1400, 750
CIRCLE_RADIUS = 20
CIRCLE_COLOR = (255,255,255)
JUMP_SPEED = -20  # Initial jump velocity
GRAVITY = 0.75  # Acceleration due to gravity

# Load the background image
background_image = pygame.image.load("space.jpg")  # Replace "background.png" with your image file name

# Resize the background image to match the screen size (optional)
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))




# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Movable Circle")


# Movement speed
move_speed = 12


# Jump state variables
is_jumping = True
jump_velocity = 0


# Initial position of the circle
circle_x, circle_y = 100,110



prev_circle_x, prev_circle_y = circle_x, circle_y







is_running = False
is_moving_left = True


# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    # Get the state of all arrow keys
    keys = pygame.key.get_pressed()
    

    # Move the circle based on arrow key input
    if keys[pygame.K_a]:
        circle_x -= move_speed
    if keys[pygame.K_d]:
        circle_x += move_speed  
    if keys[pygame.K_w]:
        circle_y -= move_speed
    if keys[pygame.K_s]:
        circle_y += move_speed  



    if(circle_y >= SCREEN_HEIGHT + 200):
        pygame.quit()
        sys.exit()


    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the background image on the screen
    screen.blit(background_image, (0, 0))

    # Draw the white screen outline (rectangle)
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), 2)






    # Draw the circle
    pygame.draw.circle(screen, CIRCLE_COLOR, (circle_x, circle_y), CIRCLE_RADIUS)


    # Update the display
    pygame.display.flip()

    # Add a small delay to control the frame rate
    pygame.time.delay(20)
