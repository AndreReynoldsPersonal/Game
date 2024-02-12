import pygame
import sys
import math
import random
from Player import Player  # Import the Player class from Player.py
from bullet import Bullet
from Asteroid import Asteroid

# Initialize Pygame
pygame.init()

# List of image paths
image_paths = ['images/Asteroid.png']

splits = ['images/piece1.png','images/piece2.png','images/piece3.png']


# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1600, 900
FRICTION = 0.95  # Friction coefficient (adjust as needed)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rotating Player")


# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Load start screen assets (images, fonts, etc.)
font = pygame.font.Font("ARCADE_N.TTF", 24)  # Adjust the font and size as needed
title_text = font.render('Press any key', True, WHITE)
start_text = font.render('to start', True, WHITE)
start_screen = pygame.image.load("images/StartScreen.png").convert()
start_screen = pygame.transform.scale(start_screen, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Function to show the start screen
def show_start_screen():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                running = False  # Exit the start screen loop to start the game

        # Draw the background image
        screen.blit(start_screen, (0, 0))
        screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, (SCREEN_HEIGHT // 3)+105))
        screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, (SCREEN_HEIGHT // 2)+20))

        pygame.display.flip()
        pygame.time.delay(100)

# Show the start screen
show_start_screen()


# Load the player sprite image
player_image = pygame.image.load("images/ship2.png")  # Replace with your image file name
player_image = pygame.transform.scale(player_image, (100, 80))  # Adjust the size as needed

player = Player(player_image,SCREEN_WIDTH,SCREEN_HEIGHT)
speed_multiplier = 0.75


bullets = pygame.sprite.Group()  # Create a sprite group to store bullets
asteroids = pygame.sprite.Group()

# Initialize a cooldown timer for firing outside the game loop
bullet_cooldown = 0
bullet_cooldown_max = 5  # Adjust this value to control firing rate

clock = pygame.time.Clock()

pygame.mouse.set_visible(False)


spawn_interval = 4000
num_spawn = 2
last_spawn_time = pygame.time.get_ticks()

# Define font and font size
font = pygame.font.Font("ARCADE_N.TTF", 30)  # You can adjust the font size as needed
score = 0


# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Get current time
    current_time = pygame.time.get_ticks()


    # Check if it's time to spawn a new object
    if current_time - last_spawn_time > spawn_interval:
        # It's time to spawn a new object
        print("Spawning a new object!")
        last_spawn_time = current_time
        num_spawn += 1

        # Example of spawning an object: Drawing a rectangle
        player_position = (player.rect.x,player.rect.y)
        for i in range(num_spawn):
            ass = Asteroid(random.choice(image_paths),SCREEN_WIDTH,SCREEN_HEIGHT,False,player_position)
            asteroids.add(ass)
    
    # Inside the game loop, replace the existing player-asteroid collision check
    for asteroid in asteroids:
        offset_x = asteroid.rect.x - player.rect.x
        offset_y = asteroid.rect.y - player.rect.y

        if player.mask.overlap(asteroid.mask, (offset_x, offset_y)):
            print("hit")
            print(current_time / 1000)
            pygame.quit()
            sys.exit()
    
    # Check for collision between bullets and asteroids
    for bullet in bullets:
        asteroid_hit_list = pygame.sprite.spritecollide(bullet, asteroids, True)
        if asteroid_hit_list:
            # Handle bullet hitting asteroid
            bullets.remove(bullet)  # Remove the bullet that hit the asteroid
            print("Asteroid destroyed!")  # Placeholder for actual collision handling
            score +=1
            # You might want to increase score, create an explosion effect, etc.

            for asteroid in asteroid_hit_list:
            # Split the asteroid into smaller pieces
                if asteroid.split == False:
                    for i in range(3):  # Create three smaller asteroids
                        new_asteroid = Asteroid(splits[i], SCREEN_WIDTH, SCREEN_HEIGHT,True,player_position)
                        new_asteroid.rect.center = asteroid.rect.center  # Position the new asteroid at the same location as the destroyed one
                        asteroids.add(new_asteroid)

        

    keys = pygame.key.get_pressed()
    # Apply friction to slow down the player
    player.velocity *= FRICTION

    if keys[pygame.K_w]:
        player.velocity.y -= speed_multiplier 
    if keys[pygame.K_s]:
        player.velocity.y += speed_multiplier 
    if keys[pygame.K_a]:
        player.velocity.x -= speed_multiplier
    if keys[pygame.K_d]:
        player.velocity.x += speed_multiplier


    #Check for mouse button press without relying on the event loop
    if pygame.mouse.get_pressed()[0]:  # Left mouse button is pressed
        if bullet_cooldown <= 0:
            bullet = Bullet(player.rect.center, player.angle)
            bullets.add(bullet)
            bullet_cooldown = bullet_cooldown_max  # Reset cooldown

    # Update cooldown
    if bullet_cooldown > 0:
        bullet_cooldown -= 1
    
    bullets.update()
    asteroids.update()
    player.update()

    # Check for off-screen asteroids and remove them
    for asteroid in list(asteroids):  # Use list to make a copy since we're modifying the group
        if asteroid.rect.right < 0 or asteroid.rect.left > SCREEN_WIDTH or asteroid.rect.bottom < 0 or asteroid.rect.top > SCREEN_HEIGHT:
            asteroids.remove(asteroid)

    # Clear the screen
    screen.fill((0, 0, 0))

    # Render and display timer text
    timer_text = font.render(f"Score:{score}", True, (255, 255, 255))
    screen.blit(timer_text, (30, 30))  # Adjust the position of the timer text as needed

    # screen.blit(background_image, (0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), 2)

    # Draw all bullets
    for bullet in bullets:
        screen.blit(bullet.image, (bullet.rect.x , bullet.rect.y))

    # Draw ass
    for ass in asteroids:
        screen.blit(ass.image, (ass.rect.x , ass.rect.y))

    # Draw the rotated player sprite
    screen.blit(player.image, (player.rect.x, player.rect.y))

    # Get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Set the size of the crosshair and the size of the gap
    crosshair_size = 10
    gap_size = 5  # This controls the size of the gap in the center of the crosshair

    # Calculate start and end points for horizontal line, leaving a gap in the center
    pygame.draw.line(screen, (255, 255, 255), (mouse_x - crosshair_size, mouse_y), (mouse_x - gap_size, mouse_y), 2)
    pygame.draw.line(screen, (255, 255, 255), (mouse_x + gap_size, mouse_y), (mouse_x + crosshair_size, mouse_y), 2)

    # Calculate start and end points for vertical line, leaving a gap in the center
    pygame.draw.line(screen, (255, 255, 255), (mouse_x, mouse_y - crosshair_size), (mouse_x, mouse_y - gap_size), 2)
    pygame.draw.line(screen, (255, 255, 255), (mouse_x, mouse_y + gap_size), (mouse_x, mouse_y + crosshair_size), 2)



    
    pygame.display.flip()
    pygame.time.delay(20)
    clock.tick(45)

    
    
