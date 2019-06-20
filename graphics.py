import genome as gene
import pygame
import formattingbs as fbs


# TEETH
def thetooth(mouf):
    left = ["", "", "", "", "", "", ""]
    right = ["", "", "", "", "", "", ""]

    athing = mouf["top"]
    for a in athing:  # L/R
        bthing = athing[a]
        for b in bthing:  # type/length
            cthing = bthing[b]
            for c in cthing:  # (indiv teeth)
                cthing[c] = str(cthing[c])
            bthing[b] = cthing
        athing[a] = bthing
    mouf["top"] = athing
    athing = mouf["bot"]
    for a in athing:  # L/R
        bthing = athing[a]
        for b in bthing:  # type/length
            cthing = bthing[b]
            for c in cthing:  # (indiv teeth)
                cthing[c] = str(cthing[c])
            bthing[b] = cthing
        athing[a] = bthing
    mouf["top"] = athing

    for arb in mouf["top"]["L"]["type"]:
        mouf["top"]["L"]["type"][arb] = str(mouf["top"]["L"]["type"][arb])

    x = 1
    while x < 7:
        if mouf["top"]["L"]["sym"][x] is False and mouf["top"]["R"]["sym"][x] is False:
            left[x] = mouf["top"]["L"]["type"][x] + mouf["top"]["L"]["type"][x] + mouf["top"]["L"]["length"][x]
            right[x] = mouf["top"]["R"]["type"][x] + mouf["top"]["R"]["type"][x] + mouf["top"]["R"]["length"][x]
        if mouf["top"]["L"]["sym"][x] is True and mouf["top"]["R"]["sym"][x] is False:
            left[x] = mouf["top"]["L"]["type"][x] + mouf["top"]["L"]["type"][x] + mouf["top"]["L"]["length"][x]
            right[x] = mouf["top"]["L"]["type"][x] + mouf["top"]["L"]["type"][x] + mouf["top"]["L"]["length"][x]
        if mouf["top"]["L"]["sym"][x] is False and mouf["top"]["R"]["sym"][x] is True:
            left[x] = mouf["top"]["R"]["type"][x] + mouf["top"]["R"]["type"][x] + mouf["top"]["R"]["length"][x]
            right[x] = mouf["top"]["R"]["type"][x] + mouf["top"]["R"]["type"][x] + mouf["top"]["R"]["length"][x]
        if mouf["top"]["L"]["sym"][x] is True and mouf["top"]["R"]["sym"][x] is True:
            toofleng = str((mouf["top"]["L"]["length"][x] + mouf["top"]["R"]["length"][x]) // 2)
            left[x] = mouf["top"]["L"]["type"][x] + mouf["top"]["R"]["type"][x] + toofleng
            right[x] = mouf["top"]["R"]["type"][x] + mouf["top"]["L"]["type"][x] + toofleng
            while left[x] != right[x]:
                # If the teeth are identical, it'll move on to the next tooth.
                if left[x][0:2] != "PC" and left[x][0:2] != "CP":
                    left[x] = "RR" + toofleng
                    right[x] = "RR" + toofleng
                if left[x][0:2] == "PC" or left[x][0:2] == "CP":
                    left[x] = "PC" + toofleng
                    right[x] = "PC" + toofleng
        x = x + 1
    jawtop = right[6] + right[5] + right[4] + right[3] + right[2] + right[1]
    jawtop = jawtop + left[1] + left[2] + left[3] + left[4] + left[5] + left[6]
    left = ["", "", "", "", "", "", ""]
    right = ["", "", "", "", "", "", ""]
    x = 1
    if mouf["bot"]["L"]["sym"][x] is False and mouf["bot"]["R"]["sym"][x] is False:
        left[x] = mouf["bot"]["L"]["type"][x] + mouf["bot"]["L"]["type"][x] + mouf["bot"]["L"]["length"][x]
        right[x] = mouf["bot"]["R"]["type"][x] + mouf["bot"]["R"]["type"][x] + mouf["bot"]["R"]["length"][x]
    if mouf["bot"]["L"]["sym"][x] is True and mouf["bot"]["R"]["sym"][x] is False:
        left[x] = mouf["bot"]["L"]["type"][x] + mouf["bot"]["L"]["type"][x] + mouf["bot"]["L"]["length"][x]
        right[x] = mouf["bot"]["L"]["type"][x] + mouf["bot"]["L"]["type"][x] + mouf["bot"]["L"]["length"][x]
    if mouf["bot"]["L"]["sym"][x] is False and mouf["bot"]["R"]["sym"][x] is True:
        left[x] = mouf["bot"]["R"]["type"][x] + mouf["bot"]["R"]["type"][x] + mouf["bot"]["R"]["length"][x]
        right[x] = mouf["bot"]["R"]["type"][x] + mouf["bot"]["R"]["type"][x] + mouf["bot"]["R"]["length"][x]
    if mouf["bot"]["L"]["sym"][x] is True and mouf["bot"]["R"]["sym"][x] is True:
        toofleng = str((mouf["bot"]["L"]["length"][x] + mouf["bot"]["R"]["length"][x]) // 2)
        left[x] = mouf["bot"]["L"]["type"][x] + mouf["bot"]["R"]["type"][x] + toofleng
        right[x] = mouf["bot"]["R"]["type"][x] + mouf["bot"]["L"]["type"][x] + toofleng
        while left[x] != right[x]:
            # If the teeth are identical, it'll move on to the next tooth.
            if left[x][0:2] != "PC" and left[x][0:2] != "CP":
                left[x] = "RR" + toofleng
                right[x] = "RR" + toofleng
            if left[x][0:2] == "PC" or left[x][0:2] == "CP":
                left[x] = "PC" + toofleng
                right[x] = "PC" + toofleng
        x = x + 1
    jawbot = right[6] + right[5] + right[4] + right[3] + right[2] + right[1]
    jawbot = jawbot + left[1] + left[2] + left[3] + left[4] + left[5] + left[6]
    return jawtop, jawbot


def thewholetooth(mouf):
    left = ["", "", "", "", "", "", ""]
    right = ["", "", "", "", "", "", ""]
    x = 1
    while x < 7:
        left[x] = mouf["top"]["L"]["type"][x] + mouf["top"]["L"]["type"][x] + mouf["top"]["L"]["length"][x]
        right[x] = mouf["top"]["R"]["type"][x] + mouf["top"]["R"]["type"][x] + mouf["top"]["R"]["length"][x]
        x = x + 1
    jawtop = right[6] + right[5] + right[4] + right[3] + right[2] + right[1]
    jawtop = jawtop + left[1] + left[2] + left[3] + left[4] + left[5] + left[6]
    left = ["", "", "", "", "", "", ""]
    right = ["", "", "", "", "", "", ""]
    x = 1
    while x < 7:
        left[x] = mouf["bot"]["L"]["type"][x] + mouf["bot"]["L"]["type"][x] + mouf["bot"]["L"]["length"][x]
        right[x] = mouf["bot"]["R"]["type"][x] + mouf["bot"]["R"]["type"][x] + mouf["bot"]["R"]["length"][x]
        x = x + 1
    jawbot = right[6] + right[5] + right[4] + right[3] + right[2] + right[1]
    jawbot = jawbot + left[1] + left[2] + left[3] + left[4] + left[5] + left[6]
    return jawtop, jawbot


def jawprint(mouf, closed=False):
    offscreen = pygame.Surface((85, 20))
    offscreen.fill((128, 128, 128))
    # Showing Teeth
    jawmain = jawprintgraphics(mouf, False)
    # Recessive Teeth
    jawtemp1 = jawprintgraphics(mouf, True)
#    jawtemp2 = pygame.transform.flip(jawtemp1, 1, 0)
#    jawtemp2.set_alpha(50)
#    jawtemp1.blit(jawtemp2, (0, 0))
    jawtemp1.set_alpha(25)
    # Finalize
    jawmain.set_alpha(90)
    offscreen.blit(jawmain, (0, 0))
    offscreen.blit(jawmain, (0, 0), None, pygame.BLEND_MULT)
    offscreen.blit(jawtemp1, (0, 0))
    offscreen.blit(jawtemp1, (0, 0), None, pygame.BLEND_ADD)
    # If dissatisfied, change jawmain alpha to 96 and remove the Blend Flag statements.

    if closed:
        # Assemble Variables
        mouth = mouf
        maxlength = int(mouth["high"])
        maxwidth = int(mouth["wide"]) * 7
        middle = 42  # 85//2 round down
        # Make temporary screen
        offscreen2 = pygame.Surface((85, 20))
        offscreen2.fill((0, 0, 0))
        offscreen2.set_colorkey((0, 0, 0))
        # Clip toothtips out of main jaw img
        toptoofers = offscreen.subsurface(pygame.Rect(middle - maxwidth, maxlength, 2*maxwidth, 9-maxlength))
        bottoofers = offscreen.subsurface(pygame.Rect(middle - maxwidth, 10, 2*maxwidth, 9-maxlength))
        # Put them onto temporary screen
        offscreen2.blit(toptoofers, (middle - maxwidth, 11))
        offscreen2.blit(bottoofers, (middle - maxwidth, 1+maxlength))
        # Fill original image with blank color and some transparency
        offscreen.fill((0, 255, 255))
        offscreen.blit(offscreen2, (0, 0))
        offscreen.set_colorkey((0, 255, 255))
        # Draw black line across middle to show the lip
        pygame.draw.line(offscreen, (0, 0, 0), (middle - maxwidth - 3, 10), (middle + maxwidth + 3, 10), 1)
    return offscreen


def jawprintgraphics(mouf, whole=False):
    jawt, jawb = thetooth(mouf)
    if whole:
        jawt, jawb = thewholetooth(mouf)
    x = 0
    offscreen = pygame.Surface((85, 20))
    offscreen.fill((0, 0, 0))
    toof = pygame.Surface((6, 10))
    toof.fill((0, 0, 0))
    here = 3 * x
    while (here+3) <= len(jawt):
        imgloc = str(jawt[here:here + 3]) + ".PNG"
        toof, toofrect = fbs.load_png(imgloc, "teef")
        toof = toof.subsurface(pygame.Rect(0, 1, 6, 9))
        if 2*here >= len(jawt):
            toof = pygame.transform.flip(toof, 1, 0)
        place = ((7*x)+1, 1)
        offscreen.blit(toof, place)
        x = x + 1
        here = 3 * x
    x = 0
    here = 3 * x
    while (here+3) <= len(jawb):
        imgloc = str(jawb[here:here + 3]) + ".PNG"
        toof, toofrect = fbs.load_png(imgloc, "teef")
        toof = pygame.transform.flip(toof, 1, 0)  # Flip just the lower jaw.  Remove?
        toof = toof.subsurface(pygame.Rect(0, 1, 6, 9))
        if (2*here) >= len(jawt):
            toof = pygame.transform.flip(toof, 1, 0)
        toof = pygame.transform.flip(toof, 0, 1)
        place = ((7*x)+1, 10)
        offscreen.blit(toof, place)
        x = x + 1
        here = 3 * x
    return offscreen


# HORNS
def hornprint(inhorn, controls):
    iconw = 33
    # inhorn is of format: {"length": 0, "curl": 0, "radial": "", "dir": "", "width": "", "tip": ""}
    # controls is:         {"select": "XX", "stunt": "XX", "type": "XX", "angle": "XX",
    #                       "noclip": "XX", "mountpt": "X", "gaps": "XX"},

    offscreen = pygame.Surface(((iconw), (iconw * 3)))
    offscreen.fill((0, 0, 0))
    # Feed all data into functions preprocessed.  No hornobj inside.
    img = hornarch(inhorn, controls["angle"])
    offscreen.blit(img, (0, 0))
    img = hornradial(controls["radial"], inhorn["width"], controls["gaps"])
    offscreen.blit(img, (0, iconw))
    img = horntip(inhorn["tip"])
    offscreen.blit(img, (0, 2*iconw))
    return offscreen


def hornsprint(me):
    numhorns = 22
    hornright1 = ""
    hornright2 = ""
    hornright3 = ""
    hornleft1 = ""
    hornleft2 = ""
    hornleft3 = ""
    descr = ""
    drh1 = False  # Describe Horn Right 1
    drh2 = False  # Describe Horn Right 2
    drh3 = False
    dlh1 = False  # Describe Horn Left 1
    dlh2 = False  # Describe Horn left 2
    dlh3 = False

    # Horn presence...
    if me["controls"]["select"] == "TT":
        numhorns = 6
        dlh1 = True
        dlh2 = True
        dlh3 = True
        hornleft1 = me["left"][1]
        hornleft2 = me["left"][2]
        hornleft3 = me["left"][3]
        drh1 = True
        drh2 = True
        drh3 = True
        hornright1 = me["right"][1]
        hornright2 = me["right"][2]
        hornright3 = me["right"][3]
    if me["controls"]["select"] == "TD":
        numhorns = 5
        dlh1 = True
        dlh2 = True
        dlh3 = True
        hornleft1 = me["left"][1]
        hornleft2 = me["left"][2]
        hornleft3 = me["left"][3]
        drh1 = True
        drh2 = True
        hornright1 = me["right"][1]
        hornright2 = me["right"][2]
        hornright3 = "none"
    if me["controls"]["select"] == "DT":
        numhorns = 5
        dlh1 = True
        dlh2 = True
        hornleft1 = me["left"][1]
        hornleft2 = me["left"][2]
        hornleft3 = "none"
        drh1 = True
        drh2 = True
        drh3 = True
        hornright1 = me["right"][1]
        hornright2 = me["right"][2]
        hornright3 = me["right"][3]
    if me["controls"]["select"] == "Td":
        numhorns = 4
        dlh1 = True
        dlh2 = True
        dlh3 = True
        hornleft1 = me["left"][1]
        hornleft2 = me["left"][2]
        hornleft3 = me["left"][3]
        drh1 = True
        hornright1 = me["right"][1]
        hornright2 = "none"
        hornright3 = "none"
    if me["controls"]["select"] == "dT":
        numhorns = 4
        dlh1 = True
        hornleft1 = me["left"][1]
        hornleft2 = "none"
        hornleft3 = "none"
        drh1 = True
        drh2 = True
        drh3 = True
        hornright1 = me["right"][1]
        hornright2 = me["right"][2]
        hornright3 = me["right"][3]
    if me["controls"]["select"] == "DD":
        numhorns = 4
        dlh1 = True
        dlh2 = True
        hornleft1 = me["left"][1]
        hornleft2 = me["left"][2]
        hornleft3 = "none"
        drh1 = True
        drh2 = True
        hornright1 = me["right"][1]
        hornright2 = me["right"][2]
        hornright3 = "none"
    if me["controls"]["select"] == "Dd":
        numhorns = 3
        dlh1 = True
        dlh2 = True
        hornleft1 = me["left"][1]
        hornleft2 = me["left"][2]
        hornleft3 = "none"
        drh1 = True
        hornright1 = me["right"][1]
        hornright2 = "none"
        hornright3 = "none"
    if me["controls"]["select"] == "dD":
        numhorns = 3
        dlh1 = True
        hornleft1 = me["left"][1]
        hornleft2 = "none"
        hornleft3 = "none"
        drh1 = True
        drh2 = True
        hornright1 = me["right"][1]
        hornright2 = me["right"][2]
        hornright3 = "none"
    if me["controls"]["select"] == "Xx":
        numhorns = 1
        hornleft1 = "none"
        hornleft2 = "none"
        hornleft3 = "none"
        drh1 = True
        hornright1 = me["right"][1]
        hornright2 = "none"
        hornright3 = "none"
    if me["controls"]["select"] == "xX":
        numhorns = 1
        hornleft1 = me["left"][1]
        hornleft2 = "none"
        hornleft3 = "none"
        dlh1 = True
        hornright1 = "none"
        hornright2 = "none"
        hornright3 = "none"
    if me["controls"]["select"] == "TX":
        numhorns = 3
        dlh1 = True
        dlh2 = True
        dlh3 = True
        hornleft1 = me["left"][1]
        hornleft2 = me["left"][2]
        hornleft3 = me["left"][3]
        hornright1 = "none"
        hornright2 = "none"
        hornright3 = "none"
    if me["controls"]["select"] == "XT":
        numhorns = 3
        hornleft1 = "none"
        hornleft2 = "none"
        hornleft3 = "none"
        drh1 = True
        drh2 = True
        drh3 = True
        hornright1 = me["right"][1]
        hornright2 = me["right"][2]
        hornright3 = me["right"][3]
    if me["controls"]["select"] == "DX":
        numhorns = 2
        dlh1 = True
        dlh2 = True
        hornleft1 = me["left"][1]
        hornleft2 = me["left"][2]
        hornleft3 = "none"
        hornright1 = "none"
        hornright2 = "none"
        hornright3 = "none"
    if me["controls"]["select"] == "XD":
        numhorns = 2
        hornleft1 = "none"
        hornleft2 = "none"
        hornleft3 = "none"
        drh1 = True
        drh2 = True
        hornright1 = me["right"][1]
        hornright2 = me["right"][2]
        hornright3 = "none"
    if me["controls"]["select"] == "XX":
        numhorns = 0
        hornleft1 = "none"
        hornleft2 = "none"
        hornleft3 = "none"
        hornright1 = "none"
        hornright2 = "none"
        hornright3 = "none"
        descr = "no horns"
    if numhorns == 22:  # If the troll has the default number of horns
        dlh1 = True
        drh1 = True
        hornleft1 = me["left"][1]    # Set to default.  This also covers when
        hornleft2 = "none"
        hornleft3 = "none"
        hornright1 = me["right"][1]  # either of the genes given are "1"
        hornright2 = "none"
        hornright3 = "none"
        numhorns = 2
        # Now, if any of the genes are 2's or 3's, overwrite appropriately:
    if me["controls"]["select"][0] == "2":
        hornleft1 = me["left"][2]
    if me["controls"]["select"][0] == "3":
        hornleft1 = me["left"][3]
    if me["controls"]["select"][1] == "2":
        hornright1 = me["right"][2]
    if me["controls"]["select"][1] == "3":
        hornright1 = me["right"][3]
    # hornright1, hornright2, hornleft1, hornleft2, and numhorns know what we're describing.

    # horn length adjustments:
    if dlh2:
        hornleft2["length"] = hornleft1["length"] - 1  # One unit shorter than the previous horn
        if hornleft2["length"] < 1:     # But at least 1 unit.
            hornleft2["length"] = 1
    if dlh3:
        hornleft3["length"] = hornleft2["length"] - 1  # One unit shorter than previous horn
        if hornleft3["length"] < 1:     # But at least 1 unit.
            hornleft3["length"] = 1
    if drh2:
        hornright2["length"] = hornright1["length"] - 1  # One unit shorter than the previous horn
        if hornright2["length"] < 1:     # But at least 1 unit.
            hornright2["length"] = 1
    if drh3:
        hornright3["length"] = hornright2["length"] - 1  # One unit shorter than the previous horn
        if hornright3["length"] < 1:     # But at least 1 unit.
            hornright3["length"] = 1

    iconw = 33
    background = pygame.Surface(((iconw*6+5), (iconw * 4)))
    background.fill((0, 255, 255))
    background.set_colorkey((0, 255, 255))
    pos = 3*iconw

    if dlh3:
        img = hornprint(hornleft3, me["controls"])
        img = pygame.transform.flip(img, 1, 0)
        background.blit(img, (pos-(3*iconw), 0))
    if dlh2:
        img = hornprint(hornleft2, me["controls"])
        img = pygame.transform.flip(img, 1, 0)
        background.blit(img, (pos-(2*iconw), 0))
    if dlh1:
        img = hornprint(hornleft1, me["controls"])
        img = pygame.transform.flip(img, 1, 0)
        background.blit(img, (pos-iconw, 0))
    if drh1:
        img = hornprint(hornright1, me["controls"])
        background.blit(img, (pos+5, 0))
    if drh2:
        img = hornprint(hornright2, me["controls"])
        background.blit(img, (pos+5+(1*iconw), 0))
    if drh3:
        img = hornprint(hornright3, me["controls"])
        background.blit(img, (pos+5+(2*iconw), 0))

    # Horn type
    ttype = me["controls"]["type"]
    ht = ""
    typeK = 0
    typeE = 0
    typeA = 0
    typeP = 0
    typeB = 0
    for arb in ttype:
        if arb == "K":
            typeK = typeK + 2
        if arb == "k":
            typeK = typeK + 1
        if arb == "E":
            typeE = typeE + 2
        if arb == "e":
            typeE = typeE + 1
        if arb == "A":
            typeA = typeA + 2
        if arb == "a":
            typeA = typeA + 1
        if arb == "P":
            typeP = typeP + 2
        if arb == "p":
            typeP = typeP + 1
        if arb == "B":
            typeB = typeB + 2
        if arb == "b":
            typeB = typeB + 1

    if typeK > 1:
        ht = ht + "/Keratin"
    if typeE > 1:
        ht = ht + "/Electrosensory"
    if typeA > 1:
        ht = ht + "/Antler"
    if typeP > 1:
        ht = ht + "/Power"
    if typeB > 1:
        ht = ht + "/Balance"
    if ht != "":
        descr = fbs.lyst(descr, ht[1:len(ht)])

        # Self-impact test.
        if me["controls"]["noclip"] == "X":
            descr = fbs.lyst(descr, "Potentially clipping")
    #    To be in danger, must have X gene, * and *horns shaped in a way that can impact.
    #    - spiraling: treat curl as 1 greater than it actually is.
    #    - All Curl > 5
    #    - Inward,with curl > 2 and length > 1.
    #    - Outward, curl > 180 degrees, length > 2
    #    - Back direction, curl > 1, length > 1.
    #    - side + wide = ear deformity
    #    - front + wide = forehead deformity
    #    - Side + in = mild skull deformities.

    # Gaps
    gaps = me["controls"]["gaps"]
    if gaps == "NN" or gaps == "Nn" or gaps == "nN" or gaps == "Nh" or gaps == "hN":
        descr = fbs.lyst(descr, "a notch")
    if gaps == "nn" or gaps == "nh":
        descr = fbs.lyst(descr, "small notches")
    if gaps == "HH" or gaps == "Hh" or gaps == "hH" or gaps == "Hn" or gaps == "nH":
        descr = fbs.lyst(descr, "a hole")
    if gaps == "hh" or gaps == "hn":
        descr = fbs.lyst(descr, "small holes")
    if gaps == "OO" or gaps == "Oo" or gaps == "oO":
        descr = fbs.lyst(descr, "hollow")
    if gaps == "oo" or gaps == "oh" or gaps == "on" or gaps == "ho" or gaps == "no":
        descr = fbs.lyst(descr, "porous")

    (mx, my) = me["controls"]["mountpt"]
    if my == 0:
        if dlh1 or drh1:
            descr = fbs.lyst("centered", descr)
    if mx > 2:
        if dlh1 or drh1:
            descr = fbs.lyst("backmounted", descr)
    if my > 2:
        if dlh1 or drh1:
            descr = fbs.lyst("sidemounted", descr)

    return background, descr


# Move Hollow=assessment to an outside function
def hornarch(horn, angle):

    # By default, horns are S-shaped.
    imgloc = "arch4.PNG"
    # Overwrite with the actual curl data:
    if horn["curl"] == 1:
        imgloc = "arch1.PNG"
    if horn["curl"] == 2:
        imgloc = "arch2.PNG"
    if horn["curl"] == 3:
        imgloc = "arch3.PNG"
    if horn["curl"] == 4:
        imgloc = "arch4.PNG"
    if horn["curl"] == 5:
        imgloc = "arch5.PNG"
    if horn["curl"] == 6:
        imgloc = "arch6.PNG"
    if horn["curl"] == 7:
        imgloc = "arch7.PNG"
    if horn["curl"] == 8:
        imgloc = "arch8.PNG"

    # Length.  By default, length 1.
    x = 1
    if horn["length"] == 1:
        x = 0
    if horn["length"] == 2:
        x = 1
    if horn["length"] == 3:
        x = 2
    if horn["length"] == 4:
        x = 3

    # Angularity, by default, smooth.
    y = 0
    if angle == "SS":
        y = 0
    if angle == "SA" or angle == "AS":
        y = 1
    if angle == "AA":
        y = 2

    offscreen = pygame.Surface((133, 100))
    offscreen.fill((0, 0, 0))
    hornimg, hornrect = fbs.load_png(imgloc, "horn")
    archfinal = pygame.Surface((33, 33))
    archfinal.fill((0, 0, 0))
    x = x * 33
    y = y * 33
    archfinal = hornimg.subsurface(pygame.Rect(x, y, 33, 33))
    return archfinal


# Move Hollow=assessment to an outside function
def hornradial(radial, wide, hollow):
    # By default, horns are solid.
    imgloc = "radialsolid.png"
    # Overwrite with the actual type:
    if hollow == "OO" or hollow == "Oo" or hollow == "oO":
        imgloc = "radialH1.png"
    if hollow == "oo" or hollow == "oh" or hollow == "ho" or hollow == "on" or hollow == "no":
        imgloc = "radialH+.png"

    # Width
    y = 0
    if wide == "w":
        y = 0
    if wide == "n":
        y = 1

    # Radial
    x = 0
    if radial == "R":
        x = 0
    if radial == "O":
        x = 1
    if radial == "T":
        x = 2
    if radial == "S":
        x = 3
    if radial == "C":
        x = 4
    if radial == "I":
        x = 5

    offscreen = pygame.Surface((133, 100))
    offscreen.fill((0, 0, 0))
    hornimg, hornrect = fbs.load_png(imgloc, "horn")
    radfinal = pygame.Surface((33, 33))
    radfinal.fill((0, 0, 0))
    x = x * 33
    y = y * 33
    radfinal = hornimg.subsurface(pygame.Rect(x, y, 33, 33))
    return radfinal


def horntip(tip):

    # All of these are in one image
    imgloc = "tips.png"

    # Rows
    y = 0
    if tip == "p":
        # List of tips on row 1.
        y = 1
    if tip == "?" or tip == "?" or tip == "?":
        # List of tips on row 2.
        y = 2

    # Rows
    x = 0
    if tip == "P" or tip == "p":
        # row 1
        x = 0
    if tip == "B":
        # row 2
        x = 2
    if tip == "b":
        x = 3
    if tip == "C":
        x = 4
    if tip == "F":
        x = 5
    if tip == "H":
        x = 6
    if tip == "J":
        x = 7
    if tip == "R":
        x = 8
    if tip == "S":
        x = 9
    if tip == "s":
        x = 10
    if tip == "L":
        x = 11

    offscreen = pygame.Surface((397, 265))
    offscreen.fill((0, 0, 0))
    hornimg, hornrect = fbs.load_png(imgloc, "horn")
    final = pygame.Surface((33, 33))
    final.fill((0, 0, 0))
    x = x * 33
    y = y * 33
    final = hornimg.subsurface(pygame.Rect(x, y, 33, 33))
    return final


def hornplacement(inhorn):
    # Have a pic with three circles of different colors (the 3 horn colors, in order?)
    # Use palleteswap to turn the unneeded two of them skintone.
    return inhorn
