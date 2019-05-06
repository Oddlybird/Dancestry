import random
import re
import names
import colorsys
import colorgarbage as colg
import slurry
import formattingbs as fbs
import genome as gene

# This file contains basic formatting information,
# Functions that are used to combine info from a slurry,
# Functions that manipulate / interact with troll data


def slurrytroll(spectrum):
    # Record Donators
    strdonator1 = "?.?"
    strdonator2 = "?.?"

    # Blood + Caste:
    a = 0
    strblood = "rr"
    while a == 0:
        strblood = slurry.premadeblood()
        for arb in spectrum:
            if arb == strblood:
                a = a + 1

    strcaste = getcaste(strblood)

    # height
    a = random.randint(85, 115)
    a = a / 100
    a = a * slurry.heightspectrum[strblood[0:2]]
    a = round(a)
    strheight = a

    # The sea-activating gene CAN be anything.
    sgenetype = slurry.spectrumgenesea[strblood[0:2]]
    if slurry.dwellspectrum == "landdweller":
        sgenetype = slurry.sgeneland
    if slurry.dwellspectrum == "seadweller":
        sgenetype = slurry.sgenesea
    strsea1 = genecombine(slurry.sgenemutant, sgenetype) # Mutant + dweller type
    strsea2 = genecombine(strsea1, sgenetype)            # Dilute that with dweller type again.
    sgenetype = slurry.spectrumgenesea[strblood[0:2]]
    strsea3 = genecombine(strsea2, sgenetype)   # Caste-specific...
    strsea = genecombine(strsea3, sgenetype)   # Caste-specific...
    gene1 = gene.Aquatic(strblood, strsea)
    strseadesc = gene1.desc()

    # Phenotype shit comes later.
    # traits come later.
    # Powers
    # Build
    # hair
    # skin

    # sex
    strsex = getsex(strblood)

    # Make horns.  The hornblender is biased, and 2/3 of results will be from the first two horns input.
    hornl = slurry.premadehorn()
    hornr = slurry.premadehorn()
    (hornl, hornr) = hornaverager(hornl, hornr)
    hornl2 = gene.HornObj(hornl)
    strhornl = hornl2.desc()
    hornr2 = gene.HornObj(hornr)
    strhornr = hornr2.desc()

    # names
    firstname = names.newname()
    lastname = names.newname()

    t1 = gene.trollobj()
    t1["firname"] = firstname
    t1["surname"] = lastname
    t1["sex"] = strsex
    t1["blood"] = strblood
    t1["caste"] = strcaste
    t1["seadesc"] = strseadesc
    t1["hornLdesc"] = strhornl
    t1["hornRdesc"] = strhornr
    t1["sea"] = strsea
    #    t1["powers"] = ,
    t1["hornL"] = hornl
    t1["hornR"] = hornr
    t1["height"] = strheight
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
    x = random.randint(1, 2)
    if x == 1:
        strblood = strblood[0] + strblood[1]
    strcaste = getcaste(strblood)

    # Height
    x = random.randint(95, 105)
    x = x / 100

    ph1 = int(p1["height"]) / slurry.heightspectrum[p1["blood"][0:2]]
    ph2 = int(p2["height"]) / slurry.heightspectrum[p2["blood"][0:2]]
    ph3 = (ph1 + ph2) / 2
    y = ph3 * slurry.heightspectrum[strblood[0:2]] * x
    y = round(y)
    strheight = int(y)

    # str-sea = Phenotype shit comes later.
    strsea = genecombine(p1["sea"], p2["sea"])
    gene1 = gene.Aquatic(strblood, strsea)
    strseadesc = gene1.desc()

    # traits come later.
    # Powers
    # Build
    # hair
    # skin

    # sex
    strsex = getsex(strblood)

    # Make horns.  The hornblender is biased, and 2/3 of results will be from the first two horns input.
    hornl = hornblender(p1["hornL"], p2["hornL"], p1["hornR"], p2["hornR"])
    hornr = hornblender(p1["hornR"], p2["hornR"], p1["hornL"], p2["hornL"])
    (hornl, hornr) = hornaverager(hornl, hornr)
    hornl2 = gene.HornObj(hornl)
    strhornl = hornl2.desc()
    hornr2 = gene.HornObj(hornr)
    strhornr = hornr2.desc()

    # names
    firstname = names.newname()
    lastname = names.newname()

    t1 = gene.trollobj()
    t1["firname"] = firstname
    t1["surname"] = lastname
    t1["sex"] = strsex
    t1["caste"] = strcaste
    t1["seadesc"] = strseadesc
    t1["hornLdesc"] = strhornl
    t1["hornRdesc"] = strhornr
    t1["blood"] = strblood
    t1["sea"] = strsea
#    t1["powers"] = ,
    t1["hornL"] = hornl
    t1["hornR"] = hornr
    t1["height"] = strheight
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


def getcastenum(b):  # trolldeets
    (cr, cg, cb) = colg.bloodtorgb(b)
    (h, s, v) = colorsys.rgb_to_hsv(cr, cg, cb)
    hue = h * 360
    hue = round(hue)
    val = v / 100
    caste = round(hue + val, 2)
    return caste


def getcastenumstr(b):  # trolldeets
    caste = getcastenum(b)
    caste = round(caste)
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


def heightstr(h):
    h = int(h)
    feet = h // 12
    inches = h % 12
    hstr = str(feet) + "'" + str(inches) + '"'
    return hstr


def describehorn(inhorn="22RIn.point"):
    temp = gene.HornObj(inhorn)
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
    descr = descr + temp.tipA + "-tip "
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


def describesea(bloodcode, sea):    # slurry.spectrumgenesea, blood[0:2]
    # "SSbbCCeeWwWwffBBSBFGGiGGiggittdeeAAAASSS"
    blood = bloodcode[0:2]
    me = gene.Aquatic(blood, sea)                      # The troll being tested
    cd = gene.Aquatic(blood, slurry.socialspectrumgenesea[blood])   # Caste Default
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
        if me.SS2 == "SSSSS":
            dwellvar = slurry.dwellspectrum[blood]
            if dwellvar != "seadweller":
                dwellvar = me.dwell()
            descr = dwellvar
            return descr
        if me.SS2 == "sssss":
            dwellvar = slurry.dwellspectrum[blood]
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
        done = True
        break

    # Below this point, everyone has Ss or sS, at least one noteworthy difference from cd, and can breathe.
    # Things that add descriptions to the list, but do not end the loop
    if me.air != "AAAA" and me.air != "aaaa":
        if countaa(me.air) > 1:
            descr = descr + "rank " + str(countaa(me.air) - 1) + " airless"

    if me.SS2[0] == "S":  # Webbing, Earfins.
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
        #ears, cheekfins, and earfins
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
    if me.code[1] == "S":  # Gills and breathing
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
            if gills == "" and me.salt == "sbf" and slurry.dwellspectrum[blood] != "landdweller":
                breathes = "breathes " + canb
            if gills == "" and me.salt == "SBF" and slurry.dwellspectrum[blood] != "seadweller":
                breathes = "breathes " + canb
        if me.SS2[2] == "S":  # Swimbladders.
            bladders = genedesc1(me.bladders, cd.bladders, "B", "swim bladders", "b", "no swim bladder", "a swim bladder")
        if me.SS2[3] == "S":  # Biolum and teeth.
            biolum = genedesc1(me.biolum, cd.biolum, "B", "biolum", "b", "no biolum", "partial biolum")
            # teeth
            # Replace or enhance this with caste-specific teeth and teeth mutation gene.  But, for now ...
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
        if me.SS2[4] == "S":  # Eyelids and body fins
            eyelids = genedesc1(me.eyelids, cd.eyelids, "E", "nictating membranes", "e", "single eyelids", "transparent eye cover")
            bodyfins = genedesc1(me.dorsalfins, cd.dorsalfins, "F", "body fins", "f", "no body fins", "mini body fins")

    if me.SS2[0] == "S":     # Skin
        descr = fbs.lyst(descr, earfins)
        descr = fbs.lyst(descr, webbing)
    if me.SS2[1] == "S":     # Organ systems
        descr = fbs.lyst(descr, gills)
        descr = fbs.lyst(descr, breathes)
    if me.SS2[2] == "S":     # ?
        descr = fbs.lyst(descr, bladders)
    if me.SS2[3] == "S":     # ?
        descr = fbs.lyst(descr, biolum)
        descr = fbs.lyst(descr, teeth)
    if me.SS2[4] == "S":     # ?
        descr = fbs.lyst(descr, eyelids)
        descr = fbs.lyst(descr, bodyfins)

    if descr == "":
        descr = cd.dwell()

    return descr


def describedwell(sea):
    self = gene.Aquatic("rr", sea)
    detail = self.code[3:len(self.code) - 3]
    landtype = slurry.sgenesea[3:len(slurry.sgeneland) - 3]
    seatype = slurry.sgenesea[3:len(slurry.sgenesea) - 3]
    weirdo = False
    descr = ""
    if self.SS2[1] == "S":
        weirdo = True
    if detail == landtype or detail == seatype:
        weirdo = False
    if weirdo:
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
    if self.SS2 == "SSSSS":
        descr = "seadweller"
    if self.SS2 == "sssss":
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


def countaa(inhale):
    a = 0
    if inhale[0] == "a":
        a = a + 1
    if inhale[1] == "a":
        a = a + 1
    if inhale[2] == "a":
        a = a + 1
    if inhale[3] == "a":
        a = a + 1
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


# Most "repair troll" functions are in the display function.  For now.
# Until I figure out why it isn't working any other way.


trollblank = gene.trollobj()
