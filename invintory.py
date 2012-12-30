#!/usr/bin/env python
import random, os, pygame, var
from pygame.locals import *
from construct import *

#######
#Invintory
#######

#Management 
def invintory(ip):
	mu = False
	if mu == False:				
		if var.invint[ip] !=[] and var.imouse==[]: #If Item in var.invintory and Mouse Empty
			var.imouse = var.invint[ip]
			var.invint[ip] = []
			mu = True
	minv = False
	if ip <=4: minv = True
	if var.imouse !=[]:
		if ip >=5 and ip <=9 and var.imouse[1] == "potion": minv = True
		if ip == 10 and var.imouse[1] == "helm": minv = True
		if ip == 11 and var.imouse[1] == "pendant": minv = True
		if ip == 12 and var.imouse[1] == "shirt": minv = True
		if ip == 13 and var.imouse[1] == "weapon": minv = True
		if ip == 14 and var.imouse[1] == "ring": minv = True
		if ip == 15 and var.imouse[1] == "shield": minv = True
		if ip == 16 and var.imouse[1] == "ring": minv = True
		if ip == 17 and var.imouse[1] == "pants": minv = True
		if ip == 18 and var.imouse[1] == "shoes": minv = True
		
		if ip == 19 and var.imouse[1] == "ingredient": minv = True
		if ip == 20 and var.imouse[1] == "ingredient": minv = True
	if minv == True:
		if mu == False:
			if var.invint[ip] == [] and var.imouse!=[]: #If var.invintory is empty and Item in Mouse		
				var.invint[ip] = var.imouse
				var.imouse = []
				mu == True
		if mu == False:
			if var.invint[ip]!=[] and var.imouse!=[]: #If var.invintory has item and mouse has item			
				ihld = var.imouse
				var.imouse = var.invint[ip]
				var.invint[ip] = ihld
	return var.imouse
#Mouse 
def minvin(imn, imx, imy):
	if var.mousepos[0] >= imx and var.mousepos[0] <=imx+34 and var.mousepos[1] >= imy and var.mousepos[1] <=imy+34:
		if var.msclick == 1: var.imouse = invintory(imn)
		#Info Over
		if var.invint[imn]!=[] and var.var.gmap==2:
			pygame.draw.rect(var.screen, (0,0,0),((var.resx-210), (var.resy-220), 200, 200),0)#Item Info Header
			var.screen.blit(var.font20.render("Items", 1, (250,250,250)), ((var.resx-145),(var.resy-220)))
			var.screen.blit(var.font20.render("Name: ", 1, (250,250,250)), ((var.resx-210),(var.resy-190)))
			if var.invint[imn][2]!=[]: var.screen.blit(var.font10.render(str(var.invint[imn][2]), 1, (250,250,250)), ((var.resx-130),(var.resy-185)))
			if var.invint[imn][3]!=[]: var.screen.blit(var.font20.render("Power: "+str(var.invint[imn][3]), 1, (250,250,250)), ((var.resx-210),(var.resy-160)))
			if var.invint[imn][4]!=[]: var.screen.blit(var.font20.render("Value: "+str(var.invint[imn][4]), 1, (250,250,250)), ((var.resx-210),(var.resy-130)))
			if var.invint[imn][5]!=[]: var.screen.blit(var.font20.render("Effect: "+str(var.invint[imn][5]), 1, (250,250,250)), ((var.resx-210),(var.resy-100)))
			var.screen.blit(var.invint[imn][0].image, (var.resx-130, var.resy-60))
		#Use Potion
		if var.invint[imn]!=[] and var.invint[imn][1]=="potion" and var.mrdown==True:
			#Health
			if var.invint[imn][2]=="Health Potion":
				var.p_hp+=var.invint[imn][3]
				UpdateText("You drink a health potion, healing "+str(var.invint[imn][3])+" HP", var.text)
				var.invint[imn]=[]
				if var.p_hp>=var.p_mhp: var.p_hp=var.p_mhp
			#Magic
			if var.invint[imn]!=[] and var.invint[imn][2]=="Magic Potion":
				var.p_mp+=var.invint[imn][3]
				UpdateText("You drink a magic potion, restoring "+str(var.invint[imn][3])+" MP", var.text)
				var.invint[imn]=[]
				if var.p_mp>=var.p_mmp: var.p_mp=var.p_mmp
		#Use Mortar and Pestal
		if var.invint[imn]!=[] and var.invint[imn][1]=="alchemy" and var.mrdown==True:
			var.alc = True
			var.movin = False
	return var.imouse
#Mouse Items
def MouseItems():
	if (var.window[2][5]==False): #If window is deactivated.....
		return var.imouse
	if var.gmap == 2: 
		pygame.draw.rect(var.screen, (0,0,0),((var.resx-210), (var.resy-220), 200, 200),0)#Item Info Header
		var.screen.blit(var.font20.render("Items", 1, (250,250,250)), ((var.resx-145),(var.resy-220)))
		#Info imouse
		if var.imouse != []: 
			var.screen.blit(var.font20.render("Name: ", 1, (250,250,250)), ((var.resx-210),(var.resy-190)))
			var.screen.blit(var.font10.render(str(var.imouse[2]), 1, (250,250,250)), ((var.resx-130),(var.resy-185)))
			var.screen.blit(var.font20.render("Power: "+str(var.imouse[3]), 1, (250,250,250)), ((var.resx-210),(var.resy-160)))
			var.screen.blit(var.font20.render("Value: "+str(var.imouse[4]), 1, (250,250,250)), ((var.resx-210),(var.resy-130)))
			var.screen.blit(var.font20.render("Effect: "+str(var.imouse[5]), 1, (250,250,250)), ((var.resx-210),(var.resy-100)))
			var.screen.blit(var.imouse[0].image, (var.resx-130, var.resy-60))
	for bi in range(0,5): var.imouse = minvin(bi, var.window[2][1]+13+(bi*35),var.window[2][2]+401)#var.belt1
	for bi in range(5,10): var.imouse = minvin(bi, var.window[2][1]+13+((bi-5)*35),var.window[2][2]+436)#var.belt2
	var.imouse = minvin(10, var.window[2][1]+22, var.window[2][2]+32)#Head
	var.imouse = minvin(11, var.window[2][1]+21, var.window[2][2]+72)#Neck
	var.imouse = minvin(12, var.window[2][1]+151, var.window[2][2]+71)#Chest
	var.imouse = minvin(13, var.window[2][1]+15, var.window[2][2]+227)#R. Hand
	var.imouse = minvin(14, var.window[2][1]+15, var.window[2][2]+265)#R. Finger
	var.imouse = minvin(15, var.window[2][1]+152, var.window[2][2]+218)#L. Hand
	var.imouse = minvin(16, var.window[2][1]+152, var.window[2][2]+256)#L. Finger
	var.imouse = minvin(17, var.window[2][1]+160, var.window[2][2]+301)#Legs
	var.imouse = minvin(18, var.window[2][1]+87, var.window[2][2]+366)#Feet
	if var.alc == True:
		var.imouse = minvin(19, 321, 248
)
		var.imouse = minvin(20, 499, 248)
		var.imouse = minvin(21, 415, 379)
	return var.imouse
#Drop and Pick up Items
def DropPickItems():
	if var.mousepos[0]>=var.plx-var.tilepix*2 and var.mousepos[0]<=var.plx+var.tilepix*2 and var.mousepos[1]>=var.ply-var.tilepix*2 and var.mousepos[1]<=var.ply+var.tilepix*2 and var.msclick==1 and  var.maparray[(var.cy+var.mousepos[1])/var.tilepix][(var.cx+var.mousepos[0])/var.tilepix]==1 and var.battle == False:
		#Drop
		if var.imouse !=[] and var.itemarray[(var.cy+var.mousepos[1])/var.tilepix][(var.cx+var.mousepos[0])/var.tilepix]==[]:
			var.itemarray[(var.cy+var.mousepos[1])/var.tilepix][(var.cx+var.mousepos[0])/var.tilepix] = var.imouse
			var.imouse = []
		#Pick
		else:
			if var.imouse == []:
				var.imouse = var.itemarray[(var.cy+var.mousepos[1])/var.tilepix][(var.cx+var.mousepos[0])/var.tilepix]
				var.itemarray[(var.cy+var.mousepos[1])/var.tilepix][(var.cx+var.mousepos[0])/var.tilepix] = []
			else: #Switch
				it = var.itemarray[(var.cy+var.mousepos[1])/var.tilepix][(var.cx+var.mousepos[0])/var.tilepix]
				var.itemarray[(var.cy+var.mousepos[1])/var.tilepix][(var.cx+var.mousepos[0])/var.tilepix] = var.imouse
				var.imouse = it
			if var.imouse !=[]: UpdateText("You pick up a "+var.imouse[2], var.text)
