import pygame
from Load import *

# This file creates the platform class, which is the platforms that the player
# can move on

class Platform(pygame.sprite.Sprite):
    
    def __init__(self, image):
        super().__init__()
        
        self.image = image # Creates image tile
        
        self.rect = self.image.get_rect() # Gets dimensions of image tile

# Moving Platform from...
# http://programarcadegames.com/python_examples/f.php?file=platform_moving.py
class MovingPlatform(Platform):
    
    def __init__(self, image):
        super().__init__(image)
        
        self.changeX = 0
        self.changeY = 0
        
        self.boundaryTop = 0
        self.boundaryBottom = 0
        self.boundaryRight = 0
        self.boundaryLeft = 0
        
        self.player = None
        self.level = None
    
    def update(self):
        self.rect.x += self.changeX
        
        hit = pygame.sprite.collide_rect(self, self.player)
        
        if hit:
            if self.changeX < 0:
                self.player.rect.right = self.rect.left
            else:
                self.player.rect.left = self.rect.right
        
        self.rect.y += self.changeY
        
        hit = pygame.sprite.collide_rect(self, self.player)
        
        if hit:
            if self.changeY < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom
        
        if self.rect.bottom > self.boundaryBottom or \
                                               self.rect.top < self.boundaryTop:
            self.changeY *= -1
        
        curPos = self.rect.x - self.level.worldShift
        if curPos < self.boundaryLeft or curPos > self.boundaryRight:
            self.changeX *= -1