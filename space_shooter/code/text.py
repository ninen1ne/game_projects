import pygame

pygame.init()
screenHeight = 600
screenWidth = 900
screenSurface = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Yolle")

player1 = pygame.Surface((100, 200))
player1.fill('red')
run = True
while run:
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # draw screen
    screenSurface.fill((119, 118, 179))
    screenSurface.blit(player1, (0,0))
    pygame.display.update()


pygame.quit()