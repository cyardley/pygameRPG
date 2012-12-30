#!/usr/bin/env python
import random, os, pygame, var
from pygame.locals import *


#######
#Events
#######
def myEvents():
	for event in pygame.event.get():
		#######
		#Keys
		#######
		if event.type == KEYDOWN:
			#Input
			if event.key == K_BACKQUOTE: var.inkey = True
			if event.key == K_SPACE: 
				var.battle = True
				var.movin = False
			#Escape
		 	if event.key == K_ESCAPE:
	 			exit(0)
			#Move
			if event.key == K_UP: var.ky_u = True
			if event.key == K_DOWN: var.ky_d = True
			if event.key == K_LEFT:	var.ky_l = True
			if event.key == K_RIGHT: var.ky_r = True
			#var.dev-Col
			if var.dev == True:
				if event.key == K_w: var.cy-=var.pspeed
				if event.key == K_s: var.cy+=var.pspeed
				if event.key == K_a: var.cx-=var.pspeed
				if event.key == K_d: var.cx+=var.pspeed
				if event.key == K_b: var.battle = True
		if event.type == KEYUP:
			if event.key == K_UP: var.ky_u = False
			if event.key == K_DOWN: var.ky_d = False
			if event.key == K_LEFT:	var.ky_l = False
			if event.key == K_RIGHT: var.ky_r = False
		#X button
		if event.type == QUIT: 
	 		exit(0) 
		#Mouse
		var.mousepos = pygame.mouse.get_pos()
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				var.msdown = True
			if event.button == 3:
				var.mrdown = True
		if event.type == pygame.MOUSEBUTTONUP:
			var.msdown = False
			var.msclick = 0
			var.mrdown = False
	if var.msdown == True:
		var.msclick +=1
#######
#Movement
#######
#Collisions
def collide(movx, movy):
	if var.maparray[var.ppy+movy][var.ppx+movx] == 1 or (var.maparray[var.ppy+movy][var.ppx+movx] >=43 and var.maparray[var.ppy+movy][var.ppx+movx] <=76) or var.maparray[var.ppy+movy][var.ppx+movx] == 78 or  var.maparray[var.ppy+movy][var.ppx+movx] == 87 or var.maparray[var.ppy+movy][var.ppx+movx] == 89 or var.maparray[var.ppy+movy][var.ppx+movx] == 97 or var.maparray[var.ppy+movy][var.ppx+movx] == 98 or var.maparray[var.ppy+movy][var.ppx+movx] == 100:
		return True
#Movement
def movement():
	if var.movin == True:
		var.ppx = (var.cx/var.tilepix)+(var.plx/var.tilepix)
		var.ppy = (var.cy/var.tilepix)+(var.ply/var.tilepix)
		if var.ky_u == True:
			if collide(0,-1) == True:
				if var.cy >0:
					if var.ply >= (var.screenheight*var.tilepix)/var.pbuffer and var.movemeth1==True:
						var.ply -= var.pspeed
					else:
						var.cy -= var.pspeed
		if var.ky_d == True:
			if collide(0,1) == True:
				if var.cy+(var.screenheight*var.tilepix) < var.worldheight*var.tilepix: 
					if var.ply <= (var.screenheight*var.tilepix)-((var.screenheight*var.tilepix)/var.pbuffer) and var.movemeth1==True:
						var.ply += var.pspeed
					else:
						var.cy += var.pspeed
		if var.ky_l == True:
			if collide(-1,0) == True:
				if var.cx > 0: 
					if var.plx >= (var.screenwidth*var.tilepix)/var.pbuffer and var.movemeth1==True:
						var.plx -= var.pspeed
					else:
						var.cx -= var.pspeed
		if var.ky_r == True:
			if collide(1,0) == True:
				if var.cx+(var.screenwidth*var.tilepix) < var.worldwidth*var.tilepix: 
					if var.plx <= (var.screenwidth*var.tilepix)-((var.screenwidth*var.tilepix)/var.pbuffer) and var.movemeth1==True:
						var.plx += var.pspeed
					else:
						var.cx += var.pspeed

#######
#inkey
#######
def userInKey():
	if var.inkey == True:
		print "Warning: These may cause problems."
		print "Use at your own risk"
		print "Type 'h' for command list"
		answ = raw_input("What would you like? ")
		if answ == "h":
			print "Commands:"
			print "'h' - Displays this help"
			print "'t' - Teleport Camera"
			print "'q' - Say Something (no function)"
			print "'m' - Activate var.dev Tools"
			print "'i' - Add an item to Mouse (Unstable)"
			print "'z' - Place Random Ingredients on Ground"
		if answ == "t":
			var.cx = input("New Camera X: ")*var.tilepix
			var.cy = input ("New Camera Y: ")*var.tilepix
		if answ == "q": UpdateText(var.p_name + ": "+raw_input ("Talk: "), var.text)
		if answ == "m": var.dev ==True
		if answ == "i": 
			print "WARNING:"
			print "This command will replace any item you currently have on the mouse"
			print "IF YOU MESS UP TYPING THE ITEM, THE GAME COULD CRASH!"
			print "Use this cheat at your own risk!"
			print "I've warned you :-)"
			iyn = raw_input("Would you like to continue with this cheat? (y=yes) ")
			if iyn=="y": var.imouse = input("Type an Item to equip: ")
		if answ == "z": placeingredients()
		var.inkey = False


