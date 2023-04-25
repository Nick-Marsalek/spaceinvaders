import pygame
import pygame.image


class Enemy:
    def __init__(self, enemyType):
        enemyType = enemyType
        if enemyType == 1:
            self.frame1 = pygame.image.load("Assets/enemy.png")
            self.frame2 = pygame.image.load("Assets/enemy2.png")
        self.currentFrame = 1

    def getFrame1(self):
        return self.frame1

    def getFrame2(self):
        return self.frame2