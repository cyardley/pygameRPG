#!/usr/bin/env python
#MAP MAKER
###################
#Resources:
#Read/Write to File: http://www.techniqal.com/blog/2005/05/17/python-simple-file-read-and-write/
###################
import random
import os, pygame
from pygame.locals import *
#Variables
mode = 2               #Modes
fname = "map.txt"           #1=Make Blank Map
worldwidth = 1000            #2=Read from Map File
worldheight = 1000
tilepix = 32
screenwidth = 1100/tilepix
screenheight = 800/tilepix
resx = tilepix*screenwidth
resy = tilepix*screenheight
cx = 5
cy = 5
msdown = False
pdir = 0
brush = 1
inkey = False
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
        self.image = pygame.image.load(os.path.join('images',fname))
        self.image = self.image.convert()
        self.image.set_colorkey((255,0,255)) #HEX: 00ff00
        self.rect = self.image.get_rect()
        self.rect.topleft = initial_position
#Generate Array
maparray=[]
for cm1y in range(worldheight):
    maparray.append([])
    for cm1x in range(worldwidth):
        maparray[cm1y].append(cm1y*cm1x)
#Read or Write
if mode == 1: #Make blank Map File
    readfile = file(os.path.join("data",fname), 'r')
    worldwidth = int(readfile.readline())
    worldheight = int(readfile.readline())
    spritenum = int(readfile.readline())
    for cm2y in range(0,worldheight):
        for cm2x in range(0,worldwidth):
            maparray[cm2y][cm2x] = spritenum
    readfile.close()
    fname = "map.txt"
    savefile = file(os.path.join("data",fname), 'w')
    print >> savefile, worldwidth
    print >> savefile, worldheight
    print >> savefile, spritenum
    print >> savefile, tilepix
    for wy in range(0, worldheight):    
        for wx in range(0,worldwidth):
            print >> savefile, maparray[wy][wx]
    savefile.close()
    print "...saved"
    exit(0)
if mode == 2: # Read from Map File
    readfile = file(os.path.join("data",fname), 'r')
    worldwidth = int(readfile.readline())
    worldheight = int(readfile.readline())
    spritenum = int(readfile.readline())
    tilepix = int(readfile.readline())
    spriten = []
    for sl in range (0,spritenum):
        spriten.append([])
    for rs in range (1, spritenum):
        spriten[rs] = Sprite(str(rs)+".png",[0, 0])
    for ry in range(0, worldheight):    
        for rx in range(0,worldwidth):
            maparray[ry][rx] = int(readfile.readline())
    readfile.close()
################
## Main Loop  ##
################
print "Map Editor by Casey Yardley"
print "Click to edit map"
print "Space for advanced options (appear in this window)"
print "'b' to quick change brush type"
bk = False
emrand = 1
pygame.mouse.set_visible(1)
screen.fill((0, 0, 0))
clock = pygame.time.Clock()
run = True
while run == True:
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
            if event.key == K_LEFT: pdir = 3
            if event.key == K_RIGHT: pdir = 4
            #Input
            if event.key == K_SPACE: inkey = True
            if event.key == K_b: bk = True
        if event.type == KEYUP:
            pdir = 0
        #X button
        if event.type == QUIT: 
            exit(0) 
        #Mouse
        mousepos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            msdown = True
        if event.type == pygame.MOUSEBUTTONUP:
            msdown = False
    #Movement
    if pdir == 1: 
        if cy >1: cy -= tilepix
    if pdir == 2: 
        if cy+(screenheight*tilepix) < worldheight*tilepix: cy += tilepix
    if pdir == 3: 
        if cx > 1: cx -= tilepix
    if pdir == 4: 
        if cx+(screenwidth*tilepix) < worldwidth*tilepix: cx += tilepix
    #Paint
    if msdown == True:
        maparray[(cy+mousepos[1])/tilepix][(cx+mousepos[0])/tilepix] = brush
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
    pygame.display.set_caption("|Map Maker| |Brush: "+str(brush) +" | |Cam Pos: "+ str(cx/tilepix)+", "+str(cy/tilepix)+"|")
    #Inkey
    if inkey == True:
        print "Type 'h' for help"
        answ = raw_input("What would you like?")
        if answ == "h":
            print "Commands:"
            print "'h' - Displays this help"
            print "'b' - Change Brush"
            print "'s' - Save Map"
        if answ == "b":
            brush = int(raw_input("What brush would you like?: "))
            print "Brush changed to ",
            print brush
        if answ == "s":
            fname = "map.txt"
            savefile = file(os.path.join("data",fname), 'w')
            print >> savefile, worldwidth
            print >> savefile, worldheight
            print >> savefile, spritenum
            print >> savefile, tilepix
            for wy in range(0, worldheight):    
                for wx in range(0,worldwidth):
                    print >> savefile, maparray[wy][wx]
            savefile.close()
            print "...saved"
        inkey = False
    if bk == True:
        brush = int(raw_input("What brush would you like?: "))
        print "Brush changed to ",
        print brush
        bk = False
    #Update Screen
    pygame.display.flip()   
    #Framerate
    clock.tick(40)
