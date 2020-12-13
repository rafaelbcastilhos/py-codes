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

    # check if the snake has collided with the edges
    if snake[0][0] < 0 or snake[0][1] < 0:
        game_over = True
        break

    # ending game
    if game_over:
        break

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[i - 1][1])

    # make the snake move
    if direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    screen.fill((0, 0, 0))
    screen.blit(fruit, fruit_position)

    # lines for better viewing
    for x in range(0, 400, 10):
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, 400))
    for y in range(0, 400, 10):
        pygame.draw.line(screen, (40, 40, 40), (0, y), (400, y))

    # show score
    score_font = font.render('score: %s' % score, True, (15, 159, 255))
    score_rect = score_font.get_rect()
    score_rect.topleft = (400 - 60, 0)
    screen.blit(score_font, score_rect)

    for position in snake:
        screen.blit(skin_snake, position)

    pygame.display.update()

# game over
while True:
    game_over_font = pygame.font.Font('freesansbold.ttf', 78)
    game_over_screen = game_over_font.render("game over", True, (255, 251, 0))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect = (0, 140)
    screen.blit(game_over_screen, game_over_rect)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            pygame.quit()
            exit()
