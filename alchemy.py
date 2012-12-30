#!/usr/bin/env python
import random, os, pygame, var
from pygame.locals import *
from construct import *

#Alchemy

def alchemy():
	#Close
		if var.alc == True:
			if var.mousepos[0]>=589 and var.mousepos[0]<=589+20 and var.mousepos[1]>=241 and var.mousepos[1]<=241+20 and var.invint[19]==[] and var.msclick==True and var.invint[19]==[] and var.invint[20]==[] and var.invint[21]==[]:
				var.alc = False
				var.movin = True
			#Mix
			if var.mousepos[0]>=405 and var.mousepos[0]<=405+56 and var.mousepos[1]>=295 and var.mousepos[1]<=295+63 and var.msclick==True:
				print "Alchemy"
				nomix = True
				#Health Potion
				if (var.invint[19]==var.i_mushroom and var.invint[20]==var.i_rflower) or (var.invint[19]==var.i_rflower and var.invint[20]==var.i_mushroom):
					var.invint[19]=[]
					var.invint[20]=[]
					var.invint[21]=var.i_healthpotion
					nomix= False
					UpdateText("You make a Health Potion!", var.text)
				#Magic Potion
				if (var.invint[19]==var.i_mushroom and var.invint[20]==var.i_bflower) or (var.invint[19]==var.i_bflower and var.invint[20]==var.i_mushroom):
					var.invint[19]=[]
					var.invint[20]=[]			
					var.invint[21]=var.i_magicpotion
					nomix= False
					UpdateText("You make a Magic Potion!", var.text)
				#Mix does not work
				if nomix==True:
					UpdateText("You do not have ingredients for a potion.", var.text)
