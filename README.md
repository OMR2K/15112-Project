# Project Description:
- Project is called "Coinlecter"
- This project is a game. It has 4 different levels, a hub, a how to play level, and a shop where you can buy a lot of different items, such as, health, double jump, invincibility power up, and different types of masks. You can collect coins by completing the different levels. Once you finish all 4 levels, you win the game. And if your HP drops to 0, you loose the game and you have to start from the beginning.

# How to run the project:
- Download all the files/images/sounds, then run the "main.py" file
	
# How to install and needed libraries:
- Only external library needed to run the project is Pygame. You can download Pygame by following this:
	- Windows: https://qwewy.gitbooks.io/pygame-module-manual/installation/windows.html
	- Mac: https://qwewy.gitbooks.io/pygame-module-manual/installation/os-x.html

# Shortcuts:
- Change line 50 to any of these numbers. (From "main.py")
	- 0 -> Hub
	- 1 -> Level1
	- 2 -> Level2
	- 3 -> Level3
	- 4 -> Level4
	- 5 -> How to Play level
	- 6 -> Shop
	- 7 -> Game Over level
	- 8 -> Win Level
		
- To add coins to test shop...
	- change value of line 28 from the "Player.py" file

- To add double jump to test it
	- change line 31 value from "Player.py" file

- To check if game over level works, change HP value to 1, then hit a spike/water tile or a monster

- To check if winning game works, uncomment lines 560 to 569, then comment 549 to 558, both from "Levels.py" file, then change currentLvlN from "main.py" file to 4.
