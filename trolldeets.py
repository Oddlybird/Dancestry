import random
import re
import names
import colorsys
import colorgarbage as colg
import slurry


# This file contains basic formatting information,
# Functions that are used to combine info from a slurry,
# Functions that manipulate / interact with troll data


class Horn:  # trolldeets
    # Horns are stored in trolls as just the code part.  Use this class when manipulating.
    # create a horn by going horn-variable = Horn("21RIn.f point"), or horn-variable = Horn(troll.hornL)
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
        descr = ""
        # Length, default 2
        if self.length == "1":
            descr = "short, "
        if self.length == "4":
            descr = "long, "
        # Width, default n
        if self.wide == "w":
            descr = descr + "wide, "
        # Direction, default Inwards
        if self.dir == "F":
            descr = descr + "front "
        if self.dir == "B":
            descr = descr + "backswept "
        if self.dir == "O":
            descr = descr + "side "
        # curves, default = 2 (slightly curved)
        if self.curl == "1":
            descr = descr + "straight "
        if self.curl == "3":
            descr = descr + "curved "
        if self.curl == "4":
            descr = descr + "curled "
        if self.curl == "5":
            descr = descr + "curly "
        if self.curl == "6":
            descr = descr + "coiled "
        if self.curl == "7":
            descr = descr + "wave-like "
        # tip shape
        descr = descr + self.tipA + "-tip "
        # radial, default round
        if self.radial == "O":
            descr = descr + "oval horn"
        if self.radial == "T":
            descr = descr + "edged horn"
        if self.radial == "S":
            descr = descr + "twisting horn"
        if self.radial == "R":
            descr = descr + "round horn"
            # strip spaces
            descr = re.sub(' +', ' ', descr)
            descr = descr.strip()
        return descr


# class Troll: #trolldeets.  just so I can pass them around easier...   Maybe?
def trollobj():  # trolldeets
    t0 = {
        "savetype": "6",  # Save Version
        "firname": "FIRNAM",  # six letters
        "surname": "SURNAM",  # six letters
        "sex": "N",  # M/N/F
        "blood": "Rg",  # RGB rgb
        "caste": "?",
        "sea": "Landdweller",
        # Landdweller, Seadweller, Beachdweller. replace with more detailed phenotype info :
        # gilltype, headgills, ribgills, earfins, webbed, glow, pawfeet, tail, wing, hairstreaks, grubscars,
        "powers": "none",  # psychic, voodoo, eldritch, none.  specify type later.  Make psychics eyes glow colors?
        "hornL": "22RIn.point",  # see horn notes.
        "hornR": "22RIn.point",
        "height": "tall",  # replace with exact height in inches later.
        "build": "medium",  # more detailed data later
        "hair": "short",  # more detailed data later.  medium/long.
        "skin": "grey",   # freckles, stripes, birthmarks, vitiligo, melanism, albinism, etc.
        "donator1": "?.?",  # higher caste donator
        "donator2": "?.?"   # lower caste donator
    }
    return t0


def slurrytroll(blood=""):
    # Record Donators
    strdonator1 = "?.?"
    strdonator2 = "?.?"

    # Blood + Caste:
    strblood = blood
    if len(blood) < 2:
        strblood = slurry.premadeblood()
    strcaste = getcaste(strblood)

    # str-sea = Phenotype shit comes later.
    # traits come later.
    # Powers
    # Height
    # Build
    # hair
    # skin

    # sex
    strsex = getsex(strblood)

    # Make horns.  The hornblender is biased, and 2/3 of results will be from the first two horns input.
    hornl = slurry.premadehorn()
    hornr = slurry.premadehorn()
    (hornl, hornr) = hornaverager(hornl, hornr)

    # names
    firstname = names.newname()
    lastname = names.newname()

    t1 = trollobj()
    t1["firname"] = firstname
    t1["surname"] = lastname
    t1["sex"] = strsex
    t1["blood"] = strblood
    t1["caste"] = strcaste
    #    t1["sea"] = ,
    #    t1["powers"] = ,
    t1["hornL"] = hornl
    t1["hornR"] = hornr
    #    t1["height"] = ,
    #    t1["build"] = ,
    #    t1["hair"] = ,
    #    t1["skin"] = ,
    t1["donator1"] = strdonator1
    t1["donator2"] = strdonator2

    return t1


def blendtroll(trolla, trollb):  # trolldeets
    # Start by making sure the donators are ready to read.
    global trollblank
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
    strcaste = getcaste(strblood)

    # str-sea = Phenotype shit comes later.
    # traits come later.
    # Powers
    # Height
    # Build
    # hair
    # skin

    # sex
    strsex = getsex(strblood)

    # Make horns.  The hornblender is biased, and 2/3 of results will be from the first two horns input.
    hornl = hornblender(p1["hornL"], p2["hornL"], p1["hornR"], p2["hornR"])
    hornr = hornblender(p1["hornR"], p2["hornR"], p1["hornL"], p2["hornL"])

    (hornl, hornr) = hornaverager(hornl, hornr)

    # names
    firstname = names.newname()
    lastname = names.newname()

    t1 = trollobj()
    t1["firname"] = firstname
    t1["surname"] = lastname
    t1["sex"] = strsex
    t1["blood"] = strblood
    t1["caste"] = strcaste
#    t1["sea"] = ,
#    t1["powers"] = ,
    t1["hornL"] = hornl
    t1["hornR"] = hornr
#    t1["height"] = ,
#    t1["build"] = ,
#    t1["hair"] = ,
#    t1["skin"] = ,
    t1["donator1"] = strdonator1
    t1["donator2"] = strdonator2

    return t1


def hornblender(horn1, horn2, horn3, horn4):
    outhorn = ""
    a = 0
    # Pick one of the parents' horn genes at random for each horn.
    while a <= 6:
        # 6 is a dot, but you need the dot, so ...
        if a < 6:
            b = random.randint(1, 6)
            if b == 1 or b == 2:
                outhorn = outhorn + horn1[a]
            if b == 3 or b == 4:
                outhorn = outhorn + horn2[a]
            if b == 5:
                outhorn = outhorn + horn3[a]
            if b == 6:
                outhorn = outhorn + horn4[a]

        if a == 6:
            # on the last loop, you need to append the point-type word.  So...
            b = random.randint(1, 6)
            if b == 1 or b == 2:
                outhorn = outhorn + horn1[a:len(horn1)]
            if b == 3 or b == 4:
                outhorn = outhorn + horn2[a:len(horn2)]
            if b == 5:
                outhorn = outhorn + horn3[a:len(horn3)]
            if b == 6:
                outhorn = outhorn + horn4[a:len(horn4)]
        # increment loop
        a = a + 1

    a = 0
    outhorn2 = ""
    while a < 2:
        b = random.randint(1, 12)
        temp1 = int(outhorn[a])
        temp2 = int(outhorn[a])
        if b == 1 or b == 2:
            temp2 = int(horn1[a])
        if b == 3 or b == 4:
            temp2 = int(horn2[a])
        if b == 5:
            temp2 = int(horn3[a])
        if b == 6:
            temp2 = int(horn4[a])
        temp3 = (temp1 + temp2) // 2
        temp4 = str(temp3)
        outhorn2 = outhorn2 + temp4
        a = a + 1

    outhorn2 = outhorn2 + outhorn[2:len(outhorn)]

    return outhorn2


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


def getcaste(innie):
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


# Original
def getcaste_orig(b):  # trolldeets
    caste = "?"

    # Dense What If Forest : Divine place on hemospectrum,
    if b[0] == "R":
        caste = "Maroon"  # R
        if len(b) > 1:
            if b[1] == "R":
                caste = "Maroon"  # RR Maroon
                if len(b) > 2:
                    if b[2] == "G":
                        caste = "Gold"  # RRG
            if b[1] == "G":
                caste = "Gold"  # RG Gold
                if len(b) > 2:
                    if b[2] == "G":
                        caste = "Lime"  # RGG
                    if b[2] == "B":
                        caste = "xBronze"  # RGB
                    if b[2] == "b":
                        caste = "xGold"  # RGb
            if b[1] == "B":
                caste = "Violet"  # RB Violet
                if len(b) > 2:
                    if b[2] == "B":
                        caste = "Indigo"   # RBB
                    if b[2] == "g":
                        caste = "xViolet"  # RBg
                    if b[2] == "b":
                        caste = "Indigo"  # RBb
            if b[1] == "r":
                caste = "Maroon"  # Rr Maroon
                if len(b) > 2:
                    if b[2] == "g":
                        caste = "Bronze"  # Rrg
                    if b[2] == "b":
                        caste = "xTyrian"  # Rrb
            if b[1] == "g":
                caste = "Bronze"  # Rg Bronze
                if len(b) > 2:
                    if b[2] == "g":
                        caste = "Gold"  # Rgg
                    if b[2] == "b":
                        caste = "xBronze"  # Rgb
            if b[1] == "b":
                caste = "Tyrian"  # Rb Tyrian
                if len(b) > 2:
                    if b[2] == "b":
                        caste = "Violet"  # Rbb
    if b[0] == "G":
        caste = "Olive"  # G
        if len(b) > 1:
            if b[1] == "G":
                caste = "Olive"  # GG Olive
            if b[1] == "B":
                caste = "Teal"  # GB Teal
            if b[1] == "r":
                caste = "Lime"  # Gr Lime
            if b[1] == "g":
                caste = "Olive"  # Gg Olive
            if b[1] == "b":
                caste = "Jade"  # Gb Jade
    if b[0] == "B":
        caste = "Bloo"  # B
        if len(b) > 1:
            if b[1] == "B":
                caste = "Blue"  # BB Bloo
            if b[1] == "r":
                caste = "Indigo"  # Br Indigo
            if b[1] == "g":
                caste = "Cerulean"  # Gb Ceru
            if b[1] == "b":
                caste = "Blue"  # Bb Bloo
    if b[0] == "r":
        caste = "Maroon"  # r
        if len(b) > 1:
            if b[1] == "r":
                caste = "Maroon"  # rr maroon
            if b[1] == "g":
                caste = "Bronze"  # rg Bronze
            if b[1] == "b":
                caste = "Mutant"  # rb vantas
    if b[0] == "g":
        caste = "olive"  # g
        if len(b) > 1:
            if b[1] == "g":
                caste = "Olive"  # gg Olive
            if b[1] == "b":
                caste = "Jade"  # gb Jade
    if b[0] == "b":
        caste = "bloo"  # b
        if len(b) > 1:
            if b[1] == "b":
                caste = "Blue"  # bb Bloo
    return caste


def getcastenum(b):  # trolldeets
    (cr, cg, cb) = colg.bloodtorgb(b)
    (h, s, v) = colorsys.rgb_to_hsv(cr, cg, cb)
    hue = h * 360
    hue = round(hue)
    val = v / 100
    caste = round(hue + val, 2)
    return caste


def getcastenumstr(b):  # trolldeets
    (cr, cg, cb) = colg.bloodtorgb(b)
    (h, s, v) = colorsys.rgb_to_hsv(cr, cg, cb)
    hue = h * 360
    hue = round(hue)
    if hue >= 345:
        hue = hue - 360
    hue = hue + 15
    val = v / 100
    caste = round(hue + val, 1)
    caste = str(caste)
    caste = caste.zfill(5)
    return caste


def highercaste(blood1, blood2):  # trolldeets
    # input two bloods, return the higher caste.
    caste1 = getcastenum(blood1)
    caste2 = getcastenum(blood2)
    bloodhigher = blood1  # By default assume the first is higher.
    if caste2 > caste1:  # ..but if it's not, fix that.
        bloodhigher = blood2
    return bloodhigher


# chibs version
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


# original version
def bloodsort_orig(blood):  # trolldeets.  Put in a group of letters.
    a = 0  # count the number of letters stripped out
    sortedblood = ""  # sorted blood code
    for arb in blood:  # for each letter...
        if arb == "R":
            sortedblood = sortedblood + "R"
            a = a + 1
        if a == len(blood):
            break
    for arb in blood:  # for each letter...
        if arb == "G":
            sortedblood = sortedblood + "G"
            a = a + 1
        if a == len(blood):
            break
    for arb in blood:  # for each letter...
        if arb == "B":
            sortedblood = sortedblood + "B"
            a = a + 1
        if a == len(blood):
            break
    for arb in blood:  # for each letter...
        if arb == "r":
            sortedblood = sortedblood + "r"
            a = a + 1
        if a == len(blood):
            break
    for arb in blood:  # for each letter...
        if arb == "g":
            sortedblood = sortedblood + "g"
            a = a + 1
        if a == len(blood):
            break
    for arb in blood:  # for each letter...
        if arb == "b":
            sortedblood = sortedblood + "b"
            a = a + 1
        if a == len(blood):
            break
    return sortedblood



trollblank = trollobj()
