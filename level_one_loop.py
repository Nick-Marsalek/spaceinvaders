import sys
import pygame
import entity
import constants as c

def level_one(display_surface):
    # Load images into pygame
    player_image = pygame.image.load('Assets/player_small.png').convert_alpha()
    player_bolt_image = pygame.image.load('Assets/player_bolt.png').convert_alpha()

    # Create groups for the entities
    player_group = pygame.sprite.GroupSingle()
    player_bolt_group = pygame.sprite.Group()

    # Create the player and put it in its own group
    player = entity.Player(c.DISPLAY_WIDTH, c.DISPLAY_HEIGHT, player_image)
    player_group.add(player)

    # Create clock object and frame-counting variables
    clock = pygame.time.Clock()
    frame_counter = 0
    firing_cooldown = 0

    while (True):
        # Sets the game loop to run this many times each second
        # I.E. This many frames per second
        clock.tick(c.GAME_LOOPS_PER_SECOND)

        # Handle user input
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.set_moving_left(True)
                if event.key == pygame.K_RIGHT:
                    player.set_moving_right(True)
                if (event.key == pygame.K_UP) or (event.key == pygame.K_SPACE):
                    player.set_firing(True)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.set_moving_left(False)
                if event.key == pygame.K_RIGHT:
                    player.set_moving_right(False)
                if (event.key == pygame.K_UP) or (event.key == pygame.K_SPACE):
                    player.set_firing(False)
            elif event.type == pygame.QUIT:
                sys.exit()

        # Update(move) the player every certain number of frames
        if ((frame_counter % c.FRAMES_PER_PLAYER_MOVEMENT) == 0):
            player_group.update()

        # Replaced by a different method of restricting firing, that also eliminates lingering bolts
        # If player should be firing, fire a bolt and then start a cooldown
        # if (firing_cooldown <= 0):
            # if player.get_firing():
                # These bolt entities just stick around and aren't deleted,
                # May be a problem if too many are fired over the course of the game
                # But it should be fine if it's under 10,000
                # player_bolt_group.add(entity.PlayerBolt(c.DISPLAY_WIDTH, c.DISPLAY_HEIGHT, player, player_bolt_image))
                # firing_cooldown = c.PLAYER_FIRING_COOLDOWN

        # Delete any player bolts that go off-screen
        for bolt in player_bolt_group:
            if bolt.get_off_screen():
                bolt.kill()

        # Fire a bolt only if there aren't too many bolts already on-screen
        # This matches the real Space Invaders behaviour more closely if limit is set to 1
        if (len(player_bolt_group) < c.PLAYER_BOLTS_ONSCREEN_LIMIT) and player.get_firing():
            player_bolt_group.add(entity.PlayerBolt(c.DISPLAY_WIDTH, c.DISPLAY_HEIGHT, player, player_bolt_image))

        # Update(move) all the bolts from the player
        if (frame_counter % c.FRAMES_PER_PLAYER_BOLT_MOVEMENT) == 0:
            player_bolt_group.update()

        # Iterate counters
        firing_cooldown -= 1
        frame_counter += 1
        # This frame counter just goes up, may be a problem if the game goes on too long
        # No idea about how Python handles number overflows
        # Should be fine for an hour or so though

        # Draw everything and flip the display
        display_surface.fill((0, 0, 0))
        player_group.draw(display_surface)
        player_bolt_group.draw(display_surface)
        pygame.display.flip()

    # Quits pygame incase the game loop is broken
    pygame.quit()
