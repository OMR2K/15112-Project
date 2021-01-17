import pygame

# File which creates the coins which can be collected and you can purchase
# different things using the coins

# Loads the starting image of the coin
start = pygame.transform.scale(pygame.image.load("coins/coin1.png"), (32,32))

# Loads the other images of the coin (Spinning animation)
spin = [
pygame.transform.scale(pygame.image.load("coins/coin1.png"), (32,32)),
pygame.transform.scale(pygame.image.load("coins/coin2.png"), (32,32)),
pygame.transform.scale(pygame.image.load("coins/coin3.png"), (32,32)),
pygame.transform.scale(pygame.image.load("coins/coin4.png"), (32,32)),
pygame.transform.scale(pygame.image.load("coins/coin5.png"), (32,32))
]

class Coins(pygame.sprite.Sprite):
    
    def __init__(self, image):
        super().__init__()
        
        self.image = image # Gets the coin image
        
        self.rect = self.image.get_rect() # Gets dimensions of coin
        
        self.cnt = 0 # Used for the animation
    
    # Animating the coins
    def update(self):
        self.cnt += 1
        
        # If the count reaches more than 16, reset it
        # Because if we do not the index would be out of range when slicing
        if self.cnt > 16:
            self.cnt = 0
        
        # Every 4 counts, change the image
        if self.cnt % 4 == 0:
            frame = self.cnt // 4
            self.image = spin[frame]