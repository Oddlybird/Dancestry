import random
import re
import colorsys
import colorgarbage as colg
import formattingbs as fbs
import names
import slurry

# Phenotype Classes, containing genes

# Eventual goal :
# -- Genes contain Objects.
# -- Objects and Genes contain a "code" text string, summarizing all other contents
# -- Objects and Genes have an init, where they can be fed a code, which will populate it with data

# Need a horn genestrand class that contains 4-6 horn objects
# Need to add horn headcanons to genestrand: keratin, sensory horns,
# Doubled-horn gene primarily activates in trolls with rG, RG, or Rg blood.
# Possibly only when there are recessive seadweller genes and active psychic ones?

# genestrand: epigenetics.  Contains blood + copies of epigenetic genes
# genestrand: psychic, eldritch, voodoo, etc
# genestrand: feral traits
# genestrand: leg / arm mutations
# genestrand: wings
# genestrand: tail
# genestrand: organ systems, internal differences based on headcanons, genetic diseased/syndromes/mutations
# genestrand: hands/fingers, toes/feet
# genestrand: discolorations (hair, skin, blood, hello karkat)
# genestrand: gender dimorphism, XY, build / body shape
# genestrand: physical / mental stats, that effect traits / interests.
#             match trolls to occupations/interests similar to dwarf therapist
# genestrand: skin issues, scales/fur/feather patches, weird hair textures, strange claws
# ----------: misc other mutations?


# Make a troll class instead?
def trolldict():  # trolldeets
    bloodreal = premadeblood()
    blood = bloodreal[0:2]
    sea = slurry.genesealand
    if slurry.spectrumdwell[blood] != "landdweller":
        sea = slurry.geneseasea
    t0 = {
        "savetype": "9",  # Save Version
        "firname": "FIRNAM",  # six letters
        "surname": "SURNAM",  # six letters
        "sex": "N",  # M/N/F
        "blood": bloodreal,  # RGB rgb
        "caste": getcastefromblood(blood),
        "dwell": slurry.spectrumdwell[blood],
        "seadesc": describesea(blood, sea),
        "mouth": slurry.spectrumgenemouth[blood],
        "sea": sea,
        # pawfeet, tail, wing, hairstreaks, grubscars, ?
        "powers": "powers",  # psychic, voodoo, eldritch, none.  specify type later.  Make psychics eyes glow colors?
        "hornL": slurry.spectrumgenehorn["rG"],           # remove eventually
        "hornR": slurry.spectrumgenehorn["rG"],           # remove eventually
        "hornLdesc": describehorn(slurry.spectrumgenehorn["rG"]),
        "hornRdesc": describehorn(slurry.spectrumgenehorn["rG"]),
        "horns": slurry.spectrumgenehorn["rG"],
        "hornsdesc": "",  # To Do
        "height": slurry.spectrumheight[blood],                     # height in inches
        "heightstr":  heightstr(slurry.spectrumheight[blood]),  # human-readable
        "build": "medium",   # more detailed data later
        "hair": "short",     # more detailed data later.  medium/long.
        "skin": "grey",      # freckles, stripes, birthmarks, vitiligo, melanism, albinism, etc.
        "donator1": "?.?",   # higher caste donator
        "donator2": "?.?",   # lower caste donator
    }
    return t0


def getpremadetroll(x=random.randint(1, 3)):
    t0 = trolldict()
    # Things that aren't really enabled yet.
    # Go through and give each troll a different one once the systems exist.
    strpowers = "None"
    strskin = "grey"
    donator1 = "The Mists"
    donator2 = "Of Time"
    height = "84"  # 7 feet
    strbuild = "thin"
    mouth = slurry.genemouthlow
    strhair = "short"
    if (x % 2) == 0:
        strbuild = "big"
        strhair = "long"

    if x == 1:
        t0["firname"] = "Libbie"
        t0["surname"] = "Pickle"
        t0["sex"] = "F"
        t0["blood"] = "rGg"
        t0["sea"] = slurry.genesealand
        t0["powers"] = strpowers
        t0["mouth"] = slurry.genemouthlow
        t0["horns"] = slurry.spectrumgenehorn["rG"]
        t0["height"] = 64
        t0["build"] = strbuild
        t0["hair"] = strhair
        t0["skin"] = strskin
        t0["donator1"] = donator1
        t0["donator2"] = donator2
    if x == 2:
        t0["firname"] = "Lester"
        t0["surname"] = "Pebble"
        t0["sex"] = "M"
        t0["blood"] = "RBb"
        t0["mouth"] = slurry.genemouthhigh
        t0["sea"] = slurry.geneseasea
        t0["powers"] = strpowers
        t0["horns"] = slurry.spectrumgenehorn["RB"]
        t0["height"] = 89
        t0["build"] = strbuild
        t0["hair"] = strhair
        t0["skin"] = strskin
        t0["donator1"] = "The Mists"
        t0["donator2"] = "Of Time"
    if x == 3:
        t0["firname"] = "Lobbah"
        t0["surname"] = "Parkle"
        t0["sex"] = "N"
        t0["blood"] = "bbb"
        t0["sea"] = slurry.geneseamutant
        t0["mouth"] = slurry.genemouthmutant
        t0["powers"] = strpowers
        # doubled genes, make just one horn doubled.
        t0["horns"] = slurry.spectrumgenehorn["bb"]
        t0["height"] = 72
        t0["build"] = strbuild
        t0["hair"] = strhair
        t0["skin"] = strskin
        t0["donator1"] = "The Mists"
        t0["donator2"] = "Of Time"
    h = t0["height"]
    t0["heightstr"] = ""
    return t0


# Incomplete
class EyeObj:
    code = ""           #
    active = "AA"       # eye present or unexpressed?
    multipupil = "PP"   # multiple pupils Y/N?  PP = Y, all else = no.
    colors = "CC"       # solid color eye?  CC = Y, all else = no.
    glow = "GG"         # eye glow?   Leave this piece unused for now.  Replace at will.
    sym = "Y"           # symmetry.  blend Y eyes together, N's together, Y's overwrite N's.
    pupilnum = 1        # number of pupils in this eye
    pupilshape = "RR"   # R = round.  Capital dominant, lowercase not dominant.
    # Octopus, goat, round, triangle, symbols, oval, slit pupil, diamond, star, ?
    nearsighted = "nn"  # capital letters = yes
    farsighted = "ff"   #
    astigmatism = "aa"  #
    blindness = "bb"    #
    colorblind = "cc"   #

    def __init__(self, code):
        self.code = code
        # When activating eye objects, include code parsing data here


class HornObj:  # trolldeets
    # Horns are stored in trolls as just the code part.  Use this class when manipulating.
    # create a horn by going horn-variable = HornObj("21RIn.f point"), or horn-variable = HornObj(troll.hornL)
    code = "21RInP"
    length = 2  # 1 = 0-1 handspans, 2 = 1-2 handspans, 3 = 2-3 handspans, 4 = 3+ handspans.
    curl = 1
    # 1 = straight, 2 = up to 45 degrees, 3 = 90 degrees +/- 45, 4 = 180 +/- 45,
    # 5 = 270 +/- 45, 6 = 360 +/-45, 7 = ampora wave-like curves
    radial = "R"  # cross-section shape.  R = round, O = Oval, T = triangular, S = spiraling like a goat.
    dir = "I"
    # primary growth direction.  F = frontwards, B = backwards, O = outwards (usually up), I = inwards (usually up).
    wide = "n"  # n = normal width like terezi.  w = wide base, like nepeta.
    tip = "P"  # shape of the point.  Point, Cone, Split/Pincher, Jagged, Round, hook, ...
    # P, C, S, J, R, H
    # Add :  HornObj bumps, doubled horns, notched and rounded-notched horns
    # bolt-tipped
    # branched / antler horns, sheet-like moose horns

    def __init__(self, code):
        t0 = horncode(code)
        self.length = t0["length"]
        self.curl = t0["curl"]
        self.radial = t0["radial"]
        self.dir = t0["dir"]
        self.wide = t0["wide"]
        self.tip = t0["tip"]
        self.code = self.update()

    def desc(self):
        # convert the current features of the horn into a verbal description as in basic version.
        # use by going description-string = horn-temp.desc()
        descr = str(describehorn(self.code))
        return descr

    def update(self):
        code = str(self.length) + str(self.curl) + str(self.radial) + str(
            self.dir) + str(self.wide) + str(self.tip)
        return code


# Incomplete
class Eyes:
    Eye1 = EyeObj  # left main, active
    Eye2 = EyeObj  # right main, active
    Eye3 = EyeObj  # inactive, left
    Eye4 = EyeObj  # inactive, right
    Eye5 = EyeObj  # inactive, center
    # need a bio function for blending and producing these
    # bio function: describe eyes

    def __init__(self, code):
        self.code = code
        # When activating Eye genes, include code parsing data here
# eye mutations:  octopus pupils, vision 8fold, 1 eye,


class Horns:
    code = ""
    blood = ""
    controls = ""
    hornleft1 = ""   # Primary
    hornleft2 = ""   # Secondary
    hornleft3 = ""   # Ultra-recessive
    hornright1 = ""  # Primary
    hornright2 = ""  # Secondary
    hornright3 = ""  # Ultra-recessive

    def __init__(self, code):
        t0 = codehorns(code)
        self.blood = t0["blood"]      # first 3 characters.  if 2-letter blood, third letter is x.
        self.controls = t0["controls"]     # 10 letters ( 5 .'s and 5 x's)
        self.hornleft1 = t0["hornleft1"]    # 6 letters
        self.hornleft2 = t0["hornleft2"]    # 6 letters
        self.hornleft3 = t0["hornleft3"]    # 6 letters
        self.hornright1 = t0["hornright1"]  # 6 letters
        self.hornright2 = t0["hornright2"]  # 6 letters
        self.hornright3 = t0["hornright3"]  # 6 letters
        self.code = self.update()
        return

    def update(self):
        self.code = str(self.blood) + str(self.controls) + "." + str(
            self.hornleft1) + "." + str(self.hornleft2) + "." + str(self.hornleft3) + "." + str(
            self.hornright1) + "." + str(self.hornright2) + "." + str(self.hornright3)
        return self.code

    def desc(self):
        descr = str(describehorns2(self.code))
        return descr


# Incomplete
class Mouth:
    # general mouth traits
    code = ""
    lipl = 6       # minimum tooth height to poke out over the lip
    lipw = 4       # furthest-out visible tooth; mouth width
    double = "dd"  # if teeth are doubled, second row identical to first.
#    length        # 0 - 9.  0 = gums, 4 = normal, 8 = 2x normal, 9 = giant.
#    sym           # T/F symmetry overrides
#    type          # Cc choppy/flat, Gg grinding, Pp pointy, serrated (?) other (?)
    symtopl = ""         # [0] = center, [6] = molar
    lengthtopl = ""      # [0] = center, [6] = molar
    typetopl = ""        # [0] = center, [6] = molar
    symtopr = ""         # [0] = center, [6] = molar
    lengthtopr = ""      # [0] = center, [6] = molar
    typetopr = ""        # [0] = center, [6] = molar
    symbotl = ""         # [0] = center, [6] = molar
    lengthbotl = ""      # [0] = center, [6] = molar
    typebotl = ""        # [0] = center, [6] = molar
    symbotr = ""         # [0] = center, [6] = molar
    lengthbotr = ""      # [0] = center, [6] = molar
    typebotr = ""        # [0] = center, [6] = molar
    # TT -> average them
    # TF -> T overwrites F
    # FF -> the two teeth are distinct

    def __init__(self, code):
        t0 = codemouth(code)
        self.lipl = t0["lipl"]
        self.lipw = t0["lipw"]
        self.double = t0["double"]
        self.symtopl = t0["symtopl"]
        self.symtopr = t0["symtopr"]
        self.symbotl = t0["symbotl"]
        self.symbotr = t0["symbotr"]
        self.lengthtopl = t0["lengthtopl"]
        self.lengthtopr = t0["lengthtopr"]
        self.lengthbotl = t0["lengthbotl"]
        self.lengthbotr = t0["lengthbotr"]
        self.typetopl = t0["typetopl"]
        self.typetopr = t0["typetopr"]
        self.typebotl = t0["typebotl"]
        self.typebotr = t0["typebotr"]
        self.code = self.update()

    def update(self):
        self.code = str(self.lipl) + str(self.lipw) + str(self.double) + str(
            self.symtopl) + str(self.lengthtopl) + str(self.typetopl) + str(
            self.symtopr) + str(self.lengthtopr) + str(self.typetopr) + str(
            self.symbotl) + str(self.lengthbotl) + str(self.typebotl) + str(
            self.symbotr) + str(self.lengthbotr) + str(self.typebotr)
        return self.code


class Aquatic:
    # This contains genes relating to aquatic and amphibious traits
    # These will be stored in trolls as just the code part.  Use this class when manipulating.
    # create gene object by going temp1 = SeaGenes("Ssx"),temp1 = SeaGenes(troll["sea"])
    blood = "rr"
    code = "ssssbbccEEwwwwffbbsbfggiggiggittdeeAAAA"  # The code used to store data longterm.
    SS = "sssss"          # SS = seadweller, Ss/sS = depends on genes, ss = land-dweller.
    s0w = "N"  # Ears, Fins, wfingers, wtoes:  are any of the genes tied to SS2[0] active?
    s1w = "N"  # gillneck, gillneckt, gillribs, gillribst, gillface, gillfacet, salt, air
    s2w = "N"  # bladders,
    s3w = "N"  # biolum, teeth
    s4w = "N"  # eyelids, dorsal / bodyfins
    bladders = "bb"    # Swim bladders - several / one / none
    cheekfins = "cc"     # yes / half / no
    # Make genes for earfin size, number of tines, etc.
    ears = "EE"        # yes / half / no.   Someday ear types?
    wfingers = "ww"    # webbed fingers?  full/half/none
    wtoes = "ww"       # webbed toes, full/half/none
    dorsalfins = "ff"  # big/small/none
    biolum = "bb"      # y/n
    # patterns, brightness, colors, conscious / unconscious control, steady state vs bloodflow, fin glow, eye glow..
    salt = "sbf"       # Saltwater(Y/n)?  Brackish (Y/N)?  Fresh (Y/N)?   S/s, B/b, F/f.
    gillneck = "gg"    # full/half/none
    gillneckt = "i"    # i: internal.  e: external.
    gillribs = "gg"     # full/half/none
    gillribst = "i"     # i: internal, e: external
    gillface = "gg"    # ocular gills, internal/external/none.
    gillfacet = "i"    # i: internal, e: external
    teeth = "ttd"      # t = land, T = barracuda, Tt = blend, d/D = doubled vs single
    eyelids = "ee"     # ee = single, eE = permanent transparent coating, EE = doubled transparent lids
    air = "AAAA"       # Can the troll breathe air?  All four must be "a" to produce a no.

    def __init__(self, blood, code):
        self.blood = blood
        a = aquaticcode(code)
        self.SS = a["SS"]
        self.air = a["air"]
        self.bladders = a["bladders"]
        self.cheekfins = a["cheekfins"]
        self.ears = a["ears"]
        self.wfingers = a["wfingers"]
        self.wtoes = a["wtoes"]
        self.dorsalfins = a["dorsalfins"]
        self.biolum = a["biolum"]
        self.salt = a["salt"]
        self.gillneck = a["gillneck"]
        self.gillneckt = a["gillneckt"]
        self.gillribs = a["gillribs"]
        self.gillribst = a["gillribst"]
        self.gillface = a["gillface"]
        self.gillfacet = a["gillfacet"]
        self.teeth = a["teeth"]
        self.eyelids = a["eyelids"]

# NOTE TO SELF
    def dwell(self):
        # land dweller or sea?
        # use by going temp2 = temp1.desc()
        descr = describedwell(self.code)
        return descr

    def desc(self):
        # verbal description of aquatic traits
        # Include specifics of all genes that differ from slurry defaults for landdweller / seadweller
        descr = describesea(self.blood, self.code)
        return descr

    def updatess(self):
        # check if any of the relevant genes are active for each
        # ld = Aquatic("rr", slurry.genesealand)
        sd = Aquatic("rr", slurry.genesealand)
        dwell = self.dwell()
        if self.SS != "SSSSS" and self.SS != "sssss":
            if self.SS[0] == "S":
                if self.ears[0] != self.ears[1]:
                    self.s0w = "Y"
                if dwell[0] != "l" and self.ears[0] == "e" or self.ears[1] == "e":
                    self.s0w = "Y"
                if dwell[0] != "s" and self.ears[0] == "S" or self.ears[1] == "S":
                    self.s0w = "Y"
                if self.cheekfins[0] == "F" or self.ears[1] == "F":
                    self.s0w = "Y"
                if self.wfingers[0] == "W" or self.wfingers[1] == "W":
                    self.s0w = "Y"
                if self.wtoes[0] == "W" or self.wtoes[1] == "W":
                    self.s0w = "Y"
                self.s0w = "Y"
            if self.SS[0] == "s":
                self.s0w = "N"
            if self.SS[1] == "S":
                if self.gillneck[0] == "G" or self.gillneck[1] == "G":
                    self.s1w = "Y"
                if self.gillfacet[0] != sd.gillfacet:
                    self.s1w = "Y"
                if self.gillribs[0] == "G" or self.gillribs[1] == "G":
                    self.s1w = "Y"
                if self.gillribst[0] != sd.gillribst:
                    self.s1w = "Y"
                if self.gillface[0] == "G" or self.gillface[1] == "G":
                    self.s1w = "Y"
                if self.gillfacet[0] != sd.gillfacet:
                    self.s1w = "Y"
                if self.salt[0] == "S" or self.salt[1] == "B" or self.salt[2] == "F":
                    self.s1w = "Y"
                if countaa(self.air) > 2:
                    self.s1w = "Y"
                self.s1w = "Y"
            if self.SS[1] == "s":
                self.s1w = "N"
            if self.SS[2] == "S":
                if self.bladders[0] == "B" or self.bladders[1] == "B":
                    self.s2w = "Y"
                self.s2w = "Y"
            if self.SS[2] == "s":
                self.s2w = "N"
            if self.SS[3] == "S":
                if self.biolum[0] == "B" or self.biolum[1] == "B":
                    self.s3w = "Y"
                if self.teeth[0] == "T" or self.teeth[1] == "T":
                    self.s3w = "Y"
                self.s3w = "Y"
            if self.SS[3] == "s":
                self.s3w = "N"
            if self.SS[4] == "S":
                if self.eyelids[0] == "E" or self.eyelids[1] == "E":
                    self.s4w = "Y"
                if self.dorsalfins[0] == "F" or self.dorsalfins[1] == "F":
                    self.s4w = "Y"
            if self.SS[4] == "s":
                self.s4w = "N"

        return


def aquaticcode(code):
    c = 0
    aSS = code[c:c + 5]  # First two letters are whether seadweller genes are active or not.
    c = c + 5
    abladders = code[c:c + 2]
    c = c + 2
    acheekfins = code[c:c + 2]
    c = c + 2
    aears = code[c:c + 2]
    c = c + 2
    awfingers = code[c:c + 2]
    c = c + 2
    awtoes = code[c:c + 2]
    c = c + 2
    adorsalfins = code[c:c + 2]
    c = c + 2
    abiolum = code[c:c + 2]
    c = c + 2
    asalt = code[c:c + 3]
    c = c + 3
    agillneck = code[c:c + 2]
    c = c + 2
    agillneckt = code[c]
    c = c + 1
    agillribs = code[c:c + 2]
    c = c + 2
    agillribst = code[c]
    c = c + 1
    agillface = code[c:c + 2]
    c = c + 2
    agillfacet = code[c]
    c = c + 1
    ateeth = code[c:c + 3]
    c = c + 3
    aeyelids = code[c:c + 2]
    c = c + 2
    aair = code[c:c + 4]
    aquacode = {
        "SS": aSS, "bladders": abladders, "cheekfins": acheekfins, "ears": aears, "wfingers": awfingers,
        "wtoes": awtoes, "dorsalfins": adorsalfins, "biolum": abiolum, "salt": asalt, "air": aair,
        "gillneck": agillneck, "gillneckt": agillneckt, "gillribs": agillribs, "gillribst": agillribst,
        "gillface": agillface, "gillfacet": agillfacet, "teeth": ateeth, "eyelids": aeyelids
        }
    return aquacode


def horncode(code):
    # Produces the individual stats from the code, on a per-horn basis
    c = 0
    curl = code[c]
    c = c + 1
    length = code[c]
    c = c + 1
    radial = code[c]
    c = c + 1
    dir = code[c]
    c = c + 1
    wide = code[c]
    c = c + 1
    tip = code[c]  # everything else in string = the tip type.
    thing = {"length": length, "curl": curl, "radial": radial, "dir": dir, "wide": wide, "tip": tip,}
    return thing


def codehorns(code):
    # produces the parts from the code, from a -set- of horns.
    c = 0
    blood = code[c:c+3]
    c = c + 3
    controls = code[c:c+10]
    c = c + 10
    c = c + 1  # Because there's a "."
    hornleft1 = code[c:c+6]
    c = c + 6
    c = c + 1  # Because there's a "."
    hornleft2 = code[c:c+6]
    c = c + 6
    c = c + 1  # Because there's a "."
    hornleft3 = code[c:c+6]
    c = c + 6
    c = c + 1  # Because there's a "."
    hornright1 = code[c:c+6]
    c = c + 6
    c = c + 1  # Because there's a "."
    hornright2 = code[c:c+6]
    c = c + 6
    c = c + 1  # Because there's a "."
    hornright3 = code[c:c+6]
    c = c + 6
    thing = {"blood": blood, "controls": controls,
             "hornleft1": hornleft1, "hornleft2": hornleft2, "hornleft3": hornleft3,
             "hornright1": hornright1, "hornright2": hornright2, "hornright3": hornright3, }
    return thing


def codemouth(code):
    c = 0
    lipl = code[c]
    c = c + 1
    lipw = code[c]
    c = c + 1
    double = code[c:c+2]
    c = c + 2

    symtopl = code[c:c+6]
    c = c + 6
    lengthtopl = code[c:c+6]
    c = c + 6
    typetopl = code[c:c+6]
    c = c + 6

    symtopr = code[c:c+6]
    c = c + 6
    lengthtopr = code[c:c+6]
    c = c + 6
    typetopr = code[c:c+6]
    c = c + 6

    symbotl = code[c:c+6]
    c = c + 6
    lengthbotl = code[c:c+6]
    c = c + 6
    typebotl = code[c:c+6]
    c = c + 6

    symbotr = code[c:c+6]
    c = c + 6
    lengthbotr = code[c:c+6]
    c = c + 6
    typebotr = code[c:c+6]
    c = c + 6

    thing = {"lipl": lipl, "lipw": lipw, "double": double,
             "symtopl": symtopl, "lengthtopl": lengthtopl, "typetopl": typetopl,
             "symtopr": symtopr, "lengthtopr": lengthtopr, "typetopr": typetopr,
             "symbotl": symbotl, "lengthbotl": lengthbotl, "typebotl": typebotl,
             "symbotr": symbotr, "lengthbotr": lengthbotr, "typebotr": typebotr,
             }
    return thing


# Below are the contents of what used to be called biology.py

# This file contains basic formatting information,
# Functions that are used to combine info from a slurry,
# Functions that manipulate / interact with troll data


def slurrytroll(spectrum):
    # Record Donators
    strdonator1 = "?.?"
    strdonator2 = "?.?"
    # Blood + Caste:
    a = 0
    strblood = "rrx"
    while a == 0:
        strblood = premadeblood()
        for arb in spectrum:
            if arb == strblood:
                a = a + 1
    strcaste = getcastefromblood(strblood)

    # height
    a = random.randint(85, 115)
    a = a / 100
    a = a * slurry.spectrumheight[strblood[0:2]]
    a = round(a)
    strheight = a

    # The sea-activating gene CAN be anything.
    sgenetype = slurry.spectrumgenesea[strblood[0:2]]
    if slurry.spectrumdwell == "landdweller":
        sgenetype = slurry.genesealand
    if slurry.spectrumdwell == "seadweller":
        sgenetype = slurry.geneseasea
    strsea1 = genecombine(slurry.geneseamutant, sgenetype)  # Mutant + dweller type
    strsea2 = genecombine(strsea1, sgenetype)             # Dilute that with dweller type again.
    sgenetype = slurry.spectrumgenesea[strblood[0:2]]
    strsea3 = genecombine(strsea2, sgenetype)   # Caste-specific...
    strsea = genecombine(strsea3, sgenetype)    # Caste-specific...
    gene1 = Aquatic(strblood, strsea)
    strseadesc = gene1.desc()

    mouthgenetype = slurry.spectrumgenemouth[strblood[0:2]]
    strmouthgene = genecombine(slurry.genemouthmutant, mouthgenetype)
    strmouthgene = mouthaverager(strmouthgene)
    strmouthgene = genecombine(strmouthgene, mouthgenetype)

# Phenotype shit comes later.
    # traits come later.
    # Powers
    # Build
    # hair
    # skin

    # sex
    strsex = getsex(strblood)

    # Make horns.
    horned = randhorns(strblood[0:2])
    hornsfinal = hornsetaverager(horned)
    hornset = Horns(hornsfinal)
    hornl = HornObj(hornset.hornleft1)
    hornr = HornObj(hornset.hornright1)
    strhornl = hornl.desc()
    strhornr = hornr.desc()

    # names
    firstname = names.newname()
    lastname = names.newname()

    t1 = trolldict()
    t1["firname"] = firstname
    t1["surname"] = lastname
    t1["sex"] = strsex
    t1["blood"] = strblood
    t1["caste"] = strcaste
    t1["seadesc"] = strseadesc
    t1["hornLdesc"] = strhornl
    t1["hornRdesc"] = strhornr
    t1["sea"] = strsea
    t1["mouth"] = strmouthgene
    #    t1["powers"] = ,
    t1["horns"] = hornsfinal
    t1["height"] = strheight
    #    t1["build"] = ,
    #    t1["hair"] = ,
    #    t1["skin"] = ,
    t1["donator1"] = strdonator1
    t1["donator2"] = strdonator2

    return t1


def blendtroll(trolla, trollb, trollblank=""):  # trolldeets
    if trollblank == "":
        trollblank = trolldict()  # Set it equal to the blank value.
    # Start by making sure the donators are ready to read.
    # error-checking code to give a default set of trolls if needed
    if trolla == trollblank:      # if p1 = default ...
        trolla = slurry.getpremadetroll(1)
    if trollb == trollblank:        # if p2 = default ...
        trollb = slurry.getpremadetroll(2)
    # decide who is p1 based on hemism.
    # by default, guess p1 is higher.
    caste1 = trolla["blood"]
    caste2 = trollb["blood"]
    p1 = trolla
    p2 = trollb
    if caste2 == highercaste(caste1, caste2):
        # if p2 is higher, swap them.
        p2 = trolla
        p1 = trollb

    # Record Donators
    strdonator1 = p1["firname"][0] + "." + p1["surname"]
    strdonator2 = p2["firname"][0] + "." + p2["surname"]

    # Blood + Caste:
    temp1 = p1["blood"]
    temp2 = p2["blood"]
    a = random.randint(0, len(temp1) - 1)
    b = random.randint(1, len(temp1) - 1)
    c = random.randint(0, len(temp2) - 1)
    d = random.randint(1, len(temp2) - 1)
    strblood = temp1[a] + temp1[b] + temp2[c] + temp2[d]
    strblood = bloodsort(strblood)
    strblood = strblood[0] + strblood[1] + strblood[2]
    x = random.randint(1, 2)
    if x == 1:
        strblood = strblood[0] + strblood[1]
    strcaste = getcastefromblood(strblood)

    # Height
    x = random.randint(95, 105)
    x = x / 100

    ph1 = int(p1["height"]) / slurry.spectrumheight[p1["blood"][0:2]]
    ph2 = int(p2["height"]) / slurry.spectrumheight[p2["blood"][0:2]]
    ph3 = (ph1 + ph2) / 2
    y = ph3 * slurry.spectrumheight[strblood[0:2]] * x
    y = round(y)
    strheight = int(y)

    # str-sea = Phenotype shit comes later.
    strsea = genecombine(p1["sea"], p2["sea"])
    gene1 = Aquatic(strblood, strsea)
    strseadesc = gene1.desc()

    castemouth = slurry.spectrumgenemouth[strblood[0:2]]
    mutationsource = mouthblender(slurry.genemouthmutant, castemouth, castemouth)
    basicmouth = mouthblender(p1["mouth"], p2["mouth"], mutationsource)
    strmouth = mouthaverager(basicmouth)

    # traits come later.
    # Powers
    # Build
    # hair
    # skin

    # sex
    strsex = getsex(strblood)

    # Make horns.  The hornblender is biased, and 2/3 of results will be from the first two horns input.
    strhorns = hornblender(p1["horns"], p2["horns"], strblood)
    horns = Horns(strhorns)
    hornl = HornObj(horns.hornleft1)
    strhornl = hornl.desc()
    hornr = HornObj(horns.hornright1)
    strhornr = hornr.desc()

    # names
    firstname = names.newname()
    lastname = names.newname()

    t1 = trolldict()
    t1["firname"] = firstname
    t1["surname"] = lastname
    t1["sex"] = strsex
    t1["caste"] = strcaste
    t1["seadesc"] = strseadesc
    t1["hornLdesc"] = strhornl
    t1["hornRdesc"] = strhornr
    t1["blood"] = strblood
    t1["sea"] = strsea
    t1["mouth"] = strmouth
#    t1["powers"] = ,
    t1["horns"] = strhorns
    t1["height"] = strheight
#    t1["build"] = ,
#    t1["hair"] = ,
#    t1["skin"] = ,
    t1["donator1"] = strdonator1
    t1["donator2"] = strdonator2

    return t1


def randhorns(inblood="Rg"):
    inblood = inblood[0:2]
    basehorn = slurry.spectrumgenehorn[inblood]
    horn1 = genecombine(basehorn, slurry.spectrumgenehorn[neighborcaste(inblood, "-", 1)])
    horn2 = genecombine(horn1, slurry.spectrumgenehorn[neighborcaste(inblood, "+", 1)])
    horn3 = genecombine(horn2, slurry.spectrumgenehorn[inblood])
    outhorn = inblood
    while len(outhorn) < 3:
        outhorn = outhorn + "x"
    outhorn = outhorn + horn3[3:len(horn3)]
    return outhorn


def randhorn(inhorn=""):
    # be able to specify particular parts of the horn for randomization via the input?
    horn = ""
    if len(inhorn) < 2:
        # length in handspans
        x = random.randint(1, 4)
        horn = str(x)
        # curliness (straight, 45 degree, 90 degree, 180, 270, 360, ampora.)
        x = random.randint(1, 7)
        horn = horn + str(x)
        # Cross-section shape.  R = round, O = oval, T = triangular/edged, S = spiral/twisted like goat.
        x = random.randint(1, 6)
        if x == 1:
            horn = horn + "S"
        if x == 2:
            horn = horn + "T"
        if x == 3:
            horn = horn + "O"
        if x > 3:
            horn = horn + "R"
        # Primary growth direction.  F = forward, B = back, O = outward/side, I = inwards/up/default.
        x = random.randint(1, 7)
        if x == 1:
            horn = horn + "F"
        if x == 2:
            horn = horn + "B"
        if x == 3:
            horn = horn + "O"
        if x == 4:
            horn = horn + "S"
        if x > 4:
            horn = horn + "I"
        # Width.  w = nepetalike, n = normal.
        x = random.randint(1, 15)
        if x == 1:
            horn = horn + "w"
        if x > 1:
            horn = horn + "n"
        # Point shape
        # change xmax to match
        x = random.randint(1, 15)
        if x == 1:
            horn = horn + "B"  # bump
        if x == 2:
            horn = horn + "b"  # branching
        if x == 3:
            horn = horn + "C"  # cone
        if x == 4:
            horn = horn + "F"  # flat
        if x == 5:
            horn = horn + "H"  # hook
        if x == 6:
            horn = horn + "J"  # jagged
        if x == 7:
            horn = horn + "N"  # notched
        if x == 8:
            horn = horn + "P"  # point
        if x == 9:
            horn = horn + "p"  # pincher
        if x == 10:
            horn = horn + "R"  # round
        if x == 11:
            horn = horn + "S"  # split
        if x == 12:
            horn = horn + "s"  # spade
        if x > 12:
            horn = horn + "P"  # point
    return horn


def hornblender(horna, hornb, strblood):
    horn1 = genecombine(horna, hornb)
    horn2 = hornsetaverager(horn1)
    horns = genecombine(horn2, slurry.spectrumgenehorn[strblood[0:2]])
    outhorn = strblood
    while len(outhorn) < 3:
        outhorn = outhorn + "x"
    t0 = outhorn + horns[3:len(horns)]
    t1 = hornsetaverager(t0)
    return t1


def hornaverager(hornl, hornr):
    # average horns together some.
    e = random.randint(1, 3)
    # average length; 2/3 same length.
    if e == 1:
        hornl = hornr[0] + hornl[1:len(hornl)]
    if e == 2:
        hornr = hornl[0] + hornr[1:len(hornr)]
    # average curl, 2/3 same curl.
    e = random.randint(1, 3)
    if e == 1:
        hornl = hornl[0] + hornr[1] + hornl[2:len(hornl)]
    if e == 2:
        hornr = hornr[0] + hornl[1] + hornr[2:len(hornr)]
    # average Radial.  They WILL have the same cross section shape, it looks silly if they don't.
    e = random.randint(1, 2)
    if e < 2:
        hornl = hornl[0] + hornl[1] + hornr[2] + hornl[3:len(hornl)]
    if e > 1:
        hornr = hornr[0] + hornr[1] + hornl[2] + hornr[3:len(hornr)]
    # average dir, 2/3 chance of matching
    e = random.randint(1, 3)
    if e == 1:
        hornl = hornl[0] + hornl[1] + hornl[2] + hornr[3] + hornl[4:len(hornl)]
    if e == 2:
        hornr = hornr[0] + hornr[1] + hornr[2] + hornl[3] + hornr[4:len(hornr)]
    # average width :  2/3 chance the width will match.
    e = random.randint(1, 3)
    if e == 1:
        hornl = hornl[0] + hornl[1] + hornl[2] + hornl[3] + hornr[4] + hornl[5:len(hornl)]
    if e == 2:
        hornr = hornr[0] + hornr[1] + hornr[2] + hornr[3] + hornl[4] + hornr[5:len(hornr)]
    # average point, 2/5 chance of match
    e = random.randint(1, 5)  #
    if e == 1:
        hornl = hornl[0] + hornl[1] + hornl[2] + hornl[3] + hornl[4] + hornr[5:len(hornr)]
    if e == 2:
        hornr = hornr[0] + hornr[1] + hornr[2] + hornr[3] + hornr[4] + hornl[5:len(hornl)]
    return hornl, hornr


def hornsetaverager(horned):
    strblood = horned[0:3]
    horns = Horns(horned)
    hornleft1 = horns.hornleft1
    hornleft2 = horns.hornleft2
    hornleft3 = horns.hornleft3
    hornright1 = horns.hornright1
    hornright2 = horns.hornright2
    hornright3 = horns.hornright3
    (hornleft1, hornleft2) = hornaverager(hornleft1, hornleft2)
    (hornright2, hornleft3) = hornaverager(hornright2, hornleft3)
    (hornright1, hornright2) = hornaverager(hornright1, hornright2)
    (hornright3, hornleft2) = hornaverager(hornright3, hornleft2)
    (hornleft1, hornright1) = hornaverager(hornleft1, hornright1)
    outhorn = strblood
    while len(outhorn) < 3:
        outhorn = outhorn + "x"
    hornsfinal = outhorn + horns.code[3:13] + "." + hornleft1 + "." + hornleft2 + "." + hornleft3 + "." + hornright1 + "." + hornright2 + "." + hornright3
    return hornsfinal


def mouthblender(mouth1, mouth2, basis):
    moutha = genecombine(mouth1, basis)
    mouthb = genecombine(mouth2, basis)
    mouth3 = genecombine(moutha, mouthb)
    return mouth3


def mouthaverager(mouth1):
    mg1 = Mouth(mouth1)
    mg2 = Mouth(mouth1)
    mg2.symtopl = genecombine(mg1.symtopr, mg1.symtopl)
    mg2.symtopr = genecombine(mg1.symtopr, mg1.symtopl)
    mg2.symbotl = genecombine(mg1.symbotr, mg1.symbotl)
    mg2.symbotr = genecombine(mg1.symbotr, mg1.symbotl)
    mg2.lengthtopl = genecombine(mg1.lengthtopr, mg1.lengthtopl)
    mg2.lengthtopr = genecombine(mg1.lengthtopr, mg1.lengthtopl)
    mg2.lengthbotl = genecombine(mg1.lengthbotr, mg1.lengthbotl)
    mg2.lengthbotr = genecombine(mg1.lengthbotr, mg1.lengthbotl)
    mg2.typetopl = genecombine(mg1.typetopr, mg1.typetopl)
    mg2.typetopr = genecombine(mg1.typetopr, mg1.typetopl)
    mg2.typebotl = genecombine(mg1.typebotr, mg1.typebotl)
    mg2.typebotr = genecombine(mg1.typebotr, mg1.typebotl)
    mg2.update()
    return mg2.code


def getcastefromcolor(r, g, b):  # trolldeets
    (h, s, v) = colorsys.rgb_to_hsv(r, g, b)
    hue = h * 360
    hue = round(hue, 3)
    caste = "-"

    if 0 <= hue < 14:
        caste = "Maroon"
    if 14 <= hue < 25:
        caste = "M/B"
    if 25 <= hue < 37:
        caste = "Bronze"
    if 37 <= hue < 58:
        caste = "B/G"
    if 58 <= hue < 75:
        caste = "Gold"
    if 75 <= hue < 88:
        caste = "G/L"
    if 88 <= hue < 105:
        caste = "Lime"
    if 105 <= hue < 118:
        caste = "L/O"
    if 118 <= hue < 135:
        caste = "Olive"
    if 135 <= hue < 148:
        caste = "O/J"
    if 148 <= hue < 165:
        caste = "Jade"
    if 165 <= hue < 178:
        caste = "J/T"
    if 178 <= hue < 195:
        caste = "Teal"
    if 195 <= hue < 208:
        caste = "T/C"
    if 208 <= hue < 225:
        caste = "Ceru"
    if 225 <= hue < 238:
        caste = "C/B"
    if 238 <= hue < 255:
        caste = "Blue"
    if 255 <= hue < 268:
        caste = "B/I"
    if 268 <= hue < 285:
        caste = "Indigo"
    if 285 <= hue < 298:
        caste = "I/V"
    if 298 <= hue < 315:
        caste = "Violet"
    if 315 <= hue < 328:
        caste = "V/T"
    if 328 <= hue < 345:
        caste = "Tyrian"
    if 345 <= hue < 361:
        caste = "T/M"

    if (r, g, b) == (255, 0, 0):
        caste = "CULL"
    return caste


def getcastefromblood(innie):
    (r, g, b) = colg.bloodtorgb(innie)
    caste = getcastefromcolor(r, g, b)
    return caste


def getsex(blood):
    # bias this based on caste later.
    sex = " "
    x = random.randint(1, 10)
    if x < 4:
        sex = "M"
    if 4 <= x <= 6:
        sex = "N"
    if x > 6:
        sex = "F"

    (rgb1, rgb2, rgb3) = colg.bloodtorgb(blood)
    hue = colg.rgbtohue(rgb1, rgb2, rgb3)

    x = random.randint(1, 100)
    # jades (hue 150) are more likely to be female.
    if 140 < hue < 160 and x < 25:
        if sex == "N":
            sex = "F"
        if sex == "M":
            sex = "N"
    if 145 < hue < 155 and x < 75:
        if sex == "N":
            sex = "F"
        if sex == "M":
            sex = "N"
    # tyrians (330) are more likely to be female.
    if 320 < hue < 340 and x < 25:
        if sex == "N":
            sex = "F"
        if sex == "M":
            sex = "N"
    if 325 < hue < 335 and x < 75:
        if sex == "N":
            sex = "F"
        if sex == "M":
            sex = "N"
    return sex


def getcastenum(b):
    (cr, cg, cb) = colg.bloodtorgb(b)
    (h, s, v) = colorsys.rgb_to_hsv(cr, cg, cb)
    hue = h * 360
    hue = round(hue)
    val = v / 100
    caste = round(hue + val, 2)
    return caste


def getcastenumstr(b):
    caste = getcastenum(b)
    caste = round(caste)
    caste = str(caste)
    caste = caste.zfill(5)
    return caste


def highercaste(blood1, blood2):
    # input two bloods, return the higher caste.
    caste1 = getcastenum(blood1)
    caste2 = getcastenum(blood2)
    bloodhigher = blood1  # By default assume the first is higher.
    if caste2 > caste1:  # ..but if it's not, fix that.
        bloodhigher = blood2
    return bloodhigher


def neighborcaste(blood, dir="+", number=1):
    castes = {"RR": 0, "Rr": 1, "rr": 2, "rG": 3, "RG": 4, "Rg": 5, "rg": 6, "GG": 7, "Gg": 8, "gg": 9, "Gb": 10,
              "GB": 11, "gB": 12, "gb": 13, "BB": 14, "Bb": 15, "bb": 16, "rB": 17, "RB": 18, "Rb": 19, "rb": 20,
              }
    givencaste = castes[blood[0:2]]
    if blood == "Cull":
        givencaste = 5
    # Define target we're trying to get to
    targetcaste = -1
    if dir == "+":
        targetcaste = givencaste + number
    if dir == "-":
        targetcaste = givencaste - number
    while targetcaste < 0:
        targetcaste = targetcaste + 20
    while targetcaste > 20:
        targetcaste = targetcaste - 20
    # Find the text version of the number in targetcaste
    neighbor = 0
    for x in castes:
        if castes[x] == targetcaste:
            neighbor = x
    return neighbor


def bloodsort(blood):
    a = 0  # count the number of letters stripped out
    sortedblood = ""  # sorted blood code
    for arb in blood:  # for each letter...
        if arb == "R":
            sortedblood = sortedblood + "R"
            a = a + 1
        if a == len(blood) + 1:
            break
    for arb in blood:  # for each letter...
        if arb == "r":
            sortedblood = sortedblood + "r"
            a = a + 1
        if a == len(blood) + 1:
            break
    for arb in blood:  # for each letter...
        if arb == "G":
            sortedblood = sortedblood + "G"
            a = a + 1
        if a == len(blood) + 1:
            break
    for arb in blood:  # for each letter...
        if arb == "g":
            sortedblood = sortedblood + "g"
            a = a + 1
        if a == len(blood) + 1:
            break
    for arb in blood:  # for each letter...
        if arb == "B":
            sortedblood = sortedblood + "B"
            a = a + 1
        if a == len(blood) + 1:
            break
    for arb in blood:  # for each letter...
        if arb == "b":
            sortedblood = sortedblood + "b"
            a = a + 1
        if a == len(blood) + 1:
            break
    return sortedblood


def getoneblood():
    blood = ""
    x = random.randint(1, 15)
    if 1 <= x < 5:
        blood = "R"
    if 5 <= x < 9:
        blood = "r"
    if 9 <= x < 12:
        blood = "G"
    if 12 <= x < 14:
        blood = "g"
    if 14 <= x < 15:
        blood = "B"
    if 15 <= x:
        blood = "b"
    return blood


def premadeblood():
    blood = getoneblood() + getoneblood()
    blood = bloodsort(blood)
    x = random.randint(1, 4)
    if x > 2:
        blood = blood + getoneblood()
    return blood


# Create text descriptions out of raw code input
def heightstr(h):
    h = int(h)
    feet = h // 12
    inches = h % 12
    hstr = str(feet) + "'" + str(inches) + '"'
    return hstr


def describehorn(inhorn="22RInP"):
    temp = HornObj(inhorn)
    descr = ""
    # Length, default 2
    if temp.length == "1":
        descr = "short, "
    if temp.length == "4":
        descr = "long, "
    # Width, default n
    if temp.wide == "w":
        descr = descr + "wide, "
    # Direction, default Inwards
    if temp.dir == "F":
        descr = descr + "front "
    if temp.dir == "B":
        descr = descr + "backswept "
    if temp.dir == "O":
        descr = descr + "outward "
    if temp.dir == "S":
        descr = descr + "side "
    # curves, default = 2 (slightly curved)
    if temp.curl == "1":
        descr = descr + "straight "
    if temp.curl == "3":
        descr = descr + "curved "
    if temp.curl == "4":
        descr = descr + "curled "
    if temp.curl == "5":
        descr = descr + "curly "
    if temp.curl == "6":
        descr = descr + "coiled "
    if temp.curl == "7":
        descr = descr + "wave-like "
    # tip shape
    if temp.tip == "B":
        descr = descr + "bump"
    if temp.tip == "b":
        descr = descr + "branching"
    if temp.tip == "C":
        descr = descr + "cone"
    if temp.tip == "F":
        descr = descr + "flat"
    if temp.tip == "H":
        descr = descr + "hook"
    if temp.tip == "J":
        descr = descr + "jagged"
    if temp.tip == "N":
        descr = descr + "notched"
    if temp.tip == "P":
        descr = descr + "point"
    if temp.tip == "p":
        descr = descr + "pincher"
    if temp.tip == "R":
        descr = descr + "round"
    if temp.tip == "S":
        descr = descr + "split"
    if temp.tip == "s":
        descr = descr + "spade"
    descr = descr + "-tip "
    # radial, default round
    if temp.radial == "O":
        descr = descr + "oval horn"
    if temp.radial == "T":
        descr = descr + "edged horn"
    if temp.radial == "S":
        descr = descr + "twisting horn"
    if temp.radial == "R":
        descr = descr + "round horn"
        # strip spaces
        descr = re.sub(' +', ' ', descr)
        descr = descr.strip()
    return descr


# Change this one to describe a full set of Horns, containing 6 horn objects and some metagenes
def describehorns2(inhorn="22RInP"):
    descr = ""
    return descr


def describesea(bloodcode, sea):    # slurry.spectrumgenesea, blood[0:2]
    # "SSSSSbbCCeeWwWwffBBSBFGGiGGiggittdeeAAAA"
    blood = bloodcode[0:2]
    me = Aquatic(blood, sea)                                   # The troll being tested
    cd = Aquatic(blood, slurry.spectrumgeneseasocial[blood])   # Caste Default
    done = False
    descr = ""
    earfins = ""
    webbing = ""
    gills = ""
    breathes = ""
    bladders = ""
    biolum = ""
    teeth = ""
    eyelids = ""
    bodyfins = ""

    while not done:
        # If someone is arbitrarily set to caste-typical
        if me.SS == "SSSSS":
            dwellvar = slurry.spectrumdwell[blood]
            if dwellvar != "seadweller":
                dwellvar = me.dwell()
            descr = dwellvar
            return descr
        if me.SS == "sssss":
            dwellvar = slurry.spectrumdwell[blood]
            if dwellvar != "landdweller":
                dwellvar = me.dwell()
            descr = dwellvar
            return descr
        # if someone happens to be caste-typical due to epigenetics
#            if not (s0w == "Y" and ((me.code[] != slurry.spectrumblood]))
        # If someone cannot breathe at all
        if me.air == "aaaa" and me.s1w == "Y":
            if me.gillface == "gg" and me.gillneck == "gg" and me.gillribs == "gg":
                descr = "no gills, cannot breathe air"
                return descr
            if me.salt == "sbf":
                descr = "cannot breathe air or water"
                return descr
        break

    # Below this point, everyone has Ss or sS, at least one noteworthy difference from cd, and can breathe.
    # Things that add descriptions to the list, but do not end the loop
    if me.air != "AAAA" and me.air != "aaaa":
        if countaa(me.air) > 1:
            descr = descr + "rank " + str(countaa(me.air) - 1) + " airless"

    if me.SS[0] == "S":  # Webbing, Earfins.
        # limb webbing?  Neck webs?
        # fingers
        fingers = genedesc1(me.wfingers, cd.wfingers, "W", "deeply webbed fingers", "w", "unwebbed fingers", "webbed fingers")
        if fingers == "":
            fingers = "xxx"
        # toes
        toes = genedesc1(me.wtoes, cd.wtoes, "W", "deeply webbed toes", "w", "unwebbed toes", "webbed toes")
        if toes == "":
            toes = "xxx"
        # webbing combo
        webbing = ""
        # If either is caste-normal:
        if fingers == "xxx" and toes != "xxx":
            webbing = toes
        if toes == "xxx" and fingers != "xxx":
            webbing = fingers
        # if both are abnormal:
        if toes != "xxx" and fingers != "xxx":
            webbing = fingers + " and " + toes
        # if both are abnormal in the same way
        if fingers[0] == "u" and toes[0] == "u":
            webbing = "unwebbed fingers and toes"
        if fingers[0] == "d" and toes[0] == "d":
            webbing = "deeply webbed fingers and toes"
        if fingers[0] == "w" and toes[0] == "w":
            webbing = "webbed fingers and toes"
        # If both are differently webbed
        if fingers[0] == "d" and toes[0] == "w":
            webbing = "webbed toes and deeply webbed fingers"
        # ears, cheekfins, and earfins
        ears = genedesc1(me.ears, cd.ears, "E", "full ears", "e", "no ears", "gimpy ears")
        if ears == "":
            ears = "xxx"
        cheekfins = genedesc1(me.cheekfins, cd.cheekfins, "C", "fins", "c", "no cheekfins", "gimpy cheekfins")
        if cheekfins == "":
            cheekfins = "xxx"
        # earfins combo
        earfins = ""
        # If either is caste-normal:
        if cheekfins == "xxx" and ears != "xxx":
            earfins = ears
        if ears == "xxx" and cheekfins != "xxx":
            earfins = cheekfins
        # if both are abnormal:
        if ears != "xxx" and cheekfins != "xxx":
            earfins = cheekfins + " and " + ears
        # if both are abnormal in the same way
        if cheekfins[0] == "n" and ears[0] == "n":
            earfins = "no fins or ears"
        if cheekfins[0] == "f" and ears[0] == "f":
            earfins = "full fins and ears"
        if cheekfins[0] == "g" and ears[0] == "g":
            earfins = "gimpy earfins"
        # If both are differently webbed
        if cheekfins[0] == "f" and ears[0] == "g":
            earfins = "earlike fins"
        if cheekfins[0] == "g" and ears[0] == "f":
            earfins = "finlike ears"
    if me.SS[1] == "S":  # Gills and breathing
        # gilltypes
        gillnecktype = ""
        if me.gillneckt != cd.gillneckt:
            if me.gillneckt == "i":
                gillnecktype = "internal"
            if me.gillneckt == "e":
                gillnecktype = "external"
        gillribstype = ""
        if me.gillribst != cd.gillribst:
            if me.gillribst == "i":
                gillribstype = "internal"
            if me.gillribst == "e":
                gillribstype = "external"
        gillfacetype = ""
        if me.gillfacet != cd.gillfacet:
            if me.gillfacet == "i":
                gillfacetype = "internal"
            if me.gillfacet == "e":
                gillfacetype = "external"
        # neckgills
        gillneck = genedesc1(me.gillneck, cd.gillneck, "G", "full ", "g", "no ", "partial ")
        if gillneck[0:2] != "no" and gillneck != "":
            gillneck = gillneck + gillnecktype + " neckgills"
            if me.gillneck == cd.gillneck:
                gillneck = gillnecktype + " neckgills"
        if gillneck[0:2] == "no":
            gillneck = "no neckgills"
        # rib gills
        gillribs = genedesc1(me.gillribs, cd.gillribs, "G", "full ", "g", "no ", "partial ")
        if gillribs[0:2] != "no" and gillribs != "":
            gillribs = gillribs + gillribstype + " rib gills"
            if me.gillribs == cd.gillribs:
                gillribs = gillribstype + " rib gills"
        if gillneck[0:2] == "no":
            gillneck = "no rib gills"
        # face gills
        gillface = genedesc1(me.gillface, cd.gillface, "G", "full ", "g", "no ", "partial ")
        if gillface[0:2] != "no" and gillface != "":
            gillface = gillface + gillfacetype + " facegills"
            if me.gillface == cd.gillface:
                gillface = gillfacetype + " facegills"
        if gillface[0:2] == "no":
            gillface = "no facegills"
        # gill summary!
        gills = ""
        # If at least one gill area is noteworthy in some way...
        if gillneck != "" or gillribs != "" or gillface != "":
            if gillneck != "":
                gills = fbs.lyst(gills, gillneck)
            if gillribs != "":
                gills = fbs.lyst(gills, gillribs)
            if gillribs != "":
                gills = fbs.lyst(gills, gillface)
            # Find ways to shorten this later maybe.  For now it works.
        # breathability
        breathes = ""
        if me.salt != cd.salt or me.air != cd.air:
            canb = ""
            cantb = ""
            ws = "salt water"
            wb = "brackwater"
            wf = "freshwater"
            wa = "air"
            if me.salt[0] == "S":
                canb = fbs.lyst(canb, ws)
            if me.salt[0] == "s":
                cantb = fbs.lyst(cantb, ws)
            if me.salt[1] == "B":
                canb = fbs.lyst(canb, wb)
            if me.salt[1] == "b":
                cantb = fbs.lyst(cantb, wb)
            if me.salt[2] == "F":
                canb = fbs.lyst(canb, wf)
            if me.salt[2] == "f":
                cantb = fbs.lyst(cantb, wf)
            if countaa(me.air) < 4:
                canb = fbs.lyst(canb, wa)
            if countaa(me.air) > 3:
                cantb = fbs.lyst(cantb, wa)
            if canb == "salt water, brackwater, freshwater":
                canb = "water"
            if cantb == "salt water, brackwater, freshwater":
                cantb = "water"
            breathes = "can breathe " + canb
            if cantb != "":
                breathes = breathes + ", but not " + cantb
            if gills == "" and me.salt == "sbf" and slurry.spectrumdwell[blood] != "landdweller":
                breathes = "breathes " + canb
            if gills == "" and me.salt == "SBF" and slurry.spectrumdwell[blood] != "seadweller":
                breathes = "breathes " + canb
    if me.SS[2] == "S":  # Swimbladders.
        bladders = genedesc1(me.bladders, cd.bladders, "B", "swim bladders", "b", "no swim bladder", "a swim bladder")
    if me.SS[3] == "S":  # Biolum and teeth.
        biolum = genedesc1(me.biolum, cd.biolum, "B", "biolum", "b", "no biolum", "partial biolum")
        # teeth
        # Replace or enhance this with caste-specific teeth and teeth mutation   But, for now ...
        teeth = ""
        if me.teeth != cd.teeth:
            if me.teeth[2] == "D" and cd.teeth[2] != "D":
                teeth = "doubled "
            if me.teeth[2] == "d" and cd.teeth[2] != "d":
                teeth = "undoubled "
            if cd.teeth[0:2] == me.teeth[0:2]:
                teeth = teeth + "teeth"
            if cd.teeth[0:2] != me.teeth[0:2]:
                teeth = teeth + genedesc1(me.teeth, cd.teeth, "T", "pure sea teeth", "t", "pure land teeth", "land/sea teeth")
    if me.SS[4] == "S":  # Eyelids and body fins
        eyelids = genedesc1(me.eyelids, cd.eyelids, "E", "nictating membranes", "e", "single eyelids", "transparent eye cover")
        bodyfins = genedesc1(me.dorsalfins, cd.dorsalfins, "F", "body fins", "f", "no body fins", "mini body fins")

    if me.SS[0] == "S":     # Skin
        descr = fbs.lyst(descr, earfins)
        descr = fbs.lyst(descr, webbing)
    if me.SS[1] == "S":     # Organ systems
        descr = fbs.lyst(descr, gills)
        descr = fbs.lyst(descr, breathes)
    if me.SS[2] == "S":     # ?
        descr = fbs.lyst(descr, bladders)
    if me.SS[3] == "S":     # ?
        descr = fbs.lyst(descr, biolum)
        descr = fbs.lyst(descr, teeth)
    if me.SS[4] == "S":     # ?
        descr = fbs.lyst(descr, eyelids)
        descr = fbs.lyst(descr, bodyfins)

    if descr.strip == "":
        descr = cd.dwell()

    return descr


def describedwell(sea):
    self = Aquatic("rr", sea)
    descr = "landdweller"
    if self.s0w == "N" and self.s1w == "N" and self.s2w == "N" and self.s3w == "N" and self.s4w == "N":
        descr = "landdweller"
    if self.s0w == "Y" or self.s1w == "Y" or self.s2w == "Y" or self.s3w == "Y" or self.s4w == "Y":
        descr = "beachdweller"
        if self.salt == "SBF":
            descr = "seadweller"
        if self.salt == "SBf":
            descr = "tidedweller"
        if self.salt == "Sbf":
            descr = "deepdweller"
        if self.salt == "sbF":
            descr = "riverdweller"
        if self.salt == "sBF":
            descr = "ponddweller"
        if self.salt == "sBf":
            descr = "deltadweller"
        if self.salt == "sbf":
            descr = "surfacedweller"
            # if surface dweller but no gills, landdweller.
            if self.gillface == "gg" and self.gillneck == "gg" and self.gillribs == "gg":
                descr = "landdweller"
    if self.SS == "SSSSS":
        descr = "seadweller"
    if self.SS == "sssss":
        descr = "landdweller"

    descr = descr.strip()
    if self.air == "aaaa" and self.SS != "ss":
        descr2 = "non-air " + descr
        descr = descr2
# For now; dweller doesn't need to mention asthma.
#    if self.air != "aaaa" and self.air != "AAAA" and self.SS != "ss" and self.SS != "SS":
#        if countaa(self.air) > 1:
#            descr2 = "breathshort " + descr
#            descr = descr2
    descr = descr.strip()
    return descr


# Gene-level combos and counters

def countaa(inhale):
    a = 0
    if inhale[0] == "a":
        a = a + 1
    if inhale[1] == "a":
        a = a + 1
    if inhale[2] == "a":
        a = a + 1
#    if inhale[3] == "a":
#        a = a + 1
    exhale = a
    return exhale


def genecombine(g1, g2):
    # Feed in the gene codes to be combined.
    x = 0
    g3 = [""]
    while x < len(g1) and x < len(g2):
        g3.append("")
        y = random.randint(1, 2)
        if y == 1:
            g3[x] = g1[x]
        if y == 2:
            g3[x] = g2[x]
        x = x + 1
    gf = ""
    x = 0
    while x < len(g1) and x < len(g2):
        gf = gf + g3[x]
        x = x + 1
    return gf


def genecombinenumbers(g1, g2):
    # Feed in the gene codes to be combined.
    g1 = str(g1)
    g2 = str(g2)
    x = 0
    g3 = [""]
    while x < len(g1) and x < len(g2):
        g3.append("")
        a = int(g1)
        b = int(g2)
        if g1 > g2:
            a = int(g2)
            b = int(g1)
        y = random.randint(a, b)
        g3[x] = str(y)
        x = x + 1
    gf = [""]
    x = 0
    while x < len(g1) and x < len(g2):
        gf.append("")
        gf[x] = g3[x]
        x = x + 1
    return gf


def genedesc1(my, cy, a, atxt, b, btxt, abtxt):
    # ab and ba have the same text string
    txt = ""
    if my != cy:
        if my == a + a:
            txt = atxt
        if my == b + b:
            txt = btxt
        if my == a + b or my == b + a:
            if cy != a + b and cy != b + a:
                txt = abtxt
            if cy == a + b or cy == b + a:
                txt = ""
    return txt


# Not actually used yet.
def genedesc2(my, cy, a, atxt, b, btxt, abtxt, batxt):
    # ab and ba have different text strings.
    txt = ""
    if my != cy:
        if my == a + a:
            txt = atxt
        if my == b + b:
            txt = btxt
        if my == a + b:
            txt = abtxt
        if my == b + a:
            txt = batxt
    return txt


def spectrumrand():
    spectrum = [
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
    ]
    return spectrum
