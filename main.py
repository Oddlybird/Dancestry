# Blank pygame program, based on Tom's Pong tutorial, courtesy of tomchance.uklinux.net
#
try:
    # Main Imports
    import sys
    import random
    import math
    import os
    import getopt
    import pygame
    import json
    from socket import *
    from pygame.locals import *
    # Parts of this project
    import colorgarbage as colg
    import formattingbs as fbs
    import genome as gene
    import slurry
    import names
    import graphics
    import traits
except ImportError:
    print("couldn't load module.")
    sys.exit(2)

# screens:  maketroll, loadingzone, bloodpage, donationpage,
# screens are named ""page, and their ScrPage objects are named page""
# to activate a new main menu button, go to btnselect(), drawmenu(),
# Pass colors around ONLY as tuples, except when communicating directly with pygame


class ScrPage:  # interface.  An item to be used to define the shape of menus.
    def __init__(self, setname="", setminbtn=0, setmaxbtn=0, setsubmenu=False, setexcmenu=False):
        self.name = setname
        self.minbtn = setminbtn
        self.maxbtn = setmaxbtn
        self.submenu = setsubmenu
        self.excmenu = setexcmenu


def main():  # Contains button functions
    gameon = True
    # Event loop
    while gameon:
        updatescreen()
        gameon = handlekeys(gameon)
    return 0


def handlekeys(gameon=True):
    # for event in pygame.event.get():
    global btncurrent, screencurrent, pageblood, pagename, pageloadtroll, pagemaketroll, pagemouf
    global troll1, troll2, troll3, libbie, lester, spectrum
    event = pygame.event.wait()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            if btncurrent < 9000:
                usedbuttons("-")
        if event.key == pygame.K_DOWN:
            if btncurrent < 9000:
                usedbuttons("+")
        if event.key == pygame.K_LEFT:
            if btncurrent < 9000:
                if btncurrent < 25:
                    if screencurrent == pagemaketroll or screencurrent == pageblood or screencurrent == pagename:
                        btncurrent = 51
                    if screencurrent == pageloadtroll:
                        btncurrent = screencurrent.maxbtn
                # if btncurrent > 25  #  If pressing left while in submenu..
                # Submenu stuff
        if event.key == pygame.K_RIGHT:
            if btncurrent > 25:
                btncurrent = 1
            # if btncurrent < 25
            # Pressing right, from main menu.
        if event.key == pygame.K_RETURN:
            # This is the loop for when someone chooses a button.
            if btncurrent == 1:  # Troll Breeding Screen
                screencurrent = pagemaketroll
                return gameon
            if btncurrent == 2:  # Screenshot current screen
                screenshot()
                return gameon
            if btncurrent == 3:  # Test out some names
                screencurrent = pagename
                return gameon
            if btncurrent == 4:  # Look in the save folder
                global loadablelist
                loadablelist = checkloadable()
                screencurrent = pageloadtroll
                return gameon
            if btncurrent == 5:  # Fiddle with hemospectrum
                screencurrent = pageblood
                # note : Change to 'eugenics' page once that's functional.
                return gameon
            if btncurrent == 6:  # Look at teeth norms
                screencurrent = pagemouf
                return gameon
            if btncurrent == 7:
                # code that makes the button do something
                return gameon
            if btncurrent == 8:
                # code that makes the button do something
                return gameon
            if btncurrent == 9:
                # code that makes the button do something
                return gameon
            if btncurrent == 10:
                # code that makes the button do something
                return gameon
            if btncurrent == 11:
                # code that makes the button do something
                return gameon
            if btncurrent == 12:
                gameon = False
                return gameon
            # End "main menu" portion of Enter loop.
            if btncurrent > 25:
                # NAME SCREEN BTNs
                if screencurrent.name == "namepage":
                    if btncurrent == 51:
                        # Btn 1 : Gen Some Names
                        global imgnamelist
                        imgnamelist = newnames()
                        updatescreen()
                        return gameon
                # TROLLMAKE SCREEN BTNs
                if screencurrent.name == "maketroll":
                    if btncurrent == 51:
                        # Btn 1 : Troll from parents
                        troll3 = gene.troll("blank")
                        troll3 = gene.trollgen("blend", spectrum, troll1, troll2)
                        updatescreen()
                        return gameon
                    if btncurrent == 52:
                        # Btn 2 : Troll from slurry
                        troll3 = gene.troll("blank")
                        troll3 = gene.trollgen("rand", spectrum)
                        updatescreen()
                        return gameon
                    if btncurrent == 53:
                        # Btn 3 : Put random default troll into slot 3
                        troll3 = gene.troll("blank")
                        troll3 = gene.getpremadetroll()
                        updatescreen()
                        return gameon
                    if btncurrent == 54:
                        # Btn 4 : Load troll3 into troll 1
                        troll1 = troll3
                        updatescreen()
                        return gameon
                    if btncurrent == 55:
                        # Btn 5 : Load troll3 into troll 2
                        troll2 = troll3
                        updatescreen()
                        return gameon
                    if btncurrent == 56:
                        # Btn 6 : Save troll3.troll
                        savetroll(troll3)
                        updatescreen()
                        return gameon
                    if btncurrent == 57:
                        # Btn 7 : Save troll1.png
                        savetrollpng(troll1)
                        updatescreen()
                        return gameon
                    if btncurrent == 58:
                        # Btn 8 : Save troll2.png
                        savetrollpng(troll2)
                        updatescreen()
                        return gameon
                    if btncurrent == 59:
                        # Btn 9 : Save troll3.png
                        savetrollpng(troll3)
                        updatescreen()
                        return gameon
                    if btncurrent == 60:
                        # Btn 10 : Put random default troll into slot 3
                        troll3 = gene.troll("blank")
                        troll3 = gene.trollgen("mutant", spectrum)
                        updatescreen()
                        return gameon
                    return gameon
                # BLOOD SCREEN BTNs
                if screencurrent == pageblood:
                    if btncurrent == 51:
                        # Btn 1 : Full Spectrum
                        spectrum = slurry.spectrumfull
                        spectrum.sort(key=gene.getcastenumstr, )
                        updatescreen()
                        return gameon
                    if btncurrent == 52:
                        # Btn 2 : Mini Spectrum
                        spectrum = slurry.spectrummini
                        spectrum.sort(key=gene.getcastenumstr, )
                        updatescreen()
                        return gameon
                    if btncurrent == 53:
                        # Btn 3 : Rando Spectrum
                        spectrum = gene.spectrumrand()
                        spectrum.sort(key=gene.getcastenumstr, )
                        updatescreen()
                        return gameon
                    if btncurrent == 54:
                        # Btn 4 : rustblood
                        spectrum = slurry.spectrumrust
                        spectrum.sort(key=gene.getcastenumstr, )
                        updatescreen()
                        return gameon
                    if btncurrent == 55:
                        # Btn 5 : greenblood
                        spectrum = slurry.spectrumgreens
                        spectrum.sort(key=gene.getcastenumstr, )
                        updatescreen()
                        return gameon
                    if btncurrent == 56:
                        # Btn 6 : blueblood
                        spectrum = slurry.spectrumblues
                        spectrum.sort(key=gene.getcastenumstr, )
                        updatescreen()
                        return gameon
                    if btncurrent == 57:
                        # Btn 7: purples
                        spectrum = slurry.spectrumpurples
                        spectrum.sort(key=gene.getcastenumstr, )
                        updatescreen()
                        return gameon
                    return gameon
                # Create a sub-menu here based off which other menu the cursor is in.
                return gameon
            # the loop for when someone presses enter to choose a button is over.
        if event.key == pygame.K_1:
            if screencurrent == pageloadtroll or screencurrent == pagemaketroll:
                # load currently selected troll into slot 1.
                troll1 = troll3
                return gameon
            return gameon
        if event.key == pygame.K_2:
            if screencurrent == pageloadtroll or screencurrent == pagemaketroll:
                # load currently selected troll into slot 2.
                troll2 = troll3
                return gameon
            return gameon
        if event.key == pygame.K_ESCAPE:
            gameon = False
            return gameon
    if event.type == QUIT:
        gameon = False
        return gameon
    return gameon


# Show what needs to be shown.
def updatescreen():  # interface.  Choose which page to show.
    global background
    background.fill((0, 0, 0))
    if screencurrent.name == "moufpage":
        background.blit(moufpage(), (0, 0))
    if screencurrent.name == "maketroll":
        background.blit(trollmakepage(), (0, 82))
    if screencurrent.name == "loadingzone":
        background.blit(loadingzone(), (0, 0))
    if screencurrent.name == "bloodpage":
        background.blit(bloodpage(), (0, 82))
    if screencurrent.name == "namepage":
        background.blit(namepage(), (0, 0))
    background = drawmenu(background)
    screen.blit(background, (0, 0))
    pygame.display.flip()
    return


def drawmenu(background):  # interface.  Contains Labels for all main and submenu buttons
    global screen_height, screen_width
    btnwbig = 190
    btnwsmall = 190
    btnhbig = 20
    btnhsmall = 20
    menubg = fbs.btn("Menu", 232, screen_height, (60, 60, 60), (255, 255, 255))

    txtcol = (50, 50, 0)
    btn01 = fbs.btn("     MAKE TROLL     ", btnwbig, btnhbig, btnselect(1), txtcol, True, "Verdana")
    btn02 = fbs.btn("     SCREENSHOT     ", btnwbig, btnhbig, btnselect(2), txtcol, True, "Verdana")
    btn03 = fbs.btn("        NAME        ", btnwbig, btnhbig, btnselect(3), txtcol, True, "Verdana")
    btn04 = fbs.btn("    LOADING AREA    ", btnwbig, btnhbig, btnselect(4), txtcol, True, "Verdana")
    btn05 = fbs.btn("    BLOOD COLORS    ", btnwbig, btnhbig, btnselect(5), txtcol, True, "Verdana")
    btn06 = fbs.btn("    CHECK TEETH     ", btnwbig, btnhbig, btnselect(6), txtcol, True, "Verdana")
    btn07 = fbs.btn("       Btn   7      ", btnwbig, btnhbig, btnselect(7), txtcol, True, "Verdana")
    btn08 = fbs.btn("       Btn   8      ", btnwbig, btnhbig, btnselect(8), txtcol, True, "Verdana")
    btn09 = fbs.btn("       Btn   9      ", btnwbig, btnhbig, btnselect(9), txtcol, True, "Verdana")
    btn10 = fbs.btn("       Btn  10      ", btnwbig, btnhbig, btnselect(10), txtcol, True, "Verdana")
    btn11 = fbs.btn("       Btn  11      ", btnwbig, btnhbig, btnselect(11), txtcol, True, "Verdana")
    btn12 = fbs.btn("       E X I T      ", btnwbig, btnhbig, btnselect(12), txtcol, True, "Verdana")

    menubg.blit(btn01, (16, 24))
    menubg.blit(btn02, (16, 72))
    menubg.blit(btn03, (16, 120))
    menubg.blit(btn04, (16, 168))
    menubg.blit(btn05, (16, 216))
    menubg.blit(btn06, (16, 264))
    menubg.blit(btn07, (16, 312))
    menubg.blit(btn08, (16, 360))
    menubg.blit(btn09, (16, 408))
    menubg.blit(btn10, (16, 456))
    menubg.blit(btn11, (16, 504))
    menubg.blit(btn12, (16, 552))
    background.blit(menubg, (screen_width - 232, 0))

    if screencurrent == pagemaketroll:
        btnA = fbs.btn("  Troll From Parents   ", btnwsmall, btnhsmall, btnselect(51), txtcol)
        btnB = fbs.btn("  Troll From Slurry    ", btnwsmall, btnhsmall, btnselect(52), txtcol)
        btnC = fbs.btn("  Rand.Normal to #3    ", btnwsmall, btnhsmall, btnselect(53), txtcol)
        btnD = fbs.btn("   Load #3 Into #1     ", btnwsmall, btnhsmall, btnselect(54), txtcol)
        btnE = fbs.btn("   Load #3 Into #2     ", btnwsmall, btnhsmall, btnselect(55), txtcol)
        btnF = fbs.btn("  Save slot3.troll     ", btnwsmall, btnhsmall, btnselect(56), txtcol)
        btnG = fbs.btn("    Save slot1.png     ", btnwsmall, btnhsmall, btnselect(57), txtcol)
        btnH = fbs.btn("    Save slot2.png     ", btnwsmall, btnhsmall, btnselect(58), txtcol)
        btnI = fbs.btn("    Save slot3.png     ", btnwsmall, btnhsmall, btnselect(59), txtcol)
        btnJ = fbs.btn("    Acquire Mutant     ", btnwsmall, btnhsmall, btnselect(60), txtcol)
        btnK = fbs.btn("", btnwsmall, btnhsmall, btnselect(61), txtcol)
        btnL = fbs.btn("", btnwsmall, btnhsmall, btnselect(62), txtcol)
        btnM = fbs.btn("", btnwsmall, btnhsmall, btnselect(63), txtcol)
        btnN = fbs.btn("", btnwsmall, btnhsmall, btnselect(64), txtcol)
        btnO = fbs.btn("", btnwsmall, btnhsmall, btnselect(65), txtcol)
        background.blit(btnA, (8, 12))
        background.blit(btnB, (8, 36))
        background.blit(btnC, (8, 60))
        background.blit(btnD, (200, 12))
        background.blit(btnE, (200, 36))
        background.blit(btnF, (200, 60))
        background.blit(btnG, (392, 12))
        background.blit(btnH, (392, 36))
        background.blit(btnI, (392, 60))
        background.blit(btnJ, (584, 12))
        background.blit(btnK, (584, 36))
        background.blit(btnL, (584, 60))
        background.blit(btnM, (776, 12))
        background.blit(btnN, (776, 36))
        background.blit(btnO, (776, 60))

    if screencurrent == pageblood:
        btnA = fbs.btn("     Full Spectrum    ", btnwsmall, btnhsmall, btnselect(51), txtcol)
        btnB = fbs.btn("     Mini Spectrum    ", btnwsmall, btnhsmall, btnselect(52), txtcol)
        btnC = fbs.btn("   Random Spectrum    ", btnwsmall, btnhsmall, btnselect(53), txtcol)
        btnD = fbs.btn("        Rusts         ", btnwsmall, btnhsmall, btnselect(54), txtcol)
        btnE = fbs.btn("        Greens        ", btnwsmall, btnhsmall, btnselect(55), txtcol)
        btnF = fbs.btn("        Blues         ", btnwsmall, btnhsmall, btnselect(56), txtcol)
        btnG = fbs.btn("       Purples        ", btnwsmall, btnhsmall, btnselect(57), txtcol)
        btnH = fbs.btn("                      ", btnwsmall, btnhsmall, btnselect(58), txtcol)
        btnI = fbs.btn("                      ", btnwsmall, btnhsmall, btnselect(59), txtcol)
        background.blit(btnA, (8, 12))
        background.blit(btnB, (8, 36))
        background.blit(btnC, (8, 60))
        background.blit(btnD, (200, 12))
        background.blit(btnE, (200, 36))
        background.blit(btnF, (200, 60))
        background.blit(btnG, (392, 12))
        background.blit(btnH, (392, 36))
        background.blit(btnI, (392, 60))

    if screencurrent == pagename:
        btnA = fbs.btn("      New Names       ", btnwsmall, btnhsmall, btnselect(51), txtcol)
        btnB = fbs.btn("                      ", btnwsmall, btnhsmall, btnselect(52), txtcol)
        btnC = fbs.btn("                      ", btnwsmall, btnhsmall, btnselect(53), txtcol)
        btnD = fbs.btn("                      ", btnwsmall, btnhsmall, btnselect(54), txtcol)
        btnE = fbs.btn("                      ", btnwsmall, btnhsmall, btnselect(55), txtcol)
        btnF = fbs.btn("                      ", btnwsmall, btnhsmall, btnselect(56), txtcol)
        btnG = fbs.btn("                      ", btnwsmall, btnhsmall, btnselect(57), txtcol)
        btnH = fbs.btn("                      ", btnwsmall, btnhsmall, btnselect(58), txtcol)
        btnI = fbs.btn("                      ", btnwsmall, btnhsmall, btnselect(59), txtcol)
        background.blit(btnA, (8, 12))
        background.blit(btnB, (8, 36))
        background.blit(btnC, (8, 60))
        background.blit(btnD, (200, 12))
        background.blit(btnE, (200, 36))
        background.blit(btnF, (200, 60))
        background.blit(btnG, (392, 12))
        background.blit(btnH, (392, 36))
        background.blit(btnI, (392, 60))
    return background


def btnselect(x):  # interface - controls which buttons are highlightable.
    # main menu and main submenu only
    global btncurrent, pagename, pageloadtroll, pageblood, pagemaketroll
    btncol = (255, 0, 0)
    if x == btncurrent:
        btncol = (200, 200, 0)
    if x != btncurrent:
        btncol = (120, 120, 0)

    # unused main menu buttons.
    if x == 7 or x == 8 or x == 9 or x == 10 or x == 11:  # Unused Buttons
        btncol = (50, 50, 0)

    # submenu buttons
    # A set of 20 or so working submenu buttons.
    if screencurrent.name == "donationpage":
        if x == 54 or x == 55 or x == 56 or x == 57 or x == 58 or x == 59 or x == 60:  # Unused Buttons
            btncol = (50, 50, 0)
        if x == 61 or x == 62 or x == 63 or x == 64 or x == 65 or x == 66 or x == 67 or x == 68 or x == 69 or x == 70:
            # Unused Buttons
            btncol = (50, 50, 0)
    if screencurrent.name == "maketroll":
        if x == 61 or x == 62 or x == 63 or x == 64 or x == 65 or x == 66 or x == 67 or x == 68 or x == 69 or x == 70:
            # Unused Buttons
            btncol = (50, 50, 0)
    if screencurrent == pageblood:
        if x == 58 or x == 59 or x == 60:  # Unused Buttons
            btncol = (50, 50, 0)
        if x == 61 or x == 62 or x == 63 or x == 64 or x == 65 or x == 66 or x == 67 or x == 68 or x == 69 or x == 70:
            # Unused Buttons
            btncol = (50, 50, 0)
    if screencurrent == pagename:
        if x == 54 or x == 55 or x == 56 or x == 57 or x == 58 or x == 59 or x == 60:  # Unused Buttons
            btncol = (50, 50, 0)
        if x == 61 or x == 62 or x == 63 or x == 64 or x == 65 or x == 66 or x == 67 or x == 68 or x == 69 or x == 70:
            # Unused Buttons
            btncol = (50, 50, 0)
    # just a ridiculous number of buttons.
    if screencurrent == pageloadtroll:
        if x > screencurrent.maxbtn:
            btncol = (50, 50, 0)
    return btncol


def usedbuttons(direction):  # interface
    global btncurrent, screencurrent
    # Main Menu
    if btncurrent < 25:
        if direction == "+":
            btncurrent = btncurrent + 1
            while btnselect(btncurrent) == (50, 50, 0):
                btncurrent = btncurrent + 1
        if direction == "-":
            btncurrent = btncurrent - 1
            while btnselect(btncurrent) == (50, 50, 0):
                btncurrent = btncurrent - 1
        # loop main menu
        if btncurrent > 12:
            btncurrent = 1
        if btncurrent < 1:
            btncurrent = 12
    # Submenu.
    if btncurrent > 25:
        if direction == "+":
            btncurrent = btncurrent + 1
        if direction == "-":
            btncurrent = btncurrent - 1
        if btncurrent == screencurrent.maxbtn + 1:
            btncurrent = screencurrent.minbtn
        if btncurrent == screencurrent.minbtn - 1:
            btncurrent = screencurrent.maxbtn
    return


# save and load to file.
def savetroll(grub):  # interface     Save Troll
    castenum = gene.getcastenumstr(grub["blood"])
    saveloc = "Caverns/CaveB/" + castenum + "." + grub["firname"] + "." + grub["surname"] + "." + grub["blood"] + ".troll"
    c = 1
    int(c)
    while os.path.exists(saveloc):
        c = c + 1
        d = str(c)
        saveloc = "Caverns/CaveB/" + castenum + "." + grub["firname"] + "." + grub["surname"] + "." + grub["blood"] + "." + d + ".troll"
    savedtroll = open(saveloc, "wt")
    y = json.dumps(grub, indent=4)
    savedtroll.write(y)
    savedtroll.close()
    return


def loadtroll(filename):  # interface     Load Troll
    trollobj = gene.troll("blank")
    savedtroll = "Caverns/AncestralCave/" + filename + ".troll"
    if os.path.exists(savedtroll):
        loadedtroll = open(savedtroll, "rt")
        y = loadedtroll.read()
        trollobj = json.loads(y)
        loadedtroll.close()
    if trollobj["savetype"] != "12":
        trollobj = gene.troll("blank")
    return trollobj


def savimg(img, filename):
    pix = img
    saveloc = filename[0:len(filename)-4]
    extension = filename[len(filename)-3:len(filename)]
    c = 1
    filename2 = filename
    while os.path.exists(filename2):
        c = c + 1
        d = str(c)
        filename2 = saveloc + d + "." + extension
    pygame.image.save(pix, filename2)
    return


def savetrollpng(grub):
    castenum = gene.getcastenumstr(grub["blood"])
    saveloc = castenum + "." + grub["firname"] + "." + grub["surname"] + "." + grub["blood"] + ".PNG"
    c = 1
    int(c)
    while os.path.exists(saveloc):
        c = c + 1
        d = str(c)
        saveloc = castenum + "." + grub["firname"] + "." + grub["surname"] + "." + grub["blood"] + "." + d + ".PNG"
    pix = displaytroll(grub)
    savimg(pix, saveloc)
    return


def screenshot():
    global background
    pix = background
    saveloc = "screenshot.PNG"
    savimg(pix, saveloc)
    return


# items that get printed to screen a Lot.  Like trolls, donations, blood colors...
def displaytroll(t0):  # interface -- prints a standard-format window display to the screen.
    # called when screencurrent.name = "maketroll"
    # behind-the-scenes-logic to find things out
    blood = t0["blood"][0:2]
    colbg = colg.bloodtorgb(t0["blood"])
    colfg = (255, 255, 255)
    h = t0["height"]
    t0["heightstr"] = gene.heightstr(h)
    seatemp = t0["sea"]
    # t0["seadesc"] = gene.describesea(blood, seatemp)
    t0["dwell"] = gene.describedwell(seatemp)
    t0["caste"] = gene.getcastefromblood(blood)
    castedefaultheight = slurry.spectrumheight[blood]
#    seawrap = fbs.wordwrap2(t0["seadesc"], 60)
    statmain = t0["stats"]["statmain"]
    statmax = t0["stats"]["statmax"]
    statsec = t0["stats"]["statsecret"]

    # Get actual graphics
    background = fbs.btn("", 512, 260, colbg, colfg)  # Background of trolldisplay chunk
    x = 0
    y = 0
    img, horndescr = trollimg(t0)   # Get Horns
    background.blit(img, (308, 0))  # Print Horns

    # Text string definition
    string1 = t0["firname"] + " " + t0["surname"] + ", " + t0["blood"] + " " + t0["sex"]
    string2 = t0["caste"] + ", " + t0["dwell"]
    string3 = t0["donator1"] + " / " + t0["donator2"]
    string4 = t0["heightstr"] + "/" + gene.heightstr(castedefaultheight) + ", " + t0["build"] + " build, "
    string5 = t0["hair"] + " hair, " + t0["skin"] + " skin"
    string6 = "."  # seawrap[0]
    string7 = "."  # "  " + seawrap[1]
    string8 = "."  # "  " + seawrap[2]
    string9 = "."  # "  " + seawrap[3]
    string10 = t0["stats"]["aspect"] + ", " + t0["powers"]
    string11 = "Horns: " + horndescr

    string12 = "Clout: " + str(statmain["clout"]) + "/" + str(statmax["clout"]) + " "
    string12 = string12 + "Grit: " + str(statmain["grit"]) + "/" + str(statmax["grit"]) + " "
    string12 = string12 + "Hunch: " + str(statmain["hunch"]) + "/" + str(statmax["hunch"]) + " "
    string12 = string12 + "Moxie: " + str(statmain["moxie"]) + "/" + str(statmax["moxie"]) + " "

    string13 = "Acumen: " + str(statmain["acumen"]) + "/" + str(statmax["acumen"]) + " "
    string13 = string13 + "Alacrity: " + str(statmain["alacrity"]) + "/" + str(statmax["alacrity"]) + " "
    string13 = string13 + "Resolve: " + str(statmain["resolve"]) + "/" + str(statmax["resolve"]) + " "
    string13 = string13 + "Psyche: " + str(statmain["psyche"]) + "/" + str(statmax["psyche"]) + " "

    string14 = "Faith: " + str(statsec["faith"])
    string14 = string14 + " Order: " + str(statsec["order"])
    string14 = string14 + " Entropy: " + str(statsec["entropy"])
    string14 = string14 + " Connection: " + str(statsec["connection"])
    string14 = string14 + " Self: " + str(statsec["self"])
    string14 = string14 + " Luck: " + str(statsec["luck"])

    string15 = "dpts: " + str(t0["stats"]["dpts"])
    string16 = "."
    string17 = "Sea:   " + t0["sea"]
    string18 = "Horns: " + t0["horns"]
    string19 = "Mouth: " + t0["mouth"][0:40]
    string20 = "Mouth: " + "      " + t0["mouth"][40:len(t0["mouth"])]

    # Print text to screen.
    textheight = 12
    background.blit(fbs.say(string1, colfg, 16, True), (x + 32, y))
    background.blit(fbs.say(string2, colfg), (x + 16, y + 2*textheight))
    background.blit(fbs.say(string3, colfg), (x + 16, y + 3*textheight))
    background.blit(fbs.say(string4, colfg), (x + 16, y + 4*textheight))
    background.blit(fbs.say(string5, colfg), (x + 16, y + 5*textheight))
    background.blit(fbs.say(string6, colfg), (x + 16, y + 6*textheight))
    background.blit(fbs.say(string7, colfg), (x + 16, y + 7*textheight))
    background.blit(fbs.say(string8, colfg), (x + 16, y + 8*textheight))
    background.blit(fbs.say(string9, colfg), (x + 16, y + 9*textheight))
    background.blit(fbs.say(string10, colfg), (x + 16, y + 10*textheight))
    background.blit(fbs.say(string11, colfg), (x + 16, y + 11*textheight))
    background.blit(fbs.say(string12, colfg), (x + 16, y + 12*textheight))
    background.blit(fbs.say(string13, colfg), (x + 16, y + 13*textheight))
    background.blit(fbs.say(string14, colfg), (x + 16, y + 14*textheight))
    background.blit(fbs.say(string15, colfg), (x + 16, y + 15*textheight))
    background.blit(fbs.say(string16, colfg), (x + 16, y + 16*textheight))
    background.blit(fbs.say(string17, colfg), (x + 16, y + 17*textheight))
    background.blit(fbs.say(string18, colfg), (x + 16, y + 18*textheight))
    background.blit(fbs.say(string19, colfg), (x + 16, y + 19*textheight))
    background.blit(fbs.say(string20, colfg), (x + 16, y + 20*textheight))
    return background


def trollimg(t0):
    #Basic logic
    blood = t0["blood"][0:2]
    colbg = colg.bloodtorgb(t0["blood"])
    colfg = (255, 255, 255)

    # Graphics-related logic
    jawprint = graphics.jawprint(t0["mouth"])
    jawprint2 = graphics.jawprint(t0["mouth"], True)
    hornsprint, horndescr = graphics.hornsprint(t0["horns"])

    background = fbs.btn("", 204, 260, colbg, colfg)
    midpt = 102
    x = 0
    y = 0
    background.blit(jawprint, (midpt - 90, 8))
    background.blit(jawprint2, (midpt, 8))
    background.blit(hornsprint, (0, 30))
    return background, horndescr


# The display for individual screens.
def trollmakepage():  # interface
    global troll1, troll2, troll3, screen_height, screen_width
    page = fbs.btn("", screen_width - 232, screen_height - 60, (0, 0, 0), (255, 255, 255))
    page.blit(displaytroll(troll1), (8, 0))
    page.blit(displaytroll(troll2), (8, 264))
    page.blit(displaytroll(troll3), (528, 120))
    return page


# Just for the mouf screen...
def displaybigdefaultmouf(blood):
    global font
    page = fbs.pysurface(170, 42, (0, 0, 0))
    jawprint = graphics.jawprint(slurry.genemouth(blood))

    page.blit(pygame.transform.scale2x(jawprint), (0, 0))
    page.blit(font.render(blood, 1, colg.bloodtorgb(blood)), (0, 10))
    return page


# Testing ground for showing all the default teef.
def moufpage():
    global screen_height, screen_width, font
    page = fbs.pysurface(screen_width, screen_height, (0, 0, 0))
    font = pygame.font.SysFont("Verdana", 16, True, False)
    page.blit(displaybigdefaultmouf("RR"), (50, 50))
    page.blit(displaybigdefaultmouf("Rr"), (50, 125))
    page.blit(displaybigdefaultmouf("rr"), (50, 200))
    page.blit(displaybigdefaultmouf("rG"), (50, 275))
    page.blit(displaybigdefaultmouf("RG"), (50, 350))
    page.blit(displaybigdefaultmouf("Rg"), (50, 425))
    page.blit(displaybigdefaultmouf("rg"), (50, 500))

    page.blit(displaybigdefaultmouf("GG"), (300, 50))
    page.blit(displaybigdefaultmouf("Gg"), (300, 125))
    page.blit(displaybigdefaultmouf("gg"), (300, 200))
    page.blit(displaybigdefaultmouf("Gb"), (300, 275))
    page.blit(displaybigdefaultmouf("GB"), (300, 350))
    page.blit(displaybigdefaultmouf("gB"), (300, 425))
    page.blit(displaybigdefaultmouf("gb"), (300, 500))

    page.blit(displaybigdefaultmouf("BB"), (550, 50))
    page.blit(displaybigdefaultmouf("Bb"), (550, 125))
    page.blit(displaybigdefaultmouf("bb"), (550, 200))
    page.blit(displaybigdefaultmouf("rB"), (550, 275))
    page.blit(displaybigdefaultmouf("RB"), (550, 350))
    page.blit(displaybigdefaultmouf("Rb"), (550, 425))
    page.blit(displaybigdefaultmouf("rb"), (550, 500))

    page.blit(pygame.transform.scale2x(graphics.jawprint(slurry.genemouth("high"))), (800, 50))
    page.blit(font.render("high", 1, colg.bloodtorgb("BB")), (800, 60))
    page.blit(pygame.transform.scale2x(graphics.jawprint(slurry.genemouth("low"))), (800, 125))
    page.blit(font.render("low", 1, colg.bloodtorgb("RR")), (800, 135))
    page.blit(pygame.transform.scale2x(graphics.jawprint(slurry.genemouth("allG"))), (800, 200))
    page.blit(font.render("allG", 1, colg.bloodtorgb("rg")), (800, 210))
    page.blit(pygame.transform.scale2x(graphics.jawprint(slurry.genemouth("allC"))), (800, 275))
    page.blit(font.render("allC", 1, colg.bloodtorgb("rg")), (800, 285))
    page.blit(pygame.transform.scale2x(graphics.jawprint(slurry.genemouth("allP"))), (800, 350))
    page.blit(font.render("allP", 1, colg.bloodtorgb("rg")), (800, 360))
    page.blit(pygame.transform.scale2x(graphics.jawprint(slurry.genemouth("length1"))), (800, 425))
    page.blit(font.render("length1", 1, colg.bloodtorgb("rg")), (800, 435))
    page.blit(pygame.transform.scale2x(graphics.jawprint(slurry.genemouth("sym1"))), (800, 500))
    page.blit(font.render("sym1", 1, colg.bloodtorgb("rg")), (800, 510))
    font = pygame.font.SysFont("Verdana", 12, False, False)
    return page


# Blood color examples and spectrum slice selection
def bloodpage():
    global screen_height, screen_width
    page = fbs.btn("", screen_width - 263, screen_height - 60, (0, 0, 0), (255, 255, 255))
    global spectrum
    z = spectrum
    spectrum.sort(key=gene.getcastenumstr, )
    h = 0
    w = 1
    numtotal = 0
    for x in z:
        if numtotal == 16 or numtotal == 32 or numtotal == 48 or numtotal == 64 or numtotal == 80 or numtotal == 96 or numtotal == 112 or numtotal == 128 or numtotal == 144:
            w = w + 13
            h = 0
        h = h + 3
        displayname = x
        (rgb1, rgb2, rgb3) = colg.bloodtorgb(x)
        displaycol = (rgb1, rgb2, rgb3)
        castename = gene.getcastefromcolor(rgb1, rgb2, rgb3)
        btn = fbs.btn(displayname + " " + castename, 100, 20, displaycol, (255, 255, 255), False)
        page.blit(btn, (w*8, h*10))
        numtotal = numtotal + 1
    return page


def namepage():
    global imgnamelist
    page = imgnamelist
    return page


def newnames():
    global screen_height, screen_width
    page = fbs.btn("", screen_width, screen_height, (0, 0, 0), (255, 255, 255))
    x = 12
    y = 10
    a = 0
    while a < 330:
        t0 = names.newname()
        a = a + 1
        y = y + 1
        page.blit(fbs.say(t0, (255, 255, 255)), (x*8, y*12))
        if a == 30 or a == 60 or a == 90 or a == 120 or a == 150 or a == 180 or a == 210 or a == 240 or a == 270 or a == 300 or a == 330:
            x = x + 10
            y = 10
    return page


def loadingzone():
    global loadablelist
    page = loadablelist
    return page


def checkloadable():
    # Make a basic page with some text on it
    global screen_height, screen_width
    page = fbs.btn("", screen_width, screen_height, (0, 0, 0), (255, 255, 255))
    page.blit(fbs.say("Arrow keys to navigate", (255, 255, 255)), (3 * 8, 2 * 12))
    page.blit(fbs.say("Press 1 to load to slot 1", (255, 255, 255)), (3 * 8, 3 * 12))
    page.blit(fbs.say("Press 2 to load to slot 2", (255, 255, 255)), (3 * 8, 4 * 12))
    # Initialize variables
    global pageloadtroll
    z = os.listdir("Caverns/AncestralCave/")
    castlist = [""]
    h = 7
    w = 1
    numtotal = 0
    # Load names into cast list.
    for arb in z:
        temp = arb
        if 20 < len(temp) < 35:
            if temp[3] == "." and temp[5] == "." and temp[12] == "." and temp[19] == ".":
                castlist.insert(numtotal, temp)
                numtotal = numtotal + 1
    numtotal = 0
    # Print out the data onto the page
    for arb in castlist:
        temp = arb
        if 20 < len(temp) < 35:
            if temp[3] == "." and temp[5] == "." and temp[12] == "." and temp[19] == ".":
                numtotal = numtotal + 1
                if numtotal == 21 or numtotal == 41 or numtotal == 61 or numtotal == 81 or numtotal == 101 or numtotal == 121 or numtotal == 141:
                    w = w + 16
                    h = 7
                h = h + 2
                bloodcol = temp[20:23]
                if bloodcol[2] == ".":
                    bloodcol = temp[20:22]
                displaycol = colg.bloodtorgb(bloodcol)
                displayname = temp[6] + "." + temp[13:19] + ", " + bloodcol
                guy = fbs.btn(displayname, 16*8, 2*12, displaycol, (255, 255, 255), False)
                page.blit(guy, (w*8, h*12))
    pageloadtroll.maxbtn = numtotal + 100
    # pageloadtroll artificial maxbtn limiter
    if pageloadtroll.maxbtn > 360:
        pageloadtroll.maxbtn = 360
    pageloadtroll.minbtn = 101
    global screencurrent
    return page

# Gamestart
# GLOBALS

# Project-specific globals, Menu/misc
screen_width = 1280
screen_height = 600
versionnum = "0.3.1"
btncurrent = 1
screencurrent = ScrPage()
# screens: maketroll, loadingzone, bloodpage, donationpage,
pageloadtroll = ScrPage("loadingzone", 101, 360, False, True)  # There is an artificial maxbtn limiter in loadtroll()
pagemaketroll = ScrPage("maketroll", 51, 60, True, False)
pageblood = ScrPage("bloodpage", 51, 57, True, False)
pagename = ScrPage("namepage", 51, 53, True, False)
pagemouf = ScrPage("moufpage", 51, 55, False, False)
# Project-specific globals, Data
libbie = gene.getpremadetroll(random.randint(1, 13))
sametroll = True
while sametroll:
    lester = gene.getpremadetroll(random.randint(1, 13))
    if lester != libbie:
        sametroll = False
troll1 = libbie
troll2 = lester
troll3 = gene.troll("blank")
trollblank = gene.troll("blank")
spectrum = slurry.spectrumfull

# Initialize pygame and graphics window
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
background = fbs.pysurface(screen_width, screen_height, (0, 0, 0))
imgnamelist = fbs.btn("", 1048, screen_height, (0, 0, 0), (255, 255, 255))
loadablelist = fbs.btn("", 1048, screen_height, (0, 0, 0), (255, 255, 255))
# Ready text                              Bold   Italic
font = pygame.font.SysFont("Verdana", 12, False, False)
pygame.display.set_caption("Dancestry " + versionnum)

# Invoke Main
if __name__ == '__main__':
    main()
