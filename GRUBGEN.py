import random
import json
import os
import libtcodpy as tcod
#getcaste(b) is a function you can use to get the plaintext of a caste.  Put in the bloodcode.

class Horn:
 #Horns are stored in trolls as just the code part.  Use this class when manipulating.
 #create a horn by going horntemp = Horn("21RIn.f point"), or horntemp = Horn(troll.hornL)
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
  description = ""
  return description
 
#have Trolls (one contributor)
#have Donations (A particular donation by 2 trolls)
#have Slurries (An array of Donations, with some meta-data)

def main(): 
 onprogramload()
 while not tcod.console_is_window_closed():
  updatescreen()
  exit = handle_keys()
  if exit:
    break
 return

def onprogramload():
 SCREEN_WIDTH = 100
 SCREEN_HEIGHT = 50
 VERSIONNUM = "0.1.5"
 font_path = 'terminal8x12_gs_tc.png'
 font_flags = tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD
 tcod.console_set_custom_font(font_path, font_flags)
 window_title = "Dancestry " + VERSIONNUM
 fullscreen = False
 tcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, window_title, fullscreen)
 global libbie, lester, troll3, btncurrent, screencurrent
 libbie = load("Libbie.Pickle.RGg")
 lester = load("Lester.Pebble.Brb")
 troll3 = CreateTroll()
 btncurrent = 1
 screencurrent = "showparents"
 return
 
def updatescreen():
 tcod.console_clear(0)
 tcod.console_set_default_foreground(0, tcod.Color(250,250,200))
 tcod.console_set_default_background(0, tcod.black)
 
 if screencurrent == "showparents":
    displaytroll(1,1,libbie)
    displaytroll(36,1,lester)
 if screencurrent == "maketroll":
    displaytroll(1,1,libbie)
    displaytroll(36,1,lester)
    displaytroll(18,25,troll3)
 if screencurrent == "loadingzone":
    z = os.listdir("Caverns/AncestralCave/")
    h = -1
    w = 1
    numtotal = 0
    for x in z:
      temp = x
      if len(temp) > 20 and len(temp) < 30:
       if temp[6] == "." and temp[13] == ".":
            numtotal = numtotal + 1
            if numtotal == 21 or numtotal == 41 or numtotal == 61 or numtotal == 81:
              w = w + 15
              h = -1
            h = h + 2
            displayname = temp[0:6] + " " + temp[7:13]
            bloodcol = temp[14:17]
            if bloodcol[2] == ".":
               bloodcol = temp[14:16]
            displaycol = bloodtorgb(bloodcol)
            rectolor(w,h,14,1, displaycol)
            draw(w+1,h+1,displayname)
 drawmenu()
 tcod.console_flush()
 return

def drawmenu():
 tcod.console_print_frame(0, 71, 0, 29, 50, True, 13, "MENU")
 tcod.console_set_color_control(0, tcod.white, tcod.Color(60,60,60))
 txtcol = tcod.Color(50,50,0)
 #Can add a tcod.Color(rrr,ggg,bbb) for:  drawbtn(x,y,"label",background,foreground)
 drawbtn(73,2, "     SHOW TROLL     ", btnselect(1), txtcol) 
 drawbtn(73,6, "     MAKE TROLL     ", btnselect(2), txtcol) 
 drawbtn(73,10,"     SAVE TROLL     ", btnselect(3), txtcol) 
 drawbtn(73,14,"    LOADING AREA    ", btnselect(4), txtcol) 
 drawbtn(73,18,"       Btn   5      ", btnselect(5), txtcol) 
 drawbtn(73,22,"       Btn   6      ", btnselect(6), txtcol) 
 drawbtn(73,26,"       Btn   7      ", btnselect(7), txtcol) 
 drawbtn(73,30,"       Btn   8      ", btnselect(8), txtcol) 
 drawbtn(73,34,"       Btn   9      ", btnselect(9), txtcol) 
 drawbtn(73,38,"       Btn  10      ", btnselect(10), txtcol) 
 drawbtn(73,42,"       Btn  11      ", btnselect(11), txtcol) 
 drawbtn(73,46,"       E X I T      ", btnselect(12), txtcol) 
 #reset defaults
 tcod.console_set_color_control(0, tcod.black, tcod.white)
 return
 
def btnselect(x):
 global btnstate
 btncol = tcod.Color(255,0,0)
 if x == btncurrent:
  btncol = tcod.Color(200,200,0)
 if x != btncurrent:
  btncol = tcod.Color(120,120,0)
 if x == 5 or x == 6 or x == 7 or x == 8 or x == 9 or x == 10 or x == 11: #Unused Buttons
  btncol = tcod.Color(50,50,0)
 return btncol
 
def drawbtn(x, y, label = "", btncolor = tcod.Color(255,255,225), txtcolor = tcod.Color(50,50,0)):
 rectolor(x,y,24,2, btncolor, txtcolor) 
 draw(x+2,y+1,label)
 return 

def rectolor(x, y, ww, hh, btncolor = tcod.Color(255,255,225), txtcolor = tcod.Color(0,0,0)):
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
 
def draw(x,y,thing):
 #draws foreground text, no color specified.
 tcod.console_print(0, x, y, thing)
 return

def usedbuttons(dir):
 global btncurrent
 while btnselect(btncurrent) == tcod.Color(50,50,0):
  if dir == "+":
   btncurrent = btncurrent + 1
  if dir == "-":
   btncurrent = btncurrent - 1
  if btncurrent == 13:
   btncurrent = 1
  if btncurrent == 0:
   btncurrent = 12
 return

def handle_keys():
 global btncurrent, screencurrent
 key = tcod.console_wait_for_keypress(True)
 if tcod.console_is_key_pressed(tcod.KEY_UP):
  btncurrent = btncurrent - 1
  usedbuttons("-")
 if tcod.console_is_key_pressed(tcod.KEY_DOWN):
  btncurrent = btncurrent + 1
  usedbuttons("+")
 #if tcod.console_is_key_pressed(tcod.KEY_LEFT):
 #if tcod.console_is_key_pressed(tcod.KEY_RIGHT):
 if btncurrent == 13:
  btncurrent = 1
 if btncurrent == 0:
  btncurrent = 12
 if tcod.console_is_key_pressed(tcod.KEY_ENTER):
  #This is the loop for when someone chooses a button.
  if btncurrent == 1:
      screencurrent = "showparents"
      return False
  if btncurrent == 2:
      screencurrent = "maketroll"
      global troll3
      troll3 = CreateTroll()
      updatescreen() 
      return False
  if btncurrent == 3:
      save(troll3)
      draw(73,20,"Saved")  
      return False
  if btncurrent == 4:
      screencurrent = "loadingzone"
      return False
  if btncurrent == 5:
   #code that makes the button do something
   return False
  if btncurrent == 6:
   #code that makes the button do something
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
  #the loop for when someone chooses a button is over.
 #elif key.vk == tcod.KEY_ESCAPE:
 #reenable the above line to make hitting escape close the program.
  return True

def save(grub):
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

def load(filename):
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

def CreateTroll():
 t0 = {
 "firname": "FIRNAM", #sixletters
 "surname": "SURNAM", #sixletters
 "sex": "N",          #M/N/F
 "blood": "Rg",       #RGBrgb
 "caste": "unclassified",
 "sea": "Landdweller", # Landdweller, Seadweller, Beachdweller. replace with more detailed phenotype info :  gilltype, headgills, ribgills, earfins, webbed, glow, pawfeet, tail, wing, hairstreaks
 "powers": "none",  #psychic, voodoo, eldritch, none.  specify type later.
 "hornL": "21RIn.f point", #see horn notes.
 "hornR": "21RIn.f point",
 "height": "tall",  #replace with exact height in inches later.
 "build": "medium", #more detailed data later
 "hair": "short",   #more detailed data later.  medium/long.
 "skin": "grey"    #freckles, stripes, birthmarks, vitiligo, melanism, albinism, etc.
 }
 return t0

def displaytroll(x,y,t0):
 #set some defaults
 colbg = tcod.Color(0,0,0)
 colfg = tcod.Color(255,255,255)
 #recolor
 colbg = bloodtorgb(t0["blood"])
 colfg = pastel(colbg)
 rectolor(x, y, 34, 20, colbg, colfg)
 string1 = t0["firname"] + " " + t0["surname"] + ", " + t0["blood"] + " " + t0["sex"]
 string2 = t0["caste"] + ", " + t0["powers"] 
 string3 = t0["sea"]
 string4 = t0["height"] + ", " + t0["build"] + " build" 
 string5 = t0["hair"] + " hair"
 string6 = t0["skin"] + " skin"
 string7 = "LHorn: " + t0["hornL"]
 string8 = "RHorn: " + t0["hornR"]
 tcod.console_print_frame(0, x, y, 35, 21, True, 13, string1)
 draw(x+2,y+1,string2)
 draw(x+2,y+2,string3)
 draw(x+2,y+3,string4)
 draw(x+2,y+4,string5)
 draw(x+2,y+5,string6)
 draw(x+2,y+6,string7)
 draw(x+2,y+7,string8)
 return
 
def bloodtorgb(b):
 #gives you the darker color associated with the code "b" which is a 3 letter string.
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

 #Mutant Fixing : No capital letters = make them neon.
 if capitals == 0:
  if rgb1 != 0:
   rgb1 = rgb1+140
  if rgb2 != 0:
   rgb2 = rgb2+140
  if rgb3 != 0:
   rgb3 = rgb3+140
 #Make dark grubs brighter.
 if rgb1+rgb2+rgb3 < 100:
  rgb1 = rgb1*2
  rgb2 = rgb2*2
  rgb3 = rgb3*2
 #Vantases are special.
 if b[0] + b[1] == "rb":
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

def getcaste(b):
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

def pastel(oldcolor):
 #This currently does not function, for unknown reasons.
 #When it starts working, replace the crimson color with a pale offwhite. 
 newcolor = tcod.color_lerp(oldcolor,tcod.Color(255,0,0),0.5)
 return newcolor












 
main()
