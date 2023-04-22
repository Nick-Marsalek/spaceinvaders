import sys

import pygame

class Entity(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        #For inheritance
        pygame.sprite.Sprite.__init__(self)

        #Get image for entity and create rect from it
        self.image = image
        self.rect = self.image.get_rect()

        #Get width and height of entity from image rect
        self.width = image.get_width()
        self.height = image.get_height()

        #Move entity to the correct place
        self.rect.update(x, y, self.width, self.height)

        #Whether or not player is firing
        self.firing = False

    #Getters for the width and height of the entity
    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_x(self):
        return self.rect.x

    def get_y(self):
        return self.rect.y

    def get_firing(self):
        return self.firing

    #Function to move the entity
    def move(self, x, y):
        self.rect.move_ip(x, y)


class Player(Entity):
    def __init__(self, display_width, display_height, image):
        #For inheritance
        Entity.__init__(self, (display_width/2)-15, display_height-35, image)

        self.display_width = display_width
        self.display_height = display_height

        self.left_down = False
        self.right_down = False

    def update(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.left_down = True
                if event.key == pygame.K_RIGHT:
                    self.right_down = True
                if event.key == pygame.K_UP:
                    self.firing = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.left_down = False
                if event.key == pygame.K_RIGHT:
                    self.right_down = False
                if event.key == pygame.K_UP:
                    self.firing = False
            elif event.type == pygame.QUIT:
                sys.exit()

        if((self.get_x() >= 1) and self.left_down == True):
            self.move(-1, 0)
            print(self.get_x())

        if((self.get_x() <= (self.display_width - self.width)) and self.right_down == True):
            self.move(1, 0)
            print(self.get_x())







class PlayerBolt(Entity):
    def __init__(self, x, y, image):
        # For inheritance
        Entity.__init__(self, x, y, image)

    def update(self):
        self.move(0, -1)



