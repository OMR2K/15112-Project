import pygame

# File that has the Monsters classes in, and the classes are in charge of
# creating the moving monsters in the different levels

class Monster(pygame.sprite.Sprite):
    
    def __init__(self, image):
        super().__init__()
        
        
        self.image = image # Sets starting image
        self.rect = self.image.get_rect() # Get the dimensions of the image
        
        # Loads monster images
        walkR0 = pygame.image.load("monster/R.png")
        walkL0 = pygame.image.load("monster/L.png")
        
        # Scales the monster images to 50x50 pxls
        self.walkR1 = pygame.transform.scale(walkR0, (50,50))
        self.walkL1 = pygame.transform.scale(walkL0, (50,50))
        
        # Loads and scales the image for when the monster dies
        self.deadImage0 = pygame.image.load("monster/D.png")
        self.deadImage = pygame.transform.scale(self.deadImage0, (50,12))
        
        self.walk = [self.walkR1, self.walkL1]
        
        # X Velocity and Y Velocity of the monster
        self.changeX = 0
        self.changeY = 0
        
        # Boundaries the monster can go to
        self.boundaryTop = 0
        self.boundaryBottom = 0
        self.boundaryRight = 0
        self.boundaryLeft = 0
        
        self.level = None
        
        # Checks if the monster is dead or not
        self.dead = False
    
    # Function which moves the monster, and checks boundaries
    def update(self):
        if self.dead == True: # If the monster is dead, move him down
            self.rect.y += self.changeY
        elif self.dead == False: # If the monster is not dead
            self.rect.x += self.changeX # Move him right/left depending on ChangeX
            
            curPosX = self.rect.x - self.level.worldShift # The current X position
            
            # Checks if X position is between the boundaries
            if curPosX < self.boundaryLeft or curPosX > self.boundaryRight:
                self.changeX *= -1
            
            position = self.rect.x + self.level.worldShift # Position of monster
            
            # Changes image of monster depending on where they are in the world
            # (Animating the monster)
            frame = (position // 50) % len(self.walk)
            self.image = self.walk[frame]
    
    # Kills the monster
    def kill(self):
        self.dead = True # The monster is dead
        self.changeX = 0 # The monster stops moving
        self.changeY = 5 # The monster falls down
        self.image = self.deadImage # Change monster image to dead image
        self.rect.y += 50 # Move the monster down

class FlyingMonster(pygame.sprite.Sprite):
    
    def __init__(self, image):
        super().__init__()
        
        # Gets image and dimensions
        self.image = image
        self.rect = self.image.get_rect()
        
        # Loads all the images for the flying monster, and scales them
        flyR10 = pygame.image.load("monster/FR1.png")
        flyR20 = pygame.image.load("monster/FR2.png")
        flyR30 = pygame.image.load("monster/FR3.png")
        
        flyL10 = pygame.image.load("monster/FL1.png")
        flyL20 = pygame.image.load("monster/FL2.png")
        flyL30 = pygame.image.load("monster/FL3.png")
        
        flyR1 = pygame.transform.scale(flyR10, (50,50))
        flyR2 = pygame.transform.scale(flyR20, (50,50))
        flyR3 = pygame.transform.scale(flyR30, (50,50))
        
        flyL1 = pygame.transform.scale(flyL10, (50,50))
        flyL2 = pygame.transform.scale(flyL20, (50,50))
        flyL3 = pygame.transform.scale(flyL30, (50,50))
        
        # Lists for all images (Right and Left)
        self.flyR = [flyR1, flyR2, flyR3]
        self.flyL = [flyL1, flyL2, flyL3]
        
        self.facing = "R" # Where the monster is facing
        
        self.changeX = 0 # X Velocity
        self.changeY = 0 # Y Velocity
        
        # Boundaries where the monster can go between
        self.boundaryTop = 0
        self.boundaryBottom = 0
        self.boundaryRight = 0
        self.boundaryLeft = 0
        
        self.level = None
    
    def update(self):
        
        self.rect.x += self.changeX # Moves flying monster on X axis
        self.rect.y += self.changeY # Moves flying monster on Y axis
        
        curPosX = self.rect.x - self.level.worldShift # Current X position
        curPosY = self.rect.y # Current Y position
        
        # If the monster hits left boundary, change directions
        if curPosX < self.boundaryLeft: 
            self.changeX *= -1
            self.facing = "R"
        # If the monster hits right boundary, change directions
        elif curPosX > self.boundaryRight:
            self.changeX *= -1
            self.facing = "L"
        # If the monster hits top or bottom boundary, change directions
        elif curPosY < self.boundaryTop or curPosY > self.boundaryBottom:
            self.changeY *= -1
        
        # Animating the monster, the same way as the player
        position = self.rect.x + self.level.worldShift
        if self.facing == "R":
            frame = (position // 40) % len(self.flyR)
            self.image = self.flyR[frame]
        elif self.facing == "L":
            frame = (position // 40) % len(self.flyL)
            self.image = self.flyL[frame]