#!/usr/bin/env python
#Create Map
#-------------------
#IMPORT
import os
#------------
#Main
#------------
fname = "map.txt"
print "Map Creator. Generates a Blank Map"
worldwidth = raw_input("Width of Map: ")
worldheight = raw_input("Height of Map: ")
spritenum = raw_input ("Tile Fill Number: ")
#Generate Array
maparray=[]
for cm1y in range(int(worldheight)):
	maparray.append([])
	for cm1x in range(int(worldwidth)):
   		maparray[cm1y].append(cm1y*cm1x)
#Set all in array to spritenum
for cm2y in range(0,int(worldheight)):
	for cm2x in range(0,int(worldwidth)):
		maparray[cm2y][cm2x] = int(spritenum)
#Save
fname = "map.txt"
savefile = file(os.path.join("/home/casey/Desktop/programming/Map Maker/data",fname), 'w')
print >> savefile, worldwidth
print >> savefile, worldheight
for wy in range(0, int(worldheight)):	
	for wx in range(0,int(worldwidth)):
		print >> savefile, maparray[wy][wx]
savefile.close()
print "...saved"
exit(0)
