import pygame
import entity

def level_one(display_surface):
    display_surface.fill((0, 0, 0))

    # Temp sprite code for testing
    player_image = pygame.image.load('Assets/playerSmall.png').convert_alpha()
    player_bolt_image = pygame.image.load('Assets/player_bolt.png').convert_alpha()
    player = entity.Player(800, 600, player_image)
    testGroup = pygame.sprite.Group()
    testGroup.add(player)
    testGroup.draw(display_surface)
    pygame.display.flip()

    player_bolt_group = pygame.sprite.Group()
    clock = pygame.time.Clock()

    # Temp sprite code for testing
    loop_counter = 0
    while(True):
        #Sets the game loop to run this many times each second
        clock.tick(300)
        loop_counter += 1

        display_surface.fill((0, 0, 0))

        player_bolt_group.draw(display_surface)


        if (loop_counter > 50):
            testGroup.update()

        print(loop_counter)

        if(loop_counter > 50):
            if (player.get_firing()):
                player_bolt_group.add(entity.PlayerBolt(player.get_x() + 13, player.get_y() - 9, player_bolt_image))
                print('PEW')
                loop_counter = 0

        if (loop_counter > 50):
            player_bolt_group.update()


        print(len(player_bolt_group))

        testGroup.draw(display_surface)
        pygame.display.flip()
