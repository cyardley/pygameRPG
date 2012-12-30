#!/usr/bin/env python
import random, os, pygame, var
from pygame.locals import *

#Sprites
class Sprite(pygame.sprite.Sprite):
    def __init__(self, fname):
	self.image = pygame.image.load(os.path.join('images/',fname))
	self.image = self.image.convert()
	self.image.set_colorkey((255,0,255)) #HEX: 00ff00
	self.rect = self.image.get_rect()
        self.rect.topleft = [0,0]

######
#Minimap
######
def MakeMiniMap():
	var.minimap = pygame.Surface((200, 200))
	for mmx in range(0, 200):
		for mmy in range (0, 200):
			if var.maparray[mmy][mmx] == 1: var.minimap.set_at((mmx,mmy),(0,100,0))#Grass
			if var.maparray[mmy][mmx] >= 6 and var.maparray[mmy][mmx]<=14: var.minimap.set_at((mmx,mmy),(0,0,250))#Ocean
			if var.maparray[mmy][mmx] >= 15 and var.maparray[mmy][mmx]<=23: var.minimap.set_at((mmx,mmy),(110,123,139))#Mountain
			if var.maparray[mmy][mmx] >= 24 and var.maparray[mmy][mmx]<=38: var.minimap.set_at((mmx,mmy),(0,154,205))#River
			if var.maparray[mmy][mmx] >= 39 and var.maparray[mmy][mmx]<=42: var.minimap.set_at((mmx,mmy),(135,206,235))#River-Ocean
			if var.maparray[mmy][mmx] >= 43 and var.maparray[mmy][mmx]<=44: var.minimap.set_at((mmx,mmy),(139,69,19))#Bridge
			if var.maparray[mmy][mmx] >= 45 and var.maparray[mmy][mmx]<=53: var.minimap.set_at((mmx,mmy),(0,50,0))#Forest
			if var.maparray[mmy][mmx] >= 54 and var.maparray[mmy][mmx]<=62: var.minimap.set_at((mmx,mmy),(255,204,51))#Desert
			if var.maparray[mmy][mmx] >= 63 and var.maparray[mmy][mmx]<=72: var.minimap.set_at((mmx,mmy),(139,69,19))#Road
			if var.maparray[mmy][mmx] >= 73 and var.maparray[mmy][mmx]<=76: var.minimap.set_at((mmx,mmy),(138,43,226))#Town
	pygame.image.save(var.minimap, 'images/minimap.bmp')
	var.p_minimap = var.Sprite("minimap.bmp")

#Text
def UpdateText(sendtext, text):
	text[4] = text[3]
	text[3] = text[2]
	text[2] = text[1]
	text[1] = text[0]
	text[0] = sendtext
#Randomly Place Ingredients
def placeingredients():
	for var.cy in range(1, var.worldheight-1):
		for var.cx in range(1, var.worldwidth-1):
			if var.itemarray[var.cy][var.cx]==var.i_mushroom: var.itemarray[var.cy][var.cx]=[]	
			if var.itemarray[var.cy][var.cx]==var.i_rflower: var.itemarray[var.cy][var.cx]=[]
			if var.itemarray[var.cy][var.cx]==var.i_bflower: var.itemarray[var.cy][var.cx]=[]
	for itp in range(1,4):
		for itn in range(0, 100):
			ix = random.randint(1, var.worldheight-1)
			iy = random.randint(1, var.worldwidth-1)
			if var.itemarray[iy][ix]==[] and var.maparray[iy][ix]==1:
				if itp==1: var.itemarray[iy][ix]=var.i_mushroom
				if itp==2: var.itemarray[iy][ix]=var.i_rflower
				if itp==3: var.itemarray[iy][ix]=var.i_bflower

#######
#MInimap Toggle
#######
def togMiniMap():
	if var.mousepos[0] >= var.window[3][1]+50 and var.mousepos[0] <=var.window[3][1]+50+32 and var.mousepos[1] >= var.window[3][2]+10 and var.mousepos[1] <=var.window[3][2]+1016 and var.msclick == 1:
		if var.gmap == 3:
			var.gmap = 1
		else:
			var.gmap +=1
