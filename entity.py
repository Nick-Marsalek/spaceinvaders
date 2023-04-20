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

    #Getters for the width and height of the entity
    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    #Function to move the entity
    def move(self, x, y):
        self.rect.move(x, y)


class Player(Entity):
    def __init__(self, x, y, image):
       #For inheritance
       Entity.__init__(self, x, y, image)

    def update(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.move(-1, 0)
                if event.key == pygame.K_RIGHT:
                    self.move(1, 0)

class PlayerBolt(Entity):
    def __init__(self, x, y, image):
        # For inheritance
        Entity.__init__(self, x, y, image)



