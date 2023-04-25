import sys
import pygame
import entity
import GAME_CONSTANTS as c

# Level constants
FRAMES_PER_PLAYER_MOVEMENT = 10
FRAMES_PER_PLAYER_BOLT_MOVEMENT = 1
PLAYER_FIRING_COOLDOWN = 100
PLAYER_BOLTS_ONSCREEN_LIMIT = 1
BARRIER_NUMBER = 4
BARRIER_DISTANCE = 40

def level_one(display_surface):
    # Load images into pygame
    player_image = pygame.image.load('Assets/player_small.png').convert_alpha()
    player_bolt_image = pygame.image.load('Assets/player_bolt.png').convert_alpha()
    bb_image_4 = pygame.image.load('Assets/barrier_block4.png').convert_alpha()
    bb_image_3 = pygame.image.load('Assets/barrier_block3.png').convert_alpha()
    bb_image_2 = pygame.image.load('Assets/barrier_block2.png').convert_alpha()
    bb_image_1 = pygame.image.load('Assets/barrier_block1.png').convert_alpha()

    # Create groups for the entities
    player_group = pygame.sprite.GroupSingle()
    player_bolt_group = pygame.sprite.Group()
    barrier_group = pygame.sprite.Group()

    # Create the player and put it in its own group
    player = entity.Player(c.DISPLAY_WIDTH, c.DISPLAY_HEIGHT, player_image)
    player_group.add(player)

    # Create clock object and frame-counting variables
    clock = pygame.time.Clock()
    frame_counter = 0
    firing_cooldown = 0

    # Calculate where each barrier should go based on display and barrier dimensions
    barrier_width = bb_image_4.get_width()*4
    barrier_height = bb_image_4.get_width()*3

    segment_width = c.DISPLAY_WIDTH/BARRIER_NUMBER
    leftover_width = segment_width - barrier_width

    barrier_y = c.DISPLAY_HEIGHT - player.get_entity_height() - barrier_height - BARRIER_DISTANCE
    barrier_x = leftover_width/2
    barrier_x_offset = leftover_width + barrier_width

    # Create barriers with build_barrier function
    for i in range(BARRIER_NUMBER):
        build_barrier(c.DISPLAY_WIDTH, c.DISPLAY_HEIGHT, barrier_x, barrier_y, barrier_group,
                      bb_image_4, bb_image_3, bb_image_2, bb_image_1)
        barrier_x += barrier_x_offset

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
        if (frame_counter % FRAMES_PER_PLAYER_MOVEMENT) == 0:
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

        # Fire a bolt only if there aren't too many bolts already on-screen, with cooldown period
        # This matches the real Space Invaders behaviour more closely if limit is set to 1
        if (len(player_bolt_group) < PLAYER_BOLTS_ONSCREEN_LIMIT) and player.get_firing() and firing_cooldown <= 0:
            player_bolt_group.add(entity.PlayerBolt(c.DISPLAY_WIDTH, c.DISPLAY_HEIGHT, player, player_bolt_image))
            firing_cooldown = PLAYER_FIRING_COOLDOWN

        # Update(move) all the bolts from the player
        if (frame_counter % FRAMES_PER_PLAYER_BOLT_MOVEMENT) == 0:
            player_bolt_group.update()

        # Check for collisions between player's bolts and the barrier and damage each block if hit
        barrier_blocks_hit_by_player = pygame.sprite.groupcollide(barrier_group, player_bolt_group, False, True)
        for block in barrier_blocks_hit_by_player:
            block.damage()
            if block.get_destroyed():
                block.kill()

        # Update the barrier block's images
        barrier_group.update()

        # Iterate frame counter and reset after exactly 30 minutes
        frame_counter += 1
        if frame_counter >= (c.GAME_LOOPS_PER_SECOND * 60 * 60):
            frame_counter = 0

        # Tick down firing cooldown timer, but don't let it go below 0
        if firing_cooldown < 0:
            firing_cooldown = 0
        else:
            firing_cooldown -= 1

        # Draw everything and flip the display
        display_surface.fill((0, 0, 0))
        player_group.draw(display_surface)
        player_bolt_group.draw(display_surface)
        barrier_group.draw(display_surface)
        pygame.display.flip()

    # Quits pygame incase the game loop is broken
    pygame.quit()


# Function to build each barrier
def build_barrier(display_width, display_height, x, y, group, image4, image3, image2, image1):
    # Set starting x value for building barrier
    this_x = x
    # Set offset counter for shape of barrier
    counter = 6
    # Build each column of barrier
    for i in range(4):
        # Set starting y for each column
        this_y = y
        # Check which column of the barrier we're building
        if (counter % 3) == 0:
            inner_range = 3
        else:
            inner_range = 2
        # Build column in block by block
        for j in range(inner_range):
            block = entity.BarrierBlock(display_width, display_height,
                                        int(this_x), int(this_y), image4, image3, image2, image1)
            group.add(block)
            this_y += block.get_entity_height()

        # Increment variables
        this_x += block.get_entity_width()
        counter -= 1
