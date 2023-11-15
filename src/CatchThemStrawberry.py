import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)

# Load images
background_image = pygame.image.load("images/background.jpg")  # Adjust the file path
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

basket_image = pygame.image.load("images/basket.png")
strawberry_image = pygame.image.load("images/strawberry.png")

# Resize images
basket_image = pygame.transform.scale(basket_image, (150, 150))
strawberry_image = pygame.transform.scale(strawberry_image, (40, 40))

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

# Create the falling strawberry
object_width, object_height = strawberry_image.get_size()
object_speed = 5

def draw_background():
    screen.blit(background_image, (0, 0))

def draw_basket(x, y):
    screen.blit(basket_image, (x, y))

def draw_object(x, y):
    screen.blit(strawberry_image, (x, y))

def game_loop():
    global basket_x  # Declare basket_x as a global variable
    clock = pygame.time.Clock()

    object_x = random.randint(0, WIDTH - object_width)
    object_y = 0

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

        object_y += object_speed
        if object_y > HEIGHT:
            object_y = 0
            object_x = random.randint(0, WIDTH - object_width)

        # Check for collision
        if (
            basket_x < object_x < basket_x + basket_width
            and basket_y < object_y < basket_y + basket_height
        ):
            object_y = 0
            object_x = random.randint(0, WIDTH - object_width)

        # Draw everything
        draw_background()  # Draw the background first
        draw_basket(basket_x, basket_y)
        draw_object(object_x, object_y)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    game_loop()