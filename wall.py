import pygame
import os

brickImage          = os.path.join('Image','brick.png')
ironImage           = os.path.join('Image','iron.png')

class Brick(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(brickImage)
        self.rect = self.image.get_rect()

class Iron(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(ironImage)
        self.rect = self.image.get_rect()

class Map():
    def __init__(self):
        self.brickGroup = pygame.sprite.Group()
        self.ironGroup  = pygame.sprite.Group()

        # 数字代表地图中的位置
        # 画砖块
        X1379 = [2, 3, 6, 7, 10, 11, 24, 25, 28, 29, 32, 33]
        Y1379 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,21, 22, 23, 24, 25,26,27,28,29,30,31,32,33]
        X28 = [14, 15, 20, 21]
        Y28 = [2, 3, 4, 5, 6, 7, 8,9,10, 11,12,15,16,17,20,21,22,23,24,25,26]
        X46 = [4, 5, 6, 7, 8, 9, 24, 25, 26, 27, 28, 29]
        Y46 = [17, 18]
        X5  = [16, 17, 18, 19]
        Y5  = [22, 23]
        # X0Y0 = [(15,32),(16,32),(17,32),(18,32),(19,32),(20,32),(15,31),(16,31),(17,31),(18,31),(19,31),(20,31),(15,33),(16,33),(17,33),(18,33),(19,33),(20,33)]
        X0 = [15, 16, 17, 18, 19, 20]
        Y0 = [31, 32, 33]

        for x in X1379:
            for y in Y1379:
                self.brick = Brick()
                self.brick.rect.left, self.brick.rect.top = 3+x * 24, 3+y * 24
                self.brickGroup.add(self.brick)
        for x in X28:
            for y in Y28:
                self.brick = Brick()
                self.brick.rect.left, self.brick.rect.top = 3+x * 24, 3+y * 24
                self.brickGroup.add(self.brick)
        for x in X46:
            for y in Y46:
                self.brick = Brick()
                self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
                self.brickGroup.add(self.brick)
        for x in X5:
            for y in Y5:
                self.brick = Brick()
                self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
                self.brickGroup.add(self.brick)
        for x in X0:
            for y in Y0:
                self.iron = Iron()
                self.iron.rect.left, self.iron.rect.top = 3 + x * 24, 3 + y * 24
                self.ironGroup.add(self.iron)

        # 画石头
        for x, y in [(0,17),(1,17),(16,8),(17,8),(18,8),(19,8),(16,9),(17,9),(18,9),(19,9),(34,17),(35,17)]:
            self.iron = Iron()
            self.iron.rect.left, self.iron.rect.top = 3 + x * 24, 3 + y * 24
            self.ironGroup.add(self.iron)
