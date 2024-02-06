import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1400, 750
CIRCLE_RADIUS = 20
CIRCLE_COLOR = (255, 255, 255)
JUMP_SPEED = -20  # Initial jump velocity
GRAVITY = 0.75  # Acceleration due to gravity
FRICTION = 0.95  # Friction coefficient (adjust as needed)

# Load the background image
background_image = pygame.image.load("space.jpg")
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Movable Circle")

# Movement speed
move_speed = 0.75

# Jump state variables
is_jumping = False
jump_velocity = 0

# Initial position and velocity of the circle
circle_x, circle_y = 100, 110
circle_velocity_x, circle_velocity_y = 0, 0

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Apply friction to slow down the ball
    circle_velocity_x *= FRICTION
    circle_velocity_y *= FRICTION

    if keys[pygame.K_a]:
        circle_velocity_x -= move_speed
    if keys[pygame.K_d]:
        circle_velocity_x += move_speed
    if keys[pygame.K_w]:
        circle_velocity_y -= move_speed
    if keys[pygame.K_s]:
        circle_velocity_y += move_speed

    # Update the ball's position based on velocity
    circle_x += circle_velocity_x
    circle_y += circle_velocity_y

    # if circle_y >= SCREEN_HEIGHT + 200:
    #     pygame.quit()
    #     sys.exit()

    screen.fill((0, 0, 0))
    screen.blit(background_image, (0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), 2)
    pygame.draw.circle(screen, CIRCLE_COLOR, (int(circle_x), int(circle_y)), CIRCLE_RADIUS)
    pygame.display.flip()
    pygame.time.delay(20)
