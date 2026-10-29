import pygame

pygame.init()

screen = pygame.display.set_mode((960, 540))
pygame.display.set_caption("stupid gay chungus window")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 128))
    pygame.display.flip()

pygame.quit()
