
import pygame
import random

# Initialize Pygame
pygame.init()

# Create window
Windows_screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Snake Game")

# Snake and fruit
snake_size = pygame.Surface((20, 20))
snake_size.fill((0, 255, 0))

fruit_size = pygame.Surface((20, 20))
fruit_size.fill((255, 0, 0))

# Starting positions
snake_x = 220
snake_y = 220

fruit_x = 200
fruit_y = 200

# Score and movement
score = 0
dx = 0
dy = 0

# Clock and font
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 40)

run = True
game_over = False

while run:

    # Handle events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        # Restart after game over
        if game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                snake_x = 220
                snake_y = 220

                dx = 0
                dy = 0

                score = 0

                fruit_x = random.randrange(0, 800, 20)
                fruit_y = random.randrange(0, 800, 20)

                game_over = False

        # Movement controls during gameplay
        elif not game_over and event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:
                dx = 20
                dy = 0

            elif event.key == pygame.K_LEFT:
                dx = -20
                dy = 0

            elif event.key == pygame.K_UP:
                dx = 0
                dy = -20

            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = 20

    # Clear screen
    Windows_screen.fill("black")

    if not game_over:

        # Move snake
        snake_x += dx
        snake_y += dy

        # Check boundaries
        if (
            snake_x < 0
            or snake_x + 20 > 800
            or snake_y < 0
            or snake_y + 20 > 800
        ):
            game_over = True

        # Check fruit collision only if still alive
        if not game_over and snake_x == fruit_x and snake_y == fruit_y:
            score += 10

            fruit_x = random.randrange(0, 800, 20)
            fruit_y = random.randrange(0, 800, 20)

        # Draw snake, fruit and score while alive
        if not game_over:
            Windows_screen.blit(snake_size, (snake_x, snake_y))
            Windows_screen.blit(fruit_size, (fruit_x, fruit_y))

            score_text = font.render(
                "Score: " + str(score),
                True,
                (255, 255, 0)
            )
            Windows_screen.blit(score_text, (20, 20))

    # Game-over screen
    if game_over:
        over_text = font.render(
            "You Died!!", True, (255, 0, 0)
        )

        final_score = font.render(
            "Final Score: " + str(score),
            True,
            (255, 255, 0)
        )

        restart_text = font.render(
            "Press R to restart",
            True,
            (255, 255, 255)
        )

        Windows_screen.blit(over_text, (250, 280))
        Windows_screen.blit(final_score, (200, 350))
        Windows_screen.blit(restart_text, (180, 430))

    # Update display every frame
    pygame.display.flip()

    # Limit frame rate
    clock.tick(10)

pygame.quit()
