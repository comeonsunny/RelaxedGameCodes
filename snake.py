import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Define colors in RGB format
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Set the width and height of the game window
width = 800
height = 600

# Create the game window
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Set the clock speed of the game
clock = pygame.time.Clock()

# Set the size of the snake block
block_size = 10

# Define the font for displaying text
font_style = pygame.font.SysFont(None, 50)

def message(msg, color):
    """
    Display a message on the screen.
    """
    mesg = font_style.render(msg, True, color)
    game_display.blit(mesg, [width / 6, height / 3])

def game_loop():
    """
    The main game loop.
    """
    game_over = False
    game_close = False

    # Set the starting position of the snake
    x1 = width / 2
    y1 = height / 2

    # Set the initial change in position of the snake
    x1_change = 0       
    y1_change = 0

    # Generate a random position for the food block
    foodx = round(random.randrange(0, width - block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, height - block_size) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            # Display a message when the game is over and prompt to play again or quit
            message("You lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        # Check if the snake hits the boundaries of the window or itself and end the game if it does.
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change

        # Fill the background with white color.
        game_display.fill(white)

        # Draw the food block on the screen.
        pygame.draw.rect(game_display, green, [foodx, foody, block_size, block_size])

        # Draw the snake on the screen.
        pygame.draw.rect(game_display, black, [x1, y1, block_size, block_size])

        # Update the display.
        pygame.display.update()

        # Check if the snake has eaten the food and generate a new food block.
        if x1 == foodx and y1 == foody:
            print("Yummy!!")
        clock.tick(20)

    # Quit Pygame and exit Python.
    pygame.quit()
    quit()

game_loop()