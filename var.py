#!/usr/bin/env python
import random, os, pygame
from construct import *
from pygame.locals import *
from windows import *

dev = True
ninjafont = False

#######
#Global Variables
#######

#Game
run = True
movemeth1=False
inkey = False
battle = False
movin = True
gmap = 1
bstat = 1
turn = 0
alc = False

maparray=[]
itemarray=[]
worldwidth=0
worldheight=0
minimap = pygame.Surface((200, 200))

#Load from Image File
fname = "tileset.txt"
readfile = file(os.path.join("images/tiles",fname), 'r')
spritenum = int(readfile.readline())
tilepix = int(readfile.readline())
readfile.close()

#Screen
resx = 800
resy = 640
screenwidth = 824/tilepix
screenheight = 668/tilepix
cx = 16*tilepix
cy = 21*tilepix

#inint
pygame.init()
(6,0)
screen = pygame.display.set_mode((resx, resy))
pygame.display.set_caption('EPIC GAME ...loading')
pygame.mouse.set_visible(1)
clock = pygame.time.Clock()
mousepos = pygame.mouse.get_pos()
#Mouse
msdown = False
imouse = []
msclick= 0
mrdown = False
mousepos = pygame.mouse.get_pos()
#Window
#0=Name, 1=xpos, 2=ypos, 3=width, 4=height, 5=satus, 6=order
window = []
winmax = 10
wins = -1
xboff = 0
yboff = 0
titlebarheight = 30
for wind in range(winmax):
	window.append([])
	for cm1x in range(7):
		window[wind].append([])
winnum = 0

#Taskbar
taskbarheight = 30
tasksize = 60
#Player
ky_u = False
ky_d = False
ky_l = False
ky_r = False
ppx = 0
ppy = 0
pspeed = tilepix
pbuffer = 5
plx = ((tilepix*screenwidth)/2)-15
ply = (tilepix*screenheight)/2
dire = ""

wld_x = cx
wld_y = cy
loc_x = 0
loc_y = 0
#Players Stats
p_name = "Hero"
p_class = "Warrior"
p_gold = 0
p_hp = 100
p_mhp = 100
p_mp = 100
p_mmp = 100
p_lvl = 1
p_exp = 0
p_atk = 10
p_def = 10
p_fdef = 10
p_wdef = 10
p_ldef = 10
p_bld = 10
p_mgk = 10
p_arm = 10
p_alc = 10

#World
location = "world"

#######
#Set Up Sprites
######
#Map
spriten = []
for sl in range (0,spritenum):
	spriten.append([])
for rs in range (1, spritenum):
	spriten[rs] = Sprite("tiles/"+str(rs)+".png")
#Characters
player_sprite = Sprite("player.png")
f_player_sprite = Sprite("fplayer.png")
bd_player_sprite = Sprite("bdplayer.png")
#GUI
sidebar = Sprite("sidebar.png")
textbar = Sprite("textbar.png")
arrow = Sprite("gui_arrow.png")
alca = Sprite("gui_alc.png")
class_icon = Sprite("class_icon.png")
invin_player = Sprite("warrior.png")
belt = Sprite("belt.png")
b_b1 = Sprite("b_1.png")
b_b2 = Sprite("b_2.png")
b_b3 = Sprite("b_3.png")
b_b4 = Sprite("b_4.png")
b_b5 = Sprite("b_5.png")
b_attack = Sprite("gui_attack.png")
b_slash = Sprite("b_slash.png")
b_magic = Sprite("gui_magic.png")
b_spell = Sprite("b_spell.png")


#######
#Fonts
#######
font = "Purisa.ttf"
if ninjafont == True:
	font = "NINJAS.TTF"
font50 = pygame.font.Font(os.path.join("data/",font), 50)#big
font30 = pygame.font.Font(os.path.join("data/",font), 30)#normal
font20 = pygame.font.Font(os.path.join("data/",font), 20)#small
font10 = pygame.font.Font(os.path.join("data/",font), 10)#tiny

######
#Items
######
#[Sprite(0), Type(1), Name(2), Strength(3), Value(4), Effect(5)]
#Potions
i_healthpotion = [Sprite("i_HP.png"), "potion", "Health Potion", 15, 50, "Restore HP"]
i_magicpotion = [Sprite("i_MP.png"), "potion", "Magic Potion", 15, 50, "Restore MP"]
#Helms
i_ironhelm = [Sprite("i_ironhelm.png"), "helm", "Iron Helm", 10, 75, "None"]
#Pendants
i_rubypendant = [Sprite("i_rubypendant.png"), "pendant", "Ruby Pendant", 0, 100, "Fire"]
i_emeraldpendant = [Sprite("i_emeraldpendant.png"), "pendant", "Emerald Pendant", 0, 100, "Poison"]
#Shirts
i_gcottonshirt = [Sprite("i_gcottonshirt.png"), "shirt", "Green Cotton Shirt", 1, 10, "None"]
#Weapons
i_ironsword = [Sprite("i_ironsword.png"), "weapon", "Iron Sword", 10, 100, "None"]
#Shields
i_ironshield = [Sprite("i_ironshield.png"), "shield", "Iron Shield", 5, 75, "None"]
#Rings
i_goldring = [Sprite("i_goldring.png"), "ring", "Ruby Ring", 50, 5, "Personality"]
#Pants
i_bpants = [Sprite("i_bpants.png"), "pants", "Brown Pants", 2, 10, "None"]
#Shoes
i_letherboots = [Sprite("i_letherboots.png"), "shoes", "Leather Boots", 4, 5, "None"]
#Ingredients
i_leaf = [Sprite("i_leaf.png"), "ingredient", "Leaf", 1, 1, "None"]
i_mushroom = [Sprite("i_mushroom.png"), "ingredient", "Mushroom", 1, 1, "Ingredient"]
i_rflower = [Sprite("i_rflower.png"), "ingredient", "Red Flower", 1, 1, "Ingredient"]
i_bflower = [Sprite("i_bflower.png"), "ingredient", "Blue Flower", 1, 1, "Ingredient"]
#Alchemy
i_mortar = [Sprite("i_mortar.png"), "alchemy", "Mortar & Pestal", 0, 10, "Alchemy"]
#Misc 
i_fork = [Sprite("i_fork.png"), "misc", "Fork", 0, 1, "None"]
#Invintory ("invint" array)
#0= belt 1-1	#5= belt 2-1 	#10=Head	#15= L. Hand	#20= Alchemy 2
#1= belt 1-2	#6= belt 2-2 	#11=Neck	#16= L. Finger	#21= Alchemy Out
#2= belt 1-2	#7= belt 2-3	#12=Chest	#17= Legs
#3= belt 1-3	#8= belt 2-4	#13=R. Hand	#18= Feet
#4= belt 1-4	#9= belt 2-5	#14=R. Finger	#19= Alcemy 1
invint =[i_mushroom, i_mortar, i_rflower, i_bflower, i_mushroom, [], i_magicpotion, [], i_healthpotion, i_magicpotion, i_ironhelm, i_rubypendant, i_gcottonshirt, [], i_goldring, i_ironshield, [], i_bpants, i_letherboots, [], [], []]

#text
text= ["Text1", "Text2 ", "Text3", "Text4", "Text5"]

######
#Enemies
######
#[Sprite(0), Name(1), HP(2), ATK(3), EXP(4), GOLD(5)] 
e_monster1 = [Sprite("e_monster1.png"), "Evil Tree", 50, 15, 10, 50]

enemy = e_monster1
######
#Attacks/Spells
######
#Attacks
atk1 = [random.randint(210, 590), random.randint(80, 350), random.randint(210, 590), random.randint(80, 350), random.randint(210, 590), random.randint(80, 350), random.randint(210, 590), random.randint(80, 350), random.randint(210, 590), random.randint(80, 350)]
#Spells
spl1 = [random.randint(210, 590), random.randint(80, 350), random.randint(210, 590), random.randint(80, 350), random.randint(210, 590), random.randint(80, 350), random.randint(210, 590), random.randint(80, 350), random.randint(210, 590), random.randint(80, 350)]

#######
#Initialize Windows
#######
#Create windows: createWindow(name, x-pos, y-pos, width, height)
#[0]World
createWindow("World", 0, -taskbarheight, screenwidth*tilepix, (screenheight*tilepix)+taskbarheight)
#[1]Player
createWindow("Player", 300, 30, 200, 100)
#[2]Invintory
createWindow("Invintory", 0,0,200,475)#screenwidth*tilepix, 100, resx-(screenwidth*tilepix), 450)
#[3]Map
createWindow("Map", 200, 250, 202, 200+titlebarheight+1)
#[4]Output
createWindow("Output", 0, 400, screenwidth*tilepix, 125)
draw_win = [0,1,2,3,4]

