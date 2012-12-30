#!/usr/bin/env python
import os, var
from construct import *
##################
#NOTES
#################
#Draw Box: 	pygame.draw.rect(var.screen, (R,G,B),(X,Y,w,h),1)
#Draw Text:	var.screen.blit(var.font20.render("TEXT", 1, (R,G,B)), (X,Y))
#
#
#################
#######
#Draw
#######

#Map
def DrawMap():
	if var.battle == False:
		#Draw map
		for layY in range(0,var.screenheight):
			dy = (layY*var.tilepix)+var.titlebarheight
			for layX in range(0,var.screenwidth):
				dx = layX*var.tilepix
				for sn in range (1, var.spritenum):
					if var.maparray[layY+(var.cy/var.tilepix)][layX+(var.cx/var.tilepix)] == sn:
						var.screen.blit(var.spriten[sn].image, (var.window[0][1]+dx, var.window[0][2]+dy))

#Items
def DrawItem():
	#Draw the Items
	for layY in range(0,var.screenheight):
		dy = layY*var.tilepix
		for layX in range(0,var.screenwidth):
			dx = layX*var.tilepix
			if var.itemarray[layY+(var.cy/var.tilepix)][layX+(var.cx/var.tilepix)] != []: 
				var.screen.blit(var.itemarray[layY+(var.cy/var.tilepix)][layX+(var.cx/var.tilepix)][0].image, (dx, dy))

#GUI
def DrawGUI():
	#GUI
	#var.screen.blit(var.sidebar.image, (800, 0)) #var.sidebar
	#var.screen.blit(var.textbar.image, (0, 640)) #var.textbar
	#Alchemy
	if var.alc == True:
		var.screen.blit(var.alca.image, (200, 200))
#Output
def DrawOutput():
	var.screen.blit(var.font20.render(var.text[0], 1, (0,0,0)), (var.window[4][1]+15,var.window[4][2]+29))
	var.screen.blit(var.font20.render(var.text[1], 1, (0,0,0)), (var.window[4][1]+15,var.window[4][2]+53))
	var.screen.blit(var.font20.render(var.text[2], 1, (0,0,0)), (var.window[4][1]+15,var.window[4][2]+77))
	var.screen.blit(var.font20.render(var.text[3], 1, (0,0,0)), (var.window[4][1]+15,var.window[4][2]+101))
	#varscreen.blit(var.font20.render(var.text[4], 1, (0,0,0)), (var.window[4][1]+15,var.window[4][2]+135))
#Player Info
def DrawPlayerInfo():
	var.screen.blit(var.font20.render(var.p_name +" ~ "+ var.p_class, 1, (250,250,250)), (var.window[1][1]+5,var.window[1][2]+25))#Name/Class
	var.screen.blit(var.class_icon.image, (var.window[1][1]+5,var.window[1][2]+40)) #Class Icon
	var.screen.blit(var.font20.render(str(var.p_hp) +" / "+ str(var.p_mhp), 1, (250,0,0)), (var.window[1][1]+85,var.window[1][2]+40))#Hit Points
	var.screen.blit(var.font20.render(str(var.p_mp) +" / "+ str(var.p_mmp), 1, (0,0,250)), (var.window[1][1]+85,var.window[1][2]+58))#Magic Points
	var.screen.blit(var.font20.render("$"+str(var.p_gold), 1, (210,200,50)), (var.window[1][1]+85,var.window[1][2]+76))#Gold
#######
#Draw invintory
#######
def DrawInvin():
	var.screen.blit(var.invin_player.image, (var.window[2][1]+2, var.window[2][2]+22)) #Player Equip
	var.screen.blit(var.belt.image, (var.window[2][1]+12, var.window[2][2]+400)) #Player var.belt1
	var.screen.blit(var.belt.image, (var.window[2][1]+12, var.window[2][2]+435)) #Player var.belt2
	for bi in range(0,22):
		if var.invint[bi]!=[]:
			if bi <=9:
				if bi <=4: 
					pygame.draw.rect(var.screen, (0,0,0),(var.window[2][1]+14+(bi*35), var.window[2][2]+402, 32, 32),0)
					var.screen.blit(var.invint[bi][0].image, (var.window[2][1]+14+(bi*35), var.window[2][2]+402))
				if bi <=9 and bi >= 5:
					pygame.draw.rect(var.screen, (0,0,0),(var.window[2][1]+14+((bi-5)*35), var.window[2][2]+437, 32, 32),0)
					var.screen.blit(var.invint[bi][0].image, (var.window[2][1]+14+((bi-5)*35), var.window[2][2]+437))
			else:
				if bi == 10: 
					pygame.draw.rect(var.screen, (0,0,0),(var.window[2][1]+22, var.window[2][2]+33, 32, 32),0)
					var.screen.blit(var.invint[bi][0].image, (var.window[2][1]+22, var.window[2][2]+33))
				if bi == 11: 
					pygame.draw.rect(var.screen, (0,0,0),(var.window[2][1]+22, var.window[2][2]+73, 32, 32),0)
					var.screen.blit(var.invint[bi][0].image, (var.window[2][1]+22, var.window[2][2]+73))
				if bi == 12: 
					pygame.draw.rect(var.screen, (0,0,0),(var.window[2][1]+152, var.window[2][2]+72, 32, 32),0)
					var.screen.blit(var.invint[bi][0].image, (var.window[2][1]+152, var.window[2][2]+72))
				if bi == 13: 
					pygame.draw.rect(var.screen, (0,0,0),(var.window[2][1]+15, var.window[2][2]+227, 32, 32),0)
					var.screen.blit(var.invint[bi][0].image, (var.window[2][1]+15, var.window[2][2]+227))
				if bi == 14: 
					pygame.draw.rect(var.screen, (0,0,0),(var.window[2][1]+15, var.window[2][2]+265, 32, 32),0)
					var.screen.blit(var.invint[bi][0].image, (var.window[2][1]+15, var.window[2][2]+265))
				if bi == 15: 
					pygame.draw.rect(var.screen, (0,0,0),(var.window[2][1]+152, var.window[2][2]+219, 32, 32),0)
					var.screen.blit(var.invint[bi][0].image, (var.window[2][1]+152, var.window[2][2]+219))
				if bi == 16: 
					pygame.draw.rect(var.screen, (0,0,0),(var.window[2][1]+152, var.window[2][2]+256, 32, 32),0)
					var.screen.blit(var.invint[bi][0].image, (var.window[2][1]+152, var.window[2][2]+256))
				if bi == 17: 
					pygame.draw.rect(var.screen, (0,0,0),(var.window[2][1]+160, var.window[2][2]+302, 32, 32),0)
					var.screen.blit(var.invint[bi][0].image, (var.window[2][1]+160, var.window[2][2]+302))
				if bi == 18: 
					pygame.draw.rect(var.screen, (0,0,0),(var.window[2][1]+87, var.window[2][2]+366, 32, 32),0)
					var.screen.blit(var.invint[bi][0].image, (var.window[2][1]+87, var.window[2][2]+366))
				if bi == 19: 
					var.screen.blit(var.invint[bi][0].image, (322, 249))
				if bi == 20: 
					var.screen.blit(var.invint[bi][0].image, (499, 249))
				if bi == 21: 
					var.screen.blit(var.invint[bi][0].image, (415, 379))
	#On Mouse
	if var.imouse!= []:
		var.screen.blit(var.imouse[0].image, (var.mousepos[0], var.mousepos[1]))

#######
#Draw Mini Map / Statistics
#######
def DrawMiniMap():
	var.screen.blit(var.arrow.image, (var.window[3][1]+50, var.window[3][2]+10)) #var.arrow
	#Map
	if var.gmap == 1:
		var.screen.blit(var.p_minimap.image, ((var.window[3][1]+1), (var.window[3][2]+var.titlebarheight))) #map
		pygame.draw.rect(var.screen, (250,0,0),(((var.window[3][1])+((var.cx+(var.screenwidth))/var.tilepix)),((var.titlebarheight+var.window[3][2])+((var.cy+(var.screenheight))/var.tilepix)),25,20),1)
	#Stats
	if var.gmap == 2:
		pygame.draw.rect(var.screen, (0,0,0),((var.window[3][1]+1), (var.window[3][2]+var.titlebarheight), 200, 200),0)
		var.screen.blit(var.font20.render("Statistics", 1, (250,250,250)), ((var.window[3][1]+5),(var.window[3][2]+var.titlebarheight)))
		var.screen.blit(var.font20.render("Level: "+ str(var.p_lvl), 1, (250,250,250)), ((var.window[3][1]+5),(var.window[3][2]+var.titlebarheight+22)))
		var.screen.blit(var.font20.render("Experience: "+ str(var.p_exp), 1, (250,250,250)), ((var.window[3][1]+5),(var.window[3][2]+var.titlebarheight+44)))
		var.screen.blit(var.font20.render("Attack: "+ str(var.p_atk), 1, (250,250,250)), ((var.window[3][1]+5),(var.window[3][2]+var.titlebarheight+66)))
		var.screen.blit(var.font20.render("Defense: "+ str(var.p_lvl), 1, (250,250,250)), ((var.window[3][1]+5),(var.window[3][2]+var.titlebarheight+88)))
		var.screen.blit(var.font20.render("Fire Def: "+ str(var.p_fdef), 1, (250,250,250)), ((var.window[3][1]+5),(var.window[3][2]+var.titlebarheight+110)))
		var.screen.blit(var.font20.render("Water Def: "+ str(var.p_wdef), 1, (250,250,250)), ((var.window[3][1]+5),(var.window[3][2]+var.titlebarheight+132)))
		var.screen.blit(var.font20.render("Lightning Def: "+ str(var.p_ldef), 1, (250,250,250)), ((var.window[3][1]+5),(var.window[3][2]+var.titlebarheight+154)))
	#Skills
	if var.gmap == 3:
		pygame.draw.rect(var.screen, (0,0,0),((var.window[3][1]+1), (var.window[3][2]+var.titlebarheight), 200, 200),0)
		var.screen.blit(var.font20.render("Skills", 1, (250,250,250)), ((var.window[3][1]+5),(var.window[3][2]+var.titlebarheight)))
		var.screen.blit(var.font20.render("Blade: "+ str(var.p_bld), 1, (250,250,250)), ((var.window[3][1]+5),(var.window[3][2]+var.titlebarheight+22)))
		var.screen.blit(var.font20.render("Magic: "+ str(var.p_arm), 1, (250,250,250)), ((var.window[3][1]+5),(var.window[3][2]+var.titlebarheight+44)))
		var.screen.blit(var.font20.render("Armor: "+ str(var.p_arm), 1, (250,250,250)), ((var.window[3][1]+5),(var.window[3][2]+var.titlebarheight+66)))
		var.screen.blit(var.font20.render("Alchemy: "+ str(var.p_alc), 1, (250,250,250)), ((var.window[3][1]+5),(var.window[3][2]+var.titlebarheight+88)))
#######
#Draw Characters
#######
def DrawCharacters():
	var.ppx = (var.cx/var.tilepix)+(var.plx/var.tilepix)
	var.ppy = (var.cy/var.tilepix)+(var.ply/var.tilepix) 
	#Player
	if var.alc == False: #Don't draw in Alchemy mode
		var.screen.blit(var.player_sprite.image, (var.plx, var.ply))
	#Player in Forrest
	if var.maparray[var.ppy][var.ppx] >= 45 and var.maparray[var.ppy][var.ppx] <= 49:
		var.screen.blit(var.f_player_sprite.image, (var.plx, var.ply))
	#Player in bed
	if var.maparray[var.ppy][var.ppx] == 100:
		var.screen.blit(var.bd_player_sprite.image, (var.plx, var.ply))
#######
#Draw Developer
#######
def DrawDeveloper():
	if var.dev == True:
		var.screen.blit(var.font30.render("Cam  Pos: "+str(var.cx/var.tilepix)+", "+str(var.cy/var.tilepix), 1, (255,255,255)), (0,0))
		var.screen.blit(var.font30.render("Mouse Pos: "+str(var.mousepos[0])+", "+str(var.mousepos[1]), 1, (255,255,255)), (0,30))
