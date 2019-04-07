import random
import json
import libtcodpy as tcod


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
 VERSIONNUM = "0.1.2"
 font_path = 'terminal8x12_gs_tc.png'
 font_flags = tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD
 tcod.console_set_custom_font(font_path, font_flags)
 window_title = "Dancestry " + VERSIONNUM
 fullscreen = False
 tcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, window_title, fullscreen)
 global libbie, lester, btncurrent
 libbie = load("Libbie.Pickle")
 lester = load("Lester.Pebble")
 btncurrent = 1
 return
 
def updatescreen():
 tcod.console_clear(0)
 tcod.console_set_default_foreground(0, tcod.white)
 tcod.console_set_default_background(0, tcod.black)
 displaytroll(1,1,libbie)
 displaytroll(36,1,lester)
 drawmenu()
 tcod.console_flush()
 return
 
def drawmenu():
 tcod.console_print_frame(0, 71, 0, 29, 50, True, 13, "MENU")
 tcod.console_set_color_control(0, tcod.white, tcod.Color(60,60,60))
 #Can add a tcod.Color(rrr,ggg,bbb) for:  drawbtn(x,y,"label",background,foreground)
 drawbtn(73,2,"Btn 1", btnselect(1)) 
 drawbtn(73,6,"Btn 2", btnselect(2)) 
 drawbtn(73,10,"Btn 3", btnselect(3)) 
 drawbtn(73,14,"Btn 4", btnselect(4)) 
 drawbtn(73,18,"Btn 5", btnselect(5)) 
 drawbtn(73,22,"Btn 6", btnselect(6)) 
 drawbtn(73,26,"Btn 7", btnselect(7)) 
 drawbtn(73,30,"Btn 8", btnselect(8)) 
 drawbtn(73,34,"       E X I T    ", btnselect(9)) 

 #tcod.console_rect(0, 72, 1, 27, 2, False, tcod.BKGND_SET) 
 #draw(76,2,"Menu location")
 #reset defaults
 tcod.console_set_color_control(0, tcod.black, tcod.white)
 return
 
def btnselect(x):
 global btnstate
 btncol = tcod.Color(255,0,0)
 if x == btncurrent:
  btncol = tcod.Color(255,255,225)
 if x != btncurrent:
  btncol = tcod.Color(205,205,275)
 #if btnstate[x] == "UNUSED":
 # btncol = tcod.Color(50,50,0)
 return btncol
 
def drawbtn(x, y, label = "", btncolor = tcod.Color(255,255,225), txtcolor = tcod.Color(50,50,0)):
 rectolor(x,y,24,2, btncolor, txtcolor) 
 draw(x+2,y+1,label)
 return 

def rectolor(x, y, ww, hh, btncolor = tcod.Color(255,255,225), txtcolor = tcod.Color(50,50,0)):
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

def handle_keys():
 global btncurrent
 key = tcod.console_wait_for_keypress(True)
 if tcod.console_is_key_pressed(tcod.KEY_UP):
  btncurrent = btncurrent - 1
 if tcod.console_is_key_pressed(tcod.KEY_DOWN):
  btncurrent = btncurrent + 1
 #if tcod.console_is_key_pressed(tcod.KEY_LEFT):
 #if tcod.console_is_key_pressed(tcod.KEY_RIGHT):
 if btncurrent == 10:
  btncurrent = 1
 if btncurrent == 0:
  btncurrent = 9
 if tcod.console_is_key_pressed(tcod.KEY_ENTER):
  #This is the loop for when someone chooses a button.
  if btncurrent == 1:
   #code that makes the button do something
   return False
  if btncurrent == 2:
   #code that makes the button do something
   return False
  if btncurrent == 3:
   #code that makes the button do something
   return False
  if btncurrent == 4:
   #code that makes the button do something
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
   return True
  #the loop for when someone chooses a button is over.
 #elif key.vk == tcod.KEY_ESCAPE:
 #reenable the above line to make hitting escape close the program.
  return True

def save(grub):
 save = open(grub["firname"] + "." + grub["surname"] + ".troll", "wt")
 save.write("#SaveVersion4#" + "\n")
 y = json.dumps(grub, indent=4)
 save.write(y)
 save.close
 return

def load(filename):
 trollobj = CreateTroll()
 load = open(filename + ".troll", "rt")
 if load.readline() == "#SaveVersion4#\n": 
  y = load.read()
  trollobj = json.loads(y)
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
 string1 = t0["firname"] + " " + t0["surname"] + ", " + t0["blood"] + " " + t0["sex"]
 string2 = t0["caste"] + ", " + t0["powers"] 
 string3 = t0["sea"]
 string4 = t0["height"] + ", " + t0["build"] + " build" 
 string5 = t0["hair"] + " hair"
 string6 = t0["skin"] + " skin"
 string7 = "LHorn: " + t0["hornL"]
 string8 = "RHorn: " + t0["hornR"]
 tcod.console_print_frame(0, x, y, 35, 40, True, 13, string1)
 draw(x+2,y+1,string2)
 draw(x+2,y+2,string3)
 draw(x+2,y+3,string4)
 draw(x+2,y+4,string5)
 draw(x+2,y+5,string6)
 draw(x+2,y+6,string7)
 draw(x+2,y+7,string8)
 #recolor
 colbg = tcod.Color(0,0,0)
 colfg = tcod.Color(255,255,255)
 
 if t0["blood"] == "RGg":
  colbg = tcod.Color(255,255,0)
  colfg = tcod.Color(50,50,0)
 if t0["blood"] == "Br":
  colbg = tcod.Color(255,0,255)
  colfg = tcod.Color(50,0,50)
 rectolor(x, y, 35, 39, colbg, colfg)
 return

def bloodtoRGB():
 #gives you the darker color associated with any valid blood code.
 return

main()
