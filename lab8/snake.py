import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Set up constants for screen dimensions and colors
snake_speed = 10
SCREEN_W = 600
SCREEN_H = 600
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Set up the game window and clock
pygame.display.set_caption('Game Snake')
game_window = pygame.display.set_mode((SCREEN_W, SCREEN_H))

clock = pygame.time.Clock()

# Initialize variables for snake and fruit positions, snake direction, score, and fruit spawning
snake_position = [100, 50]

snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]

# Foods with different weights
food_weights = [1, 2, 3]

# Variables to control food spawning and timer
food_spawn = False
food_timer = 5  # seconds

fruit_position = [random.randrange(1, (SCREEN_W // 10)) * 10,
                  random.randrange(1, (SCREEN_H // 10)) * 10]

direction = 'RIGHT'
change_to = direction

score = 0


# Function to display the score on the screen
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('SCORE: ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)


# Function to display game over message and quit the game
def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)

    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)

    game_over_rect = game_over_surface.get_rect()

    game_over_rect.midtop = (SCREEN_W / 2, SCREEN_H / 4)

    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    time.sleep(2)

    pygame.quit()

    quit()


while True:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Update snake direction based on user input
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Move the snake in the current direction
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    snake_body.insert(0, list(snake_position))

    # Check if snake eats the food
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += random.choice(food_weights)  # Random weight
        food_spawn = False
    else:
        snake_body.pop()

    # Respawn the food at a random location if eaten by the snake or timer expires
    if not food_spawn or food_timer == 0:
        fruit_position = [random.randrange(1, (SCREEN_W // 10)) * 10,
                          random.randrange(1, (SCREEN_H // 10)) * 10]
        food_spawn = True
        food_timer = 100  # Reset timer

    # Draw the snake and food on the screen
    game_window.fill(white)
    for pos in snake_body:
        pygame.draw.rect(game_window, blue, pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(game_window, red, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    # Check for game over conditions (collision with walls or snake body)
    if snake_position[0] < 0 or snake_position[0] > SCREEN_W - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > SCREEN_H - 10:
        game_over()

    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # Display the score on the screen
    show_score(1, black, 'times new roman', 20)

    # Update the display
    pygame.display.update()

    clock.tick(snake_speed)
    food_timer -= 1  # Decrement food timer