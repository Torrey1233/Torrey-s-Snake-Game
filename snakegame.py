# Welcome to my test of making the snake game using pygame
# Eat the apples to get longer by using arrow keys
# By Torrey Liu

# Importing Libraries 
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants and Variables
WIDTH = 600
HEIGHT = 600
sqrSize = 20
speed = 10
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (90, 90, 90)

# Create the game window
windowSize = pygame.display.set_mode((WIDTH, HEIGHT))
# Setting the display name
pygame.display.set_caption("Torrey's Snake Game")

# Initialize the Snake
snake = [(100, 100), (90, 100), (80, 100)]
snake_direction = (sqrSize, 0)

# Initialize the first apple position
# Randomizing where it appears
apple = (random.randint(0, (WIDTH - sqrSize) // sqrSize) * sqrSize,
        random.randint(0, (HEIGHT - sqrSize) // sqrSize) * sqrSize)

# Set up the clock
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Change snake direction with arrow keys
        
        elif event.type == pygame.KEYDOWN:
            # Up
            if event.key == pygame.K_UP and snake_direction != (0, sqrSize):
                snake_direction = (0, -sqrSize)
            # Down
            elif event.key == pygame.K_DOWN and snake_direction != (0, -sqrSize):
                snake_direction = (0, sqrSize)
            # Left
            elif event.key == pygame.K_LEFT and snake_direction != (sqrSize, 0):
                snake_direction = (-sqrSize, 0)
            # Right
            elif event.key == pygame.K_RIGHT and snake_direction != (-sqrSize, 0):
                snake_direction = (sqrSize, 0)

    # Move the Snake
    newHead = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
    snake.insert(0, newHead)

    # Check for collisions with the walls or itself
    if (newHead[0] < 0 or newHead[0] >= WIDTH or
            newHead[1] < 0 or newHead[1] >= HEIGHT or
            newHead in snake[1:]):
        pygame.quit()
        sys.exit()

    # Check if the Snake ate the apple
    if newHead == apple:
        # Creates a new random apple
        apple = (random.randint(0, (WIDTH - sqrSize) // sqrSize) * sqrSize,
                random.randint(0, (HEIGHT - sqrSize) // sqrSize) * sqrSize)
    else:
        snake.pop()

    # Draw black background
    windowSize.fill(BLACK)

    # Draw grid lines
    # Draw vertical lines
    for x in range(0, WIDTH, sqrSize):
        pygame.draw.line(windowSize, GRAY, (x, 0), (x, HEIGHT))
        # Draw horizontal lines
    for y in range(0, HEIGHT, sqrSize):
        pygame.draw.line(windowSize, GRAY, (0, y), (WIDTH, y))

    # Draw the Snake
    for segment in snake:
        pygame.draw.rect(windowSize, GREEN, (segment[0], segment[1], sqrSize, sqrSize))

    # Draw the apple
    pygame.draw.rect(windowSize, RED, (apple[0], apple[1], sqrSize, sqrSize))

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(speed)
