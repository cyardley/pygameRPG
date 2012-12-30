#!/usr/bin/env python
import random, os, pygame, var
from pygame.locals import *
from construct import *

#######
#Battle
#######
#Main battle
def battle():
	if var.battle == True:
		if var.bstat == 1: #Setup
			var.enemy = var.e_monster1 #Random This Later
			UpdateText("A "+var.enemy[1]+" attacks you!", var.text)
			var.e_mhp = var.enemy[2]
			var.e_hp = var.enemy[2]
			var.bstat = 2
		if var.bstat == 2:
			pygame.draw.rect(var.screen, (0,0,0),(0, 0, var.screenwidth*var.tilepix, var.screenheight*var.tilepix),0)
			var.screen.blit(var.enemy[0].image, (300, 100))
			var.screen.blit(var.b_attack.image, (100, 500))
			var.screen.blit(var.b_magic.image, (300, 500))
			batYourturn()
			if var.e_hp <= 0:
				var.bstat = 1
				UpdateText("You Win!", var.text)
				UpdateText("Gained "+str(var.enemy[4])+" Experience", var.text)
				var.p_exp += var.enemy[4]
				UpdateText("Received "+str(var.enemy[5])+" gold", var.text)
				var.p_gold += var.enemy[5]
		if var.bstat == 1: 
			var.battle = False
			var.movin = True
#Your Turn
def batYourturn():
	dmg = 0	
	atkd = False
	#Attack
	if var.mousepos[0] >= 100 and var.mousepos[0] <=100+100 and var.mousepos[1] >= 500 and var.mousepos[1] <=500+50 and var.msclick == 1:
		dmg = batBclick(var.atk1, var.b_slash, var.p_bld, False) #(Buttons, attack type, Attack Sprite, Player Damage, Magic?)
		dmg *= var.p_atk
		UpdateText("You attack for "+str(dmg)+" damage", var.text)
		atkd = True
	#Spells
	if var.mousepos[0] >= 300 and var.mousepos[0] <=300+100 and var.mousepos[1] >= 500 and var.mousepos[1] <=500+50 and var.msclick == 1:
		dmg = batBclick(var.spl1, var.b_spell, var.p_mgk, True) #(Buttons, attack type, Attack Sprite, Player Damage, Magic?)
		dmg *= var.p_mgk
		UpdateText("You cast magic for "+str(dmg)+" damage", var.text)
		atkd = True
	#Damage
	var.e_hp -= dmg
	if atkd == True: var.p_hp = batenemyturn()

#Clicking
def batBclick(clk, a_img, pwr, magic):
	var.screen.blit(var.b_b1.image, (clk[0], clk[1]))
	var.screen.blit(var.b_b2.image, (clk[2], clk[3]))
	var.screen.blit(var.b_b3.image, (clk[4], clk[5]))
	var.screen.blit(var.b_b4.image, (clk[6], clk[7]))
	var.screen.blit(var.b_b5.image, (clk[8], clk[9]))
	pygame.display.flip()
	dmg = 0	
	cla = True
	bclST = pygame.time.get_ticks()
	while cla == True:
		var.mousepos = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN: var.msclick = 1
			if event.type == pygame.MOUSEBUTTONUP: var.msclick = 0
		if magic == True: var.msclick = 1
		if var.mousepos[0]>=clk[0] and var.mousepos[0]<=clk[0]+32 and var.mousepos[1]>=clk[1] and var.mousepos[1]<=clk[1]+32 and var.msclick==1 and dmg==0:
			dmg+=1
			var.screen.blit(a_img.image, (clk[0]-16, clk[1]-16))
		if var.mousepos[0]>=clk[2] and var.mousepos[0]<=clk[2]+32 and var.mousepos[1]>=clk[3] and var.mousepos[1]<=clk[3]+32 and var.msclick==1 and dmg==1:
			dmg+=1
			var.screen.blit(a_img.image, (clk[2]-16, clk[3]-16))
		if var.mousepos[0]>=clk[4] and var.mousepos[0]<=clk[4]+32 and var.mousepos[1]>=clk[5] and var.mousepos[1]<=clk[5]+32 and var.msclick==1 and dmg==2:
			dmg+=1
			var.screen.blit(a_img.image, (clk[4]-16, clk[5]-16))
		if var.mousepos[0]>=clk[6] and var.mousepos[0]<=clk[6]+32 and var.mousepos[1]>=clk[7] and var.mousepos[1]<=clk[7]+32 and var.msclick==1 and dmg==3:
			dmg+=1
			var.screen.blit(a_img.image, (clk[6]-16, clk[7]-16))
		if var.mousepos[0]>=clk[8] and var.mousepos[0]<=clk[8]+32 and var.mousepos[1]>=clk[9] and var.mousepos[1]<=clk[9]+32 and var.msclick==1 and dmg==4:
			dmg+=1
			var.screen.blit(a_img.image, (clk[8]-16, clk[9]-16))
		bclNT = pygame.time.get_ticks()
		pygame.draw.rect(var.screen, (250,250,250), (150, 40, 500, 30),0)
		pygame.draw.rect(var.screen, (250,0,0), (150, 40, 500-(((bclNT-bclST)/5)+pwr*10), 30),0)
		pygame.display.flip()
		if bclNT > bclST+((pwr/5)*1000) or dmg == 5:
			cla = False
	return dmg

#var.enemy's turn
def batenemyturn():
	if var.e_hp > 0:
		if var.p_hp <=0: UpdateText("YOU ARE DEAD!! FAIL U n00b!", var.text)#Die
		dmg = var.enemy[3]-((var.p_def+var.p_arm)/2)
		if dmg <= 0:dmg=0 #Cant get healed by crappy monsters
		var.p_hp -= dmg
		UpdateText(var.enemy[1]+" attacks you for "+str(dmg)+" damage", var.text)
	return var.p_hp
