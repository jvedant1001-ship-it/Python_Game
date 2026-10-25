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
dx = 0 
dy = 0

clock = pygame.time.Clock()

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
                dx = 20
                dy = 0
            if event.key == pygame.K_LEFT:
                dx = -20
                dy = 0
            if event.key == pygame.K_UP:
                dy = -20
                dx = 0
            if event.key == pygame.K_DOWN:
                 dy = +20
                 dx = 0

    snake_x += dx
    snake_y += dy

    Windows_screen.blit(snake_size,(snake_x,snake_y))
    Windows_screen.blit(fruit_size,(fruit_x,fruit_y))

    pygame.display.flip()
    clock.tick(10)
    
pygame.quit()