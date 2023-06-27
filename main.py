import pygame

# initialize pygame - start
pygame.init()

# screen create
width = 1024
height = 768
screen = pygame.display.set_mode((width, height))

# main game cycle
game_continue = True
    
while game_continue:
    for event in pygame.event.get(): # every move or mouse/key click or any other stuff is called event in pygame
        print(event)
        if event.type == pygame.QUIT:
            game_continue = False





# end of initialization
pygame.quit()