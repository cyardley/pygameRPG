#!/usr/bin/env python
import random, os, pygame, var
from pygame.locals import *
from loadmap import *


def toWorld():
	if (var.cy <=0) or (var.cy+(var.screenheight*var.tilepix) >= var.worldheight*var.tilepix) or (var.cx <= 0) or (var.cx+(var.screenwidth*var.tilepix) >= var.worldwidth*var.tilepix):
		var.cx = var.wld_x+var.tilepix
		var.cy = var.wld_y
		var.location = "world"
		loadMap("world.txt")

#Special Location Trigger Tiles

def towns():
########
#World
#######
	if var.location=="world":
		#Town 1
		if var.cx/var.tilepix==14 and var.cy/var.tilepix==23:
			var.wld_x = var.cx
			var.wld_y = var.cy
			var.cx = 24*var.tilepix
			var.cy = 16*var.tilepix
			var.location = "town1"
			loadMap("town1.txt")
		#Town 2
		if var.cx/var.tilepix==103 and var.cy/var.tilepix==35:
			var.wld_x = var.cx
			var.wld_y = var.cy
			var.cx = 43*var.tilepix
			var.cy = 79*var.tilepix
			var.location = "town2"
			loadMap("town2.txt")
#########
#Town 1
#########
	if var.location =="town1":
		#Exit Town
		toWorld()
		#Enter Buildings
		####
		#House
		if var.cx/var.tilepix==18 and var.cy/var.tilepix==7:
			loadMap("house1.txt")
			var.location = "house1"
			var.cx = 8 *var.tilepix
			var.cy = 7 *var.tilepix
		#Shop
		if var.cx/var.tilepix==5 and var.cy/var.tilepix==13:
			loadMap("house1.txt")
			var.location = "house1"
			var.cx = 8 *var.tilepix
			var.cy = 70 *var.tilepix
		#Inn
		if var.cx/var.tilepix==12 and var.cy/var.tilepix==23:
			loadMap("house1.txt")
			var.location = "house1"
			var.cx = 49 *var.tilepix
			var.cy = 23 *var.tilepix
	##########
	#House 1
	##########
	if var.location =="house1":
		#Exit House
		if (var.cx/var.tilepix==8 and var.cy/var.tilepix==8) or (var.cx/var.tilepix==9 and var.cy/var.tilepix==8):
			loadMap("town1.txt")
			var.location = "town1"
			var.cx = 18 *var.tilepix
			var.cy = 8 *var.tilepix
		#Exit Shop
		if (var.cx/var.tilepix==8 and var.cy/var.tilepix==71):
			loadMap("town1.txt")
			var.location = "town1"
			var.cx = 5 *var.tilepix
			var.cy = 14 *var.tilepix
		#Exit Inn
		if (var.cx/var.tilepix==49 and var.cy/var.tilepix==24) or (var.cx/var.tilepix==50 and var.cy/var.tilepix==24):
			loadMap("town1.txt")
			var.location = "town1"
			var.cx = 12 *var.tilepix
			var.cy = 24 *var.tilepix
		#INN: Up Stairs
		if (var.cx/var.tilepix==60 and var.cy/var.tilepix==22):
			var.cx = 65 *var.tilepix
			var.cy = 38 *var.tilepix
		#INN: Down Stairs
		if (var.cx/var.tilepix==65 and var.cy/var.tilepix==37):
			var.cx = 59 *var.tilepix
			var.cy = 22 *var.tilepix
##########
#Town 2
##########
	if var.location =="town2":
		#Exit
		toWorld()
		#Inn:
		if var.cx/var.tilepix==33 and var.cy/var.tilepix==73:
			loadMap("house2.txt")
			var.location = "house2"
			var.cx = 20 *var.tilepix
			var.cy = 27 *var.tilepix
		#Items:
		if var.cx/var.tilepix==15 and var.cy/var.tilepix==71:
			loadMap("house2.txt")
			var.location = "house2"
			var.cx = 112 *var.tilepix
			var.cy = 12 *var.tilepix
		#Left Side House:
		if var.cx/var.tilepix==8 and var.cy/var.tilepix==59:
			loadMap("house2.txt")
			var.location = "house2"
			var.cx = 142 *var.tilepix
			var.cy = 8 *var.tilepix
		#Armour:
		if var.cx/var.tilepix==1 and var.cy/var.tilepix==43:
			loadMap("house2.txt")
			var.location = "house2"
			var.cx = 171 *var.tilepix
			var.cy = 11 *var.tilepix
		#Mansion Front:
		if var.cx/var.tilepix==16 and var.cy/var.tilepix==23:
			loadMap("house2.txt")
			var.location = "house2"
			var.cx = 17 *var.tilepix
			var.cy = 84 *var.tilepix
		#Mansion Side:
		if var.cx/var.tilepix==30 and var.cy/var.tilepix==13:
			loadMap("house2.txt")
			var.location = "house2"
			var.cx = 42 *var.tilepix
			var.cy = 56 *var.tilepix
		#Sword:
		if var.cx/var.tilepix==41 and var.cy/var.tilepix==37:
			loadMap("house2.txt")
			var.location = "house2"
			var.cx = 125 *var.tilepix
			var.cy = 40 *var.tilepix
		#Right House:
		if var.cx/var.tilepix==53 and var.cy/var.tilepix==44:
			loadMap("house2.txt")
			var.location = "house2"
			var.cx = 110 *var.tilepix
			var.cy = 62 *var.tilepix
		#Magic Shop:
		if var.cx/var.tilepix==61 and var.cy/var.tilepix==69:
			loadMap("house2.txt")
			var.location = "house2"
			var.cx = 156 *var.tilepix
			var.cy = 46 *var.tilepix
		##########
		#House 2
		##########
	if var.location =="house2":
		#Exit Inn
		if (var.cx/var.tilepix==20 and var.cy/var.tilepix==28) or (var.cx/var.tilepix==21 and var.cy/var.tilepix==28):
			loadMap("town2.txt")
			var.location = "town2"
			var.cx = 33 *var.tilepix
			var.cy = 74 *var.tilepix
		#Inn: Up Stairs
		if (var.cx/var.tilepix==57 and var.cy/var.tilepix==3):
			var.cx = 80 *var.tilepix
			var.cy = 9 *var.tilepix
		#Inn: Down Stairs
		if (var.cx/var.tilepix==81 and var.cy/var.tilepix==9):
			var.cx = 56 *var.tilepix
			var.cy = 3 *var.tilepix
		#Exit Item
		if (var.cx/var.tilepix==112 and var.cy/var.tilepix==13) or (var.cx/var.tilepix==113 and var.cy/var.tilepix==13):
			loadMap("town2.txt")
			var.location = "town2"
			var.cx = 15 *var.tilepix
			var.cy = 72 *var.tilepix	
		#Exit Left House
		if (var.cx/var.tilepix==142 and var.cy/var.tilepix==9) or (var.cx/var.tilepix==143 and var.cy/var.tilepix==9):
			loadMap("town2.txt")
			var.location = "town2"
			var.cx = 8 *var.tilepix
			var.cy = 60 *var.tilepix
		#Exit Armour
		if (var.cx/var.tilepix==171 and var.cy/var.tilepix==12):
			loadMap("town2.txt")
			var.location = "town2"
			var.cx = 1 *var.tilepix
			var.cy = 44 *var.tilepix
		#Exit Mansion Front
		if (var.cx/var.tilepix==17 and var.cy/var.tilepix==85) or (var.cx/var.tilepix==18 and var.cy/var.tilepix==85):
			loadMap("town2.txt")
			var.location = "town2"
			var.cx = 16 *var.tilepix
			var.cy = 24 *var.tilepix
		#Exit Mansion Side
		if (var.cx/var.tilepix==42 and var.cy/var.tilepix==57):
			loadMap("town2.txt")
			var.location = "town2"
			var.cx = 30 *var.tilepix
			var.cy = 14 *var.tilepix
		#Mansion UP Stairs
		if (var.cx/var.tilepix==48 and var.cy/var.tilepix==54):
			var.cx = 79 *var.tilepix
			var.cy = 33 *var.tilepix
		#Mansion DOWN Stairs
		if (var.cx/var.tilepix==79 and var.cy/var.tilepix==34):
			var.cx = 47 *var.tilepix
			var.cy = 54 *var.tilepix
		#Exit Sword
		if (var.cx/var.tilepix==125 and var.cy/var.tilepix==41) or (var.cx/var.tilepix==126 and var.cy/var.tilepix==41):
			loadMap("town2.txt")
			var.location = "town2"
			var.cx = 41 *var.tilepix
			var.cy = 38 *var.tilepix
		#Exit Right House
		if (var.cx/var.tilepix==110 and var.cy/var.tilepix==63):
			loadMap("town2.txt")
			var.location = "town2"
			var.cx = 53 *var.tilepix
			var.cy = 45 *var.tilepix
		#Exit Magic Shop
		if (var.cx/var.tilepix==156 and var.cy/var.tilepix==47):
			loadMap("town2.txt")
			var.location = "town2"
			var.cx = 61 *var.tilepix
			var.cy = 70 *var.tilepix
		
