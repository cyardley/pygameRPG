#!/usr/bin/env python
#PYGAME RPG
###################
import random, os, pygame
from pygame.locals import *
from var import *
from loadmap import *
from draw import *
from construct import *
from invintory import *
from alchemy import *
from battle import *
from userinput import *
from locations import *
from windows import *

loadMap("world.txt")
MakeMiniMap()
placeingredients()
print "PYGAME GAME BY CASEY YARDLEY"
clock = pygame.time.Clock()
var.cx = 17*var.tilepix
var.cy = 20*var.tilepix
while var.run == True:
	pygame.display.set_caption("PYGAME GAME")
	#User Input
	myEvents()
	movement()       
	userInKey()
	var.imouse = MouseItems()
	DropPickItems()
	#Actions
	togMiniMap()
	alchemy()
	battle()
	towns()
	#Windows
        windowAll()
	pygame.display.flip()
	clock.tick(40)
