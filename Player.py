import pygame
from playsound import playsound
from Platforms import *
from Levels import *

pygame.init()

jumpSound = pygame.mixer.Sound("sounds/jump.wav")
oofSound = pygame.mixer.Sound("sounds/OOF.wav")
collectCoin = pygame.mixer.Sound("sounds/coin.wav")

class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        
        self.changeX = 0
        self.changeY = 0
        
        self.facing = "R"
        self.level = None # Level objects (Platforms)
        
        self.image = pygame.image.load("char/R1.png") # Starting image
        self.rect = self.image.get_rect() # Dimensions of image
        self.rect.width = 30 # Set the width of image to 30 for smaller hitbox
        self.rect.height = 50 # Set the height of image to 55 for smaller hitbox
        self.coins = 0 # The amount of coins the player has
        
        self.hp = 3 # Health of player
        self.doubleJump = 0 # Amount of double jumps you have left
        
        self.gameOver = False
        self.win = False
        
        # How many times a double jump has been used while in air
        self.doubleJumpCnt = 0
        
        # Counts how many jumps we had, so we know when a double jump is allowed
        self.jumpCount = 0 
        
        self.lvl2Lock = True # Locks level2
        self.lvl3Lock = True # Locks level3
        self.lvl4Lock = True # Locks level4
        
        self.samar = False # Checks if Samar mask has been bought
        self.nadim = False # Checks if Nadim mask has been bought
        self.omar = False # Checks if Omar mask has been bought
        self.yusuf = False # Checks if Yusuf mask has been bought
        
        self.nadimMask = False # Checks if Nadim mask is equipped
        self.samarMask = False # Checks if Samar mask is equipped
        self.omarMask = False # Checks if Omar mask is equipped
        self.yusufMask = False # Checks if Yusuf mask is equipped
        
        # Walking Right animations
        self.walkR = [
                        pygame.image.load("char/R1.png"),
                        pygame.image.load("char/R2.png"),
                        pygame.image.load("char/R3.png"),
                        pygame.image.load("char/R4.png"),
                        pygame.image.load("char/R5.png"),
                        pygame.image.load("char/R6.png"),
                        pygame.image.load("char/R7.png"),
                        pygame.image.load("char/R8.png"),
                        pygame.image.load("char/R9.png")
                                                        ]
        
        # Walking left animations
        self.walkL = [
                        pygame.image.load("char/L1.png"),
                        pygame.image.load("char/L2.png"),
                        pygame.image.load("char/L3.png"),
                        pygame.image.load("char/L4.png"),
                        pygame.image.load("char/L5.png"),
                        pygame.image.load("char/L6.png"),
                        pygame.image.load("char/L7.png"),
                        pygame.image.load("char/L8.png"),
                        pygame.image.load("char/L9.png")
                                                        ]
    
    # Updates the player
    def update(self):
        
        self.gravity() # Pulls the player down if not on ground
        
        self.rect.x += self.changeX # Adds the changeX to player x position
        
        # Finds position of player in the world
        position = self.rect.x + self.level.worldShift
        
        # The animation for the player depending if they are moving left or right
        # and where they are in the level
        if self.facing == "R":
            frame = (position // 10) % len(self.walkR)
            self.image = self.walkR[frame]
        elif self.facing == "L":
            frame = (position // 10) % len(self.walkL)
            self.image = self.walkL[frame]
        
        # Checks the player for collisions with platforms
        blockHit = pygame.sprite.spritecollide(self, self.level.platformList, \
                                                                          False)
        
        # Goes through the collisions list and does not allow the move
        for b in blockHit:
            
            # If player going right, and collides, sets right side of player to
            # left side of block, to stop movement
            if self.changeX > 0:
                self.rect.right = b.rect.left
            # Elif player going left, and collides, set left side of player to
            # right side of block, to stop movement
            elif self.changeX < 0:
                self.rect.left = b.rect.right
        
        # Does the same thing as x axis, but for y axis
        self.rect.y += self.changeY
        
        blockHit = pygame.sprite.spritecollide(self, self.level.platformList, \
                                                                          False)
        
        for b in blockHit:
            
            if self.changeY > 0:
                self.rect.bottom = b.rect.top
            elif self.changeY < 0:
                self.rect.top = b.rect.bottom
    
    # SOME OF "Gavity and Jump" Functions from...
    # http://programarcadegames.com/python_examples/f.php?file=platform_moving.py
    # Most of them I have written
    
    # Function that creates the gravity in the game
    def gravity(self):
        
        if self.changeY == 0:
            self.changeY = 1
        else:
            self.changeY += 0.5
        
        if self.rect.y >= screenHeight - self.rect.height and self.changeY >= 0:
            self.changeY = 0
            self.rect.y = screenHeight - self.rect.height
        
        d = ((screenHeight - (self.rect.y + self.rect.height))**2)**0.5
        
        collision = pygame.sprite.spritecollide(self, self.level.platformList, \
                                                                          False)
        
        if len(collision) > 0:
            self.changeY = 0
            self.rect.y = screenHeight - self.rect.height - d - 70
    
    # Function that allow the player to jump
    def jump(self):
        
        self.rect.y += 4 
        platformList = pygame.sprite.spritecollide(self, \
                                                self.level.platformList, False)
        self.rect.y -= 4
        
        if len(platformList) > 0 or self.rect.bottom >= screenHeight:
            jumpSound.play()
            self.changeY = -10
            self.jumpCount += 1
        
        if self.doubleJump > 0 and self.jumpCount % 2 == 0 and \
                                                        self.doubleJumpCnt == 0:
            jumpSound.play()
            self.doubleJumpCnt += 1
            self.doubleJump -= 1
            self.changeY = -10
            if self.doubleJumpCnt > 1:
                self.changeY = +10
        
        if self.onGround():
            self.doubleJumpCnt = 0
        
        self.jumpCount = 0
    
    # Function that checks if the player is on the ground
    def onGround(self):
        
        self.rect.y += 4 
        platformList = pygame.sprite.spritecollide(self, \
                                                self.level.platformList, False)
        self.rect.y -= 4
        
        if len(platformList) > 0:
            return True
        return False
    
    # Function that allows the player to climb a ladder, if they are colliding
    # with one
    def climbLadder(self):
        
        # Collision between player and ladder
        ladderList = pygame.sprite.spritecollide(self, self.level.ladderList, \
                                                                          False)
        
        if len(ladderList) > 0: # If there is collision, climb
            self.changeY = -4
    
    # Function that allows the player to collect coins
    def collectCoin(self):
        
        # Collision between player and coin, and deletes from sprite group
        coinList = pygame.sprite.spritecollide(self, self.level.coinList, True)
        
        if len(coinList) > 0: # If there is collision, increase 
            collectCoin.play() # Plays the collect coin sound
            self.coins += len(coinList) # Increase amount of coins player has
    
    def changeLevel(self, currentLvlN):
        
        # Checks collision between player and all different gates
        lvl1Win = pygame.sprite.spritecollide(self, self.level.lvl1Win, False)
        lvl2Win = pygame.sprite.spritecollide(self, self.level.lvl2Win, False)
        lvl3Win = pygame.sprite.spritecollide(self, self.level.lvl3Win, False)
        lvl1 = pygame.sprite.spritecollide(self, self.level.lvl1List, False)
        lvl2 = pygame.sprite.spritecollide(self, self.level.lvl2List, False)
        lvl3 = pygame.sprite.spritecollide(self, self.level.lvl3List, False)
        lvl4 = pygame.sprite.spritecollide(self, self.level.lvl4List, False)
        howToPlay = pygame.sprite.spritecollide(self, self.level.howToPlayList, 
                                                                          False)
        shop = pygame.sprite.spritecollide(self, self.level.shopList, False)
        
        # If there is collision, change level and location accordingly
        if len(lvl1) > 0:
            currentLvlN = 1
            self.rect.x = 75 + self.level.worldShift
            self.rect.y = 25
        elif len(lvl2) > 0 and self.lvl2Lock == False:
            currentLvlN = 2
            self.rect.x = 75 + self.level.worldShift
            self.rect.y = 25
        elif len(lvl3) > 0 and self.lvl3Lock == False:
            currentLvlN = 3
            self.rect.x = 75 + self.level.worldShift
            self.rect.y = 25
        elif len(lvl4) > 0 and self.lvl4Lock == False:
            currentLvlN = 4
            self.rect.x = 75 + self.level.worldShift
            self.rect.y = 25
        elif len(howToPlay) > 0:
            currentLvlN = 5
            self.rect.x = 75 + self.level.worldShift
            self.rect.y = 25
        elif len(shop) > 0:
            currentLvlN = 6
            self.rect.x = 75 + self.level.worldShift
            self.rect.y = 25
        elif len(lvl1Win) > 0:
            currentLvlN = 2
            self.rect.x = 75 + self.level.worldShift
            self.rect.y = 25
            self.lvl2Lock = False
        elif len(lvl2Win) > 0:
            currentLvlN = 3
            self.rect.x = 75 + self.level.worldShift
            self.rect.y = 25
            self.lvl3Lock = False
        elif len(lvl3Win) > 0:
            currentLvlN = 4
            self.rect.x = 75 + self.level.worldShift
            self.rect.y = 25
            self.lvl4Lock = False
        
        return currentLvlN
    
    # Function that buys items from the shop
    def buy(self):
        
        # Checks collision between player and item shops
        hpShop = pygame.sprite.spritecollide(self, self.level.buyHealthList, \
                                                                          False)
        jumpShop = pygame.sprite.spritecollide(self, self.level.buyJumpList, \
                                                                          False)
        samarShop = pygame.sprite.spritecollide(self, self.level.buySamarMask, \
                                                                          False)
        nadimShop = pygame.sprite.spritecollide(self, self.level.buyNadimMask, \
                                                                          False)
        omarShop = pygame.sprite.spritecollide(self, self.level.buyOmarMask, \
                                                                          False)
        yusufShop = pygame.sprite.spritecollide(self, self.level.buyYusufMask, \
                                                                          False)
        
        # If there is collision, and they press "b", 
        # buy the item and decrease coins
        if len(hpShop) > 0:
            if self.coins >= 2 and self.hp < 5:
                self.hp += 1
                self.coins -= 2
        elif len(jumpShop) > 0:
            if self.coins >= 2 and self.doubleJump < 3:
                self.doubleJump += 1
                self.coins -= 2
        elif len(samarShop) > 0 and self.samar == False:
            if self.coins >= 5:
                self.samar = True
                self.coins -= 5
        elif len(nadimShop) > 0 and self.nadim == False:
            if self.coins >= 5:
                self.nadim = True
                self.coins -= 5
        elif len(omarShop) > 0 and self.omar == False:
            if self.coins >= 5:
                self.omar = True
                self.coins -= 5
        elif len(yusufShop) > 0 and self.yusuf == False:
            if self.coins >= 5:
                self.yusuf = True
                self.coins -= 5
    
    # Function that kills the player
    def kill(self):
        self.hp -= 1
    
    # Function that moves the player to the right
    def right(self):
        self.changeX = 8
        self.facing = "R"
    
    # Function that moves the player to the left
    def left(self):
        self.changeX = -8
        self.facing = "L"
    
    # Function that stops the player from moving
    def stop(self):
        self.changeX = 0