import sys
import pygame

def game_over(display_surface):
    while (True):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()

        display_surface.fill((0, 0, 0))
        pygame.display.flip()
