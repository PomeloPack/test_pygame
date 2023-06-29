import pygame

pygame.init()

width = 1024
height = 768
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Harry Potter game")

game_continue = True

while game_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_continue = False


pygame.quit()