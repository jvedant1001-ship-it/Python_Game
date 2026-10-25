import pygame

#initialize pygame
pygame.init()

Windows_screen = pygame.display.set_mode((800,800))

player_size = pygame.Surface((20,20))
pos_x = 800//2
pos_y = 800//2
run = True

while run:
    Windows_screen.fill((100,50,88))
    
    for event in pygame.event.get():
        pygame.font.get_default_font()
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_RIGHT:
                pos_x += 10
            if event.key == pygame.K_LEFT:
                        pos_x -= 10
            if event.key == pygame.K_UP:
                        pos_y -= 10
            
            if event.key == pygame.K_DOWN:
                    pos_y += 10
    Windows_screen.blit(player_size,(pos_x,pos_y))
    pygame.display.flip()