#Professional GUI - PYGAME
import pygame
import random
import os

# ---------------- INITIALIZE ----------------
pygame.init()

# ---------------- SCREEN ----------------
WIDTH = 800
HEIGHT = 600
CELL_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Evolution")

clock = pygame.time.Clock()

# ---------------- COLORS ----------------
BG_COLOR = (15, 18, 25)
GRID_COLOR = (30, 35, 45)

SNAKE_HEAD = (80, 220, 120)
SNAKE_BODY = (45, 170, 90)

FOOD_COLOR = (255, 80, 80)
WHITE = (245, 245, 245)
GRAY = (160, 165, 175)
YELLOW = (255, 210, 70)

# ---------------- FONTS ----------------
title_font = pygame.font.Font(None, 70)
big_font = pygame.font.Font(None, 50)
medium_font = pygame.font.Font(None, 34)
small_font = pygame.font.Font(None, 26)

# ---------------- HIGH SCORE ----------------
HIGH_SCORE_FILE = "highscore.txt"


def load_high_score():
    if os.path.exists(HIGH_SCORE_FILE):
        try:
            with open(HIGH_SCORE_FILE, "r") as file:
                return int(file.read())
        except:
            return 0

    return 0


def save_high_score(score):
    with open(HIGH_SCORE_FILE, "w") as file:
        file.write(str(score))


high_score = load_high_score()

# ---------------- GAME VARIABLES ----------------
snake = []
food = None

direction = (1, 0)
next_direction = (1, 0)

score = 0
game_speed = 8

game_state = "MENU"


# ---------------- CREATE SNAKE ----------------
def create_snake():

    return [
        (400, 300),
        (380, 300),
        (360, 300),
        (340, 300)
    ]


# ---------------- CREATE FOOD ----------------
def create_food():

    while True:

        x = random.randrange(0, WIDTH, CELL_SIZE)
        y = random.randrange(0, HEIGHT, CELL_SIZE)

        position = (x, y)

        if position not in snake:
            return position


# ---------------- RESET GAME ----------------
def reset_game():

    global snake
    global food
    global direction
    global next_direction
    global score
    global game_speed

    snake = create_snake()

    direction = (1, 0)
    next_direction = (1, 0)

    score = 0
    game_speed = 8

    food = create_food()


# ---------------- DRAW GRID ----------------
def draw_grid():

    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(
            screen,
            GRID_COLOR,
            (x, 0),
            (x, HEIGHT)
        )

    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(
            screen,
            GRID_COLOR,
            (0, y),
            (WIDTH, y)
        )


# ---------------- DRAW SNAKE ----------------
def draw_snake():

    for index, (x, y) in enumerate(snake):

        rect = pygame.Rect(
            x + 2,
            y + 2,
            CELL_SIZE - 4,
            CELL_SIZE - 4
        )

        if index == 0:
            pygame.draw.rect(
                screen,
                SNAKE_HEAD,
                rect,
                border_radius=6
            )

            # Eyes
            eye_size = 3

            pygame.draw.circle(
                screen,
                (10, 20, 15),
                (x + 7, y + 6),
                eye_size
            )

            pygame.draw.circle(
                screen,
                (10, 20, 15),
                (x + 14, y + 6),
                eye_size
            )

        else:

            pygame.draw.rect(
                screen,
                SNAKE_BODY,
                rect,
                border_radius=5
            )


# ---------------- DRAW FOOD ----------------
def draw_food():

    x, y = food

    center = (
        x + CELL_SIZE // 2,
        y + CELL_SIZE // 2
    )

    pygame.draw.circle(
        screen,
        FOOD_COLOR,
        center,
        CELL_SIZE // 2 - 2
    )

    # Small highlight
    pygame.draw.circle(
        screen,
        (255, 170, 170),
        (x + 7, y + 6),
        3
    )


# ---------------- DRAW SCORE ----------------
def draw_score():

    score_text = small_font.render(
        f"Score: {score}",
        True,
        WHITE
    )

    high_text = small_font.render(
        f"High Score: {high_score}",
        True,
        YELLOW
    )

    screen.blit(score_text, (20, 15))
    screen.blit(high_text, (20, 45))


# ---------------- CENTER TEXT ----------------
def draw_center_text(text, font, color):

    surface = font.render(
        text,
        True,
        color
    )

    rect = surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2)
    )

    screen.blit(surface, rect)


# ---------------- MENU SCREEN ----------------
def draw_menu():

    screen.fill(BG_COLOR)

    draw_center_text(
        "SNAKE EVOLUTION",
        title_font,
        SNAKE_HEAD
    )

    text = medium_font.render(
        "Press ENTER to Start",
        True,
        WHITE
    )

    text_rect = text.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 70)
    )

    screen.blit(text, text_rect)

    controls = small_font.render(
        "Arrow Keys  |  P = Pause  |  ESC = Quit",
        True,
        GRAY
    )

    controls_rect = controls.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 130)
    )

    screen.blit(controls, controls_rect)


# ---------------- GAME OVER SCREEN ----------------
def draw_game_over():

    screen.fill(BG_COLOR)

    draw_center_text(
        "GAME OVER",
        title_font,
        FOOD_COLOR
    )

    score_text = medium_font.render(
        f"Your Score: {score}",
        True,
        WHITE
    )

    score_rect = score_text.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 70)
    )

    screen.blit(score_text, score_rect)

    restart_text = small_font.render(
        "Press ENTER to Play Again",
        True,
        GRAY
    )

    restart_rect = restart_text.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 120)
    )

    screen.blit(restart_text, restart_rect)


# ---------------- PAUSE SCREEN ----------------
def draw_pause():

    overlay = pygame.Surface(
        (WIDTH, HEIGHT),
        pygame.SRCALPHA
    )

    overlay.fill((0, 0, 0, 150))

    screen.blit(overlay, (0, 0))

    draw_center_text(
        "PAUSED",
        title_font,
        WHITE
    )

    text = small_font.render(
        "Press P to Resume",
        True,
        GRAY
    )

    rect = text.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 60)
    )

    screen.blit(text, rect)


# ---------------- MOVE SNAKE ----------------
def move_snake():

    global food
    global score
    global game_speed
    global game_state
    global high_score

    head_x, head_y = snake[0]

    dx, dy = next_direction

    new_head = (
        head_x + dx * CELL_SIZE,
        head_y + dy * CELL_SIZE
    )

    # Wall collision
    if (
        new_head[0] < 0
        or new_head[0] >= WIDTH
        or new_head[1] < 0
        or new_head[1] >= HEIGHT
    ):
        game_state = "GAME_OVER"
        return

    # Body collision
    if new_head in snake[:-1]:
        game_state = "GAME_OVER"
        return

    snake.insert(0, new_head)

    # Food collision
    if new_head == food:

        score += 1

        if score > high_score:
            high_score = score
            save_high_score(high_score)

        food = create_food()

        # Increase speed gradually
        game_speed = min(
            18,
            8 + score // 3
        )

    else:

        snake.pop()


# ---------------- MAIN LOOP ----------------
reset_game()

running = True

move_timer = 0

while running:

    dt = clock.tick(60)

    move_timer += dt

    # ---------------- EVENTS ----------------
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            # Quit
            if event.key == pygame.K_ESCAPE:
                running = False

            # Start / Restart
            if event.key == pygame.K_RETURN:

                if game_state == "MENU":

                    reset_game()
                    game_state = "PLAYING"

                elif game_state == "GAME_OVER":

                    reset_game()
                    game_state = "PLAYING"

            # Pause
            if event.key == pygame.K_p:

                if game_state == "PLAYING":
                    game_state = "PAUSED"

                elif game_state == "PAUSED":
                    game_state = "PLAYING"

            # Movement
            if game_state == "PLAYING":

                if event.key == pygame.K_UP:
                    if direction != (0, 1):
                        next_direction = (0, -1)

                elif event.key == pygame.K_DOWN:
                    if direction != (0, -1):
                        next_direction = (0, 1)

                elif event.key == pygame.K_LEFT:
                    if direction != (1, 0):
                        next_direction = (-1, 0)

                elif event.key == pygame.K_RIGHT:
                    if direction != (-1, 0):
                        next_direction = (1, 0)

    # ---------------- GAME UPDATE ----------------
    if game_state == "PLAYING":

        move_delay = 1000 // game_speed

        if move_timer >= move_delay:

            direction = next_direction

            move_snake()

            move_timer = 0

    # ---------------- DRAW ----------------
    if game_state == "MENU":

        draw_menu()

    elif game_state == "PLAYING":

        screen.fill(BG_COLOR)

        draw_grid()
        draw_food()
        draw_snake()
        draw_score()

    elif game_state == "PAUSED":

        screen.fill(BG_COLOR)

        draw_grid()
        draw_food()
        draw_snake()
        draw_score()

        draw_pause()

    elif game_state == "GAME_OVER":

        draw_game_over()

    pygame.display.flip()


pygame.quit()