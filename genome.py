import slurry
import trolldeets as deets

# Phenotype Classes, containing genes


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
        "sea": slurry.sgeneland,
        # pawfeet, tail, wing, hairstreaks, grubscars, ?
        "powers": "powers",  # psychic, voodoo, eldritch, none.  specify type later.  Make psychics eyes glow colors?
        "hornL": "22RIn.point",  # see horn notes.
        "hornR": "22RIn.point",
        "height": 84,       # height in inches
        "strheightstr":  deets.heightstr(84),
        "build": "medium",  # more detailed data later
        "hair": "short",    # more detailed data later.  medium/long.
        "skin": "grey",     # freckles, stripes, birthmarks, vitiligo, melanism, albinism, etc.
        "donator1": "?.?",  # higher caste donator
        "donator2": "?.?",   # lower caste donator
    }
    return t0


# Need a horn genestrand class that contains 4-6 horn objects
# Need to add horn headcanons to genestrand: keratin, sensory horns,
# Doubled-horn gene primarily activates in trolls with rG, RG, or Rg blood.
# Possibly only when there are recessive seadweller genes and active psychic ones?

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

# Incomplete
class ToothObj:
    code = "02TCC"  # Summary of contents
    length = 0      # 0 - 9.  0 = gums, 4 = normal, 8 = 2x normal, 9 = giant.
    width = 2       # 0 (needles), 1, 2, 3 (wide)
    sym = True      # T/F symmetry overrides
    type = "CC"     # Cc choppy, Gg grinding, Pp pointy, serrated (?) other (?)

    def __init__(self, code):
        self.code = code
        self.length = code[0]
        self.width = code[1]
        if code[2] == "T":
            self.sym = True
        if code[2] == "F":
            self.sym = False
        self.type = code[3:5]


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
        self.length = code[0]
        self.curl = code[1]
        self.radial = code[2]
        self.dir = code[3]
        self.wide = code[4]
        self.tipA = code[6:len(code)]  # everything else in string = the tip type.

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


# Incomplete
class Mouth:
    # general mouth traits
    lipl = 6      # minimum tooth height to poke out over the lip
    lipw = "D"    # furthest-out visible tooth; mouth width
    double = "F"  # if teeth are doubled, second row identical to first.
    # Upper Jaw
    GL = ToothObj("42TGp")  # grindy
    FL = ToothObj("42TGp")  # grindy
    EL = ToothObj("42TGp")  # grindy
    DL = ToothObj("42TPc")  # incisor 2
    CL = ToothObj("52TPP")  # incisor zone
    BL = ToothObj("42TCp")  # one out ..
    AL = ToothObj("42TCp")  # center left top
    AR = ToothObj("42TCp")  # center right top
    BR = ToothObj("42TCp")  # one out ..
    CR = ToothObj("52TPP")  # incisor zone
    DR = ToothObj("42TPc")  # incisor 2
    ER = ToothObj("42TGp")  # grindy
    FR = ToothObj("42TGp")  # grindy
    GR = ToothObj("42TGp")  # grindy
    # Lower Jaw
    gl = ToothObj("42TGp")  # grindy
    fl = ToothObj("42TGp")  # grindy
    el = ToothObj("42TGp")  # grindy
    dl = ToothObj("52TPc")  # incisor 2
    cl = ToothObj("42TPP")  # incisor zone
    bl = ToothObj("42TCp")  # one out ..
    al = ToothObj("42TCp")  # center left bottom
    ar = ToothObj("42TCp")  # center right bottom
    br = ToothObj("42TCp")  # one out ..
    cr = ToothObj("42TPP")  # incisor zone
    dr = ToothObj("52TPc")  # incisor 2
    er = ToothObj("42TGp")  # grindy
    fr = ToothObj("42TGp")  # grindy
    gr = ToothObj("42TGp")  # grindy
    # If AR.sym = T and AL.sym = T: Use the average of AR and AL, for the expression of both
    # If AR.sym = T and AL.sym = F: AL=AR, AR=AR
    # If AR.sym = F and AL.sym = T: AL=AL, AR=AL
    # If AR.sym = F and AL.sym = F: AL=AL, AR=AR
    # Need description summary function.


class Aquatic:
    # This contains genes relating to aquatic and amphibious traits
    # These will be stored in trolls as just the code part.  Use this class when manipulating.
    # create gene object by going temp1 = SeaGenes("Ssx"),temp1 = SeaGenes(troll["sea"])
    blood = "rr"
    code = "ssbbccEEwwwwffbbsbfggiggiggittdeeAAAAsss"  # The code used to store data longterm.
    SS = "ss"          # SS = seadweller, Ss/sS = depends on genes, ss = land-dweller.
    SS2 = "sssss"      # extended.  [0:2] and [37:40]
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
        self.code = code
        self.SS = code[0:2]  # First two letters are whether seadweller genes are active or not.
        self.bladders = code[2:4]
        self.cheekfins = code[4:6]
        self.ears = code[6:8]
        self.wfingers = code[8:10]
        self.wtoes = code[10:12]
        self.dorsalfins = code[12:14]
        self.biolum = code[14:16]
        self.salt = code[16:19]
        self.gillneck = code[19:21]
        self.gillneckt = code[21:22]
        self.gillribs = code[22:24]
        self.gillribst = code[24:25]
        self.gillface = code[25:27]
        self.gillfacet = code[27:28]
        self.teeth = code[28:31]
        self.eyelids = code[31:33]
        self.air = code[33:37]
        temp = code[0:2] + code[37:40]
        self.SS2 = temp
        self.updatess()
#        self.tipA = code[6:len(code)]  # Not sure if I'll need this format or not.

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
        if self.SS2 != "SSSSS" and self.SS2 != "sssss":
            if self.SS2[0] == "S":
                if self.ears[0] == "E" or self.ears[1] == "E":
                    self.s0w = "Y"
                if self.cheekfins[0] == "F" or self.ears[1] == "F":
                    self.s0w = "Y"
                if self.wfingers[0] == "W" or self.wfingers[1] == "W":
                    self.s0w = "Y"
                if self.wtoes[0] == "W" or self.wtoes[1] == "W":
                    self.s0w = "Y"
                self.s0w = "Y"
            if self.SS2[0] == "s":
                self.s0w = "N"
            if self.SS2[1] == "S":
                if self.gillneck[0] == "G" or self.gillneck[1] == "G":
                    self.s1w = "Y"
                if self.gillfacet[0] != slurry.sgeneland[21]:
                    self.s1w = "Y"
                if self.gillribs[0] == "G" or self.gillribs[1] == "G":
                    self.s1w = "Y"
                if self.gillribst[0] != slurry.sgeneland[24]:
                    self.s1w = "Y"
                if self.gillface[0] == "G" or self.gillface[1] == "G":
                    self.s1w = "Y"
                if self.gillfacet[0] != slurry.sgeneland[27]:
                    self.s1w = "Y"
                if self.salt[0] == "S" or self.salt[1] == "B" or self.salt[2] == "F":
                    self.s1w = "Y"
                if deets.countaa(self.air) > 1:
                    self.s1w = "Y"
                self.s1w = "Y"
            if self.SS2[1] == "s":
                self.s1w = "N"
            if self.SS2[2] == "S":
                if self.bladders[0] == "B" or self.bladders[1] == "B":
                    self.s2w = "Y"
                self.s2w = "Y"
            if self.SS2[2] == "s":
                self.s2w = "N"
            if self.SS2[3] == "S":
                if self.biolum[0] == "B" or self.biolum[1] == "B":
                    self.s3w = "Y"
                if self.teeth[0] == "T" or self.teeth[1] == "T":
                    self.s3w = "Y"
                self.s3w = "Y"
            if self.SS2[3] == "s":
                self.s3w = "N"
            if self.SS2[4] == "S":
                if self.eyelids[0] == "E" or self.eyelids[1] == "E":
                    self.s4w = "Y"
                if self.dorsalfins[0] == "F" or self.dorsalfins[1] == "F":
                    self.s4w = "Y"
            if self.SS2[4] == "s":
                self.s4w = "N"

        return


# Need a phenotype class for misc. physical traits usually defined by universe norms
# Need a feral traits class
# Need a psychic / voodoo traits class
# Need a ...eldritch...?
#      ...mutations...?
# eye mutations:  octopus pupils, vision 8fold, 1 eye,
