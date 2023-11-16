import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
PINK = (255, 105, 180)
WHITE = (255, 255, 255)

# Load images
background_image = pygame.image.load("images/background.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

basket_image = pygame.image.load("images/basket.png")
strawberry_image = pygame.image.load("images/strawberry.png")

# Resize images
basket_image = pygame.transform.scale(basket_image, (150, 150))
strawberry_image = pygame.transform.scale(strawberry_image, (50, 50))

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Strawberries")

# Create the basket
basket_width, basket_height = basket_image.get_size()
basket_width *= 2
basket_height *= 2
basket_x = (WIDTH - basket_width) // 2
basket_y = HEIGHT - basket_height - 10
basket_speed = 5

# Create the falling strawberries
strawberry_width, strawberry_height = strawberry_image.get_size()
strawberry_speed = 5

# Initialize score and difficulty
score = 0
difficulty = 0  # Controls the difficulty level

font = pygame.font.Font(None, 36)

def draw_background():
    screen.blit(background_image, (0, 0))

def draw_basket(x, y):
    screen.blit(basket_image, (x, y))

def draw_strawberry(x, y):
    screen.blit(strawberry_image, (x, y))

def draw_score():
    score_text = font.render("Score: {}".format(score), True, PINK)
    screen.blit(score_text, (10, 10))

def increase_difficulty():
    global difficulty
    if score > 5 and difficulty == 0:
        difficulty = 1
    if score > 10 and difficulty == 1:
        difficulty = 2

def create_strawberry():
    return {'x': random.randint(0, WIDTH - strawberry_width), 'y': -strawberry_height}

def update_strawberries(strawberries):
    for strawberry in strawberries:
        strawberry['y'] += strawberry_speed + difficulty
        if strawberry['y'] > HEIGHT:
            strawberry['y'] = -strawberry_height
            strawberry['x'] = random.randint(0, WIDTH - strawberry_width)

def check_collision(basket_x, basket_y, strawberries):
    global score
    for strawberry in strawberries:
        if (
            basket_x < strawberry['x'] < basket_x + basket_width
            and basket_y < strawberry['y'] < basket_y + basket_height
        ):
            strawberry['y'] = -strawberry_height
            strawberry['x'] = random.randint(0, WIDTH - strawberry_width)
            score += 1

def game_loop():
    global basket_x, score
    clock = pygame.time.Clock()

    strawberries = [create_strawberry() for _ in range(5)]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and basket_x > 0:
            basket_x -= basket_speed
        if keys[pygame.K_RIGHT] and basket_x < WIDTH - basket_width:
            basket_x += basket_speed

        # Increase difficulty
        increase_difficulty()

        # Update falling strawberries
        update_strawberries(strawberries)

        # Check for collision
        check_collision(basket_x, basket_y, strawberries)

        # Draw everything
        draw_background()
        draw_basket(basket_x, basket_y)
        for strawberry in strawberries:
            draw_strawberry(strawberry['x'], strawberry['y'])
        draw_score()

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    game_loop()
