import pygame

# initialize pygame - start
pygame.init()

# screen create
width = 1024
height = 768
screen = pygame.display.set_mode((width, height))

# set name of the game
pygame.display.set_caption("Harry Potter Game")

# definition of colors
# red, green, blue
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# background color
screen.fill(black)

# shapes
pygame.draw.line(screen, white, (00, 384), (width, height/2), 1)
pygame.draw.circle(screen, yellow, (width/2, height/2), 100, 6 )
pygame.draw.circle(screen, red, (width/2, height/2), 96, 0)
pygame.draw.rect(screen, blue, (300, 267, 100, 100), 2)


# main game cycle
game_continue = True
    
while game_continue:
    for event in pygame.event.get(): # every move or mouse/key click or any other stuff is called event in pygame
        # print(event) show events in log
        if event.type == pygame.QUIT:
            game_continue = False

    # refresh/update of scree
    pygame.display.update()





# end of initialization
pygame.quit()