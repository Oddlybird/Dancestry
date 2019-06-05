import genome as gene
import pygame
import formattingbs as fbs


# TEETH
def thetooth(moufstr):
    mouf = gene.Mouth(moufstr)
    left = ["", "", "", "", "", ""]
    right = ["", "", "", "", "", ""]
    x = 0
    while x < 6:
        if mouf.symtopl[x] == "F" and mouf.symtopr[x] == "F":
            left[x] = mouf.typetopl[x] + mouf.typetopl[x] + mouf.lengthtopl[x]
            right[x] = mouf.typetopr[x] + mouf.typetopr[x] + mouf.lengthtopr[x]
        if mouf.symtopl[x] == "T" and mouf.symtopr[x] == "F":
            left[x] = mouf.typetopl[x] + mouf.typetopl[x] + mouf.lengthtopl[x]
            right[x] = mouf.typetopl[x] + mouf.typetopl[x] + mouf.lengthtopl[x]
        if mouf.symtopl[x] == "F" and mouf.symtopr[x] == "T":
            left[x] = mouf.typetopr[x] + mouf.typetopr[x] + mouf.lengthtopr[x]
            right[x] = mouf.typetopr[x] + mouf.typetopr[x] + mouf.lengthtopr[x]
        if mouf.symtopl[x] == "T" and mouf.symtopr[x] == "T":
            toofleng = str((int(mouf.lengthtopl[x]) + int(mouf.lengthtopr[x])) // 2)
            left[x] = mouf.typetopl[x] + mouf.typetopr[x] + toofleng
            right[x] = mouf.typetopr[x] + mouf.typetopl[x] + toofleng
            while left[x] != right[x]:
                # If the teeth are identical, it'll move on to the next tooth.
                if left[x][0:2] != "PC" and left[x][0:2] != "CP":
                    left[x] = "RR" + toofleng
                    right[x] = "RR" + toofleng
                if left[x][0:2] == "PC" or left[x][0:2] == "CP":
                    left[x] = "PC" + toofleng
                    right[x] = "PC" + toofleng
        x = x + 1
    jawtop = right[5] + right[4] + right[3] + right[2] + right[1] + right[0]
    jawtop = jawtop + left[0] + left[1] + left[2] + left[3] + left[4] + left[5]
    left = ["", "", "", "", "", ""]
    right = ["", "", "", "", "", ""]
    x = 0
    while x < 6:
        if mouf.symbotl[x] == "F" and mouf.symbotr[x] == "F":
            left[x] = mouf.typebotl[x] + mouf.typebotl[x] + mouf.lengthbotl[x]
            right[x] = mouf.typebotr[x] + mouf.typebotr[x] + mouf.lengthbotr[x]
        if mouf.symbotl[x] == "T" and mouf.symbotr[x] == "F":
            left[x] = mouf.typebotl[x] + mouf.typebotl[x] + mouf.lengthbotl[x]
            right[x] = mouf.typebotl[x] + mouf.typebotl[x] + mouf.lengthbotl[x]
        if mouf.symbotl[x] == "F" and mouf.symbotr[x] == "T":
            left[x] = mouf.typebotr[x] + mouf.typebotr[x] + mouf.lengthbotr[x]
            right[x] = mouf.typebotr[x] + mouf.typebotr[x] + mouf.lengthbotr[x]
        if mouf.symbotl[x] == "T" and mouf.symbotr[x] == "T":
            toofleng = str((int(mouf.lengthbotl[x]) + int(mouf.lengthbotr[x])) // 2)
            left[x] = mouf.typebotl[x] + mouf.typebotr[x] + toofleng
            right[x] = mouf.typebotr[x] + mouf.typebotl[x] + toofleng
            while left[x] != right[x]:
                # If the teeth are identical, it'll move on to the next tooth.
                if left[x][0:2] != "PC" and left[x][0:2] != "CP":
                    left[x] = "RR" + toofleng
                    right[x] = "RR" + toofleng
                if left[x][0:2] == "PC" or left[x][0:2] == "CP":
                    left[x] = "PC" + toofleng
                    right[x] = "PC" + toofleng
        x = x + 1
    jawbot = right[5] + right[4] + right[3] + right[2] + right[1] + right[0]
    jawbot = jawbot + left[0] + left[1] + left[2] + left[3] + left[4] + left[5]
    return jawtop, jawbot


def thewholetooth(moufstr):
    mouf = gene.Mouth(moufstr)
    left = ["", "", "", "", "", ""]
    right = ["", "", "", "", "", ""]
    x = 0
    while x < 6:
        left[x] = mouf.typetopl[x] + mouf.typetopl[x] + mouf.lengthtopl[x]
        right[x] = mouf.typetopr[x] + mouf.typetopr[x] + mouf.lengthtopr[x]
        x = x + 1
    jawtop = right[5] + right[4] + right[3] + right[2] + right[1] + right[0]
    jawtop = jawtop + left[0] + left[1] + left[2] + left[3] + left[4] + left[5]
    left = ["", "", "", "", "", ""]
    right = ["", "", "", "", "", ""]
    x = 0
    while x < 6:
        left[x] = mouf.typebotl[x] + mouf.typebotl[x] + mouf.lengthbotl[x]
        right[x] = mouf.typebotr[x] + mouf.typebotr[x] + mouf.lengthbotr[x]
        x = x + 1
    jawbot = right[5] + right[4] + right[3] + right[2] + right[1] + right[0]
    jawbot = jawbot + left[0] + left[1] + left[2] + left[3] + left[4] + left[5]
    return jawtop, jawbot


def jawprint(mouf):
    offscreen = pygame.Surface((85, 21))
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
    return offscreen


def jawprintgraphics(mouf, whole=False):
    jawt, jawb = thetooth(mouf)
    if whole:
        jawt, jawb = thewholetooth(mouf)
    x = 0
    offscreen = pygame.Surface((85, 21))
    offscreen.fill((0, 0, 0))
    toof = pygame.Surface((6, 10))
    toof.fill((0, 0, 0))
    here = 3 * x
    while (here+3) <= len(jawt):
        imgloc = str(jawt[here:here + 3]) + ".PNG"
        toof, toofrect = fbs.load_png(imgloc, "teef")
        if 2*here >= len(jawt):
            toof = pygame.transform.flip(toof, 1, 0)
        place = ((7*x)+1, 0)
        offscreen.blit(toof, place)
        x = x + 1
        here = 3 * x
    x = 0
    here = 3 * x
    while (here+3) <= len(jawb):
        imgloc = str(jawb[here:here + 3]) + ".PNG"
        toof, toofrect = fbs.load_png(imgloc, "teef")
        toof = pygame.transform.flip(toof, 1, 0)  # Flip just the lower jaw.  Remove?
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
    # Do a few backflips to put the variables where we want them.
    hornscode = "Rgx2dccPBACTn.12RSnH.12RSnH.12RSnH.12RSnH.12RSnH.12RSnH"
    hornset = gene.Horns(hornscode)
    hornset.controls = controls
    hornset.hornleft1 = inhorn
    hornset.update()
    hornscode = hornset.code
    hornset = gene.Horns(hornscode)
    hornleft1 = gene.HornObj(hornset.hornleft1)
    # Hornset now contains the right controls, and hornleft1 is the horn we want.

    offscreen = pygame.Surface(((iconw), (iconw * 3)))
    offscreen.fill((0, 0, 0))
    # Feed all data into functions preprocessed.  No hornobj inside.
    img = hornarch(hornset.hornleft1, hornset.angle)
    offscreen.blit(img, (0, 0))
    img = hornradial(hornleft1.radial, hornleft1.wide, hornset.gaps)
    offscreen.blit(img, (0, iconw))
    img = horntip(hornleft1.tip)
    offscreen.blit(img, (0, 2*iconw))
    return offscreen


def hornsprint(inhorns):
    numhorns = 22
    hornright1 = ""
    hornright2 = ""
    hornright3 = ""
    hornleft1 = ""
    hornleft2 = ""
    hornleft3 = ""
    drh1 = False  # Describe Horn Right 1
    drh2 = False  # Describe Horn Right 2
    drh3 = False
    dlh1 = False  # Describe Horn Left 1
    dlh2 = False  # Describe Horn left 2
    dlh3 = False
    me = gene.Horns(inhorns)

    # Horn presence...
    if me.select == "TT":
        numhorns = 6
        dlh1 = True
        dlh2 = True
        dlh3 = True
        hornleft1 = me.hornleft1
        hornleft2 = me.hornleft2
        hornleft3 = me.hornleft3
        drh1 = True
        drh2 = True
        drh3 = True
        hornright1 = me.hornright1
        hornright2 = me.hornright2
        hornright3 = me.hornright3
    if me.select == "TD":
        numhorns = 5
        dlh1 = True
        dlh2 = True
        dlh3 = True
        hornleft1 = me.hornleft1
        hornleft2 = me.hornleft2
        hornleft3 = me.hornleft3
        drh1 = True
        drh2 = True
        hornright1 = me.hornright1
        hornright2 = me.hornright2
        hornright3 = "none"
    if me.select == "DT":
        numhorns = 5
        dlh1 = True
        dlh2 = True
        hornleft1 = me.hornleft1
        hornleft2 = me.hornleft2
        hornleft3 = "none"
        drh1 = True
        drh2 = True
        drh3 = True
        hornright1 = me.hornright1
        hornright2 = me.hornright2
        hornright3 = me.hornright3
    if me.select == "Td":
        numhorns = 4
        dlh1 = True
        dlh2 = True
        dlh3 = True
        hornleft1 = me.hornleft1
        hornleft2 = me.hornleft2
        hornleft3 = me.hornleft3
        drh1 = True
        hornright1 = me.hornright1
        hornright2 = "none"
        hornright3 = "none"
    if me.select == "Td":
        numhorns = 4
        dlh1 = True
        hornleft1 = me.hornleft1
        hornleft2 = "none"
        hornleft3 = "none"
        drh1 = True
        drh2 = True
        drh3 = True
        hornright1 = me.hornright1
        hornright2 = me.hornright2
        hornright3 = me.hornright3
    if me.select == "DD":
        numhorns = 4
        dlh1 = True
        dlh2 = True
        hornleft1 = me.hornleft1
        hornleft2 = me.hornleft2
        hornleft3 = "none"
        drh1 = True
        drh2 = True
        hornright1 = me.hornright1
        hornright2 = me.hornright2
        hornright3 = "none"
    if me.select == "Dd":
        numhorns = 3
        dlh1 = True
        dlh2 = True
        hornleft1 = me.hornleft1
        hornleft2 = me.hornleft2
        hornleft3 = "none"
        drh1 = True
        hornright1 = me.hornright1
        hornright2 = "none"
        hornright3 = "none"
    if me.select == "dD":
        numhorns = 3
        dlh1 = True
        hornleft1 = me.hornleft1
        hornleft2 = "none"
        hornleft3 = "none"
        drh1 = True
        drh2 = True
        hornright1 = me.hornright1
        hornright2 = me.hornright2
        hornright3 = "none"
    if me.select == "Xx":
        numhorns = 1
        hornleft1 = "none"
        hornleft2 = "none"
        hornleft3 = "none"
        drh1 = True
        hornright1 = me.hornright1
        hornright2 = "none"
        hornright3 = "none"
    if me.select == "xX":
        numhorns = 1
        hornleft1 = me.hornleft1
        hornleft2 = "none"
        hornleft3 = "none"
        dlh1 = True
        hornright1 = "none"
        hornright2 = "none"
        hornright3 = "none"
    if me.select == "TX":
        numhorns = 3
        dlh1 = True
        dlh2 = True
        dlh3 = True
        hornleft1 = me.hornleft1
        hornleft2 = me.hornleft2
        hornleft3 = me.hornleft3
        hornright1 = "none"
        hornright2 = "none"
        hornright3 = "none"
    if me.select == "XT":
        numhorns = 3
        hornleft1 = "none"
        hornleft2 = "none"
        hornleft3 = "none"
        drh1 = True
        drh2 = True
        drh3 = True
        hornright1 = me.hornright1
        hornright2 = me.hornright2
        hornright3 = me.hornright3
    if me.select == "DX":
        numhorns = 2
        dlh1 = True
        dlh2 = True
        hornleft1 = me.hornleft1
        hornleft2 = me.hornleft2
        hornleft3 = "none"
        hornright1 = "none"
        hornright2 = "none"
        hornright3 = "none"
    if me.select == "XD":
        numhorns = 2
        hornleft1 = "none"
        hornleft2 = "none"
        hornleft3 = "none"
        drh1 = True
        drh2 = True
        hornright1 = me.hornright1
        hornright2 = me.hornright2
        hornright3 = "none"
    if me.select == "XX":
        numhorns = 0
        hornleft1 = "none"
        hornleft2 = "none"
        hornleft3 = "none"
        hornright1 = "none"
        hornright2 = "none"
        hornright3 = "none"
    if numhorns == 22:  # If the troll has the default number of horns
        dlh1 = True
        drh1 = True
        hornleft1 = me.hornleft1    # Set to default.  This also covers when
        hornleft2 = "none"
        hornleft3 = "none"
        hornright1 = me.hornright1  # either of the genes given are "1"
        hornright2 = "none"
        hornright3 = "none"
        numhorns = 2
        # Now, if any of the genes are 2's or 3's, overwrite appropriately:
    if me.select[0] == "2":
        hornleft1 = me.hornleft2
    if me.select[0] == "3":
        hornleft1 = me.hornleft3
    if me.select[1] == "2":
        hornright1 = me.hornright2
    if me.select[1] == "3":
        hornright1 = me.hornright3
    # hornright1, hornright2, hornleft1, hornleft2, and numhorns know what we're describing.

    iconw = 33
    background = pygame.Surface(((iconw*6), (iconw * 4)))
    background.fill((0, 255, 255))
    background.set_colorkey((0, 255, 255))
    pos = 3*iconw
    if dlh3:
        img = hornprint(hornleft3, me.controls)
        img = pygame.transform.flip(img, 1, 0)
        background.blit(img, (pos-(3*iconw), 0))
    if dlh2:
        img = hornprint(hornleft2, me.controls)
        img = pygame.transform.flip(img, 1, 0)
        background.blit(img, (pos-(2*iconw), 0))
    if dlh1:
        img = hornprint(hornleft1, me.controls)
        img = pygame.transform.flip(img, 1, 0)
        background.blit(img, (pos-iconw, 0))
    if drh1:
        img = hornprint(hornright1, me.controls)
        background.blit(img, (pos, 0))
    if drh2:
        img = hornprint(hornright2, me.controls)
        background.blit(img, (pos+(1*iconw), 0))
    if drh3:
        img = hornprint(hornright3, me.controls)
        background.blit(img, (pos+(2*iconw), 0))

    return background


def hornarch(inhorn, angle):
    horn = gene.HornObj(inhorn)

    # By default, horns are S-shaped.
    imgloc = "arch4.PNG"
    # Overwrite with the actual curl data:
    if horn.curl == "1":
        imgloc = "arch1.PNG"
    if horn.curl == "2":
        imgloc = "arch2.PNG"
    if horn.curl == "3":
        imgloc = "arch3.PNG"
    if horn.curl == "4":
        imgloc = "arch4.PNG"
    if horn.curl == "5":
        imgloc = "arch5.PNG"
    if horn.curl == "6":
        imgloc = "arch6.PNG"
    if horn.curl == "7":
        imgloc = "arch7.PNG"
    if horn.curl == "8":
        imgloc = "arch8.PNG"

    # Length.  By default, length 1.
    x = 1
    if horn.length == "1":
        x = 0
    if horn.length == "2":
        x = 1
    if horn.length == "3":
        x = 2
    if horn.length == "4":
        x = 3

    # Angularity, by default, smooth.
    y = 0
    if angle == "S":
        y = 0
    if angle == "B":
        y = 1
    if angle == "A":
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


def hornradial(radial, wide, hollow):

    # By default, horns are solid.
    imgloc = "radialsolid.png"
    # Overwrite with the actual type:
    if hollow == "O":
        imgloc = "radialH1.png"
    if hollow == "o":
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
    if tip == "?" or tip == "?" or tip == "?":
        # List of tips on row 1.
        y = 1
    if tip == "?" or tip == "?" or tip == "?":
        # List of tips on row 2.
        y = 2

    # Rows
    x = 0
    if tip == "P" or tip == "P":
        # row 1
        x = 0
    if tip == "B" or tip == "B":
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
    #
    #
    return inhorn
