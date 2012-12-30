#!/usr/bin/env python
#MAP MAKER
###################
import random
import os, pygame
from pygame.locals import *
#Variables
fname = "tileset.txt"
readfile = file(os.path.join("/home/casey/Programming/archive2/Map Maker/images/",fname), 'r')
spritenum = int(readfile.readline())
tilepix = int(readfile.readline())
readfile.close()
fname = "map.txt"
readfile = file(os.path.join("/home/casey/Programming/archive2/Map Maker/data/",fname), 'r')
worldwidth = int(readfile.readline())
worldheight = int(readfile.readline())
palette = True
if palette == True:
	prx = 80
else:
	prx = 0
screenwidth = 824/tilepix #36
screenheight = 668/tilepix #24
run = True
resx = tilepix*25#screenwidth
resy = tilepix*23#screenheight
cx = 5
cy = 5
dimmini= True
msdown = False
pdir = 0
brush = 1
inkey = False
bk = False
bs = 1
sv = False
pts = 1
svd =False
sc = (250, 250, 250)
mini = False
togmini= 1
big = False
tmini = False
lbr = False
ex = False
#Init
pygame.init()
(6,0)
screen = pygame.display.set_mode((resx+prx, resy))
pygame.display.set_caption('Map Maker ..loading ("/data/map.txt/")')
pygame.mouse.set_visible(1)
clock = pygame.time.Clock()
#Generate Array
maparray=[]
for cm1y in range(worldheight):
	maparray.append([])
	for cm1x in range(worldwidth):
   		maparray[cm1y].append(cm1y*cm1x)
#Sprites
class Sprite(pygame.sprite.Sprite):
    def __init__(self, fname, initial_position):
	self.image = pygame.image.load(os.path.join('/home/casey/Programming/archive2/Map Maker/images/',fname))
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
player_sprite = Sprite("player.png",[0,0])
#Fonts
font1 = pygame.font.Font(os.path.join("/home/casey/Programming/archive2/Map Maker/data/","Purisa.ttf"), 50)#big
font2 = pygame.font.Font(os.path.join("/home/casey/Programming/archive2/Map Maker/data/","Purisa.ttf"), 20)#small
font3 = pygame.font.Font(os.path.join("/home/casey/Programming/archive2/Map Maker/data/","Purisa.ttf"), 10)#tiny
#Read from File
for ry in range(0, worldheight):	
	for rx in range(0,worldwidth):
		maparray[ry][rx] = int(readfile.readline())
readfile.close()
######
#Setup Minimap
######
minimap = pygame.Surface((worldwidth, worldheight))
def rminimap():
	print "Redraw"
	for mmy in range(0, worldheight):
		for mmx in range (0, worldwidth):
			global minimap
			if maparray[mmy][mmx] == 1: minimap.set_at((mmx,mmy),(0,100,0))#Grass
			if maparray[mmy][mmx] >= 6 and maparray[mmy][mmx]<=14: minimap.set_at((mmx,mmy),(0,0,250))#Ocean
			if maparray[mmy][mmx] >= 15 and maparray[mmy][mmx]<=23: minimap.set_at((mmx,mmy),(110,123,139))#Mountain
			if maparray[mmy][mmx] >= 24 and maparray[mmy][mmx]<=38: minimap.set_at((mmx,mmy),(0,154,205))#River
			if maparray[mmy][mmx] >= 39 and maparray[mmy][mmx]<=42: minimap.set_at((mmx,mmy),(135,206,235))#River-Ocean
			if maparray[mmy][mmx] >= 43 and maparray[mmy][mmx]<=44: minimap.set_at((mmx,mmy),(139,69,19))#Bridge
			if maparray[mmy][mmx] >= 45 and maparray[mmy][mmx]<=53: minimap.set_at((mmx,mmy),(0,50,0))#Forest
			if maparray[mmy][mmx] >= 54 and maparray[mmy][mmx]<=62: minimap.set_at((mmx,mmy),(255,204,51))#Desert
	pygame.image.save(minimap, '/home/casey/Programming/archive2/Map Maker/images/minimap.bmp')
	return Sprite("minimap.bmp",[0,0])
sp_minimap = rminimap()
################
## Main Loop  ##
################
print "Map Editor by Casey Yardley"
print "Click to edit map"
print "Space for advanced options (appear in this window)"
print "'b' to quick change brush type"
emrand = 1
pygame.mouse.set_visible(1)
screen.fill((0, 0, 0))
clock = pygame.time.Clock()
while run == True:
	#Events
	for event in pygame.event.get():
		#Keys
		if event.type == KEYDOWN:
			#Escape
		 	if event.key == K_ESCAPE:
	 			ex = True
			#Move
			if event.key == K_UP: pdir = 1
			if event.key == K_DOWN: pdir = 2
			if event.key == K_LEFT:	pdir = 3
			if event.key == K_RIGHT: pdir = 4
			#Input
			if event.key == K_SPACE: inkey = True
			if event.key == K_b: bk = True
			if event.key == K_PAGEUP: bs += 1
			if event.key == K_PAGEDOWN: bs -=1
			if bs <= 0: bs = 1
			if event.key == K_RIGHTBRACKET: brush += 1
			if brush >= spritenum: brush = spritenum-1
			if event.key == K_LEFTBRACKET: brush -= 1
			if brush <=0: brush = 1
			if event.key == K_z: pts -=1
			if pts <=1: pts = 1
			if event.key == K_x: pts +=1
			if pts >= spritenum-12: pts = spritenum-12
			if event.key == K_m: tmini = True
			if event.key == K_r:
				if dimmini==True: dimmini==False
				else: dimmini==True
			if event.key == K_COMMA: lbr=True
		if event.type == KEYUP:
			pdir = 0
			if event.key == K_COMMA:lbr=False
		#X button
		if event.type == QUIT: 
	 		ex = True
		#Mouse
		mousepos = pygame.mouse.get_pos()
		if event.type == pygame.MOUSEBUTTONDOWN:
			svd = False
			msdown = True
		if event.type == pygame.MOUSEBUTTONUP:
			msdown = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.dict['button'] == 4:#Wheel up
				pts -=1
				if pts <=1: pts = 1
			if event.dict['button'] == 5:#Wheel down
				pts +=1
				if pts >= spritenum-12: pts = spritenum-12
			
	#Movement
	if pdir == 1: 
		if cy >tilepix: cy -= tilepix
	if pdir == 2: 
		if cy+(screenheight*tilepix) <= worldheight*tilepix: cy += tilepix
	if pdir == 3: 
		if cx >tilepix: cx -= tilepix
	if pdir == 4: 
		if cx+(screenwidth*tilepix) <= worldwidth*tilepix: cx += tilepix
	#Paint
	if big == False:
		if mousepos[0] >= 0 and mousepos[0] <=screenwidth*tilepix and mousepos[1] >= 0 and mousepos[1] <=screenheight*tilepix:
			if msdown == True:
				if bs == 1:
					maparray[(cy+mousepos[1])/tilepix][(cx+mousepos[0])/tilepix] = brush
				else:
					for bsy in range (0, bs):
						for bsx in range (0, bs):
							maparray[((cy+mousepos[1])/tilepix)-bsy][((cx+mousepos[0])/tilepix)-bsx] = brush
				if mini==True and dimmini==True: sp_minimap = rminimap()
	if big == True:
		if mousepos[0] >= 0 and mousepos[0] <=screenwidth and mousepos[1] >= 0 and mousepos[1] <=screenheight:
			if msdown == True:
				if bs == 1:
					maparray[mousepos[1]][mousepos[0]] = brush
				else:
					for bsy in range (0, bs):
						for bsx in range (0, bs):
							maparray[mousepos[1]-bsy][mousepos[0]-bsx] = brush
	if big ==False:
		#Draw Screen
		screen.fill((0, 0, 0))
		for layY in range(0,screenheight):
			dy = layY*tilepix
			for layX in range(0,screenwidth):
				dx = layX*tilepix
				for sn in range (1, spritenum):
					if maparray[layY+(cy/tilepix)][layX+(cx/tilepix)] == sn:
						screen.blit(spriten[sn].image, (dx, dy))
	#Window Caption
	pygame.display.set_caption("|Map Maker| |Brush: "+str(brush) +" || Brush Size: " + str(bs)+" | |Cam Pos: "+ str(cx/tilepix)+", "+str(cy/tilepix)+"| |Mouse Tile: "+str((cx+mousepos[0])/tilepix)+", "+str((cy+mousepos[1])/tilepix)+"|")
	#Inkey
	if inkey == True:
		print "Type 'h' for help"
		answ = raw_input("What would you like?")
		if answ == "h":
			print "Commands:"
			print "'h' - Displays this help"
			print "'b' - Change Brush"
			print "'s' - Save Map"
			print "'x' - Chage Brush Size"
			print "'t' - Teleport Camera"
			print "'m' - Toggle mini-map"
			print "'n' - Redraw mini-map and big-map"
		if answ == "b":
			bk = True #Change Brush
		if answ == "s":
			sv = True
		if answ == "t":
			cx = input("New Camera X: ")*tilepix
			cy = input ("New Camera Y: ")*tilepix
		if answ == "x":
			bs = input("New Brush Size: ")
		inkey = False
		if answ == "m":
			tmini = True
		if answ == "n":
			redomap()
	if bk == True:
		brush = int(input("What brush would you like?: "))
		print "Brush changed to ",
		print brush
		bk = False
	if sv == True:
		fname = "map.txt"
		savefile = file(os.path.join("/home/casey/Programming/archive2/Map Maker/data/",fname), 'w')
		print >> savefile, worldwidth
		print >> savefile, worldheight
		for wy in range(0, worldheight):	
			for wx in range(0,worldwidth):
				print >> savefile, maparray[wy][wx]
		savefile.close()
		print "...saved"
		svd = True
		sv = False
	man = True
	if tmini ==True:
		if togmini==1:
			if man ==True:
				togmini=2
				mini = False
				big = False
				man = False
		if togmini==2:
			if man ==True:
				togmini=3
				mini = True
				big = False
				man = False
		if togmini==3:
			if man ==True:
				togmini=1
				mini = False
				big = True
				man = False
	tmini = False
	#Exit
	if ex == True:
		print "CHECK IF YOU SAVED!!"
		answ = raw_input("Do you want to exit?")
		if answ == "y": exit(0)
		ex = False
	#Palette
	if palette == True:
		#Save Button
		if svd == True: sc = (250, 250, 250)
		if svd == False: sc = (250, 0, 0)
		screen.blit(font2.render("Save", 1, sc), (resx+20,0))
		pygame.draw.rect(screen, (250,250,250),(resx+15,5,55,20),1)
		if msdown == True:
			if mousepos[0] >= resx+15 and mousepos[0] <=resx+15+55 and mousepos[1] >= 5 and mousepos[1] <=5+20:
				sv = True
		#Brush Display
		screen.blit(font2.render("Brush", 1, (250, 250, 250)), (resx+10,65))
		screen.blit(spriten[brush].image, (resx+25, 100))
		pygame.draw.rect(screen, (250,0,0),(resx+25-5,100-5,tilepix+10,tilepix+10),3)
		#Palette
		screen.blit(font2.render("Palette", 1, (250, 250, 250)), (resx+5,140))
		pla = 0
		for plt in range(pts, spritenum-1):
			pla+=1
			if pla >15: pla = 15
			screen.blit(spriten[plt].image, (resx+25, 150+(pla*tilepix)+(pla*3)))
			#Select
			if msdown == True:
				if mousepos[0] >= resx+25 and mousepos[0] <=resx+25+tilepix and mousepos[1] >= 150+(pla*tilepix)+(pla*3) and mousepos[1] <=150+(pla*tilepix)+(pla*3)+tilepix: brush = plt
		#Scroll
		pygame.draw.rect(screen, (250,250,250),(resx+10,168,65,12),1)
		screen.blit(font2.render("^", 1, (250, 250, 250)), (resx+38,165))
		if mousepos[0] >= resx+10 and mousepos[0] <=resx+10+65 and mousepos[1] >= 160 and mousepos[1] <=160+12:
			pts -=1
			if pts <=1: pts = 1
		pygame.draw.rect(screen, (250,250,250),(resx+10,716,65,12),1)
		screen.blit(font3.render("v", 1, (250, 250, 250)), (resx+38,714))
		if mousepos[0] >= resx+10 and mousepos[0] <=resx+10+65 and mousepos[1] >= 716 and mousepos[1] <=716+15:
			pts +=1
			if pts >= spritenum-15: pts = spritenum-15
	#Mini-Map
	if mini == True:
		screen.blit(sp_minimap.image, ((resx-210), (resy-230)))
		pygame.draw.rect(screen, (250,0,0),(((resx-210)+((cx+(screenwidth))/tilepix)),((resy-230)+((cy+(screenheight))/tilepix)),screenwidth,screenheight),1)
	#Big Map
	if lbr == False:
		if big == True:
			for mmy in range(0, worldheight):
				for mmx in range (0, worldwidth):
					if maparray[mmy][mmx] == 6:
						screen.set_at((mmx,mmy),(0,0,250))
					else: 
						screen.set_at((mmx,mmy),(0,250,0))
	#Draw the "Player"
	plx = ((tilepix*screenwidth)/2)-15
	ply = (tilepix*screenheight)/2
	screen.blit(player_sprite.image, (plx, ply))
	#Update Screen
	pygame.display.flip()	
	#Framerate
	clock.tick(40)
