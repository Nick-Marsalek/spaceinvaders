import pygame
import entity

def level_one(display_surface):
    display_surface.fill((0, 0, 0))

    # Temp sprite code for testing
    plimage = pygame.image.load('Assets/playerSmall.png').convert_alpha()
    player = entity.Player(100, 10, plimage)
    testGroup = pygame.sprite.Group()
    testGroup.add(player)
    testGroup.draw(display_surface)
    # Temp sprite code for testing
    hello = 1
    while(True):
        display_surface.flip()