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
 SCREEN_WIDTH = 80
 SCREEN_HEIGHT = 50
 VERSIONNUM = "0.1.2"
 global player_x, player_y
 player_x = SCREEN_WIDTH // 2
 player_y = SCREEN_HEIGHT // 2
 font_path = 'terminal8x12_gs_tc.png'
 font_flags = tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD
 tcod.console_set_custom_font(font_path, font_flags)
 window_title = "Dancestry " + VERSIONNUM
 fullscreen = False
 tcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, window_title, fullscreen)
 global libbie, lester
 libbie = load("Libbie.Pickle")
 lester = load("Lester.Pebble")
 return
 
def updatescreen():
 tcod.console_set_default_foreground(0, tcod.white)
 #displaytroll(1,1,libbie)
 #displaytroll(40,1,lester)
 draw(player_x,player_y,"@")
 tcod.console_flush()
 draw(player_x,player_y," ")
 return

def draw(x,y,thing):
 #draws a foreground element.
 #Have a separate function for background boxes.
 tcod.console_put_char(0, x, y, thing, tcod.BKGND_NONE)
 return

def handle_keys():
 global player_x, player_y
 key = tcod.console_wait_for_keypress(True)
 if tcod.console_is_key_pressed(tcod.KEY_UP):
  player_y = player_y - 1
 if tcod.console_is_key_pressed(tcod.KEY_DOWN):
  player_y = player_y + 1
 if tcod.console_is_key_pressed(tcod.KEY_LEFT):
  player_x = player_x - 1
 if tcod.console_is_key_pressed(tcod.KEY_RIGHT):
  player_x = player_x + 1
 elif key.vk == tcod.KEY_ESCAPE:
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
 draw(x,y,t0["firname"] + " " + t0["surname"] + ", " + t0["blood"] + " " + t0["sex"] + ", " + t0["caste"] + ", " + t0["powers"]) 
 draw(x,y,t0["sea"])
 draw(x,y,t0["height"] + ", " + t0["build"] + " build, " + t0["hair"] + " hair, " + t0["skin"] + " skin")
 draw(x,y,"LHorn: " + t0["hornL"])
 draw(x,y,"RHorn: " + t0["hornR"])
 return
 
main()
