import pygame
import sys
import math
from Player import Player  # Import the Player class from Player.py
from bullet import Bullet
from Asteroid import Asteroid

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1600, 900
FRICTION = 0.95  # Friction coefficient (adjust as needed)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rotating Player")


# Load the player sprite image
player_image = pygame.image.load("images/ship2.png")  # Replace with your image file name
player_image = pygame.transform.scale(player_image, (100, 80))  # Adjust the size as needed

player = Player(player_image,SCREEN_WIDTH,SCREEN_HEIGHT)
speed_multiplier = 0.75


bullets = pygame.sprite.Group()  # Create a sprite group to store bullets
asteroids = pygame.sprite.Group()
space_pressed = False

# Initialize a cooldown timer for firing outside the game loop
bullet_cooldown = 0
bullet_cooldown_max = 5  # Adjust this value to control firing rate

clock = pygame.time.Clock()

spawn_interval = 4000
num_spawn = 4
last_spawn_time = pygame.time.get_ticks()


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
        num_spawn +=2
        # Reset the last spawn time
        last_spawn_time = current_time

        # Example of spawning an object: Drawing a rectangle
        for i in range(num_spawn):
            ass = Asteroid("images/Asteroid.png",SCREEN_WIDTH,SCREEN_HEIGHT)
            asteroids.add(ass)
    
    # Check for collision between the player and any asteroid
    player_hit_list = pygame.sprite.spritecollide(player, asteroids, False)
    if player_hit_list:
            print("hit")
            print(current_time/1000)
            pygame.quit()
            sys.exit()
    
    # Check for collision between bullets and asteroids
    for bullet in bullets:
        asteroid_hit_list = pygame.sprite.spritecollide(bullet, asteroids, True)
        if asteroid_hit_list:
            # Handle bullet hitting asteroid
            bullets.remove(bullet)  # Remove the bullet that hit the asteroid
            print("Asteroid destroyed!")  # Placeholder for actual collision handling
            # You might want to increase score, create an explosion effect, etc.

        

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

    
    # Check if spacebar is pressed and it wasn't pressed in the previous frame
    # if keys[pygame.MOUSEBUTTONDOWN] and not space_pressed:
    #     # Create a new bullet and add it to the sprite group
    #     bullet = Bullet(player.rect.center, player.angle)
    #     bullets.add(bullet)
    #     space_pressed = True  # Set the flag to True

    # # Update the flag if spacebar is not pressed
    # if not keys[pygame.K_SPACE]:
    #     space_pressed = False

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

    # Clear the screen
    screen.fill((0, 0, 0))
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

    # Draw a visual representation of the mouse
    pygame.draw.circle(screen, (255,255,255), pygame.mouse.get_pos(), 10)


    pygame.display.flip()
    pygame.time.delay(20)

    
    
