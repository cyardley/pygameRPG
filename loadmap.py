#!/usr/bin/env python
import os, var
#######
#Load a Map from File
#######
def loadMap(fname):
	var.maparray=[]
	var.itemarray=[]
	#Load from Map File
	readfile = file(os.path.join("data/maps",fname), 'r')
	var.worldwidth = int(readfile.readline())
	var.worldheight = int(readfile.readline())
	#######
	#Generate Array
	#######
	for cm1y in range(var.worldheight):
		var.maparray.append([])
		var.itemarray.append([])
		for cm1x in range(var.worldwidth):
	   		var.maparray[cm1y].append([])
			var.itemarray[cm1y].append([])

	#######
	#Read Map from File
	#######
	for ry in range(0, var.worldheight):	
		for rx in range(0,var.worldwidth):
			var.maparray[ry][rx] = int(readfile.readline())
	readfile.close()
