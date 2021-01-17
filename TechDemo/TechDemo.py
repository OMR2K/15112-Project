import pygame

# This is the TechDemo for pygame

pygame.init()

screen = pygame.display.set_mode((600,400))
clock = pygame.time.Clock()
bg = pygame.image.load("bg.jpeg")
jump = pygame.mixer.Sound("jump.wav")
music = pygame.mixer.music.load("bgMusic.mp3")

class Player(object):
    def __init__(self, x, y, width, height):
        self.px = x
        self.py = y
        self.pwidth = width
        self.pheight = height
        self.image = pygame.image.load("R1.png")
        self.isJumping = False
        self.jumpCnt = 10
        self.hitbox = (self.px, self.py, self.pwidth, self.pheight)
    
    def draw(self):
        self.hitbox = (self.px + 10, self.py + 10, self.pwidth - 20, self.pheight - 12)
        screen.blit(self.image, (self.px, self.py))
        pygame.draw.rect(screen, -1, self.hitbox, 1)
    
    def jump(self):
        if self.jumpCnt >= -10:
            n = 1
            if self.jumpCnt < 0:
                n = -1
            self.py -= (self.jumpCnt ** 2) * 0.5 * n
            self.jumpCnt -= 1
        else:
            self.isJumping = False
            self.jumpCnt = 10
    
class Obstacle(object):
    
    def __init__(self, x, y, width, height):
        self.ox = x
        self.oy = y
        self.owidth = width
        self.oheight = height
        self.hitbox = (self.ox, self.oy, self.owidth, self.oheight)
    
    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), (self.ox, self.oy, 
                                                self.owidth, self.oheight))

p1 = Player(25, 325, 64, 64)
o1 = Obstacle(200, 375, 100, 20)
pygame.mixer.music.play(-1)

def redrawAll():
    screen.blit(bg, (0,0))
    p1.draw()
    # o1.draw()
    
    pygame.display.update()

run = True
isJump = False

while run:
    time = clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        p1.px -= 5
    if keys[pygame.K_RIGHT]:
        p1.px += 5
    
    if p1.isJumping == False:
        if keys[pygame.K_SPACE]:
            jump.play()
            p1.isJumping = True
    else:
        p1.jump()
    
    redrawAll()    

pygame.quit()