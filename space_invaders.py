import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Game title
pygame.display.set_caption("Space Invaders")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Player
player_width = 30
player_height = 20
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 20
player_speed = 5

# Enemy
enemy_width = 30
enemy_height = 20
enemy_color = red
enemy_speed = 2
enemies = []

# Create enemies (you'll modify this later for more complexity)
for i in range(5):
    enemies.append([random.randint(0, screen_width - enemy_width), 50 + i * 50]) 

# Bullet
bullet_width = 5
bullet_height = 10
bullet_color = green
bullet_speed = 10
bullet_x = 0
bullet_y = 0
bullet_state = "ready"  # "ready" or "fire"

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Player movement (you'll add controls later)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x -= player_speed
            if event.key == pygame.K_RIGHT:
                player_x += player_speed

        # Fire bullet (you'll add controls later)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_x = player_x + player_width // 2 - bullet_width // 2
                    bullet_y = player_y
                    bullet_state = "fire"

    # Keep player within bounds
    if player_x < 0:
        player_x = 0
    elif player_x > screen_width - player_width:
        player_x = screen_width - player_width

    # Enemy movement
    for enemy in enemies:
        enemy[0] += enemy_speed
        if enemy[0] < 0 or enemy[0] > screen_width - enemy_width:
            enemy_speed *= -1

    # Bullet movement
    if bullet_state == "fire":
        bullet_y -= bullet_speed
        if bullet_y < 0:
            bullet_y = player_y
            bullet_state = "ready"

    # Collision detection (you'll implement this later)

    # Draw everything
    screen.fill(black)  # Clear screen
    pygame.draw.rect(screen, white, [player_x, player_y, player_width, player_height]) 
    pygame.draw.rect(screen, bullet_color, [bullet_x, bullet_y, bullet_width, bullet_height])

    for enemy in enemies:
        pygame.draw.rect(screen, enemy_color, [enemy[0], enemy[1], enemy_width, enemy_height])

    pygame.display.update()  # Update the display

# Quit Pygame
pygame.quit()
quit()