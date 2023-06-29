# import pygame
import pygame

# initialize pygame - start
pygame.init()

# screen create
width = 1024
height = 768

# main game cycle
game_continue = True

while game_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_continue = False

# end of initialization
pygame.quit()