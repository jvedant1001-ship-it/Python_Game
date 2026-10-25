import pygame
import random

#initialize pygame
pygame.init()

Windows_screen = pygame.display.set_mode((800,800))

snake_size = pygame.Surface((20,20))
fruit_size = pygame.Surface((20,20))
fruit_x = 200
fruit_y = 200
snake_x = 220
snake_y = 220
score = 0 
run = True

while run:
    Windows_screen.fill("black")
    fruit_size.fill((255,0,0))
    snake_size.fill((0,255,0))

    if snake_x == fruit_x and snake_y == fruit_y:
                   fruit_x = random.randrange(0,800,20) 
                   fruit_y = random.randrange(0,800,20)
                   
    
    for event in pygame.event.get():
        pygame.font.get_default_font()
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_RIGHT:
                snake_x += 20
            if event.key == pygame.K_LEFT:
                        snake_x -= 20
            if event.key == pygame.K_UP:
                        snake_y -= 20
            
            if event.key == pygame.K_DOWN:
                    snake_y += 20
    Windows_screen.blit(snake_size,(snake_x,snake_y))
    Windows_screen.blit(fruit_size,(fruit_x,fruit_y))
    pygame.display.flip()