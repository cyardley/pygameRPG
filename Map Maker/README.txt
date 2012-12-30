Map Maker
by Casey Yardley
----------------------
INTRO
----------------------
This Python and Pygame application allows you to create 2d maps using custom sprites.
You can easily edit the sprite size, and the width and height of the map.
----------------------
SPRITES
----------------------
You can put your sprites in the /images/ folder.
They must be .PNG format.
They must all be the same width and height.
The width and height must be equal.
They must be named numericaly.
1.png, 2.png, 3.png, 4.png,.....,34.png, etc
YOU MUST NOT LEAVE GAPS IN NUMBERS...!
----------------------
CREATEMAP.PY
----------------------
You can use this program to generate a blank map to edit with EDITMAP.PY
First, go to /data/ and create a new BLANK file named "map.txt".
Then, run CREATEMAP.PY.
Answer the questions.
-Width of Map
-Height of Map
-Tile Fill Number (Number that the map will be filled with)
-Width/Height of Tile in Pixles (for example, type "32" if your tiles are 32x32)
-Number of Sprites in Sprite Set. (this can be changed later if you make more sprites by chaging number in third line. Always use +1 of the real value)
----------------------
EDITMAP.PY
----------------------
You edit the map that is called "map.txt" in /data/.
Click on the screen to "paint" tiles.
You can move around your map using the arrow keys.
Change Brush Number with "{" or "}"
Change Brush Size with "PageUP" or "PageDOWN".

---------------------------------------------------------------------------------
THE PROGRAM IS NOT FINISHED. IT WILL BE EASER TO TO THE FOLLOWING WHEN IT IS DONE:
---------------------------------------------------------------------------------
-To View All Commands
-----------------------
-Press Space.
-Go to the Console Window.
-Type "h". Enter.
-----------------------------------------------------------------------------------
To Change Tile "brush":
-----------------------
-Press Space.
-Go to the Console Window.
-Type "b". Enter.
-Type the number of tile you want. Enter.
-Go back to main window. Your brush is changed.
-----------------------------------------------------------------------------------
-To Change Brush SIZE
-----------------------
-Press Space.
-Go to the Console Window.
-Type "x". Enter.
-Type the size of brush you want. Enter.
-----------------------------------------------------------------------------------
-To SAVE:
-----------------------
-Press Space.
-Go to the Console Window. 
-Type "s". Enter.
-It should save. You can exit or continue editing.
-----------------------------------------------------------------------------------
-To TELEPORT CAMERA:
-----------------------
-Press Space.
-Go to the Console Window.
-Type "t". Enter.
