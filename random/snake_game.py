# simple snake game made with pygame
import pygame
import random
from pygame.locals import *


# align fruit
def grid_config():
    x = random.randint(0, 390)
    y = random.randint(0, 390)
    return x // 10 * 10, y // 10 * 10


def collision(x1, x2):
    return (x1[0] == x2[0]) and (x1[1] == x2[1])


pygame.init()
# screen config
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("snake")

clock = pygame.time.Clock()

# defining movements
UP = 0
DOWN = 1
RIGHT = 2
LEFT = 3
direction = RIGHT

# fruit config
fruit_position = grid_config()
fruit = pygame.Surface((10, 10))
fruit.fill((255, 251, 0))

# snake config
snake = [(100, 100), (110, 100), (120, 100)]
skin_snake = pygame.Surface((10, 10))
skin_snake.fill((15, 159, 255))

font = pygame.font.Font('freesansbold.ttf', 12)
game_over = False
score = 0

while not game_over:
    clock.tick(15)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    if event.type == KEYDOWN:
        if event.key == K_UP and direction != DOWN:
            direction = UP
        if event.key == K_DOWN and direction != UP:
            direction = DOWN
        if event.key == K_LEFT and direction != RIGHT:
            direction = LEFT
        if event.key == K_RIGHT and direction != LEFT:
            direction = RIGHT

    if collision(snake[0], fruit_position):
        fruit_position = grid_config()
        snake.append((0, 0))
        score += 1

    # check if the snake has collided with the edges
    if snake[0][0] == 400 or snake[0][1] == 400:
        game_over = True
        break

