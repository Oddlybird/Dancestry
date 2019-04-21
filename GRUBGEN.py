import random
import json
import os
import re
import libtcodpy as tcod
#getcaste(b) is a function you can use to get the plaintext of a caste.  Put in the bloodcode.
#Will be tagging each function / class / etc
#If I ever figure out modules, that will be which modules they go in.
#tags so far:  #trolldeets, #interface,
#screens:  showparents, maketroll, loadingzone, bloodpage, donationpage, 
#screens are named ""page, and their scrpage objects are named page""
#to activate a new main menu button, go to btnselect(), drawmenu(), 

#have Trolls (one contributor)
#have Donations (A particular donation by 2 trolls)
#have Slurries (An array of Donations, with some meta-data)

 
class Horn:  #Trolldeets
 #Horns are stored in trolls as just the code part.  Use this class when manipulating.
 #create a horn by going hornvariable = Horn("21RIn.f point"), or hornvariable = Horn(troll.hornL)
 code = "21RIn.f point"
 length = 2   # 1 = 0-1 handspans, 2 = 1-2 handspans, 3 = 2-3 handspans, 4 = 3+ handspans.
 curl = 1     # 1 = straight, 2 = up to 45 degrees, 3 = 90 degrees +/- 45, 4 = 180 +/- 45, 5 = 270 +/- 45, 6 = 360 +/-45, 7 = ampora wave-like curves
 radial = "R" # cross-section shape.  R = round, O = Oval, T = triangular, S = spiraling like a goat.
 dir = "I"    # primary growth direction.  F = frontwards, B = backwards, O = outwards (usually up), I = inwards (usually up). 
 wide = "n"   # n = normal width like terezi.  w = wide base, like nepeta. 
 tipAdir = "f"# direction the tip is pointed.  f = front/straight, sollux equius vriska's pincher.  s = sideways.  b = backwards, like the point on vriska's other horn that becomes a hook
 tipA = "point" # verbal description of the shape of the point.  Point, Cone, Spade, Pincher, Jagged, Round.
 def __init__(self, code):
  self.code = code
  self.length = code[0]
  self.curl = code[1]
  self.radial = code[2]
  self.dir = code[3]
  self.wide = code[4]
  self.tipAdir = code[6]
  self.tipA = code[7:len(code)] #everthing else in string = the tip type.
 def desc(self):
  #convert the current features of the horn into a verbal description as in basic version.
  #use by going descriptionstring = horntemp.desc()
  descr = ""
  #Length, default 2
  if self.length == "1":
   descr = "short, "
  if self.length == "3":
   descr = "long, "
  if self.length == "4":
   descr = "very long, "
  #Width, default n
  if self.wide == "w":
   descr = descr + "wide, "
  #Direction, default Inwards
  if self.dir == "F":
   descr = descr + "forward"
  if self.dir == "B":
   descr = descr + "backswept "
  if self.dir == "O":
   descr = descr + "outward "
  #curves, default = 2 (slightly curved)
  if self.curl == "1":
   descr = descr + "straight"
  if self.curl == "3":
   descr = descr + "curved"
  if self.curl == "4":
   descr = descr + "curled"
  if self.curl == "5":
   descr = descr + "curly"
  if self.curl == "6":
   descr = descr + "curled-around"
  if self.curl == "7":
   descr = descr + "wave-like"
  #Tips, default forward
#  if self.tipAdir == "s":
#   descr = descr + "sideways" + self.tipA + "-tipped "
#  if self.tipAdir == "b":
#   descr = descr + "back" + self.tipA + "-tipped "
#  if self.tipAdir == "f":
  descr = descr + self.tipA + "-tipped "
  #radial, default round
  if self.radial == "O":
   descr = descr + "oval horn"
  if self.radial == "T":
   descr = descr + "triangular horn"
  if self.radial == "S":
   descr = descr + "spiralling horn"
  if self.radial == "R":
   descr = descr + "horn"
   #strip spaces
   descr = re.sub(' +', ' ',descr)
   descr = descr.strip()
  return descr
class scrpage: #interface.  An item to be used to define the shape of menus.
   name = "name"
   submenu = False
   excmenu = False 
   maxbtn = 0
   minbtn = 0

#class Troll: #trolldeets.  just so I can pass them around easier...   Maybe?
def CreateTroll(): #trolldeets
 t0 = {
 "firname": "FIRNAM", #sixletters
 "surname": "SURNAM", #sixletters
 "sex": "N",          #M/N/F
 "blood": "Rg",       #RGBrgb
 "caste": "unclassified",
 "sea": "Landdweller", # Landdweller, Seadweller, Beachdweller. replace with more detailed phenotype info :  gilltype, headgills, ribgills, earfins, webbed, glow, pawfeet, tail, wing, hairstreaks, grubscars, 
 "powers": "none",  #psychic, voodoo, eldritch, none.  specify type later.  Make psychics eyes glow colors?
 "hornL": "22RIn.f point", #see horn notes.
 "hornR": "22RIn.f point",
 "height": "tall",  #replace with exact height in inches later.
 "build": "medium", #more detailed data later
 "hair": "short",   #more detailed data later.  medium/long.
 "skin": "grey"    #freckles, stripes, birthmarks, vitiligo, melanism, albinism, etc.
 }
 return t0
def CreateDonation(troll1,troll2): #trolldeets
 #All data is partially formatted into a troll-like state.
 
 #Errorchecking code to give a default set of trolls if needed : Currently nonfunctional.
 #if p1["firname"] + P1["surname"] == "FIRNAMSURNAM":
 # global libbie
 # p1 = libbie
 #if p2["firname"] + P2["surname"] == "FIRNAMSURNAM":
 # global lester
 # p1 = lester

 #decide who is p1 based on hemism.
 caste1 = troll1["blood"]
 caste2 = troll2["blood"]
 if caste1 == highercaste(caste1,caste2):
  p1 = troll1
  p2 = troll2
 if caste2 == highercaste(caste1,caste2):
  p2 = troll1
  p1 = troll2
 
 #Record Donators
 strDonator1 = p1["firname"][0] + "." + p1["surname"]
 strDonator2 = p2["firname"][0] + "." + p2["surname"]
 
 #Blood :
 temp1 = p1["blood"]
 temp2 = p2["blood"]
 a = random.randint(0,len(temp1)-1)
 b = random.randint(1,len(temp1)-1)
 c = random.randint(0,len(temp2)-1)
 d = random.randint(1,len(temp2)-1)
 strBlood = temp1[a] + temp1[b] + temp2[c] + temp2[d]
 strBlood = bloodsort(strBlood)
  
 #str-sea = Phenotype shit comes later.

 #traits come later.
 horn1L = p1["hornL"]
 horn2L = p2["hornL"]
 horn1R = p1["hornR"]
 horn2R = p2["hornR"]
 
 strhornlength  = horn1L[0] + horn2L[0] + horn1R[0] + horn2R[0]
 strhorncurl    = horn1L[1] + horn2L[1] + horn1R[1] + horn2R[1]
 strhornradial  = horn1L[2] + horn2L[2] + horn1R[2] + horn2R[2]
 strhorndir     = horn1L[3] + horn2L[3] + horn1R[3] + horn2R[3]
 strhornwide    = horn1L[4] + horn2L[4] + horn1R[4] + horn2R[4]
 strhorntipAdir = horn1L[6] + horn2L[6] + horn1R[6] + horn2R[6]
 strhorntip1    = horn1L[7:len(horn1L)] #tip type
 strhorntip2    = horn2L[7:len(horn2L)] #tip type
 strhorntip3    = horn1R[7:len(horn1R)] #tip type
 strhorntip4    = horn2R[7:len(horn2R)] #tip type
 t1 = {
 "donator1": strDonator1,
 "donator2": strDonator2,
 "blood": strBlood,
 "hornlength": strhornlength,
 "horncurl": strhorncurl,
 "hornradial": strhornradial,
 "horndir": strhorndir,
 "hornwide": strhornwide,
 "horntipAdir": strhorntipAdir,
 "horntip1": strhorntip1,
 "horntip2": strhorntip2,
 "horntip3": strhorntip3,
 "horntip4": strhorntip4 
 }
 global pail
 pail = t1
 return t1
def getcaste(b): #trolldeets
 caste = "?"
 #Dense What If Forest : Divine place on hemospectrum,
 #use this only for initial placement.  Adjust by third letter later.
 if b[0] == "R":
   if b[1] == "R":
    caste = "Maroon" #RR Maroon
   if b[1] == "G":
    caste = "Gold" #RG Gold
   if b[1] == "B":   
    caste = "Violet" #RB Violet
   if b[1] == "r":
    caste = "Maroon" #Rr Maroon
   if b[1] == "g":
    caste = "Bronze" #Rg Bronze
   if b[1] == "b":   
    caste = "Tyrian" #Rb Tyrian
 if b[0] == "G":
   if b[1] == "G":
    caste = "Olive" #GG Olive
   if b[1] == "B":   
    caste = "Teal" #GB Teal
   if b[1] == "r":
    caste = "Lime" #Gr Lime
   if b[1] == "g":
    caste = "Olive" #Gg Olive
   if b[1] == "b":   
    caste = "Jade" #Gb Jade
 if b[0] == "B":
   if b[1] == "B":   
    caste = "Blue" #BB Bloo
   if b[1] == "r":
    caste = "Indigo" #Br Indigo
   if b[1] == "g":
    caste = "Cerulean" #Gb Ceru
   if b[1] == "b":   
    caste = "Blue" #Bb Bloo
 if b[0] == "r":
   if b[1] == "r":
    caste = "Maroon" #rr maroon
   if b[1] == "g":
    caste = "Bronze" #rg Bronze
   if b[1] == "b":   
    caste = "Mutant" #rb vantas
 if b[0] == "g":
   if b[1] == "g":
    caste = "Olive" #gg Olive
   if b[1] == "b":   
    caste = "Jade" #gb Jade
 if b[0] == "b":
   if b[1] == "b":   
    caste = "Blue" #bb Bloo
 return caste
def getcastenum(b): #trolldeets
 b = b + "..."
 caste = 0
 if b[0] == "R":
   if b[1] == "R":   #RR Maroon
    if b[2] == "R":
     caste = 2 #RRR
    if b[2] == "G":
     caste = 12 #RRG
    if b[2] == "B":
     caste = 72 #RRB
    if b[2] == "r":
     caste = 5 #RRr
    if b[2] == "g":
     caste = 10 #RRg
    if b[2] == "b":
     caste = 74 #RRb
   if b[1] == "G":   #RG Gold
    if b[2] == "G":
     caste = 23 #RGG
    if b[2] == "B":
     caste = 20 #RGB
    if b[2] == "r":
     caste = 16 #RGr
    if b[2] == "g":
     caste = 22 #RGg
    if b[2] == "b":
     caste = 21 #RGb
   if b[1] == "B":   #RB Violet
    if b[2] == "B":
     caste = 64 #RBB
    if b[2] == "r":
     caste = 70 #RBr
    if b[2] == "g":
     caste = 68 #RBg
    if b[2] == "b":
     caste = 67 #RBb
   if b[1] == "r":   #Rr Maroon
    if b[2] == "r":
     caste = 6 #Rrr
    if b[2] == "g":
     caste = 11 #Rrg
    if b[2] == "b":
     caste = 75 #Rrb
   if b[1] == "g":   #Rg Bronze
    if b[2] == "g":
     caste = 15 #Rgg
    if b[2] == "b":
     caste = 21 #Rgb
   if b[1] == "b":   #Rb Tyrian
    if b[2] == "b":
     caste = 71 #Rbb
 if b[0] == "G":
   if b[1] == "G":   #GG Olive
    if b[2] == "G":
     caste = 33 #GGG
    if b[2] == "B":
     caste = 39 #GGB
    if b[2] == "r":
     caste = 28 #GGr
    if b[2] == "g":
     caste = 31 #GGg
    if b[2] == "b":
     caste = 37 #GGb
   if b[1] == "B":   #GB Teal
    if b[2] == "B":
     caste = 48 #GBB
    if b[2] == "r":
     caste = 45 #GBr
    if b[2] == "g":
     caste = 44 #GBg
    if b[2] == "b":
     caste = 47 #GBb
   if b[1] == "r":   #Gr Lime
    if b[2] == "r":
     caste = 24 #Grr
    if b[2] == "g":
     caste = 26 #Grg
    if b[2] == "b":
     caste = 27 #Grb
   if b[1] == "g":   #Gg Olive
    if b[2] == "g":
     caste = 33 #Ggg
    if b[2] == "b":
     caste = 38 #Ggb
   if b[1] == "b":   #Gb Jade
    if b[2] == "b":
     caste = 41 #Gbb
 if b[0] == "B":
   if b[1] == "B":   #BB Bloo
    if b[2] == "B":
     caste = 57 #BBB
    if b[2] == "r":
     caste = 60 #BBr
    if b[2] == "g":
     caste = 52 #BBg
    if b[2] == "b":
     caste = 55 #BBb
   if b[1] == "r":   #Br Indigo
    if b[2] == "r":
     caste = 63 #Brr
    if b[2] == "g":
     caste = 62 #Brg
    if b[2] == "b":
     caste = 61 #Brb
   if b[1] == "g":   #Gb Ceru
    if b[2] == "g":
     caste = 49 #Bgg
    if b[2] == "b":
     caste = 50 #Bgb
   if b[1] == "b":   #Bb Bloo
    if b[2] == "b":
     caste = 56 #Bbb
 if b[0] == "r":
   if b[1] == "r":   #rr maroon
    if b[2] == "r":
     caste = 7 #rrr
    if b[2] == "g":
     caste = 9 #rrg
    if b[2] == "b":
     caste = 1 #rrb
   if b[1] == "g":   #rg Bronze/gold?
    if b[2] == "g":
     caste = 18 #rgg
    if b[2] == "b":
     caste = 13 #rgb
   if b[1] == "b":   #rb vantas 
    if b[2] == "b":
     caste = 71 #rbb
 if b[0] == "g":
   if b[1] == "g":  #gg Olive
    if b[2] == "g":
     caste = 34 #ggg
    if b[2] == "b":
     caste = 36 #ggb 
   if b[1] == "b":  #gb Jade 
    if b[2] == "b":
     caste = 42 #gbb
 if b[0] == "b":
   if b[1] == "b": #bb Bloo
    if b[2] == "b":
     caste = 58 #bbb
 return caste
def highercaste(blood1, blood2): #trolldeets
 #input two bloods, return the higher caste.
 caste1 = getcastenum(blood1)
 caste2 = getcastenum(blood2)
 bloodhigher = blood1  #By default assume the first is higher.
 if caste2 > caste1:   #..but if it's not, fix that.
  bloodhigher = blood2   
 return bloodhigher
def bloodsort(blood): #trolldeets.  Put in a group of letters.
 a = 0   #count the number of letters stripped out
 sorted = "" # sorted blood code
 for arb in blood: #for each letter... 
  if arb == "R":
   sorted = sorted + "R"
   a = a + 1
  if a == len(blood):
   break
 for arb in blood: #for each letter... 
  if arb == "G":
   sorted = sorted + "G"
   a = a + 1
  if a == len(blood):
   break
 for arb in blood: #for each letter... 
  if arb == "B":
   sorted = sorted + "B"
   a = a + 1
  if a == len(blood):
   break
 for arb in blood: #for each letter... 
  if arb == "r":
   sorted = sorted + "r"
   a = a + 1
  if a == len(blood):
   break
 for arb in blood: #for each letter... 
  if arb == "g":
   sorted = sorted + "g"
   a = a + 1
  if a == len(blood):
   break
 for arb in blood: #for each letter... 
  if arb == "b":
   sorted = sorted + "b"
   a = a + 1
  if a == len(blood):
   break
 return sorted

#Initialization and main loop.
def main(): #main / interface
 onprogramload()
 while not tcod.console_is_window_closed():
  updatescreen()
  exit = handle_keys()
  if exit:
    break
 return
def onprogramload(): #main / interface.  Contains global variables.
 SCREEN_WIDTH = 160
 SCREEN_HEIGHT = 50
 VERSIONNUM = "0.1.7"
 font_path = 'terminal8x12_gs_tc.png'
 font_flags = tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD
 tcod.console_set_custom_font(font_path, font_flags)
 window_title = "Dancestry " + VERSIONNUM
 fullscreen = False
 tcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, window_title, fullscreen)
 global libbie, lester, troll3, pail, btncurrent, screencurrent
 libbie = load("Libbie.Pickle.RGg")
 lester = load("Lester.Pebble.Brb")
 troll3 = CreateTroll()
 pail = CreateDonation(libbie,lester)
 btncurrent = 1
 screencurrent = scrpage()
 
 global pageloadtroll, pagedonation, pagemaketroll, pageblood 
 #screens: maketroll, loadingzone, bloodpage, donationpage, 
 
 pageloadtroll = scrpage()
 pageloadtroll.name = "loadingzone"
 pageloadtroll.minbtn = 101
 pageloadtroll.maxbtn = 180
 pageloadtroll.excmenu = True

 pagedonation = scrpage()
 pagedonation.name = "donationpage"
 pagedonation.minbtn = 51
 pagedonation.maxbtn = 59
 pagedonation.submenu = True

 pagemaketroll = scrpage()
 pagemaketroll.name = "maketroll"
 pagemaketroll.minbtn = 51
 pagemaketroll.maxbtn = 51
 pagemaketroll.submenu = True

 pageblood = scrpage()
 pageblood.name = "bloodpage"
 pageblood.minbtn = 101
 pageblood.maxbtn = 101
 pageblood.excmenu = True
  
 return
 
#Show what needs to be shown.
def updatescreen(): #interface.  Choose which page to show.
 tcod.console_clear(0)
 tcod.console_set_default_foreground(0, tcod.Color(250,250,200))
 tcod.console_set_default_background(0, tcod.black)
 
 if screencurrent.name == "showparents":
    showparentspage()
 if screencurrent.name == "maketroll":
    trollcreationpage()
 if screencurrent.name == "loadingzone":
    loadingzone()
 if screencurrent.name == "bloodpage":
    bloodpage()
 if screencurrent.name == "donationpage":
    donationpage()
 drawmenu()
 tcod.console_flush()
 return
def drawmenu(): #interface.  Contains Labels for all main and submenu buttons.
 tcod.console_print_frame(0, 131, 0, 29, 50, True, 13, "MENU")
 tcod.console_set_color_control(0, tcod.white, tcod.Color(60,60,60))
 txtcol = tcod.Color(50,50,0)
 #Can add a tcod.Color(rrr,ggg,bbb) for:  drawbtn(x,y,"label",background,foreground)
 drawbtn(133,2, "     MAKE TROLL     ", btnselect(1), txtcol) 
 drawbtn(133,6, "     FOR   RENT     ", btnselect(2), txtcol) 
 drawbtn(133,10,"        SAVE        ", btnselect(3), txtcol) 
 drawbtn(133,14,"    LOADING AREA    ", btnselect(4), txtcol) 
 drawbtn(133,18,"    BLOOD COLORS    ", btnselect(5), txtcol) 
 drawbtn(133,22,"      DONATION      ", btnselect(6), txtcol) 
 drawbtn(133,26,"       Btn   7      ", btnselect(7), txtcol) 
 drawbtn(133,30,"       Btn   8      ", btnselect(8), txtcol) 
 drawbtn(133,34,"       Btn   9      ", btnselect(9), txtcol) 
 drawbtn(133,38,"       Btn  10      ", btnselect(10), txtcol) 
 drawbtn(133,42,"       Btn  11      ", btnselect(11), txtcol) 
 drawbtn(133,46,"       E X I T      ", btnselect(12), txtcol) 
 #reset defaults
 tcod.console_set_color_control(0, tcod.black, tcod.white)
 
 if screencurrent.name == "donationpage":
  drawsmallbtn(1,1,  "    Create Donation   ", btnselect(51), txtcol) 
  drawsmallbtn(1,3,  "                      ", btnselect(52), txtcol) 
  drawsmallbtn(1,5,  "                      ", btnselect(53), txtcol) 
  drawsmallbtn(25,1, "                      ", btnselect(54), txtcol) 
  drawsmallbtn(25,3, "                      ", btnselect(55), txtcol) 
  drawsmallbtn(25,5, "                      ", btnselect(56), txtcol) 
  drawsmallbtn(49,1, "                      ", btnselect(57), txtcol) 
  drawsmallbtn(49,3, "                      ", btnselect(58), txtcol) 
  drawsmallbtn(49,5, "                      ", btnselect(59), txtcol) 
  
 return

#make the menu buttons work.
def btnselect(x): #interface - controls which buttons are highlightable.
 #mainmenu and main submenu only
 global btnstate, pagedonation, pageloadtroll, pageblood, pagemaketroll
 btncol = tcod.Color(255,0,0)
 if x == btncurrent:
  btncol = tcod.Color(200,200,0)
 if x != btncurrent:
  btncol = tcod.Color(120,120,0)
  
 #unused main menu buttons.
 if x == 2 or x == 7 or x == 8 or x == 9 or x == 10 or x == 11: #Unused Buttons
  btncol = tcod.Color(50,50,0)

 #submenu buttons
 #A set of 20 or so working submenu buttons.
 if screencurrent.name == "donationpage": 
  if x == 54 or x == 55 or x == 56 or x == 57 or x == 58 or x == 59 or x == 60: #Unused Buttons
   btncol = tcod.Color(50,50,0)
  if x == 61 or x == 62 or x == 63 or x == 64 or x == 65 or x == 66 or x == 67 or x == 68 or x == 69 or x == 70: #Unused Buttons
   btncol = tcod.Color(50,50,0)
 if screencurrent.name == "maketroll": 
  if x == 54 or x == 55 or x == 56 or x == 57 or x == 58 or x == 59 or x == 60: #Unused Buttons
   btncol = tcod.Color(50,50,0)
  if x == 61 or x == 62 or x == 63 or x == 64 or x == 65 or x == 66 or x == 67 or x == 68 or x == 69 or x == 70: #Unused Buttons
   btncol = tcod.Color(50,50,0)
 #just a ridiculous number of buttons.
 if screencurrent.name == "loadingzone":
  if x > screencurrent.maxbtn:
   btncol = tcod.Color(50,50,0)
 return btncol
def usedbuttons(dir): #interface
#mainmenu only
 global btncurrent, currentscreen
 if btncurrent < 25: #mainmenu
     if dir == "+":
      btncurrent = btncurrent + 1
      while btnselect(btncurrent) == tcod.Color(50,50,0):
       btncurrent = btncurrent + 1
     if dir == "-":
      btncurrent = btncurrent - 1
      while btnselect(btncurrent) == tcod.Color(50,50,0):
       btncurrent = btncurrent - 1
     #loop main menu
     if btncurrent > 12:
      btncurrent = 1
     if btncurrent < 1:
      btncurrent = 12
 #loop submenu.
 if btncurrent > 25:
     if dir == "+":
      btncurrent = btncurrent + 1
     if dir == "-":
      btncurrent = btncurrent - 1
     if btncurrent == screencurrent.maxbtn + 1:
      btncurrent = screencurrent.minbtn
     if btncurrent == screencurrent.minbtn - 1:
      btncurrent = screencurrent.maxbtn
 return
def handle_keys(): #interface - button functions, and loops as needed.
 global btncurrent, screencurrent, pageblood, pagedonation, pageloadtroll, pagemaketroll
 global pail, troll3, libbie, lester
 key = tcod.console_wait_for_keypress(True)
 if tcod.console_is_key_pressed(tcod.KEY_UP):
  if btncurrent < 9000:
    usedbuttons("-")
 if tcod.console_is_key_pressed(tcod.KEY_DOWN):
  if btncurrent < 9000:
    usedbuttons("+")
 if tcod.console_is_key_pressed(tcod.KEY_LEFT):
  if btncurrent < 25:
    if screencurrent.name == "donationpage":
     btncurrent = 51
    if screencurrent.name == "loadingzone":
     btncurrent = screencurrent.maxbtn
#  if btncurrent > 25:
    #submenu stuff  Pressing left while on a submenu
 if tcod.console_is_key_pressed(tcod.KEY_RIGHT):
  if btncurrent > 25:
    btncurrent = 1
#  if btncurrent < 25:
    #Pressing right while on the main menu
    
 if tcod.console_is_key_pressed(tcod.KEY_ENTER):
  #This is the loop for when someone chooses a button.
  if btncurrent == 1:
      screencurrent = pagemaketroll
      return False
  if btncurrent == 2:
      #screencurrent = ""
      return False
  if btncurrent == 3:
    if screencurrent == "maketroll":
      save(troll3)
      draw(73,20,"Saved")  
    if screencurrent == "donationpage":
      savedon(pail)
      draw(73,20,"Saved")  
      return False
  if btncurrent == 4:
      screencurrent = pageloadtroll
      return False
  if btncurrent == 5:
      screencurrent = pageblood
	  #note : Change to 'eugenics' page once that's functional.
      return False
  if btncurrent == 6:
      screencurrent = pagedonation
      return False
  if btncurrent == 7:
   #code that makes the button do something
   return False
  if btncurrent == 8:
   #code that makes the button do something
   return False
  if btncurrent == 9:
   #code that makes the button do something
   return False
  if btncurrent == 10:
   #code that makes the button do something
   return False
  if btncurrent == 11:
   #code that makes the button do something
   return False
  if btncurrent == 12:
   return True
  if btncurrent > 25:
   if screencurrent.name == "donationpage":
    if btncurrent == 51:
      pail = CreateDonation(libbie,lester)
      return False
    return False
   if screencurrent.name == "maketroll":
    if btncurrent == 51:
      troll3 = CreateTroll(libbie, lester)
      updatescreen()
      return False
    return False
   #End "main menu" portion of Enter loop.
   #Create a sub-menu here based off which other menu the cursor is in.
   return False
  #the loop for when someone presses enter to choose a button is over.
 if tcod.console_is_key_pressed(tcod.KEY_1):
  if screencurrent.name == "pageloadtroll":
   #load currently selected troll into slot 1.
   return False
  return False
 if tcod.console_is_key_pressed(tcod.KEY_2):
  if screencurrent.name == "pageloadtroll":
   #load currently selected troll into slot 2.
   return False
  return False

 elif key.vk == tcod.KEY_ESCAPE:
 #reenable the above line to make hitting escape close the program.
  return True

#save and load to file.
def save(grub):        #interface     Save Troll
 saveloc = "Caverns/CaveB/" +grub["firname"] + "." + grub["surname"] + "." + grub["blood"] + ".troll"
 c = 1
 int(c)
 while os.path.exists(saveloc):
   c = c+1
   d = str(c)
   saveloc = "Caverns/CaveB/" +grub["firname"] + "." + grub["surname"] + "." + grub["blood"] + "." + d + ".troll"
 save = open(saveloc, "wt")
 save.write("#SaveVersion4#" + "\n")
 y = json.dumps(grub, indent=4)
 save.write(y)
 save.close
 return
def load(filename):    #interface     Load Troll
 trollobj = CreateTroll()
 savedtroll = "Caverns/AncestralCave/" + filename + ".troll"
 if os.path.exists(savedtroll):
  load = open(savedtroll, "rt")
  if load.readline() == "#SaveVersion4#\n": 
     y = load.read()
     trollobj = json.loads(y)
  elif load.readline() != "#SaveVersion4#\n":
    draw(18,45,"WRONG SAVETYPE")
  load.close
 return trollobj
def savedon(donation): #interface     Save Donation
 folder = "Caverns/CaveB/"
 saveloc = folder + "." + donation["blood"] + "." + donation["donator1"] + "." + donation["donator2"] + ".donation"
 c = 1
 int(c)
 while os.path.exists(saveloc):
   c = c+1
   d = str(c)
   saveloc = folder + donation["blood"] + "." + donation["donator1"] + "." + donation["donator2"] + d + ".donation"
 save = open(saveloc, "wt")
 save.write("#SaveVersion4#" + "\n")
 y = json.dumps(grub, indent=4)
 save.write(y)
 save.close
 return
def loaddon(filename): #interface     Load Donation
 donation = CreateDonation()
 saveddon = "Caverns/AncestralCave/" + filename + ".donation"
 if os.path.exists(saveddon):
  load = open(saveddon, "rt")
  if load.readline() == "#SaveVersion4#\n": 
     y = load.read()
     donation = json.loads(y)
  elif load.readline() != "#SaveVersion4#\n":
    draw(18,45,"WRONG SAVETYPE")
  load.close
 return donation
 
#menu-related boxen. 
def drawbtn(x, y, label = "", btncolor = tcod.Color(255,255,225), txtcolor = tcod.Color(50,50,0)): #interface
 rectolor(x,y,24,2, btncolor, txtcolor) 
 draw(x+2,y+1,label)
 return 
def drawsmallbtn(x, y, label = "", btncolor = tcod.Color(255,255,225), txtcolor = tcod.Color(50,50,0)): #interface
 rectolor(x,y,21,0, btncolor, txtcolor) 
 draw(x,y,label)
 return 
def rectolor(x, y, ww, hh, btncolor = tcod.Color(255,255,225), txtcolor = tcod.Color(0,0,0)): #interface
 h = 0
 w = 0
 while h <= hh:
   while w <= ww:
     tcod.console_set_char_background(0, x+w, y+h, btncolor, tcod.BKGND_SET)
     tcod.console_set_char_foreground(0, x+w, y+h, txtcolor)
     w = w + 1
   w = 0
   h = h + 1
 return 
def draw(x,y,thing): #interface
 #draws foreground text, no color specified.
 tcod.console_print(0, x, y, thing)
 return

#items that get printed to screen a Lot.  Like trolls, donations, blood colors...
def displaytroll(x,y,t0): #interface -- prints a standard-format window display to the screen.
 #set some defaults
 #called when screencurrent.name = "showparents"
 #called when screencurrent.name = "maketroll"
 colbg = tcod.Color(0,0,0)
 colfg = tcod.Color(255,255,255)
 #recolor
 colbg = bloodtorgb(t0["blood"])
 colfg = pastel(colbg)
 hornL1 = t0["hornL"]
 hornL2 = Horn(hornL1)
 hornR1 = t0["hornR"]
 hornR2 = Horn(hornR1)
 rectolor(x, y, 64, 20, colbg, colfg)
 string1 = t0["firname"] + " " + t0["surname"] + ", " + t0["blood"] + " " + t0["sex"]
 string2 = t0["caste"] + ", " + t0["powers"] 
 string3 = t0["sea"]
 string4 = t0["height"] + ", " + t0["build"] + " build" 
 string5 = t0["hair"] + " hair"
 string6 = t0["skin"] + " skin"
 string7 = "LHorn: " + hornL2.desc()
 string8 = "RHorn: " + hornR2.desc()
 tcod.console_print_frame(0, x, y, 65, 21, True, 13, string1)
 draw(x+2,y+1,string2)
 draw(x+2,y+2,string3)
 draw(x+2,y+3,string4)
 draw(x+2,y+4,string5)
 draw(x+2,y+5,string6)
 draw(x+2,y+6,string7)
 draw(x+2,y+7,string8)
 return
def displaydonation(x,y,t0): #interface -- prints a standard-format window display to the screen.
 colbg = tcod.Color(0,0,0)
 colfg = tcod.Color(255,255,255)
 #recolor
 bloodtemp = t0["blood"]
 bloodtemp = bloodtemp[0:3]
 colbg = bloodtorgb(bloodtemp)
 colfg = pastel(colbg)
 #called when screen = donationpage
 rectolor(x, y, 64, 42, colbg, colfg)
 string0 = t0["donator1"] + " / " + t0["donator2"]
 string1 = "Blood: " + t0["blood"]
 string2 = "Direction:    " + t0["horndir"] + "    Width:  " + t0["hornwide"] + "    Curl:    " + t0["horncurl"]
 string3 = "Radial Shape: " + t0["hornradial"] + "    Length: " + t0["hornlength"] + "    Tip dir: " + t0["horntipAdir"]
 string4 = "Tips:" + t0["horntip1"] + "," + t0["horntip2"] + "," + t0["horntip3"] + "," + t0["horntip4"]
 tcod.console_print_frame(0, x, y, 65, 43, True, 13, string0)
 draw(x+2,y+1,string1)
 tcod.console_print_frame(0, x+1, y+2, 63, 5, True, 13, "Horns") 
 draw(x+2,y+3,string2)
 draw(x+2,y+4,string3)
 draw(x+2,y+5,string4)
def bloodtorgb(b): #interface, because this is the display color only / specifically.
 #gives you the darker color associated with the code "b" which is a 2-3 letter string.
 rgb1 = 0
 rgb2 = 0
 rgb3 = 0
 capitals = 0
 if b[0] == "r" or b[1] == "r": #recessive colors
  rgb1 = 60
 if b[0] == "g" or b[1] == "g":
  rgb2 = 60
 if b[0] == "b" or b[1] == "b":
  rgb3 = 60
 if b[0] == "R" or b[1] == "R": #dominant colors
  rgb1 = 120
  capitals = capitals + 1
 if b[0] == "G" or b[1] == "G":
  rgb2 = 120
  capitals = capitals + 1
 if b[0] == "B" or b[1] == "B":
  rgb3 = 120
  capitals = capitals + 1

 #Mutant Fixing : No capital letters = ***slightly*** brighter.
 if capitals == 0:
  if rgb1 != 0:
   rgb1 = rgb1+30
  if rgb1 > 210:
   rgb1 = rgb1-20
  if rgb2 != 0:
   rgb2 = rgb2+30
  if rgb2 > 220:
   rgb2 = rgb2-20
  if rgb3 != 0:
   rgb3 = rgb3+30
  if rgb3 > 240:
   rgb3 = rgb3-20
 #Make dark grubs brighter.
 if rgb1+rgb2+rgb3 < 100:
  rgb1 = rgb1*2
  rgb2 = rgb2*2
  rgb3 = rgb3*2
 #Vantases are special.
 if b == "rb":
  rgb1 = 255
  rgb2 = 0
  rgb3 = 0
 
 #Modulate color by 3rd letter.
 if len(b) == 3:
   if b[2] == "R":
    rgb1 = rgb1 + 25
    rgb2 = rgb2 - 25
    rgb3 = rgb3 - 25
   if b[2] == "G":
    rgb1 = rgb1 - 25
    rgb2 = rgb2 + 25
    rgb3 = rgb3 - 25
   if b[2] == "B":
    rgb1 = rgb1 - 25
    rgb2 = rgb2 - 25
    rgb3 = rgb3 + 25
   if b[2] == "r":
    rgb1 = rgb1 + 25
   if b[2] == "g":
    rgb2 = rgb2 + 25
   if b[2] == "b":
    rgb3 = rgb3 + 25
 
#Return things to normal color ranges.
 if rgb1 > 255:
  rgb1 = 255
 if rgb2 > 255:
  rgb2 = 255
 if rgb3 > 255:
  rgb3 = 255  
 if rgb1 <0:
  rgb1 = 0
 if rgb2 <0:
  rgb2 = 0
 if rgb3 <0:
  rgb3 = 0

 finalcolor = tcod.Color(rgb1,rgb2,rgb3)
 return finalcolor
def pastel(oldcolor): #interface (currently nonfunctional)
 #This currently does not function, for unknown reasons.
 #When it starts working, replace the crimson color with a pale offwhite. 
 newcolor = tcod.color_lerp(oldcolor,tcod.Color(255,0,0),0.5)
 return newcolor
 
#The display for individual screens.
def bloodpage(): #interface - page of blood color examples
 #screencurrent.name = bloodpage
 #all the display stuff for this page goes here since it's spammy
 z = ["rb","rrb","RRR","RR","Rr","RRr","Rrr","rrr","rr","rrg","RRg","Rrg","RRG","Rgb","Rg","Rgg","RGr","RG","rg","RGB","RGb","rgg","RGg","Grr","RGG","Gr","Grg","Grb","GGr","GG","Gg","GGg","Ggg","GGG","ggg","gg","ggb","GGb","Ggb","GGB","Gb","Gbb","gbb","gb","GBg","GBr","GB","GBb","GBB","Bgg","Bgb","Bg","BBg","BB","Bb","BBb","Bbb","BBB","bbb","bb","BBr","Brb","Brg","Br","RBB","Brr","rbb","RBb","RBg","RB","RBr","Rbb","Rb","RRB","RRb","Rrb"]
 h = 4
 w = 10
 numtotal = 0
 for x in z:
   numtotal = numtotal + 1
   if numtotal == 14 or numtotal == 27 or numtotal == 40 or numtotal == 53 or numtotal == 66 or numtotal == 89:
     w = w + 18
     h = 4
   h = h + 3
   displayname = x
   displaycol = bloodtorgb(x)
   rectolor(w,h,16,2, displaycol)
   draw(w+1,h+1,displayname)
 return
def donationpage(): #interface - page to interact with creating donations
 global libbie, lester, pail
 displaytroll(1,7,libbie)
 displaytroll(1,29,lester)
 displaydonation(66,7,pail)
 return
def loadingzone(): #interface - page to load trolls from file
 tcod.console_print_frame(0, 1, 1, 35, 5, True, 13, "Instructions")
 draw(3,2,"Arrow keys to navigate.")
 draw(3,3,"Press 1 to load to slot 1.")  #currently nonfunctional
 draw(3,4,"      2 to load to slot 2.")

 global pageloadtroll
 z = os.listdir("Caverns/AncestralCave/")
 tcod.console_set_default_foreground(0, tcod.Color(250,250,200))
 h = 7
 w = 7
 numtotal = 0
 for arb in z:
    temp = arb
    if len(temp) > 20 and len(temp) < 30:
     if temp[6] == "." and temp[13] == ".":
          numtotal = numtotal + 1
          if numtotal == 21 or numtotal == 41 or numtotal == 61 or numtotal == 81:
            w = w + 15
            h = 7
          h = h + 2		    
          displayname = temp[0:6] + " " + temp[7:13]
          bloodcol = temp[14:17]
          if bloodcol[2] == ".":
             bloodcol = temp[14:16]
          displaycol = bloodtorgb(bloodcol)
          rectolor(w,h,14,1,displaycol)
          if btncurrent != numtotal + 100:
           tcod.console_set_default_foreground(0, tcod.Color(10,10,10))
           draw(w+1,h+1,displayname)
           tcod.console_set_default_foreground(0, tcod.Color(250,250,200))
          if btncurrent == numtotal + 100:
           draw(w+1,h+1,displayname)
 pageloadtroll.maxbtn = numtotal + 100
 if pageloadtroll.maxbtn > 180:
  pageloadtroll.maxbtn = 180
 pageloadtroll.minbtn = 101
 screencurrent = pageloadtroll
def trollcreationpage(): #interface -- may be combined with showparents.
 displaytroll(1,7,libbie)
 displaytroll(1,29,lester)
 displaytroll(66,17,troll3)
 return


main()
