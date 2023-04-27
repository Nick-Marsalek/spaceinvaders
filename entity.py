import pygame
import GAME_CONSTANTS as C


class Entity(pygame.sprite.Sprite):
    def __init__(self, display_width, display_height, x, y, image):
        # For inheritance
        pygame.sprite.Sprite.__init__(self)

        # Information about the display
        self.display_width = display_width
        self.display_height = display_height

        # Get image for entity and create rect from it
        self.image = image
        self.rect = self.image.get_rect()

        # Get width and height of entity from image rect
        self.width = image.get_width()
        self.height = image.get_height()

        # Move entity to the correct place
        self.rect.update(x, y, self.width, self.height)

    # Getters for the entity's properties
    def get_entity_width(self):
        return self.width

    def get_entity_height(self):
        return self.height

    def get_display_width(self):
        return self.display_width

    def get_display_height(self):
        return self.display_height

    def get_x(self):
        return self.rect.x

    def get_y(self):
        return self.rect.y

    # Function to move the entity
    def move(self, x, y):
        self.rect.move_ip(x, y)


class Player(Entity):
    def __init__(self, display_width, display_height, image):
        # For inheritance
        Entity.__init__(self, display_width, display_height, (display_width / 2) - 15, display_height - 35, image)

        # States of the player
        self.firing = False
        self.moving_left = False
        self.moving_right = False

    def update(self):
        if ((self.get_x() >= 1) and self.moving_left == True):
            self.move(-C.PLAYER_MOVE_INCREMENTS, 0)

        if ((self.get_x() <= (self.display_width - self.width)) and self.moving_right == True):
            self.move(C.PLAYER_MOVE_INCREMENTS, 0)

    # Getters for Player's states
    def get_firing(self):
        return self.firing

    # Setters for Player's states
    def set_moving_left(self, boolean):
        self.moving_left = boolean

    def set_moving_right(self, boolean):
        self.moving_right = boolean

    def set_firing(self, boolean):
        self.firing = boolean


class PlayerBolt(Entity):
    def __init__(self, display_width, display_height, player, image):
        # For inheritance
        Entity.__init__(self, display_width, display_height,
                        player.get_x() + (player.get_entity_width() / 2) - (image.get_width() / 2),
                        player.get_y() - image.get_height(), image)

        # Player that fired this bolt
        self.player = player
        self.is_off_screen = False

    # Getter for whether bolt is off-screen
    def get_off_screen(self):
        return self.is_off_screen

    def update(self):
        # Move up at constant speed forever
        self.move(0, -C.PLAYER_BOLT_MOVE_INCREMENTS)

        # Determine if this bolt is off-screen
        if (self.get_y() < 0):
            self.is_off_screen = True


class BarrierBlock(Entity):
    def __init__(self, display_width, display_height, x, y, health_image4, health_image3, health_image2, health_image1):
        # For inheritance
        Entity.__init__(self, display_width, display_height, x, y, health_image4)

        # Set starting health variables
        self.barrier_health = 4
        self.destroyed = False

        # Set images for each stage of health
        self.health_image4 = health_image4
        self.health_image3 = health_image3
        self.health_image2 = health_image2
        self.health_image1 = health_image1

    # Getter for whether block should be destroyed
    def get_destroyed(self):
        return self.destroyed

    # Function to decrease block's health
    def damage(self):
        if self.barrier_health >= 0:
            self.barrier_health -= 1
        if self.barrier_health <= 0:
            self.destroyed = True

    # Update function switches current image depending on current health
    def update(self):
        if self.barrier_health >= 4:
            self.image = self.health_image4
        elif self.barrier_health == 3:
            self.image = self.health_image3
        elif self.barrier_health == 2:
            self.image = self.health_image2
        else:
            self.image = self.health_image1


class Enemy(Entity):
    def __init__(self, display_width, display_height, image, frame1img, frame2img):
        # For inheritance
        Entity.__init__(self, C.DISPLAY_WIDTH, C.DISPLAY_HEIGHT, display_width, display_height, image)
        self.frame1img = frame1img
        self.frame2img = frame2img
        self.frame1 = False
        self.shoot = True
        self.x = display_width
        self.y = display_height

    def update(self, newx, newy):
        self.move(newx, newy)
        if self.frame1:
            self.image = self.frame1img
            self.frame1 = False
        else:
            self.image = self.frame2img
            self.frame1 = True

    def get_enemy_x(self):
        return self.x

    def get_enemy_y(self):
        return self.y

    def add_x(self, num):
        self.x += num

    def add_y(self, num):
        self.y += num


class EnemyBolt(Entity):
    # For inheritance
    def __init__(self, display_width, display_height, firer, image):
        Entity.__init__(self, display_width, display_height,
                        firer.get_x() + (firer.get_entity_width() / 2) - (image.get_width() / 2),
                        firer.get_y() + image.get_height(), image)

        self.is_off_screen = False

    # Getter for whether bolt is off-screen
    def get_off_screen(self):
        return self.is_off_screen

    def update(self):
        # Move up at constant speed forever
        self.move(0, 1)

        # Determine if this bolt is off-screen
        if (self.get_y() < 0):
            self.is_off_screen = True
