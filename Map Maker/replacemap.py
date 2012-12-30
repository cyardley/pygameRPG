#!/usr/bin/env python
#Replace Numbers
import random
import os, pygame
from pygame.locals import *
#Variables
fname = "map.txt"
readfile = file(os.path.join("/home/casey/Desktop/Map Maker/data/",fname), 'r')
worldwidth = int(readfile.readline())
worldheight = int(readfile.readline())
spritenum = int(readfile.readline())
tilepix = int(readfile.readline())
#Generate Array
maparray=[]
for cm1y in range(worldheight):
	maparray.append([])
	for cm1x in range(worldwidth):
   		maparray[cm1y].append(cm1y*cm1x)
#Load Array from File
for ry in range(0, worldheight):	
	for rx in range(0,worldwidth):
		maparray[ry][rx] = int(readfile.readline())
readfile.close()
#Replace
numr = raw_input("What number to replace? ")
numw = raw_input("Replace with which number? ")
for wy in range(0, worldheight):	
	for wx in range(0,worldwidth):
		if maparray[wy][wx] == numr:
			maparray[wy][wx] = numw
print "Replaced ",
print numr,
print " with ",
print numw
#Save
savefile = file(os.path.join("/home/casey/Desktop/Map Maker/data/",fname), 'w')
print >> savefile, worldwidth
print >> savefile, worldheight
print >> savefile, spritenum
print >> savefile, tilepix
for wy in range(0, worldheight):	
	for wx in range(0,worldwidth):
		print >> savefile, maparray[wy][wx]
savefile.close()
print "...saved"



screenwidth = 25
screenheight = 20
run = True
resx = tilepix*screenwidth
resy = tilepix*screenheight
cx = 5
cy = 5
msdown = False
pdir = 0
brush = 1
inkey = False
bk = False
bs = 1
sv = False
#Draw Screen
#Init
pygame.init()
(6,0)
screen = pygame.display.set_mode((resx, resy))
pygame.display.set_caption('Map Maker')
pygame.mouse.set_visible(1)
clock = pygame.time.Clock()
#Sprites
class Sprite(pygame.sprite.Sprite):
    def __init__(self, fname, initial_position):
	self.image = pygame.image.load(os.path.join('/home/casey/Desktop/Map Maker/images/',fname))
	self.image = self.image.convert()
	self.image.set_colorkey((255,0,255)) #HEX: 00ff00
	self.rect = self.image.get_rect()
        self.rect.topleft = initial_position
#Set Up Sprites
spriten = []
for sl in range (0,spritenum):
	spriten.append([])
for rs in range (1, spritenum):
	spriten[rs] = Sprite(str(rs)+".png",[0, 0])
ru = True
while ru == True:
	screen.fill((0, 0, 0))
	for layY in range(0,screenheight):
		dy = layY*tilepix
		for layX in range(0,screenwidth):
			dx = layX*tilepix
			for sn in range (1, spritenum):
				if maparray[layY+(cy/tilepix)][layX+(cx/tilepix)] == sn:
					screen.blit(spriten[sn].image, (dx, dy))
	#Events
	for event in pygame.event.get():
		#Keys
		if event.type == KEYDOWN:
			#Escape
		 	if event.key == K_ESCAPE:
	 			exit(0)
			#Move
			if event.key == K_UP: pdir = 1
			if event.key == K_DOWN: pdir = 2
			if event.key == K_LEFT:	pdir = 3
			if event.key == K_RIGHT: pdir = 4
	#Window Caption
	pygame.display.set_caption("|Map Maker| |Brush: "+str(brush) +" || Brush Size: " + str(bs)+" | |Cam Pos: "+ str(cx/tilepix)+", "+str(cy/tilepix)+"|")
	#Movement
	if pdir == 1: 
		if cy >0: cy -= tilepix
	if pdir == 2: 
		if cy+(screenheight*tilepix) < worldheight*tilepix: cy += tilepix
	if pdir == 3: 
		if cx > 0: cx -= tilepix
	if pdir == 4: 
		if cx+(screenwidth*tilepix) < worldwidth*tilepix: cx += tilepix
	#Update Screen
	pygame.display.flip()	
