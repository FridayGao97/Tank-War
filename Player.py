import pygame
import os
import bulletClass


tank_T1_0 = os.path.join('image','tank_T1_0.png')

tank_T2_0 = os.path.join('image','tank_T2_0.png')



class MyTank(pygame.sprite.Sprite):
    def __init__(self, playerNumber):
        pygame.sprite.Sprite.__init__(self)

        
        self.life = True


        '''
        convert and convert_alpha are both used to convert surfaces to the same pixel format as used by the screen. 
        This ensures that you won't lose performance because of conversions when you're blitting them to the screen. 
        convert throws away any alpha channel, whereas convert_alpha keeps it. 
        The comment that you see refers to the choice to use convert_alpha instead of convert, 
        rather than a choice to use convert_alpha instead of nothing.
        '''
        if playerNumber == 1:
            self.tank = pygame.image.load(tank_T1_0).convert_alpha()
            
        if playerNumber == 2:
            self.tank = pygame.image.load(tank_T2_0).convert_alpha()
            
        
        self.tank_R0 = self.tank.subsurface((0, 0),(48, 48))
        self.tank_R1 = self.tank.subsurface((48, 0),(48, 48))
        self.rect = self.tank_R0.get_rect()

        if playerNumber == 1:
            self.rect.left, self.rect.top = 3 + 24 * 13, 3 + 24 * 33
        if playerNumber == 2:
            self.rect.left, self.rect.top = 3 + 24 * 21, 3 + 24 * 33

        self.speed = 3
        self.dir_x, self.dir_y = 0, -1
        self.life = 3
        self.bulletNotCooling = True
        self.bullet = bulletClass.Bullet()
        #self.bullet.rect.left, self.bullet.rect.right = 3 + 12 * 24, 3 + 24 * 24

    def shoot(self):
        # �ӵ�
        self.bullet.life = True
        self.bullet.changeImage(self.dir_x, self.dir_y)

        if self.dir_x == 0 and self.dir_y == -1:
            self.bullet.rect.left = self.rect.left + 20
            self.bullet.rect.bottom = self.rect.top + 1
        elif self.dir_x == 0 and self.dir_y == 1:
            self.bullet.rect.left = self.rect.left + 20
            self.bullet.rect.top = self.rect.bottom - 1
        elif self.dir_x == -1 and self.dir_y == 0:
            self.bullet.rect.right = self.rect.left - 1
            self.bullet.rect.top = self.rect.top + 20
        elif self.dir_x == 1 and self.dir_y == 0:
            self.bullet.rect.left = self.rect.right + 1
            self.bullet.rect.top = self.rect.top + 20

        if self.level == 1:
            self.bullet.speed  = 16
            self.bullet.strong = False
        if self.level == 2:
            self.bullet.speed  = 16
            self.bullet.strong = True
        if self.level == 3:
            self.bullet.speed  = 48
            self.bullet.strong = True


    def levelUp(self):
        if self.level < 2:
            self.level += 1
        if self.level == 0:
            self.tank = self.tank_L0_image
        if self.level == 1:
            self.tank = self.tank_L1_image
        if self.level == 2:
            self.tank = self.tank_L2_image
        if self.level == 3:
            self.tank = self.tank_L2_image

    def levelDown(self):
        if self.level > 0:
            self.level -= 1
        if self.level == 0:
            self.tank = self.tank_L0_image
            self.bullet.speed  = 6
            self.bullet.strong = False
        if self.level == 1:
            self.tank = self.tank_L1_image
        if self.level == 2:
            self.tank = self.tank_L2_image


    def moveUp(self, tankGroup, brickGroup, ironGroup):
        self.rect = self.rect.move(self.speed * 0, self.speed * -1)
        if self.rect.top < 3:
            self.rect = self.rect.move(self.speed * 0, self.speed * 1)
        if pygame.sprite.spritecollide(self, brickGroup, False, None) \
            or pygame.sprite.spritecollide(self, ironGroup, False, None):
            self.rect = self.rect.move(self.speed * 0, self.speed * 1)
        if pygame.sprite.spritecollide(self, tankGroup, False, None):
            self.rect = self.rect.move(self.speed * 0, self.speed * 1)
        self.tank_R0 = self.tank.subsurface((0, 0),(48, 48))
        self.tank_R1 = self.tank.subsurface((48, 0),(48, 48))
        self.dir_x, self.dir_y = 0, -1
    def moveDown(self, tankGroup, brickGroup, ironGroup):
        self.rect = self.rect.move(self.speed * 0, self.speed * 1)
        if self.rect.bottom > 630 - 3:
            self.rect = self.rect.move(self.speed * 0, self.speed * -1)
        if pygame.sprite.spritecollide(self, brickGroup, False, None) \
            or pygame.sprite.spritecollide(self, ironGroup, False, None):
            self.rect = self.rect.move(self.speed * 0, self.speed * -1)
        if pygame.sprite.spritecollide(self, tankGroup, False, None):
            self.rect = self.rect.move(self.speed * 0, self.speed * -1)
        self.tank_R0 = self.tank.subsurface((0, 48),(48, 48))
        self.tank_R1 = self.tank.subsurface((48, 48),(48, 48))
        self.dir_x, self.dir_y = 0, 1
    def moveLeft(self, tankGroup, brickGroup, ironGroup):
        self.rect = self.rect.move(self.speed * -1, self.speed * 0)
        if self.rect.left < 3:
            self.rect = self.rect.move(self.speed * 1, self.speed * 0)
        if pygame.sprite.spritecollide(self, brickGroup, False, None) \
            or pygame.sprite.spritecollide(self, ironGroup, False, None):
            self.rect = self.rect.move(self.speed * 1, self.speed * 0)
        if pygame.sprite.spritecollide(self, tankGroup, False, None):
            self.rect = self.rect.move(self.speed * 1, self.speed * 0)
        self.tank_R0 = self.tank.subsurface((0, 96),(48, 48))
        self.tank_R1 = self.tank.subsurface((48, 96),(48, 48))
        self.dir_x, self.dir_y = -1, 0
    def moveRight(self, tankGroup, brickGroup, ironGroup):
        self.rect = self.rect.move(self.speed * 1, self.speed * 0)
        if self.rect.right > 630 - 3:
            self.rect = self.rect.move(self.speed * -1, self.speed * 0)
        if pygame.sprite.spritecollide(self, brickGroup, False, None) \
            or pygame.sprite.spritecollide(self, ironGroup, False, None):
            self.rect = self.rect.move(self.speed * -1, self.speed * 0)
        if pygame.sprite.spritecollide(self, tankGroup, False, None):
            self.rect = self.rect.move(self.speed * -1, self.speed * 0)
        self.tank_R0 = self.tank.subsurface((0, 144),(48, 48))
        self.tank_R1 = self.tank.subsurface((48, 144),(48, 48))
        self.dir_x, self.dir_y = 1, 0
