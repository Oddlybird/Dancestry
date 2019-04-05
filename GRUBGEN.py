import random
import json

class Troll:
#An individual contributor's genetics
 firname = "FIRNAM"
 surname = "SURNAM" 
 sex = "N"
 blood = "Rg" #Bronze by default
 caste = "unclassified"
 sea = "N" #(yes/maybe/no)
 #gilltype (innie, outtie)
 #headgills (y/n)
 #ribgills (y/n)
 #earfins (full, half, none)
 #webbed (fingers, toes, none)
 #glow (none, weak, strong.  have pattern types eventually?)
 #pawfeet (4, 2, partial)
 #tail (no / stub / type of tail)
 #wing (no / bugtype)
 powers = "none" #(psychic, voodoo, eldritch, none)
 #specify type of psychic, voodoo, and eldritch powers later.
 hornL = "21RIn.f point"
 hornR = "21RIn.f point"
 #These should be examples of the horn class.
 height = "tall"
 #have a default-height-for-trolls record, and a height-compared-to-normal-troll-of-type record?
 build = "medium"
 #figure out numbers for build later.
 hair = "short hair"
 #make a hair class later
 skin = "grey" #(freckles, stripes, birthmarks, vitiligo, melanism/albinism, etc)
 
class Horn:
 #horn class can possibly be removed and replaced with just a string, with the interpretations hardcoded.
 code = "21RIn.f point"
 length = 2   # 1 = 0-1 handspans, 2 = 1-2 handspans, 3 = 2-3 handspans, 4 = 3+ handspans.
 curl = 1     # 1 = straight, 2 = up to 45 degrees, 3 = 90 degrees +/- 45, 4 = 180 +/- 45, 5 = 270 +/- 45, 6 = 360 +/-45, 7 = ampora wave-like curves
 radial = "R" # cross-section shape.  R = round, O = Oval, T = triangular, S = spiraling like a goat.
 dir = "I"    # primary growth direction.  F = frontwards, B = backwards, O = outwards (usually up), I = inwards (usually up). 
 wide = "n"   # n = normal width like terezi.  w = wide base, like nepeta. 
 tipAdir = "f"# direction the tip is pointed.  f = front/straight, sollux equius vriska's pincher.  s = sideways.  b = backwards, like the point on vriska's other horn that becomes a hook
 tipA = "point" # verbal description of the shape of the point.  Point, Cone, Spade, Pincher, Jagged, Round.
 desc = ""    #Make a function that converts the code to a verbal description as in basic version.
  
#class Donation:
#A particular donation by 2 trolls

#class Slurry:
#An array of Donations, with some meta-data.

def main(): 
 troll0 = Troll()
 save(troll0)
 troll0 = load("parent")
 displaytroll(troll0) 
 return

def save(grub):
 save = open(grub.firname + grub.surname + ".troll", "wt")
 savearray = ""
 save.write("#SaveVersion1#" + "\n")
 save.write(grub.firname + "\n")
 save.write(grub.surname + "\n")
 save.write(grub.blood + "\n")
 save.write(grub.sex + "\n")
 save.write(grub.caste + "\n")
 save.write(grub.powers + "\n")
 save.write(grub.sea + "\n")
 save.write(grub.height + "\n")
 save.write(grub.build + "\n")
 save.write(grub.hair + "\n")
 save.write(grub.skin + "\n")
 save.write(grub.hornL + "\n")
 save.write(grub.hornR + "\n")
 save.write("#end#")
 save.close
 return

def load(filename):
 trollobj = Troll()
 load = open(filename + ".troll", "rt")
 if load.readline() == "#SaveVersion1#\n": 
  trollobj.firname = load.readline()
  trollobj.surname = load.readline()
 if load.readline() != "#end#\n": 
  print("LoadSuccessful")
  #remove the trailing \n from each item
  trollobj.firname = trollobj.firname[0:len(trollobj.firname) - 1]
  trollobj.surname = trollobj.surname[0:len(trollobj.surname) - 1]
 load.close
 return trollobj

def displaytroll(t0):
 print(t0.firname + " " + t0.surname + ", " + t0.blood + " " + t0.sex + ", " + t0.caste + ", " + t0.powers) 
 #display seadweller status t0.sea = "N"
 print(t0.height + ", " + t0.build + " build, " + t0.hair + ", " + t0.skin + " skin")
 print("L: " + t0.hornL)
 print("R: " + t0.hornR)
 return
 
main()
