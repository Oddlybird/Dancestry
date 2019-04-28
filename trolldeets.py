import random
import re
import names


class Horn:  # trolldeets
    # Horns are stored in trolls as just the code part.  Use this class when manipulating.
    # create a horn by going horn-variable = Horn("21RIn.f point"), or horn-variable = Horn(troll.hornL)
    code = "21RIn.f point"
    length = 2  # 1 = 0-1 handspans, 2 = 1-2 handspans, 3 = 2-3 handspans, 4 = 3+ handspans.
    curl = 1
    # 1 = straight, 2 = up to 45 degrees, 3 = 90 degrees +/- 45, 4 = 180 +/- 45,
    # 5 = 270 +/- 45, 6 = 360 +/-45, 7 = ampora wave-like curves
    radial = "R"  # cross-section shape.  R = round, O = Oval, T = triangular, S = spiraling like a goat.
    dir = "I"
    # primary growth direction.  F = frontwards, B = backwards, O = outwards (usually up), I = inwards (usually up).
    wide = "n"  # n = normal width like terezi.  w = wide base, like nepeta.
    tipAdir = "f"
    # direction the tip is pointed.  f = front/straight, sollux equius vriska's pincher.  s = sideways.
    # b = backwards, like the point on vriska's other horn that becomes a hook
    tipA = "point"  # verbal description of the shape of the point.  Point, Cone, Spade, Pincher, Jagged, Round.

    def __init__(self, code):
        self.code = code
        self.length = code[0]
        self.curl = code[1]
        self.radial = code[2]
        self.dir = code[3]
        self.wide = code[4]
        self.tipAdir = code[6]
        self.tipA = code[7:len(code)]  # everything else in string = the tip type.

    def desc(self):
        # convert the current features of the horn into a verbal description as in basic version.
        # use by going description-string = horn-temp.desc()
        descr = ""
        # Length, default 2
        if self.length == "1":
            descr = "short, "
        if self.length == "3":
            descr = "long, "
        if self.length == "4":
            descr = "very long, "
        # Width, default n
        if self.wide == "w":
            descr = descr + "wide, "
        # Direction, default Inwards
        if self.dir == "F":
            descr = descr + "forward"
        if self.dir == "B":
            descr = descr + "backswept "
        if self.dir == "O":
            descr = descr + "outward "
        # curves, default = 2 (slightly curved)
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
        # Tips, default forward
        #  if self.tipAdir == "s":
        #   descr = descr + "sideways" + self.tipA + "-tipped "
        #  if self.tipAdir == "b":
        #   descr = descr + "back" + self.tipA + "-tipped "
        #  if self.tipAdir == "f":
        descr = descr + self.tipA + "-tipped "
        # radial, default round
        if self.radial == "O":
            descr = descr + "oval horn"
        if self.radial == "T":
            descr = descr + "triangular horn"
        if self.radial == "S":
            descr = descr + "spiralling horn"
        if self.radial == "R":
            descr = descr + "horn"
            # strip spaces
            descr = re.sub(' +', ' ', descr)
            descr = descr.strip()
        return descr


# class Troll: #trolldeets.  just so I can pass them around easier...   Maybe?
def createtroll():  # trolldeets
    t0 = {
        "firname": "FIRNAM",  # six letters
        "surname": "SURNAM",  # six letters
        "sex": "N",  # M/N/F
        "blood": "Rg",  # RGB rgb
        "caste": "unclassified",
        "sea": "Landdweller",
        # Landdweller, Seadweller, Beachdweller. replace with more detailed phenotype info :
        # gilltype, headgills, ribgills, earfins, webbed, glow, pawfeet, tail, wing, hairstreaks, grubscars,
        "powers": "none",  # psychic, voodoo, eldritch, none.  specify type later.  Make psychics eyes glow colors?
        "hornL": "22RIn.f point",  # see horn notes.
        "hornR": "22RIn.f point",
        "height": "tall",  # replace with exact height in inches later.
        "build": "medium",  # more detailed data later
        "hair": "short",  # more detailed data later.  medium/long.
        "skin": "grey"  # freckles, stripes, birthmarks, vitiligo, melanism, albinism, etc.
    }
    return t0


def createtroll3(troll1, troll2):  # trolldeets
    # All data is partially formatted into a troll-like state.

    # error-checking code to give a default set of trolls if needed : Currently nonfunctional.
    # if p1["firname"] + P1["surname"] == "FIRNAMSURNAM":
    # global libbie
    # p1 = libbie
    # if p2["firname"] + P2["surname"] == "FIRNAMSURNAM":
    # global lester
    # p1 = lester

    # decide who is p1 based on hemism.
    caste1 = troll1["blood"]
    caste2 = troll2["blood"]
    p1 = caste1
    p2 = caste2
    if caste2 == highercaste(caste1, caste2):
        p2 = troll1
        p1 = troll2

    # Record Donators
    strdonator1 = p1["firname"][0] + "." + p1["surname"]
    strdonator2 = p2["firname"][0] + "." + p2["surname"]

    # Blood :
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
    hornl = hornblender(p1["hornL"], p2["hornL"], p1["hornR"], p2["hornR"])
    hornr = hornblender(p1["hornR"], p2["hornR"], p1["hornL"], p2["hornL"])

#    "donator1": strdonator1,
#    "donator2": strdonator2,

    firstname = names.newname()
    lastname = names.newname()
    t1 = {
        "firname": firstname,
        "surname": lastname,
        "sex": "N",  # M/N/F
        "blood": strblood,
        "caste": strcaste,
        "sea": "Landdweller",
        "powers": "none",  # psychic, voodoo, eldritch, none.  specify type later.  Make psychics eyes glow colors?
        "hornL": hornl,  # see horn notes.
        "hornR": hornr,
        "height": "tall",  # replace with exact height in inches later.
        "build": "medium",  # more detailed data later
        "hair": "short",  # more detailed data later.  medium/long.
        "skin": "grey"  # freckles, stripes, birthmarks, vitiligo, melanism, albinism, etc.
    }
    return t1


def hornblender(horn1, horn2, horn3, horn4):
    outhorn = ""
    a = 0

    while a <= 8:
        # 6 is a dot, but you need the dot, so ...
        if a < 8:
            b = random.randint(1, 6)
            if b == 1 or b == 2:
                outhorn = outhorn + horn1[a]
            if b == 3 or b == 4:
                outhorn = outhorn + horn2[a]
            if b == 5:
                outhorn = outhorn + horn3[a]
            if b == 6:
                outhorn = outhorn + horn4[a]

        if a == 8:
            # on the last loop, you need to append the point-type word.  So...
            b = random.randint(1, 6)
            if b == 1 or b == 2:
                outhorn = outhorn + horn1[a:len(horn1)]
            if b == 3 or b == 4:
                outhorn = outhorn + horn2[a:len(horn1)]
            if b == 5:
                outhorn = outhorn + horn3[a:len(horn1)]
            if b == 6:
                outhorn = outhorn + horn4[a:len(horn1)]
        # increment loop
        a = a + 1

    return outhorn


def getcaste(b):  # trolldeets
    caste = "?"
    # Dense What If Forest : Divine place on hemospectrum,
    # use this only for initial placement.  Adjust by third letter later.
    if b[0] == "R":
        if b[1] == "R":
            caste = "Maroon"  # RR Maroon
        if b[1] == "G":
            caste = "Gold"  # RG Gold
        if b[1] == "B":
            caste = "Violet"  # RB Violet
        if b[1] == "r":
            caste = "Maroon"  # Rr Maroon
        if b[1] == "g":
            caste = "Bronze"  # Rg Bronze
        if b[1] == "b":
            caste = "Tyrian"  # Rb Tyrian
    if b[0] == "G":
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
        if b[1] == "B":
            caste = "Blue"  # BB Bloo
        if b[1] == "r":
            caste = "Indigo"  # Br Indigo
        if b[1] == "g":
            caste = "Cerulean"  # Gb Ceru
        if b[1] == "b":
            caste = "Blue"  # Bb Bloo
    if b[0] == "r":
        if b[1] == "r":
            caste = "Maroon"  # rr maroon
        if b[1] == "g":
            caste = "Bronze"  # rg Bronze
        if b[1] == "b":
            caste = "Mutant"  # rb vantas
    if b[0] == "g":
        if b[1] == "g":
            caste = "Olive"  # gg Olive
        if b[1] == "b":
            caste = "Jade"  # gb Jade
    if b[0] == "b":
        if b[1] == "b":
            caste = "Blue"  # bb Bloo
    return caste


def getcastenum(b):  # trolldeets
    b = b + "..."
    caste = 0
    if b[0] == "R":
        if b[1] == "R":  # RR Maroon
            if b[2] == "R":
                caste = 2  # RRR
            if b[2] == "G":
                caste = 12  # RRG
            if b[2] == "B":
                caste = 72  # RRB
            if b[2] == "r":
                caste = 5  # RRr
            if b[2] == "g":
                caste = 10  # RRg
            if b[2] == "b":
                caste = 74  # RRb
        if b[1] == "G":  # RG Gold
            if b[2] == "G":
                caste = 23  # RGG
            if b[2] == "B":
                caste = 20  # RGB
            if b[2] == "r":
                caste = 16  # RGr
            if b[2] == "g":
                caste = 22  # RGg
            if b[2] == "b":
                caste = 21  # RGb
        if b[1] == "B":  # RB Violet
            if b[2] == "B":
                caste = 64  # RBB
            if b[2] == "r":
                caste = 70  # RBr
            if b[2] == "g":
                caste = 68  # RBg
            if b[2] == "b":
                caste = 67  # RBb
        if b[1] == "r":  # Rr Maroon
            if b[2] == "r":
                caste = 6  # Rrr
            if b[2] == "g":
                caste = 11  # Rrg
            if b[2] == "b":
                caste = 75  # Rrb
        if b[1] == "g":  # Rg Bronze
            if b[2] == "g":
                caste = 15  # Rgg
            if b[2] == "b":
                caste = 21  # Rgb
        if b[1] == "b":  # Rb Tyrian
            if b[2] == "b":
                caste = 71  # Rbb
    if b[0] == "G":
        if b[1] == "G":  # GG Olive
            if b[2] == "G":
                caste = 33  # GGG
            if b[2] == "B":
                caste = 39  # GGB
            if b[2] == "r":
                caste = 28  # GGr
            if b[2] == "g":
                caste = 31  # GGg
            if b[2] == "b":
                caste = 37  # GGb
        if b[1] == "B":  # GB Teal
            if b[2] == "B":
                caste = 48  # GBB
            if b[2] == "r":
                caste = 45  # GBr
            if b[2] == "g":
                caste = 44  # GBg
            if b[2] == "b":
                caste = 47  # GBb
        if b[1] == "r":  # Gr Lime
            if b[2] == "r":
                caste = 24  # Grr
            if b[2] == "g":
                caste = 26  # Grg
            if b[2] == "b":
                caste = 27  # Grb
        if b[1] == "g":  # Gg Olive
            if b[2] == "g":
                caste = 33  # Ggg
            if b[2] == "b":
                caste = 38  # Ggb
        if b[1] == "b":  # Gb Jade
            if b[2] == "b":
                caste = 41  # Gbb
    if b[0] == "B":
        if b[1] == "B":  # BB Bloo
            if b[2] == "B":
                caste = 57  # BBB
            if b[2] == "r":
                caste = 60  # BBr
            if b[2] == "g":
                caste = 52  # BBg
            if b[2] == "b":
                caste = 55  # BBb
        if b[1] == "r":  # Br Indigo
            if b[2] == "r":
                caste = 63  # Brr
            if b[2] == "g":
                caste = 62  # Brg
            if b[2] == "b":
                caste = 61  # Brb
        if b[1] == "g":  # Gb Ceru
            if b[2] == "g":
                caste = 49  # Bgg
            if b[2] == "b":
                caste = 50  # Bgb
        if b[1] == "b":  # Bb Bloo
            if b[2] == "b":
                caste = 56  # Bbb
    if b[0] == "r":
        if b[1] == "r":  # rr maroon
            if b[2] == "r":
                caste = 7  # rrr
            if b[2] == "g":
                caste = 9  # rrg
            if b[2] == "b":
                caste = 1  # rrb
        if b[1] == "g":  # rg Bronze/gold?
            if b[2] == "g":
                caste = 18  # rgg
            if b[2] == "b":
                caste = 13  # rgb
        if b[1] == "b":  # rb vantas
            if b[2] == "b":
                caste = 71  # rbb
    if b[0] == "g":
        if b[1] == "g":  # gg Olive
            if b[2] == "g":
                caste = 34  # ggg
            if b[2] == "b":
                caste = 36  # ggb
        if b[1] == "b":  # gb Jade
            if b[2] == "b":
                caste = 42  # gbb
    if b[0] == "b":
        if b[1] == "b":  # bb Bloo
            if b[2] == "b":
                caste = 58  # bbb
    return caste


def highercaste(blood1, blood2):  # trolldeets
    # input two bloods, return the higher caste.
    caste1 = getcastenum(blood1)
    caste2 = getcastenum(blood2)
    bloodhigher = blood1  # By default assume the first is higher.
    if caste2 > caste1:  # ..but if it's not, fix that.
        bloodhigher = blood2
    return bloodhigher


def bloodsort(blood):  # trolldeets.  Put in a group of letters.
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
