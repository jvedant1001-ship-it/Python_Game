import pygame

#initialize pygame
pygame.init()

#first screen to user
Windows_screen = pygame.display.set_mode((800,800))



run = True
while run:
    for event in pygame.event.get():
        pygame.font.get_default_font()
        if event.type == pygame.QUIT:
            run = False

pygame.display.flip()