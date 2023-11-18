import sys
import pygame
import time
import random

Snake_speed = 15

# window size
window_x = 720
window_y = 480

# def colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
yellow = pygame.Color(0, 0, 255)

# init pygame
pygame.init()

# initialise game window
pygame.display.set_caption('SnakeGamePY')
game_window = pygame.display.set_mode((window_x, window_y))

# fps controller
fps = pygame.time.Clock()

# def snake default position
snake_position = [100, 50]

# def first 4 blocks of snake body
snake_body = [
    [100, 50],
    [90, 50],
    [80, 50],
    [70, 50]
]

# fruit position
fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                  random.randrange(1, (window_y // 10)) * 10]

fruit_spaw = True

# setting default snake direction towards
# right
direction = 'RIGHT'
change_to = direction

# initial score
score = 0

# displaying Score Function

def ask(screen, question):
    pygame.font.init()
    current_string = ""
    font = pygame.font.SysFont('calibri', 40)
    text_font = pygame.font.SysFont('calibri', 30)
    input_box = pygame.Rect(window_x / 2 - 100, window_y / 2 - 25, 200, 50)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return current_string
                    elif event.key == pygame.K_BACKSPACE:
                        current_string = current_string[:-1]
                    else:
                        current_string += event.unicode

        screen.fill((30, 30, 30))
        pygame.draw.rect(screen, color, input_box, 2)

        question_surface = font.render(question, True, color)
        question_rect = question_surface.get_rect(center=(window_x / 2, window_y / 2 - 40))
        screen.blit(question_surface, question_rect)

        text_surface = text_font.render(current_string, True, color)
        text_rect = text_surface.get_rect(center=(window_x / 2, window_y / 2 + 10))
        screen.blit(text_surface, text_rect)

        pygame.display.flip()
        clock.tick(30)

def get_key():
    while True:
        event = pygame.event.poll()
        if event.type == pygame.KEYDOWN:
            return event.key
        else:
            pass
def display_box(screen, message):
    fontobject = pygame.font.Font(None, 18)
    pygame.draw.rect(screen, (0, 0, 0),
                     ((screen.get_width() / 2) - 100,
                      (screen.get_height() / 2) - 10,
                      200, 20), 0)
    pygame.draw.rect(screen, (255, 255, 255),
                     ((screen.get_width() / 2) - 102,
                      (screen.get_height() / 2) - 12,
                      204, 24), 1)
    if len(message) != 0:
        screen.blit(fontobject.render(message, 1, (255, 255, 255)),
                    ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10))
    pygame.display.flip()
def show_score(choice, color, font, size):
    global player_name
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)

    # create the display surface object
    score_surface = score_font.render(player_name + ' Score : ' + str(score), True, color)

    # create a rectangular object for the text
    # surface score
    score_rect = score_surface.get_rect()

    # display text
    game_window.blit(score_surface, score_rect)

# show menu function
def show_game_over():
    global player_name
    menu_font = pygame.font.SysFont('calibri', 30)

    menu_surface = menu_font.render(player_name + ' Score: ' + str(score), True, white)
    menu_rect = menu_surface.get_rect()
    menu_rect.midtop = (window_x / 2, window_y / 4)

    game_window.blit(menu_surface, menu_rect)

    menu_surface = menu_font.render('Press Esc to Quit', True, red)
    menu_rect = menu_surface.get_rect()
    menu_rect.midtop = (window_x / 2, window_y / 2)

    game_window.blit(menu_surface, menu_rect)

    menu_surface = menu_font.render('Press Enter to Retry', True, red)
    menu_rect = menu_surface.get_rect()
    menu_rect.midtop = (window_x / 2, window_y / 1.5)

    game_window.blit(menu_surface, menu_rect)

    pygame.display.flip()

    waiting_for_key = True
    while waiting_for_key:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_RETURN:
                    restart_game()
                    waiting_for_key = False


# restart game function
def restart_game():
    global player_name
    global snake_position, snake_body, fruit_position, fruit_spaw, direction, change_to, score

    # reset snake position and body
    snake_position = [100, 50]
    snake_body = [
        [100, 50],
        [90, 50],
        [80, 50],
        [70, 50]
    ]

    # reset fruit position and spawn
    fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                      random.randrange(1, (window_y // 10)) * 10]
    fruit_spaw = True

    # reset direction and change_to
    direction = 'RIGHT'
    change_to = direction

    # reset score
    score = 0

# Get the player's name within the game window
player_name = ask(game_window, "Enter your Player Name")

# main Function
while True:
    # handling key events
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
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_RETURN:
                restart_game()

    # if two keys pressed simultaneously
    # we don't want the snake to move into two
    # directions simultaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # If the player has not set a name, show the name input screen
    if player_name is None:
        player_name = ask(game_window, "Enter your name")

    # snake body growing mechanism
    # if fruits and snakes collide then scores
    # will be incremented by 10
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spaw = False
    else:
        snake_body.pop()

    if not fruit_spaw:
        fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                          random.randrange(1, (window_y // 10)) * 10]

    fruit_spaw = True
    game_window.fill(black)

    for pos in snake_body:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10
    ))

    # game Over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        show_game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        show_game_over()

    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            show_game_over()

    # displaying score continuously
    show_score(1, white, 'calibri', 20)

    # refresh game screen
    pygame.display.update()

    # fps/refresh rate
    fps.tick(Snake_speed)