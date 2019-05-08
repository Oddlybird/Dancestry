import slurry
import trolldeets as deets

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
def trollobj():  # trolldeets
    t0 = {
        "savetype": "8",  # Save Version
        "firname": "FIRNAM",  # six letters
        "surname": "SURNAM",  # six letters
        "sex": "N",  # M/N/F
        "blood": "Rg",  # RGB rgb
        "caste": "caste",
        "dwell": "dwell",
        "seadesc": "seadesc",
        "hornLdesc": "hornL",
        "hornRdesc": "hornR",
        "mouth": slurry.genemouthlow,
        "sea": slurry.genesealand,
        # pawfeet, tail, wing, hairstreaks, grubscars, ?
        "powers": "powers",  # psychic, voodoo, eldritch, none.  specify type later.  Make psychics eyes glow colors?
        "hornL": "22RIn.point",  # see horn notes.
        "hornR": "22RIn.point",
        "height": 84,       # height in inches
        "heightstr":  deets.heightstr(84),
        "build": "medium",  # more detailed data later
        "hair": "short",    # more detailed data later.  medium/long.
        "skin": "grey",     # freckles, stripes, birthmarks, vitiligo, melanism, albinism, etc.
        "donator1": "?.?",  # higher caste donator
        "donator2": "?.?",   # lower caste donator
    }
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
    code = "21RIn.point"
    length = 2  # 1 = 0-1 handspans, 2 = 1-2 handspans, 3 = 2-3 handspans, 4 = 3+ handspans.
    curl = 1
    # 1 = straight, 2 = up to 45 degrees, 3 = 90 degrees +/- 45, 4 = 180 +/- 45,
    # 5 = 270 +/- 45, 6 = 360 +/-45, 7 = ampora wave-like curves
    radial = "R"  # cross-section shape.  R = round, O = Oval, T = triangular, S = spiraling like a goat.
    dir = "I"
    # primary growth direction.  F = frontwards, B = backwards, O = outwards (usually up), I = inwards (usually up).
    wide = "n"  # n = normal width like terezi.  w = wide base, like nepeta.
    tipA = "point"  # shape of the point.  Point, Cone, Spade, Pincher, Jagged, Round, hook, ...
    # Add :  HornObj bumps, doubled horns, notched and rounded-notched horns
    # bolt-tipped
    # branched / antler horns, sheet-like moose horns

    def __init__(self, code):
        self.code = code
        c = 0
        self.length = code[c]
        c = c + 1
        self.curl = code[c]
        c = c + 1
        self.radial = code[c]
        c = c + 1
        self.dir = code[c]
        c = c + 1
        self.wide = code[c]
        c = c + 2
        self.tipA = code[c:len(code)]  # everything else in string = the tip type.

    def desc(self):
        # convert the current features of the horn into a verbal description as in basic version.
        # use by going description-string = horn-temp.desc()
        descr = deets.describehorn(self.code)
        return descr


# Incomplete
class Eyes:
    Eye1 = EyeObj  # left main, active
    Eye2 = EyeObj  # right main, active
    Eye3 = EyeObj  # inactive, left
    Eye4 = EyeObj  # inactive, right
    Eye5 = EyeObj  # inactive, center
    # need a deets function for blending and producing these
    # deets function: describe eyes

    def __init__(self, code):
        self.code = code
        # When activating Eye genes, include code parsing data here
# eye mutations:  octopus pupils, vision 8fold, 1 eye,


# Incomplete
class Mouth:
    # general mouth traits
    code = "6DddTTTTTT445444CCPPGG222222TTTTTT445444CCPPGG222222TTTTTT444544CCPPGG222222TTTTTT444544CCPPGG222222"
    lipl = 6       # minimum tooth height to poke out over the lip
    lipw = 4       # furthest-out visible tooth; mouth width
    double = "dd"  # if teeth are doubled, second row identical to first.
#    length        # 0 - 9.  0 = gums, 4 = normal, 8 = 2x normal, 9 = giant.
#    width         # 0 (needles), 1, 2, 3 (wide)
#    sym           # T/F symmetry overrides
#    type          # Cc choppy/flat, Gg grinding, Pp pointy, serrated (?) other (?)
    symtopl = "TTTTTT"         # [0] = center, [6] = molar
    lengthtopl = "445444"      # [0] = center, [6] = molar
    typetopl = "CCPPGG"  # [0] = center, [6] = molar
    widthtopl = "222222"       # [0] = center, [6] = molar
    symtopr = "TTTTTT"         # [0] = center, [6] = molar
    lengthtopr = "445444"      # [0] = center, [6] = molar
    typetopr = "CCPPGG"  # [0] = center, [6] = molar
    widthtopr = "222222"       # [0] = center, [6] = molar
    symbotl = "TTTTTT"         # [0] = center, [6] = molar
    lengthbotl = "444544"      # [0] = center, [6] = molar
    typebotl = "CCPPGG"  # [0] = center, [6] = molar
    widthbotl = "222222"       # [0] = center, [6] = molar
    symbotr = "TTTTTT"         # [0] = center, [6] = molar
    lengthbotr = "444544"      # [0] = center, [6] = molar
    typebotr = "CCPPGG"  # [0] = center, [6] = molar
    widthbotr = "222222"       # [0] = center, [6] = molar
    # TT -> average them
    # TF -> T overwrites F
    # FF -> the two teeth are distinct

    def __init__(self, code):
        self.code = code
        c = 0
        self.lipl = code[c]
        c = c + 1
        self.lipw = code[c]
        c = c + 1
        self.double = code[c:c+1]
        c = c + 2
        self.symtopl = code[c:c+6]
        c = c + 6
        self.lengthtopl = code[c:c+6]
        c = c + 6
        self.typetopl = code[c:c+6]
        c = c + 6
        self.widthtopl = code[c:c+6]
        c = c + 6
        self.symtopr = code[c:c+6]
        c = c + 6
        self.lengthtopr = code[c:c+6]
        c = c + 6
        self.typetopr = code[c:c+6]
        c = c + 6
        self.widthtopr = code[c:c+6]
        c = c + 6
        self.symbotl = code[c:c+6]
        c = c + 6
        self.lengthbotl = code[c:c+6]
        c = c + 6
        self.typebotl = code[c:c+6]
        c = c + 6
        self.widthbotl = code[c:c+6]
        c = c + 6
        self.symbotr = code[c:c+6]
        c = c + 6
        self.lengthbotr = code[c:c+6]
        c = c + 6
        self.typebotr = code[c:c+6]
        c = c + 6
        self.widthbotr = code[c:c+6]

    def update(self):
        self.code = self.lipl + self.lipw + self.double
        self.code = self.code + self.symtopl + self.lengthtopl + self.typetopl + self.widthtopl
        self.code = self.code + self.symtopr + self.lengthtopr + self.typetopr + self.widthtopr
        self.code = self.code + self.symbotl + self.lengthbotl + self.typebotl + self.widthbotl
        self.code = self.code + self.symbotr + self.lengthbotr + self.typebotr + self.widthbotr


class Aquatic:
    # This contains genes relating to aquatic and amphibious traits
    # These will be stored in trolls as just the code part.  Use this class when manipulating.
    # create gene object by going temp1 = SeaGenes("Ssx"),temp1 = SeaGenes(troll["sea"])
    blood = "rr"
    code = "ssssbbccEEwwwwffbbsbfggiggiggittdeeAAAA"  # The code used to store data longterm.
    SS = "sssss"          # SS = seadweller, Ss/sS = depends on genes, ss = land-dweller.
    s0w = "N"  # are any of the genes tied to SS2[0] active?
    s1w = "N"
    s2w = "N"
    s3w = "N"
    s4w = "N"
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
        descr = deets.describedwell(self.code)
        return descr

    def desc(self):
        # verbal description of aquatic traits
        # Include specifics of all genes that differ from slurry defaults for landdweller / seadweller
        descr = deets.describesea(self.blood, self.code)
        return descr

    def updatess(self):
        # check if any of the relevant genes are active for each
        ld = Aquatic("rr", slurry.genesealand)
        sd = Aquatic("rr", slurry.genesealand)
        if self.SS != "SSSSS" and self.SS != "sssss":
            if self.SS[0] == "S":
                if self.ears[0] == "E" or self.ears[1] == "E":
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
                if deets.countaa(self.air) > 1:
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
    widthtopl = code[c:c+6]
    c = c + 6
    typetopl = code[c:c+6]
    c = c + 6
    symtopr = code[c:c+6]
    c = c + 6
    lengthtopr = code[c:c+6]
    c = c + 6
    widthtopr = code[c:c+6]
    c = c + 6
    typetopr = code[c:c+6]
    c = c + 6
    symbotl = code[c:c+6]
    c = c + 6
    lengthbotl = code[c:c+6]
    c = c + 6
    widthbotl = code[c:c+6]
    c = c + 6
    typebotl = code[c:c+6]
    c = c + 6
    symbotr = code[c:c+6]
    c = c + 6
    lengthbotr = code[c:c+6]
    c = c + 6
    widthbotr = code[c:c+6]
    c = c + 6
    typebotr = code[c:c+6]

    thing = {"lipl": lipl, "lipw": lipw, "double": double,
             "symtopl": symtopl, "lengthtopl": lengthtopl, "widthtopl": widthtopl, "typetopl": typetopl,
             "symtopr": symtopr, "lengthtopr": lengthtopr, "widthtopr": widthtopr, "typetopr": typetopr,
             "symbotl": symbotl, "lengthbotl": lengthbotl, "widthbotl": widthbotl, "typebotl": typebotl,
             "symbotr": symbotr, "lengthbotr": lengthbotr, "widthbotr": widthbotr, "typebotr": typebotr,
             }
    return thing


#def codetooth(code):
#    c = 0
#    length = code[c]
#    c = c + 1
#    width = code[c]
#    c = c + 1
#    sym = code[c]
#    c = c + 1
#    type = code[c:c+1]
#
#    thing = {"length": length, "width": width, "sym": sym, "type": type}
#    return thing

