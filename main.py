import pygame
import sys
from Levels import *
from Player import *
from Load import *
from Coins import *
from Monsters import * 

# Main file which runs the game

def main():
    
    pygame.init()
    
    screenWidth = 630
    screenHeight = 560
    
    # Sets up the screen
    screen = pygame.display.set_mode([screenWidth, screenHeight])
    pygame.display.set_caption("Coinlecter - Term Project")
    
    # Plays background music
    # music = pygame.mixer.music.load("sounds/bgMusic.mp3")
    # pygame.mixer.music.play(-1)
    
    # Creates the player
    player = Player()
#     
    # Adds all levels to a list
    levelList = []
    levelList.append(Hub(player)) # Add hub
    levelList.append(Level_1(player)) # Add level 1
    levelList.append(Level_2(player)) # Add level 2
    levelList.append(Level_3(player)) # Add level 3
    levelList.append(Level_4(player)) # Add level 4
    levelList.append(HowToPlay(player)) # Add How to Play level
    levelList.append(Shop(player)) # Add Shop level
    levelList.append(GameOver(player)) # Add GameOver level
    levelList.append(Win(player)) # Add Win level
    
    # 0 -> Hub
    # 1 -> Level 1
    # 2 -> Level 2
    # 3 -> Level 3
    # 4 -> Level 4
    # 5 -> How To Play
    # 6 -> Shop
    # 7 -> Game Over
    # 8 -> Win
    currentLvlN = 5 # Start at the How to Play level
    
    curSpritesLst = pygame.sprite.Group()
    
    # Sets up the starting location of the player
    player.rect.x = 75
    player.rect.y = screenHeight - 140
    
    curSpritesLst.add(player) # Adds player to a sprite group, to draw later
    
    clock = pygame.time.Clock() # Creates the clock and timer
    
    timer = 0
    time = 0
    
    run = True
    
    while run:
        
        currentLvl = levelList[currentLvlN] # Chooses current level
        
        player.level = currentLvl # Makes the players level the current level
        
        # Manages the key presses ( Moving, Jumping... etc )
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If press the "x" quit game
                pygame.quit()
                sys.exit()
                run = False
            
            # If key is pressed down
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_LEFT: # If press left arrow, move left
                    player.left()
                
                if event.key == pygame.K_RIGHT:#If press right arrow, move right
                    player.right()
                
                if event.key == pygame.K_UP: # If press up arrow, jump
                    player.jump()
                
                # If press "s", equip/unequip Samar's mask
                if event.key == pygame.K_s and player.samar == True:
                    if player.samarMask == True: # If already equipped, unequip
                        player.samarMask = False
                    else: # Else, equip, and unequip other masks
                        player.samarMask = True
                        player.nadimMask = False
                        player.omarMask = False
                        player.yusufMask = False
                
                # If press "n", equip/unequip Nadim's mask
                if event.key == pygame.K_n and player.nadim == True:
                    if player.nadimMask == True: # If already equipped, unequip
                        player.nadimMask = False
                    else: # Else, equip, and unequip other masks
                        player.nadimMask = True
                        player.samarMask = False
                        player.omarMask = False
                        player.yusufMask = False
                
                # If press "o", equip/unequip Omar's mask
                if event.key == pygame.K_o and player.omar == True:
                    if player.omarMask == True: # If already equipped, unequip
                        player.omarMask = False
                    else: # Else, equip, and unequip other masks
                        player.omarMask = True
                        player.samarMask = False
                        player.nadimMask = False
                        player.yusufMask = False
                
                if event.key == pygame.K_y and player.yusuf == True:
                    if player.yusufMask == True:
                        player.yusufMask = False
                    else:
                        player.yusufMask = True
                        player.samarMask = False
                        player.nadimMask = False
                        player.omarMask = False
            
            # If key no longer pressed
            if event.type == pygame.KEYUP:
                
                # Doing this because if I do not do it, the player will not
                # stop and will keep going the same direction
                
                # If left arrow was pressed and we are moving left, stop moving
                if event.key == pygame.K_LEFT and player.changeX < 0:
                    player.stop()
                # If right arrow was pressed and we are moving right, stop moving
                if event.key == pygame.K_RIGHT and player.changeX > 0:
                    player.stop()
        
        # Gets the keys that are being pressed/hold
        keys = pygame.key.get_pressed()
        
        # If the player is colliding with a ladder, 
        # and the player presses space, climb the ladder
        if keys[pygame.K_SPACE]:
            player.climbLadder()
        
        # If the player is colliding with a level gate, and they press e, 
        # go to the specified level
        if keys[pygame.K_e]:
            currentLvlN = player.changeLevel(currentLvlN)
        
        # If the player is colliding with a shop item, and they press b, 
        # buy the item
        if keys[pygame.K_b]:
            player.buy()
        
        # If the player presses h, go back to the hub
        if keys[pygame.K_h] and player.gameOver == False:
            if currentLvlN != 0:
                currentLvlN = 0
                player.rect.y -= 140
        
        #If player presses r, and they either lost or won the game, restart game
        if keys[pygame.K_r] and (player.gameOver == True or player.win == True):
            main()
        
        curSpritesLst.update() # Updates the sprite group (Which has player)
        currentLvl.update() # Updates the level
        
        # Shifts the world to the right
        if not ((player.rect.right + 500) >= \
                  (len(currentLvl.level[0]) * 70 + currentLvl.worldShift) + 35):
            if player.rect.right >= 130:
                dif = player.rect.right - 130
                player.rect.right = 130
                currentLvl.shiftWorld(-dif)
        
        # Shifts the world to the left
        if player.rect.left <= 130:
            dif = 130 - player.rect.left
            player.rect.left = 130
            currentLvl.shiftWorld(dif)
        
        # Checks if player is colliding with coins, and if so, collects coin
        player.collectCoin()
        
        # Checks if the player hits something that kills him
        deathList = pygame.sprite.spritecollide(player, player.level.killList, \
                                                                          False)
        monsterDeathList = pygame.sprite.spritecollide(player, \
                                                player.level.monsterList, False)
        
        if len(deathList) > 0: # If he does...
            if player.hp - 1 == 0: # And he has 1 HP... Game is over
                player.hp = 0
                player.doubleJump = 0
                player.coins = 0
                currentLvlN = 7
                player.rect.x = 75
                player.rect.y = 25
                player.gameOver = True
            else: # Else, remove 1 HP, and teleport to start of level
                oofSound.play()
                player.rect.x = 75 + player.level.worldShift
                player.rect.y = 25
                player.kill()
        
        if len(monsterDeathList) > 0:
            
            if player.rect.bottom == monsterDeathList[0].rect.top + 6 or \
               player.rect.bottom == monsterDeathList[0].rect.top + 7 or \
               player.rect.bottom == monsterDeathList[0].rect.top + 8 or \
               player.rect.bottom == monsterDeathList[0].rect.top + 9:
                monsterDeathList[0].kill()
                player.changeY = -7
                player.coins += 2
                collectCoin.play()
            else:
                if player.hp - 1 == 0: # And he has 1 HP... Game is over
                    player.hp = 0
                    player.doubleJump = 0
                    player.coins = 0
                    currentLvlN = 7
                    player.rect.x = 75
                    player.rect.y = 25
                    player.gameOver = True
                else: # Else, remove 1 HP, and teleport to start of level
                    oofSound.play()
                    player.rect.x = 75 + player.level.worldShift
                    player.rect.y = 25
                    player.kill()
        
        # Checks if the player has won (By checking collions with win sign)
        win = pygame.sprite.spritecollide(player, player.level.winSign, False)
        
        if len(win) > 0: # If he did win
            currentLvlN = 8 # Change level to Win level
            player.rect.x = 75
            player.rect.y = 25
            player.win = True
        
        # Draws the Level, and the Heart, Coins, and Double Jump top left
        currentLvl.draw(screen)
        currentLvl.allObjList.draw(screen)
        curSpritesLst.draw(screen)
        screen.blit(heart, (20,0))
        screen.blit(coin, (160, 0))
        screen.blit(boots, (300, -5))
        
        # If you do have one double jump or more, equips it on player
        if player.doubleJump > 0:
            screen.blit(pygame.transform.flip(bootsEquip, True, False), \
                                            (player.rect.x, player.rect.y + 37))
        
        # If you have Nadim's mask equipped, equips on player
        if player.nadimMask == True:
            screen.blit(nadimMask, (player.rect.x - 2, player.rect.y))
        
        # If you have Samar's mask equipped, equips on player
        if player.samarMask == True:
            screen.blit(samarMask, (player.rect.x - 2, player.rect.y))
        
        # If you have Omar's mask equipped, equips on player
        if player.omarMask == True:
            screen.blit(omarMask, (player.rect.x - 2, player.rect.y))
        
        # If Yusuf's mask equipped, epuip on player
        if player.yusufMask == True:
            screen.blit(yusufMask, (player.rect.x, player.rect.y))
        
        # If player in hub, and level2 is locked, draw the "Locked" text
        # Above gate
        if player.lvl2Lock == True and currentLvlN == 0:
            basicfont = pygame.font.SysFont(None, 48)
            text = basicfont.render('Locked', True, (0, 0, 0), -1)
            textrect = text.get_rect()
            textrect.x = 1033 + player.level.worldShift
            textrect.y = 350
            screen.blit(text, textrect)
        
        # If player in hub, and level3 is locked, draw the "Locked" text
        # Above gate
        if player.lvl3Lock == True and currentLvlN == 0:
            basicfont = pygame.font.SysFont(None, 48) # Font size
            text = basicfont.render('Locked', True, (0, 0, 0), -1) # The text
            textrect = text.get_rect() # Gets text dimensions
            textrect.x = 1243 + player.level.worldShift # Sets x coords for text
            textrect.y = 350 # Sets y coords for text
            screen.blit(text, textrect) # Draws text
            
            # And similarly for each one...
        
        # If player in hub, and level4 is locked, draw the "Locked" text
        # above gate
        if player.lvl4Lock == True and currentLvlN == 0:
            basicfont = pygame.font.SysFont(None, 48)
            text = basicfont.render('Locked', True, (0, 0, 0), -1)
            textrect = text.get_rect()
            textrect.x = 1453 + player.level.worldShift
            textrect.y = 350
            screen.blit(text, textrect)
        
        # If player in GamOver level, draw the GameOver text, and how to restart
        # game
        if currentLvlN == 7:
            basicfont = pygame.font.SysFont(None, 48)
            
            text = basicfont.render('GAME OVER', True, (255, 0, 0), -1)
            textrect = text.get_rect()
            textrect.x = 200 + player.level.worldShift
            textrect.y = 280
            screen.blit(text, textrect)
            
            basicfont2 = pygame.font.SysFont(None, 32)
            
            text2 = basicfont2.render('Press "r" to play again!', True, \
                                                              (255, 20, 20), -1)
            text2rect = text2.get_rect()
            text2rect.x = 183 + player.level.worldShift
            text2rect.y = 320
            screen.blit(text2, text2rect)
        
        # If player in Shop, draw the item description text and how much they 
        # are on top of them
        if currentLvlN == 6:
            basicfont = pygame.font.SysFont(None, 32)
            
            # Health description
            hpDisc = basicfont.render('Buy Health!', True, (255, 0, 0), -1)
            hpDiscRect = hpDisc.get_rect()
            hpDiscRect.x = 330 + player.level.worldShift
            hpDiscRect.y = 280
            
            # Health price
            hpPrice = basicfont.render('2x Coins', True, (255, 0, 0), -1)
            hpPriceRect = hpDisc.get_rect()
            hpPriceRect.x = 340 + player.level.worldShift
            hpPriceRect.y = 320
            
            # Draws the texts
            screen.blit(hpDisc, hpDiscRect)
            screen.blit(hpPrice, hpPriceRect)
            
            # Double jump description
            dblJDisc = basicfont.render('Buy Double Jump!',True,(255, 0, 0),-1)
            dblJDiscRect = dblJDisc.get_rect()
            dblJDiscRect.x = 510 + player.level.worldShift
            dblJDiscRect.y = 280
            
            # Double jump price
            dblJPrice = basicfont.render('2x Coins', True, (255, 0, 0), -1)
            dblJPriceRect = dblJPrice.get_rect()
            dblJPriceRect.x = 550 + player.level.worldShift
            dblJPriceRect.y = 320
            
            # Draws the texts
            screen.blit(dblJDisc, dblJDiscRect)
            screen.blit(dblJPrice, dblJPriceRect)
            
            # If you have not bought Nadim's mask, draw the desc and price texts
            if player.nadim == False:
                nadimMaskDisc = basicfont.render("Buy Nadim's mask!", True, \
                                                                (255, 0, 0), -1)
                nadimMaskDiscRect = nadimMaskDisc.get_rect()
                nadimMaskDiscRect.x = 780 + player.level.worldShift
                nadimMaskDiscRect.y = 280
                
                nadimMaskPrice = basicfont.render("5x Coins", True, \
                                                                (255, 0, 0), -1)
                nadimMaskPriceRect = nadimMaskPrice.get_rect()
                nadimMaskPriceRect.x = 830 + player.level.worldShift
                nadimMaskPriceRect.y = 320
                
                screen.blit(nadimMaskDisc, nadimMaskDiscRect)
                screen.blit(nadimMaskPrice, nadimMaskPriceRect)
            else: # Else draw the how to equip text
                nadimEquip = basicfont.render("Press 'n' to equip!", True, \
                                                                (255, 0, 0), -1)
                nadimEquipRect = nadimEquip.get_rect()
                nadimEquipRect.x = 780 + player.level.worldShift
                nadimEquipRect.y = 300
                
                screen.blit(nadimEquip, nadimEquipRect)
            
            # If you have not bought Samar's mask, draw the desc and price texts
            if player.samar == False:
                samarMaskDisc = basicfont.render("Buy Samar's mask!", True, \
                                                                (255, 0, 0), -1)
                samarMaskDiscRect = samarMaskDisc.get_rect()
                samarMaskDiscRect.x = 1060 + player.level.worldShift
                samarMaskDiscRect.y = 280
                
                samarMaskPrice = basicfont.render("5x Coins", True, \
                                                                (255, 0, 0), -1)
                samarMaskPriceRect = samarMaskPrice.get_rect()
                samarMaskPriceRect.x = 1110 + player.level.worldShift
                samarMaskPriceRect.y = 320
                
                screen.blit(samarMaskDisc, samarMaskDiscRect)
                screen.blit(samarMaskPrice, samarMaskPriceRect)
            else: # Else draw the how to equip text
                samarEquip = basicfont.render("Press 's' to equip!", True, \
                                                                (255, 0, 0), -1)
                samarEquipRect = samarEquip.get_rect()
                samarEquipRect.x = 1060 + player.level.worldShift
                samarEquipRect.y = 300
                
                screen.blit(samarEquip, samarEquipRect)
            
            if player.yusuf == False:
                yusufMaskDisc = basicfont.render("Buy Yusuf's mask!", True, \
                                                                (255, 0, 0), -1)
                yusufMaskDiscRect = yusufMaskDisc.get_rect()
                yusufMaskDiscRect.x = 1340 + player.level.worldShift
                yusufMaskDiscRect.y = 280
                
                yusufMaskPrice = basicfont.render("5x Coins", True, \
                                                                (255, 0, 0), -1)
                yusufMaskPriceRect = yusufMaskPrice.get_rect()
                yusufMaskPriceRect.x = 1390 + player.level.worldShift
                yusufMaskPriceRect.y = 320
                
                screen.blit(yusufMaskDisc, yusufMaskDiscRect)
                screen.blit(yusufMaskPrice, yusufMaskPriceRect)
            else: # Else draw the how to equip text
                yusufEquip = basicfont.render("Press 'y' to equip!", True, \
                                                                (255, 0, 0), -1)
                yusufEquipRect = yusufEquip.get_rect()
                yusufEquipRect.x = 1340 + player.level.worldShift
                yusufEquipRect.y = 300
                
                screen.blit(yusufEquip, yusufEquipRect)
        
        #If player in Win level,draw Congratulations and how to play again texts
        if currentLvlN == 8:
            basicfont = pygame.font.SysFont(None, 48)
            basicfont2 = pygame.font.SysFont(None, 32)
            
            text = basicfont.render('CONGRATULATIONS!', True, (255, 0, 0), -1)
            textrect = text.get_rect()
            textrect.x = 340 + player.level.worldShift
            textrect.y = 200
            screen.blit(text, textrect)
            
            text2 = basicfont2.render('Press "r" to play again!', True, \
                                                              (255, 20, 20), -1)
            text2rect = text2.get_rect()
            text2rect.x = 390 + player.level.worldShift
            text2rect.y = 240
            screen.blit(text2, text2rect)
            
            text3 = basicfont2.render('OR', True, (255, 20, 20), -1)
            text3rect = text3.get_rect()
            text3rect.x = 500 + player.level.worldShift
            text3rect.y = 280
            screen.blit(text3, text3rect)
            
            text4 = basicfont2.render('Press "h" to go to hub!', True, \
                                                              (255, 20, 20), -1)
            text4rect = text4.get_rect()
            text4rect.x = 390 + player.level.worldShift
            text4rect.y = 320
            screen.blit(text4, text4rect)
            
            if player.omar == False:
                omarMaskDisc = basicfont2.render("Buy Omar's mask!", True, \
                                                                (255, 0, 0), -1)
                omarMaskDiscRect = omarMaskDisc.get_rect()
                omarMaskDiscRect.x = 710 + player.level.worldShift
                omarMaskDiscRect.y = 280
                
                omarMaskPrice = basicfont2.render("5x Coins", True, \
                                                                (255, 0, 0), -1)
                omarMaskPriceRect = omarMaskPrice.get_rect()
                omarMaskPriceRect.x = 760 + player.level.worldShift
                omarMaskPriceRect.y = 320
                
                screen.blit(omarMaskDisc, omarMaskDiscRect)
                screen.blit(omarMaskPrice, omarMaskPriceRect)
            else: # Else draw the how to equip text
                omarEquip = basicfont2.render("Press 'o' to equip!", True, \
                                                                (255, 0, 0), -1)
                omarEquipRect = omarEquip.get_rect()
                omarEquipRect.x = 710 + player.level.worldShift
                omarEquipRect.y = 300
                
                screen.blit(omarEquip, omarEquipRect)
        
        # CITATION: How to draw texts learned from... 
        # https://sivasantosh.wordpress.com/2012/07/18/displaying-text-in-pygame/
        basicfont = pygame.font.SysFont(None, 48)
        text = basicfont.render('|        x %d |        x %d |         x %d'\
                                %(player.hp,player.coins,player.doubleJump), \
                                                            True, (0, 0, 0), -1)
        textrect = text.get_rect()
        textrect.y = 10
        screen.blit(text, textrect)
        
        clock.tick(60)
    
        pygame.display.update()

main() # Runs the game
