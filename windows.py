#!/usr/bin/env python
#Windows
###################
import random, os, pygame, var
from pygame.locals import *
from draw import *


#Tasks
def tasks():
	#Clear Screen
	pygame.draw.rect(var.screen, (0,0,0),(0, 0, var.resx, var.resy),0)

#Create New Window
def createWindow(name, xpos, ypos, width, height):
	var.window[var.winnum][0] = name
	var.window[var.winnum][1] = xpos
	var.window[var.winnum][2] = ypos
	var.window[var.winnum][3] = width
	var.window[var.winnum][4] = height
	var.window[var.winnum][5] = True
	var.window[var.winnum][6] = var.winnum
	var.winnum += 1
#Draw Windows
def drawWindows(z):
	i = var.window[z][6]
	#Main Window
	pygame.draw.rect(var.screen, (112,57,12),(var.window[i][1], var.window[i][2], var.window[i][3], var.window[i][4]),0)
	#TitleBar
	pygame.draw.rect(var.screen, (72,33,0),(var.window[i][1], var.window[i][2], var.window[i][3], var.titlebarheight),0)
	var.screen.blit(var.font20.render(var.window[i][0], 1, (0,0,0)), (var.window[i][1]+5,var.window[i][2]))
	#Outline
	pygame.draw.rect(var.screen, (200,200,200),(var.window[i][1], var.window[i][2], var.window[i][3], var.window[i][4]),1)
	#Output (var.window[0][x]
	if (i==0):
		DrawMap()
		DrawItem()
		DrawGUI()
		DrawDeveloper()
		DrawCharacters()
        #Player (var.window[1][x]
        if (i==1):
		DrawPlayerInfo()
	#Invintory (var.window[2][x]
	if (i==2):
		DrawInvin()
	#Mini Map (var.window[3][x]
	if (i==3):
		DrawMiniMap()
	#World (var.window[4][x]
	if (i==4):
		DrawOutput()

#Move Windows
def moveWindows(i):
	var.winon=False
	#If you are inside the top window
	if (var.mousepos[0]>=var.window[var.winnum-1][1] and var.mousepos[0]<=var.window[var.winnum-1][1]+var.window[var.winnum-1][3] 
			and var.mousepos[1]>=var.window[var.winnum-1][2] and var.mousepos[1]<=var.window[var.winnum-1][2]+var.window[var.winnum-1][4]):
		var.winon=True
	#If currently selected window is up, or your mouse is not in that window (for others)
	if (i == var.winnum-1) or (var.winon==False):
		#If button is down, you are not "moving", and you are in the window
		if (var.wins==-1 and var.msdown==True and var.mousepos[0]>=var.window[i][1] and var.mousepos[0]<=var.window[i][1]+var.window[i][3] 
				and var.mousepos[1]>=var.window[i][2] and var.mousepos[1]<=var.window[i][2]+var.window[i][4]):
			#If you are in the title bar
			if (var.mousepos[1]<=var.window[i][2]+var.titlebarheight):
				var.xboff = var.window[i][1] - var.mousepos[0]
				var.yboff = var.window[i][2] - var.mousepos[1]
				var.wins = i
				#re-order windows
				#temp = var.draw_win[i]
				#var.draw_win[i] = var.draw_win[var.winnum-1]
				#var.draw_win[var.winnum-1] = temp
		if var.msdown==True and var.wins == i:
			var.window[i][1] = var.mousepos[0]+var.xboff
			var.window[i][2] = var.mousepos[1]+var.yboff
		if var.msdown==False:
			var.wins = -1
			var.xboff = 0
			var.yboff = 0
#Window Tasks
def windowTasks():
	for i in range (0, var.winnum):
		j = var.draw_win[i]
		if (var.window[j][5]==True):
			drawWindows(j)
			moveWindows(j)
#Task Bar
def taskBar():
	#Draw Task Bar
	pygame.draw.rect(var.screen, (230,230,230),(0, var.resy-var.taskbarheight, var.resx, var.taskbarheight),0)
	for i in range(0, var.winnum):
		tx = i*1.1*var.tasksize
		ty = var.resy-var.taskbarheight+5
		tw = var.tasksize
		th = var.taskbarheight-5
		#Draw Tasks
		pygame.draw.rect(var.screen, (100,100,100),(tx, ty, tw, th),0)
		var.screen.blit(var.font10.render(var.window[i][0], 1, (250,250,250)), (tx+5, ty+5))
		#Mouse Tasks
		if (var.msclick ==1 and var.mousepos[0]>=tx and var.mousepos[0]<=tx+tw and var.mousepos[1]>=ty and var.mousepos[1]<=ty+th):
			#min/max
			if var.window[i][5]==True:
				var.window[i][5]=False
			else:
				var.window[i][5]=True
	


#Main
def windowAll():
	tasks()
	windowTasks()
	taskBar()
