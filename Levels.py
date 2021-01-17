import pygame
import random
from Platforms import *
from Coins import *
from Monsters import *

# Tiles for the levels keys
# Each tile 70 pxl wide

# AR -> Arrow Right
# ES -> Exit Sign
# GR -> Grass Right
# GL -> Grass Left
# GM -> Grass Middle
# TR -> Tree
# TO -> Torch
# BR -> Bridge
# GT -> Gate
# GU -> Gate Up
# PO -> Power Up Block
# LD -> Ladder
# LE -> Ladder End
# ST -> Stone
# CO -> Coins
# PE -> Press E Sign
# SM -> Sand Middle
# SR -> Sand Right
# SL -> Sand Left

screenWidth = 630
screenHeight = 560

def levelCreator(self, x, y, obj):
    if obj == "AR":
        other = Platform(rightArrow) # Creates platform
        other.rect.x = x + 5 # Sets the x value of the sprite
        other.rect.y = y # Sets the y value of the sprite
        other.player = self.player # Sets the player to the same current player
        self.allObjList.add(other) # Adds the sprite to their sprite group
    elif obj == "TO": # Similarly for each one...
        other = Platform(torch)
        other.rect.x = x
        other.rect.y = y
        other.player = self.player
        self.allObjList.add(other)
    elif obj == "ES":
        other = Platform(exitSign)
        other.rect.x = x
        other.rect.y = y
        other.player = self.player
        self.allObjList.add(other)
    elif obj == "LD":
        ladderO = Platform(ladder)
        ladderO.rect.x = x
        ladderO.rect.y = y
        ladderO.player = self.player
        self.ladderList.add(ladderO)
        self.allObjList.add(ladderO)
    elif obj == "LE":
        ladderO = Platform(ladderEnd)
        ladderO.rect.x = x
        ladderO.rect.y = y
        ladderO.player = self.player
        self.ladderList.add(ladderO)
        self.allObjList.add(ladderO)
    elif obj == "GL":
        block = Platform(grassLeft)
        block.rect.x = x
        block.rect.y = y
        block.player = self.player
        self.platformList.add(block)
        self.allObjList.add(block)
    elif obj == "GM":
        block = Platform(grassMiddle)
        block.rect.x = x
        block.rect.y = y
        block.player = self.player
        self.platformList.add(block)
        self.allObjList.add(block)
    elif obj == "GR":
        block = Platform(grassRight)
        block.rect.x = x
        block.rect.y = y
        block.player = self.player
        self.platformList.add(block)
        self.allObjList.add(block)
    elif obj == "BR":
        block = Platform(bridge)
        block.rect.x = x
        block.rect.y = y
        block.player = self.player
        self.platformList.add(block)
        self.allObjList.add(block)
    elif obj == "ST":
        block = Platform(stone)
        block.rect.x = x
        block.rect.y = y
        block.player = self.player
        self.platformList.add(block)
        self.allObjList.add(block)
    elif obj == "CO":
        coin = Coins(start)
        coin.rect.x = x
        coin.rect.y = y
        coin.player = self.player
        self.coinList.add(coin)
        self.allObjList.add(coin)
    elif obj == "GU":
        gate1 = Platform(gateUp)
        gate1.rect.x = x
        gate1.rect.y = y + 35
        gate1.player = self.player
        self.allObjList.add(gate1)
    elif obj == "PE":
        e = Platform(pressE)
        e.rect.x = x
        e.rect.y = y
        e.player = self.player
        self.allObjList.add(e)
    elif obj == "S1":
        sign = Platform(level1Sign)
        sign.rect.x = x
        sign.rect.y = y
        sign.player = self.player
        self.allObjList.add(sign)
    elif obj == "S2":
        sign = Platform(level2Sign)
        sign.rect.x = x
        sign.rect.y = y
        sign.player = self.player
        self.allObjList.add(sign)
    elif obj == "S3":
        sign = Platform(level3Sign)
        sign.rect.x = x
        sign.rect.y = y
        sign.player = self.player
        self.allObjList.add(sign)
    elif obj == "SS":
        sign = Platform(shopSign)
        sign.rect.x = x
        sign.rect.y = y
        sign.player = self.player
        self.allObjList.add(sign)
    elif obj == "SK":
        s = Platform(spike)
        s.rect.x = x
        s.rect.y = y
        s.player = self.player
        self.killList.add(s)
        self.allObjList.add(s)
    elif obj == "TB":
        sign = Platform(toBuySign)
        sign.rect.x = x
        sign.rect.y = y
        sign.player = self.player
        self.allObjList.add(sign)
    elif obj == "WA":
        w = Platform(water)
        w.rect.x = x
        w.rect.y = y
        w.player = self.player
        self.killList.add(w)
        self.allObjList.add(w)
    elif obj == "OG":
        sign = Platform(gateSign)
        sign.rect.x = x
        sign.rect.y = y
        sign.player = self.player
        self.allObjList.add(sign)
    elif obj == "TE":
        sign = Platform(enterSign)
        sign.rect.x = x
        sign.rect.y = y
        sign.player = self.player
        self.allObjList.add(sign)
    elif obj == "DN":
        sign = Platform(doNotSign)
        sign.rect.x = x
        sign.rect.y = y
        sign.player = self.player
        self.allObjList.add(sign)
    elif obj == "Tc":
        sign = Platform(touchSign)
        sign.rect.x = x
        sign.rect.y = y
        sign.player = self.player
        self.allObjList.add(sign)

class Level(object):
    
    def __init__(self, player):
        
        self.worldShift = 0 # The amount that the world has shifted
        self.player = player # The player
        
        self.background = None # Background of level
        
        self.isLvl2Locked = True # Checks if level2 is locked
        self.isLvl3Locked = True # Checks if lvel3 is locked
        
        # Setting up sprite groups for all different kinds of sprites
        self.allObjList = pygame.sprite.Group() # All objects group
        
        self.platformList = pygame.sprite.Group() # Platforms list
        self.ladderList = pygame.sprite.Group() # Ladders that you climb
        self.coinList = pygame.sprite.Group() # Coins to collect
        
        self.howToPlayList = pygame.sprite.Group() # How to play gate
        self.shopList = pygame.sprite.Group() # Shop gate
        
        self.buyHealthList = pygame.sprite.Group() # Buy HP list
        self.buyJumpList = pygame.sprite.Group() # Buy double jump list
        
        self.buyNadimMask = pygame.sprite.Group() # Buy Nadim mask list
        self.buySamarMask = pygame.sprite.Group() # Buy Samar mask list
        self.buyOmarMask = pygame.sprite.Group() # Buy Omar mask list
        self.buyYusufMask = pygame.sprite.Group() # Buy Yusuf mask list
        
        # List that cointains sprites that kills the player
        self.killList = pygame.sprite.Group()
        self.monsterList = pygame.sprite.Group()
        
        # Lists that cointain gates for each level 
        self.lvl1List = pygame.sprite.Group()
        self.lvl2List = pygame.sprite.Group()
        self.lvl3List = pygame.sprite.Group()
        self.lvl4List = pygame.sprite.Group()
        
        # Lists that contain gates for winning a level
        self.lvl1Win = pygame.sprite.Group()
        self.lvl2Win = pygame.sprite.Group()
        self.lvl3Win = pygame.sprite.Group()
        
        # List that cointains sign at the end of level 4, which if you collide
        # with, you win the game
        self.winSign = pygame.sprite.Group()
    
    # Function that updates all objects
    def update(self):
        self.allObjList.update()
    
    # Draws the background
    def draw(self, screen):
        screen.blit(self.background, (self.worldShift // 3, 0))
    
    # Functions that shifts the world
    def shiftWorld(self, shiftX):
        # Shifts the screen
        self.worldShift += shiftX
        
        # Shifts the objects
        for o in self.allObjList:
            o.rect.x += shiftX

class Hub(Level):
    
    def __init__(self, player):
        Level.__init__(self, player)
        
        # The hub background
        self.backgroundO = pygame.image.load("bg.jpeg")
        self.background = pygame.transform.rotozoom(self.backgroundO, 0, 2)
        
        # The hub tiles
        self.level = [
["ST","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","ST"],
["ST","  ","  ","  ","  ","  ","GU","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","ST"],
["ST","  ","  ","  ","  ","SS","SP","SS","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","ST"],
["ST","  ","  ","  ","LE","GL","GM","GR","LE","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","ST"],
["ST","  ","  ","  ","LD","  ","  ","  ","LD","  ","PE","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","ST"],
["ST","  ","  ","  ","LD","  ","GU","  ","LD","  ","OG","  ","GU","  ","  ","GU","  ","  ","GU","  ","  ","GU","  ","ST"],
["ST","  ","  ","  ","LD","HT","HW","HT","LD","  ","TE","S1","L1","  ","S2","L2","  ","S3","L3","  ","S4","L4","  ","ST"],
["ST","GL","GM","GM","GM","GM","GM","GM","GM","GM","GM","GM","GM","GM","GM","GM","GM","GM","GM","GM","GM","GM","GR","ST"]
                                                                                                                    ]
        
        x = 0
        y = 0
        
        # Adds all tiles to their sprite group, with their x, y location
        for row in self.level:
            for obj in row:
                
                levelCreator(self, x, y, obj)
                
                if obj == "HW":
                    howToPlay = Platform(gate)
                    howToPlay.rect.x = x
                    howToPlay.rect.y = y
                    howToPlay.player = self.player
                    self.howToPlayList.add(howToPlay)
                    self.allObjList.add(howToPlay)
                elif obj == "SP":
                    shop = Platform(gate)
                    shop.rect.x = x
                    shop.rect.y = y
                    shop.player = self.player
                    self.shopList.add(shop)
                    self.allObjList.add(shop)
                elif obj == "L1":
                    lvl = Platform(gate)
                    lvl.rect.x = x
                    lvl.rect.y = y
                    lvl.player = self.player
                    self.lvl1List.add(lvl)
                    self.allObjList.add(lvl)
                elif obj == "L2":
                    lvl = Platform(gate)
                    lvl.rect.x = x
                    lvl.rect.y = y
                    lvl.player = self.player
                    self.lvl2List.add(lvl)
                    self.allObjList.add(lvl)
                elif obj == "L3":
                    lvl = Platform(gate)
                    lvl.rect.x = x
                    lvl.rect.y = y
                    lvl.player = self.player
                    self.lvl3List.add(lvl)
                    self.allObjList.add(lvl)
                elif obj == "HT":
                    sign = Platform(howToPlaySign)
                    sign.rect.x = x
                    sign.rect.y = y
                    sign.player = self.player
                    self.allObjList.add(sign)
                elif obj == "L4":
                    lvl = Platform(gate)
                    lvl.rect.x = x
                    lvl.rect.y = y
                    lvl.player = self.player
                    self.lvl4List.add(lvl)
                    self.allObjList.add(lvl)
                elif obj == "S4":
                    sign = Platform(level4Sign)
                    sign.rect.x = x
                    sign.rect.y = y
                    self.allObjList.add(sign)
                x += 70
            y += 70
            x = 0

class Level_1(Level):
    
    def __init__(self, player):
        Level.__init__(self, player)
        
        # Background of level1
        self.backgroundO = pygame.image.load("bg.jpeg")
        self.background = pygame.transform.rotozoom(self.backgroundO, 0, 2)
        
        # Level1 tiles
        self.level = [
        ["ST","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","ST"],
        ["ST","  ","  ","  ","  ","  ","LE","  ","  ","  ","CO","CO","  ","  ","  ","  ","  ","  ","  ","  ","  ","ST"],
        ["ST","  ","  ","  ","  ","  ","LD","SK","AR","CO","  ","  ","CO","  ","CO","SK","  ","CO","  ","  ","  ","ST"],
        ["ST","  ","  ","  ","  ","  ","LD","GL","GM","GM","BR","BR","BR","BR","GM","GR","  ","  ","CO","  ","  ","ST"],
        ["ST","  ","  ","  ","  ","  ","LD","ST","WA","WA","WA","WA","WA","WA","WA","ST","  ","  ","CO","  ","  ","ST"],
        ["ST","  ","S1","  ","  ","  ","LD","ST","WA","WA","WA","WA","WA","WA","WA","ST","  ","  ","GU","  ","  ","ST"],
        ["ST","TO","AR","  ","GL","GM","GR","ST","WA","WA","WA","WA","WA","WA","WA","ST","  ","PE","GT","  ","  ","ST"],
        ["ST","GL","GM","GM","GM","GM","GM","GM","GM","GM","GM","GM","GM","GM","GM","GM","GM","GM","GM","GM","GR","ST"]
                                                                                                                        ]
        
        x = 0
        y = 0
        
        # Adds all tiles to their sprite group, with their x, y location
        for row in self.level:
            for obj in row:
                
                levelCreator(self, x, y, obj)
                
                if obj == "GT":
                    gate1 = Platform(gate)
                    gate1.rect.x = x
                    gate1.rect.y = y
                    gate1.player = self.player
                    self.lvl1Win.add(gate1)
                    self.allObjList.add(gate1)
                elif obj == "WA":
                    block = Platform(water)
                    block.rect.x = x
                    block.rect.y = y
                    block.player = self.player
                    self.platformList.add(block)
                    self.allObjList.add(block)
                
                x += 70
            y += 70
            x = 0
        
        monster = Monster(monsterR)
        monster.rect.x = 565
        monster.rect.y = 160
        monster.boundaryLeft = 565
        monster.boundaryRight = 980
        monster.changeX = 5
        monster.player = self.player
        monster.level = self
        self.monsterList.add(monster)
        self.allObjList.add(monster)
    
class Level_2(Level):
    def __init__(self, player):
        Level.__init__(self, player)
        
        # Background of level2
        self.backgroundO = pygame.image.load("bg.jpeg")
        self.background = pygame.transform.rotozoom(self.backgroundO, 0, 2)
        
        # Level2 tiles        
        self.level = [
        ["ST","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","ST"],
        ["ST","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","CO","  ","  ","  ","  ","  ","GU","  ","ST"],
        ["ST","  ","  ","  ","  ","CO","  ","LD","CO","  ","  ","  ","LE","  ","  ","  ","  ","  ","GT","  ","ST"],
        ["ST","  ","  ","  ","  ","LD","CO","  ","  ","CO","  ","  ","LD","  ","  ","  ","  ","GL","GM","GR","ST"],
        ["ST","  ","  ","  ","CO","LD","  ","  ","  ","  ","  ","  ","LD","  ","  ","  ","  ","  ","  ","  ","ST"],
        ["ST","  ","S2","  ","LD","CO","  ","  ","  ","  ","LD","  ","CO","  ","  ","  ","  ","  ","  ","  ","ST"],
        ["ST","TO","AR","  ","LD","  ","  ","  ","  ","  ","LD","  ","  ","  ","  ","  ","  ","  ","  ","  ","ST"],
        ["ST","GL","GM","GM","SK","SK","SK","SK","SK","SK","SK","SK","SK","SK","SK","SK","SK","SK","SK","SK","ST"]
                                                                                                                        ]
        
        x = 0
        y = 0
        
        # Adds all tiles to their sprite group, with their x, y location
        for row in self.level:
            for obj in row:
                
                levelCreator(self, x, y, obj)
                
                if obj == "GT":
                    gate1 = Platform(gate)
                    gate1.rect.x = x
                    gate1.rect.y = y
                    gate1.player = self.player
                    self.lvl2Win.add(gate1)
                    self.allObjList.add(gate1)
                
                x += 70
            y += 70
            x = 0
        
        block = MovingPlatform(grassMiddle)
        block.rect.x = 1050
        block.rect.y = 210
        block.boundaryTop = 210
        block.boundaryBottom = 490
        block.changeY = 3
        block.player = self.player
        block.level = self
        self.platformList.add(block)
        self.allObjList.add(block)
        
        monster = FlyingMonster(flyMonsR)
        monster.rect.x = 280
        monster.rect.y = 210
        monster.boundaryLeft = 280
        monster.boundaryRight = 1050
        monster.boundaryTop = 70
        monster.boundaryBottom = 420
        monster.changeX = random.randint(5,10)
        monster.changeY = random.randint(5,10)
        monster.player = self.player
        monster.level = self
        self.monsterList.add(monster)
        self.allObjList.add(monster)

class Level_3(Level):
    
    def __init__(self, player):
        Level.__init__(self, player)
        
        # Background of level3
        self.backgroundO = pygame.image.load("bg.jpeg")
        self.background = pygame.transform.rotozoom(self.backgroundO, 0, 2)
        
        # Level3 tiles
        self.level = [
        ["ST", "  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","ST"],
        ["ST", "  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","ST"],
        ["ST", "  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","ST"],
        ["ST", "  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","CO","  ","  ","  ","  ","  ","  ","ST"],
        ["ST", "  ","  ","  ","  ","  ","  ","  ","  ","LD","CO","CO","LD","CO","  ","  ","  ","  ","  ","  ","ST"],
        ["ST", "  ","S3","  ","  ","  ","  ","  ","  ","CO","  ","LD","SK","  ","  ","  ","  ","  ","GU","  ","ST"],
        ["ST", "TO","AR","  ","  ","SK","  ","  ","  ","SK","  ","  ","ST","  ","  ","  ","SK","  ","GT","  ","ST"],
        ["ST", "GL","GM","GM","GM","GM","WA","WA","WA","WA","WA","WA","WA","WA","WA","WA","WA","GM","GM","GR","ST"]
                                                                                                                        ]
        
        x = 0
        y = 0
        
        # Adds all tiles to their sprite group, with their x, y location
        for row in self.level:
            for obj in row:
                
                levelCreator(self, x, y, obj)
                
                if obj == "WA":
                    w = Platform(water)
                    w.rect.x = x
                    w.rect.y = y
                    w.player = self.player
                    self.killList.add(w)
                    self.allObjList.add(w)
                elif obj == "GT":
                    gate1 = Platform(gate)
                    gate1.rect.x = x
                    gate1.rect.y = y
                    gate1.player = self.player
                    self.lvl3Win.add(gate1)
                    self.allObjList.add(gate1)
                
                x += 70
            y += 70
            x = 0
        
        block = MovingPlatform(grassMiddle)
        block.rect.x = 980
        block.rect.y = 490
        block.boundaryLeft = 420
        block.boundaryRight = 1120
        block.changeX = 7
        block.player = self.player
        block.level = self
        self.platformList.add(block)
        self.allObjList.add(block)
        
        monster = Monster(monsterR)
        monster.rect.x = 500
        monster.rect.y = 440
        monster.boundaryLeft = 420
        monster.boundaryRight = 1120
        monster.changeX = 8
        monster.player = self.player
        monster.level = self
        self.monsterList.add(monster)
        self.allObjList.add(monster)
    
class Level_4(Level):
    
    def __init__(self, player):
        Level.__init__(self, player)
        
        # Background of level4
        self.backgroundO = pygame.image.load("bg.jpeg")
        self.background = pygame.transform.rotozoom(self.backgroundO, 0, 2)
        
        # Level4 tiles
        self.level = [
["ST","  ","  ","LD","LD","SW","LD","SW","LD","SW","LD","LD","LD","SW","LD","LD","LD","SW","LD","SW","LD","  ","  ","ST"],
["ST","  ","  ","LD","LD","SW","LD","LD","LD","SW","LD","LD","LD","SW","LD","LD","LD","SW","LD","LD","LD","  ","  ","ST"],
["ST","  ","  ","LD","LD","SW","LD","LD","LD","SW","LD","SW","LD","SW","LD","SW","LD","SW","LD","LD","SW","  ","  ","ST"],
["ST","  ","  ","LD","LD","LD","LD","SW","LD","SW","LD","SW","LD","SW","LD","SW","LD","LD","LD","SW","SW","  ","  ","ST"],
["ST","  ","  ","LD","LD","LD","LD","SW","LD","SW","LD","SW","LD","SW","LD","SW","LD","LD","SW","LD","SW","  ","  ","ST"],
["ST","  ","S4","LD","LD","SW","LD","SW","LD","LD","LD","SW","LD","LD","LD","SW","LD","SW","LD","LD","SW","  ","  ","ST"],
["ST","TO","AR","LD","LD","SW","LD","SW","LD","LD","SW","SW","LD","LD","SW","LD","LD","SW","LD","LD","SW","  ","CS","ST"],
["ST","GL","GM","WA","WA","WA","WA","WA","WA","WA","WA","WA","WA","WA","WA","WA","WA","WA","WA","WA","WA","GM","GR","ST"]
                                                                                                                        ]
        
        # self.level = [
        # ["ST","  ","  ","  ","  ","  ","  ","  ","ST"],
        # ["ST","  ","  ","  ","  ","  ","  ","  ","ST"],
        # ["ST","  ","  ","  ","  ","  ","  ","  ","ST"],
        # ["ST","  ","  ","  ","  ","  ","  ","  ","ST"],
        # ["ST","  ","  ","  ","  ","  ","  ","  ","ST"],
        # ["ST","  ","  ","  ","  ","  ","  ","  ","ST"],
        # ["ST","  ","  ","  ","  ","  ","CS","  ","ST"],
        # ["ST","GL","GM","GM","GM","GM","GM","GR","ST"]
        #                                                 ]
        
        x = 0
        y = 0
        
        # Adds all tiles to their sprite group, with their x, y location
        for row in self.level:
            for obj in row:
                
                levelCreator(self, x, y, obj)
                
                if obj == "CS":
                    sign = Platform(congratsSign)
                    sign.rect.x = x
                    sign.rect.y = y
                    sign.player = self.player
                    self.winSign.add(sign)
                    self.allObjList.add(sign)
                elif obj == "SW":
                    spike = Platform(spikeWall)
                    spike.rect.x = x
                    spike.rect.y = y
                    self.killList.add(spike)
                    self.allObjList.add(spike)
                elif obj == "S4":
                    sign = Platform(level4Sign)
                    sign.rect.x = x
                    sign.rect.y = y
                    self.allObjList.add(sign)
                x += 70
            y += 70
            x = 0

class HowToPlay(Level):
    
    def __init__(self, player):
        Level.__init__(self, player)
        
        # Background of How To Play
        self.backgroundO = pygame.image.load("bg.jpeg")
        self.background = pygame.transform.rotozoom(self.backgroundO, 0, 2)
        
        # How To Play tiles
        self.level = [
        ["ST","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","ST"],
        ["ST","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","ST"],
        ["ST","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","ST"],
        ["ST","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","LE","  ","  ","  ","  ","  ","  ","  ","  ","  ","ST"],
        ["ST","  ","  ","  ","  ","DN","Tc","  ","  ","  ","  ","LD","  ","  ","  ","  ","  ","  ","  ","  ","  ","ST"],
        ["ST","  ","TM","  ","  ","GM","GM","  ","  ","  ","PS","LD","  ","  ","CC","  ","  ","  ","  ","PH","  ","ST"],
        ["ST","TO","AR","  ","GM","SK","WA","GM","  ","  ","TC","LD","  ","  ","TB","  ","CO","  ","  ","TH","  ","ST"],
        ["ST","GL","GM","GM","GM","GM","GM","GM","GM","GM","GM","GM","GM","GM","GM","GM","GM","GM","GM","GM","GR","ST"]
                                                                                                                        ]
        
        # PS -> Press Space Sign
        # TC -> To Climb
        # TM -> Arrows To Move Sign
        # OG -> On Gate Sign
        # TE -> To Enter Sign
        # CC -> Collect Coins Sign
        # TB -> To Buy Sign
        # PH -> Press H Sign
        # TH -> To Go To Hub Sign
        
        x = 0
        y = 0
        
        # Adds all tiles to their sprite group, with their x, y location
        for row in self.level:
            for obj in row:
                
                levelCreator(self, x, y, obj)
                
                if obj == "PS":
                    sign = Platform(pressSpaceSign)
                    sign.rect.x = x
                    sign.rect.y = y
                    sign.player = self.player
                    self.allObjList.add(sign)
                elif obj == "TC":
                    sign = Platform(climbSign)
                    sign.rect.x = x
                    sign.rect.y = y
                    sign.player = self.player
                    self.allObjList.add(sign)
                elif obj == "TM":
                    sign = Platform(arrowsSign)
                    sign.rect.x = x
                    sign.rect.y = y
                    sign.player = self.player
                    self.allObjList.add(sign)
                elif obj == "CC":
                    sign = Platform(collectCoinsSign)
                    sign.rect.x = x
                    sign.rect.y = y
                    sign.player = self.player
                    self.allObjList.add(sign)
                elif obj == "PH":
                    sign = Platform(pressHSign)
                    sign.rect.x = x
                    sign.rect.y = y
                    sign.player = self.player
                    self.allObjList.add(sign)
                elif obj == "TH":
                    sign = Platform(goToHubSign)
                    sign.rect.x = x
                    sign.rect.y = y
                    sign.player = self.player
                    self.allObjList.add(sign)
                x += 70
            y += 70
            x = 0

class Shop(Level):
    
    def __init__(self, player):
        Level.__init__(self, player)
        
        # Background of shop
        self.backgroundO = pygame.image.load("bg.jpeg")
        self.background = pygame.transform.rotozoom(self.backgroundO, 0, 2)
        
        # Shop tiles
        self.level = [
["ST","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","ST"],
["ST","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","ST"],
["ST","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","ST"],
["ST","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","ST"],
["ST","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","ST"],
["ST","  ","SS","Pb","  ","HP","  ","  ","JP","  ","  ","  ","NM","  ","  ","  ","SM","  ","  ","  ","YM","  ","ST"],
["ST","TO","AR","TB","  ","PH","  ","  ","PP","  ","  ","  ","PM","  ","  ","  ","PB","  ","  ","  ","YB","  ","ST"],
["ST","GL","GM","GM","GM","GM","GM","GM","GM","GM","GM","GM","GM","GM","GM","GM","GM","GM","GM","GM","GM","GR","ST"]
                                                                                                                    ]
        
        x = 0
        y = 0
        
        # Adds all tiles to their sprite group, with their x, y location
        for row in self.level:
            for obj in row:
                
                levelCreator(self, x, y, obj)
                
                if obj == "HP":
                    power = Platform(heart)
                    power.rect.x = x + 10
                    power.rect.y = y + 10
                    power.player = self.player
                    self.buyHealthList.add(power)
                    self.allObjList.add(power)
                elif obj == "JP":
                    power = Platform(boots)
                    power.rect.x = x
                    power.rect.y = y
                    power.player = self.player
                    self.buyJumpList.add(power)
                    self.allObjList.add(power)
                elif obj == "PH":
                    block = Platform(powerUpBlock)
                    block.rect.x = x
                    block.rect.y = y
                    block.player = self.player
                    self.buyHealthList.add(block)
                    self.allObjList.add(block)
                elif obj == "PP":
                    block = Platform(powerUpBlock)
                    block.rect.x = x
                    block.rect.y = y
                    block.player = self.player
                    self.buyJumpList.add(block)
                    self.allObjList.add(block)
                elif obj == "PM":
                    block = Platform(powerUpBlock)
                    block.rect.x = x
                    block.rect.y = y
                    block.player = self.player
                    self.buyNadimMask.add(block)
                    self.allObjList.add(block)
                elif obj == "NM":
                    mask = Platform(nadim)
                    mask.rect.x = x
                    mask.rect.y = y
                    mask.player = self.player
                    self.buyNadimMask.add(mask)
                    self.allObjList.add(mask)
                elif obj == "PB":
                    block = Platform(powerUpBlock)
                    block.rect.x = x
                    block.rect.y = y
                    block.player = self.player
                    self.buySamarMask.add(block)
                    self.allObjList.add(block)
                elif obj == "SM":
                    mask = Platform(samar)
                    mask.rect.x = x
                    mask.rect.y = y
                    mask.player = self.player
                    self.buySamarMask.add(mask)
                    self.allObjList.add(mask)
                elif obj == "Pb":
                    sign = Platform(pressBSign)
                    sign.rect.x = x
                    sign.rect.y = y
                    sign.player = self.player
                    self.allObjList.add(sign)
                elif obj == "YB":
                    block = Platform(powerUpBlock)
                    block.rect.x = x
                    block.rect.y = y
                    block.player = self.player
                    self.buyYusufMask.add(block)
                    self.allObjList.add(block)
                elif obj == "YM":
                    mask = Platform(yusuf)
                    mask.rect.x = x
                    mask.rect.y = y
                    mask.player = self.player
                    self.buyYusufMask.add(mask)
                    self.allObjList.add(mask)
                x += 70
            y += 70
            x = 0

class GameOver(Level):
    
    def __init__(self, player):
        Level.__init__(self, player)
        
        # Background of game over
        self.backgroundO = pygame.image.load("bg.jpeg")
        self.background = pygame.transform.rotozoom(self.backgroundO, 0, 2)
        
        # gameover tiles
        self.level = [
        ["ST","  ","  ","  ","  ","  ","  ","  ","ST"],
        ["ST","  ","  ","  ","  ","  ","  ","  ","ST"],
        ["ST","  ","  ","  ","  ","  ","  ","  ","ST"],
        ["ST","  ","  ","  ","  ","  ","  ","  ","ST"],
        ["ST","  ","  ","  ","  ","  ","  ","  ","ST"],
        ["ST","  ","  ","  ","  ","  ","  ","  ","ST"],
        ["ST","  ","  ","  ","  ","  ","  ","  ","ST"],
        ["ST","GL","GM","GM","GM","GM","GM","GR","ST"]
                                                        ]
        
        x = 0
        y = 0
        
        # Adds all tiles to their sprite group, with their x, y location
        for row in self.level:
            for obj in row:
                
                levelCreator(self, x, y, obj)
                
                x += 70
            y += 70
            x = 0

class Win(Level):
    
    def __init__(self, player):
        Level.__init__(self, player)
        
        # Background of game over
        self.backgroundO = pygame.image.load("bg.jpeg")
        self.background = pygame.transform.rotozoom(self.backgroundO, 0, 2)
        
        # win tiles
        self.level = [
        ["ST","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","ST"],
        ["ST","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","ST"],
        ["ST","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","ST"],
        ["ST","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","ST"],
        ["ST","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","ST"],
        ["ST","  ","  ","CO","  ","CO","  ","CO","  ","CO","  ","OM","  ","ST"],
        ["ST","  ","CO","  ","CO","  ","CO","  ","CO","  ","CO","PO","  ","ST"],
        ["ST","GL","GM","GM","GM","GM","GM","GM","GM","GM","GM","GM","GR","ST"]
                                                                                                                    ]
        
        x = 0
        y = 0
        
        # Adds all tiles to their sprite group, with their x, y location
        for row in self.level:
            for obj in row:
                
                levelCreator(self, x, y, obj)
                
                if obj == "PO":
                    block = Platform(powerUpBlock)
                    block.rect.x = x
                    block.rect.y = y
                    block.player = self.player
                    self.buyOmarMask.add(block)
                    self.allObjList.add(block)
                elif obj == "OM":
                    mask = Platform(omar)
                    mask.rect.x = x
                    mask.rect.y = y
                    mask.player = self.player
                    self.buyOmarMask.add(mask)
                    self.allObjList.add(mask)
                
                x += 70
            y += 70
            x = 0