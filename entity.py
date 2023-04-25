import pygame
import constants as c


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
            self.move(-c.PLAYER_MOVE_INCREMENTS, 0)

        if ((self.get_x() <= (self.display_width - self.width)) and self.moving_right == True):
            self.move(c.PLAYER_MOVE_INCREMENTS, 0)

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

    def update(self):
        self.move(0, -c.PLAYER_BOLT_MOVE_INCREMENTS)
