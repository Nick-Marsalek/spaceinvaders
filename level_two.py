import sys
import pygame

def level_two(display_surface):
    while (True):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()

        display_surface.fill((123, 0, 0))
        pygame.display.flip()
