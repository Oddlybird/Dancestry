import json
import os
import trolldeets as deets
import libtcodpy as tcod
import names
import colorgarbage as colg
import slurry
import genome as gene
import formattingbs as fbs
# getcastefromblood(b) is a function you can use to get the plaintext of a caste.  Put in the blood-code.
# Will be tagging each function / class / etc
# If I ever figure out modules, that will be which modules they go in.
# tags so far:  #trolldeets, #interface,
# screens:  maketroll, loadingzone, bloodpage, donationpage,
# screens are named ""page, and their ScrPage objects are named page""
# to activate a new main menu button, go to btnselect(), drawmenu(),

# have Trolls (one contributor)
# have Slurries (An array of trolls + genes, with some meta-data)

# Pass colors around ONLY as tuples.  Only use tcod.Color when giving a command directly to tcod.


class ScrPage:  # interface.  An item to be used to define the shape of menus.
    def __init__(self, setname="", setminbtn=0, setmaxbtn=0, setsubmenu=False, setexcmenu=False):
        self.name = setname
        self.minbtn = setminbtn
        self.maxbtn = setmaxbtn
        self.submenu = setsubmenu
        self.excmenu = setexcmenu


# main loop.
def main():  # main / interface
    # onprogramload()
    while not tcod.console_is_window_closed():
        updatescreen()
        exitcase = handle_keys()
        if exitcase:
            break
    return


# Show what needs to be shown.
def updatescreen():  # interface.  Choose which page to show.
    tcod.console_clear(0)
    tcod.console_set_default_foreground(0, tcod.Color(250, 250, 200))
    tcod.console_set_default_background(0, tcod.black)

    if screencurrent.name == "maketroll":
        trollmakepage()
    if screencurrent.name == "loadingzone":
        loadingzone()
    if screencurrent.name == "bloodpage":
        bloodpage()
    if screencurrent.name == "namepage":
        namepage()
    drawmenu()
    tcod.console_flush()
    return


def drawmenu():  # interface.  Contains Labels for all main and submenu buttons.
    tcod.console_print_frame(0, 131, 0, 29, 50, True, 13, "MENU")
    tcod.console_set_color_control(0, tcod.white, tcod.Color(60, 60, 60))
    txtcol = (50, 50, 0)
    # Can add a tcod.Color(rrr,ggg,bbb) for:  drawbtn(x,y,"label",background,foreground)
    drawbtn(133, 2,  "     MAKE TROLL     ", btnselect(1), txtcol)
    drawbtn(133, 6,  "        SAVE        ", btnselect(2), txtcol)
    drawbtn(133, 10, "        NAME        ", btnselect(3), txtcol)
    drawbtn(133, 14, "    LOADING AREA    ", btnselect(4), txtcol)
    drawbtn(133, 18, "    BLOOD COLORS    ", btnselect(5), txtcol)
    drawbtn(133, 22, "       Btn   6      ", btnselect(6), txtcol)
    drawbtn(133, 26, "       Btn   7      ", btnselect(7), txtcol)
    drawbtn(133, 30, "       Btn   8      ", btnselect(8), txtcol)
    drawbtn(133, 34, "       Btn   9      ", btnselect(9), txtcol)
    drawbtn(133, 38, "       Btn  10      ", btnselect(10), txtcol)
    drawbtn(133, 42, "       Btn  11      ", btnselect(11), txtcol)
    drawbtn(133, 46, "       E X I T      ", btnselect(12), txtcol)
    # reset defaults
    tcod.console_set_color_control(0, tcod.black, tcod.white)

    if screencurrent == pagemaketroll:
        drawsmallbtn(1, 1,  "  Troll From Parents  ", btnselect(51), txtcol)
        drawsmallbtn(1, 3,  "  Troll From Slurry   ", btnselect(52), txtcol)
        drawsmallbtn(1, 5,  "        Save          ", btnselect(53), txtcol)
        drawsmallbtn(25, 1, "   Load Into Slot 1   ", btnselect(54), txtcol)
        drawsmallbtn(25, 3, "   Load Into Slot 2   ", btnselect(55), txtcol)
        drawsmallbtn(25, 5, "                      ", btnselect(56), txtcol)
        drawsmallbtn(49, 1, "                      ", btnselect(57), txtcol)
        drawsmallbtn(49, 3, "                      ", btnselect(58), txtcol)
        drawsmallbtn(49, 5, "                      ", btnselect(59), txtcol)

    if screencurrent == pageblood:
        drawsmallbtn(1, 1,  "     Full Spectrum    ", btnselect(51), txtcol)
        drawsmallbtn(1, 2,  "     Mini Spectrum    ", btnselect(52), txtcol)
        drawsmallbtn(1, 3,  "   Random Spectrum    ", btnselect(53), txtcol)
        drawsmallbtn(25, 1, "        Rusts         ", btnselect(54), txtcol)
        drawsmallbtn(25, 2, "        Greens        ", btnselect(55), txtcol)
        drawsmallbtn(25, 3, "        Blues         ", btnselect(56), txtcol)
        drawsmallbtn(50, 1, "       Purples        ", btnselect(57), txtcol)
        drawsmallbtn(50, 2, "                      ", btnselect(58), txtcol)
        drawsmallbtn(50, 3, "                      ", btnselect(59), txtcol)

    return


# make the menu buttons selectable
def btnselect(x):  # interface - controls which buttons are highlightable.
    # main menu and main submenu only
    global btncurrent, pagename, pageloadtroll, pageblood, pagemaketroll
    btncol = (255, 0, 0)
    if x == btncurrent:
        btncol = (200, 200, 0)
    if x != btncurrent:
        btncol = (120, 120, 0)

    # unused main menu buttons.
    if x == 6 or x == 7 or x == 8 or x == 9 or x == 10 or x == 11:  # Unused Buttons
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
        if x == 56 or x == 57 or x == 58 or x == 59 or x == 60:  # Unused Buttons
            btncol = (50, 50, 0)
        if x == 61 or x == 62 or x == 63 or x == 64 or x == 65 or x == 66 or x == 67 or x == 68 or x == 69 or x == 70:
            # Unused Buttons
            btncol = (50, 50, 0)
    if screencurrent == pageblood:
        if x == 58 or x == 59 or x == 60:  # Unused Buttons
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


def handle_keys():  # interface - button functions, and loops as needed.
    global btncurrent, screencurrent, pageblood, pagename, pageloadtroll, pagemaketroll
    global troll1, troll2, troll3, libbie, lester, spectrum
    key = tcod.console_wait_for_keypress(True)
    if tcod.console_is_key_pressed(tcod.KEY_UP):
        if btncurrent < 9000:
            usedbuttons("-")
    if tcod.console_is_key_pressed(tcod.KEY_DOWN):
        if btncurrent < 9000:
            usedbuttons("+")
    if tcod.console_is_key_pressed(tcod.KEY_LEFT):
        if btncurrent < 25:
            if screencurrent == pagemaketroll or screencurrent == pageblood:
                btncurrent = 51
            if screencurrent == pageloadtroll:
                btncurrent = screencurrent.maxbtn
    #  if btncurrent > 25:
    # submenu stuff  Pressing left while on a submenu
    if tcod.console_is_key_pressed(tcod.KEY_RIGHT):
        if btncurrent > 25:
            btncurrent = 1
    #  if btncurrent < 25:
    # Pressing right while on the main menu

    if tcod.console_is_key_pressed(tcod.KEY_ENTER):
        # This is the loop for when someone chooses a button.
        if btncurrent == 1:
            screencurrent = pagemaketroll
            return False
        if btncurrent == 2:
            if screencurrent == pagemaketroll:
                savetroll(troll3)
                draw(73, 20, "Saved")
                return False
        if btncurrent == 3:
            screencurrent = pagename
            return False
        if btncurrent == 4:
            screencurrent = pageloadtroll
            return False
        if btncurrent == 5:
            screencurrent = pageblood
            # note : Change to 'eugenics' page once that's functional.
            return False
        if btncurrent == 6:
            # code
            return False
        if btncurrent == 7:
            # code that makes the button do something
            return False
        if btncurrent == 8:
            # code that makes the button do something
            return False
        if btncurrent == 9:
            # code that makes the button do something
            return False
        if btncurrent == 10:
            # code that makes the button do something
            return False
        if btncurrent == 11:
            # code that makes the button do something
            return False
        if btncurrent == 12:
            return True
        # End "main menu" portion of Enter loop.
        if btncurrent > 25:
            # TROLLMAKE SCREEN BTNs
            if screencurrent.name == "maketroll":
                if btncurrent == 51:
                    # Btn 1 : Troll from parents
                    troll3 = gene.trollobj()
                    troll3 = deets.blendtroll(troll1, troll2)
                    updatescreen()
                    return False
                if btncurrent == 52:
                    # Btn 2 : Troll from slurry
                    troll3 = gene.trollobj()
                    troll3 = deets.slurrytroll(spectrum)
                    updatescreen()
                    return False
                if btncurrent == 53:
                    # Btn 3 : Save.
                    savetroll(troll3)
                    draw(73, 20, "Saved")
                    return False
                if btncurrent == 54:
                    # Btn 4 : Load into troll 1
                    troll1 = troll3
                    updatescreen()
                    return False
                if btncurrent == 55:
                    # Btn 5 : Load into troll 2
                    troll2 = troll3
                    updatescreen()
                    return False
                return False
            # TROLLMAKE SCREEN BTNs
            if screencurrent == pageblood:
                if btncurrent == 51:
                    # Btn 1 : Full Spectrum
                    spectrum = slurry.spectrumfull
                    spectrum.sort(key=deets.getcastenumstr,)
                    updatescreen()
                    return False
                if btncurrent == 52:
                    # Btn 2 : Mini Spectrum
                    spectrum = slurry.spectrummini
                    spectrum.sort(key=deets.getcastenumstr,)
                    updatescreen()
                    return False
                if btncurrent == 53:
                    # Btn 3 : Rando Spectrum
                    spectrum = slurry.spectrumrand()
                    spectrum.sort(key=deets.getcastenumstr,)
                    updatescreen()
                    return False
                if btncurrent == 54:
                    # Btn 4 : rustblood
                    spectrum = slurry.spectrumrust
                    spectrum.sort(key=deets.getcastenumstr,)
                    updatescreen()
                    return False
                if btncurrent == 55:
                    # Btn 5 : greenblood
                    spectrum = slurry.spectrumgreens
                    spectrum.sort(key=deets.getcastenumstr,)
                    updatescreen()
                    return False
                if btncurrent == 56:
                    # Btn 6 : blueblood
                    spectrum = slurry.spectrumblues
                    spectrum.sort(key=deets.getcastenumstr,)
                    updatescreen()
                    return False
                if btncurrent == 57:
                    # Btn 7: purples
                    spectrum = slurry.spectrumpurples
                    spectrum.sort(key=deets.getcastenumstr,)
                    updatescreen()
                    return False
                return False
            # Create a sub-menu here based off which other menu the cursor is in.
            return False
        # the loop for when someone presses enter to choose a button is over.
    if tcod.console_is_key_pressed(tcod.KEY_1):
        if screencurrent == pageloadtroll or screencurrent == pagemaketroll:
            # load currently selected troll into slot 1.
            troll1 = troll3
            return False
        return False
    if tcod.console_is_key_pressed(tcod.KEY_2):
        if screencurrent == pageloadtroll or screencurrent == pagemaketroll:
            # load currently selected troll into slot 2.
            troll2 = troll3
            return False
        return False

    elif key.vk == tcod.KEY_ESCAPE:
        # reenable the above line to make hitting escape close the program.
        return True


# save and load to file.
def savetroll(grub):  # interface     Save Troll
    castenum = deets.getcastenumstr(grub["blood"])
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
    trollobj = gene.trollobj()
    savedtroll = "Caverns/AncestralCave/" + filename + ".troll"
    if os.path.exists(savedtroll):
        loadedtroll = open(savedtroll, "rt")
        y = loadedtroll.read()
        trollobj = json.loads(y)
        loadedtroll.close()
    if trollobj["savetype"] != "5":
        trollobj = gene.trollobj()
    return trollobj


# menu-related boxen.
def drawbtn(x, y, label="", btncolor=(255, 255, 225), txtcolor=(50, 50, 0)):  # interface
    rectolor(x, y, 24, 2, btncolor, txtcolor)
    draw(x + 2, y + 1, label)
    return


def drawsmallbtn(x, y, label="", btncolor=(255, 255, 225), txtcolor=(50, 50, 0)):  # interface
    rectolor(x, y, 21, 0, btncolor, txtcolor)
    draw(x, y, label)
    return


def rectolor(x, y, ww, hh, btncolor=(255, 255, 225), txtcolor=(0, 0, 0)):  # interface
    h = 0
    w = 0
    (btnr, btng, btnb) = btncolor
    btnr = round(btnr)
    btng = round(btng)
    btnb = round(btnb)
    (txtr, txtg, txtb) = txtcolor
    txtr = round(txtr)
    txtg = round(txtg)
    txtb = round(txtb)
    while h <= hh:
        while w <= ww:
            tcod.console_set_char_background(0, x + w, y + h, tcod.Color(btnr, btng, btnb), tcod.BKGND_SET)
            tcod.console_set_char_foreground(0, x + w, y + h, tcod.Color(txtr, txtg, txtb))
            w = w + 1
        w = 0
        h = h + 1
    return


def draw(x, y, thing):  # interface
    # draws foreground text, no color specified.
    tcod.console_print(0, x, y, thing)
    return


# items that get printed to screen a Lot.  Like trolls, donations, blood colors...
def displaytroll(x, y, t0):  # interface -- prints a standard-format window display to the screen.
    # set some defaults
    # called when screencurrent.name = "maketroll"
    blood = t0["blood"][0:2]
    colbg = colg.bloodtorgb(t0["blood"])
    colfg = (255, 255, 255)
    hornl1 = t0["hornL"]
    hornr1 = t0["hornR"]
    hornl2 = gene.HornObj(hornl1)
    hornr2 = gene.HornObj(hornr1)
    t0["hornLdesc"] = hornl2.desc()
    t0["hornRdesc"] = hornr2.desc()
    h = t0["height"]
    t0["heightstr"] = deets.heightstr(h)
    seatemp = t0["sea"]
    t0["seadesc"] = deets.describesea(blood, seatemp)
    t0["dwell"] = deets.describedwell(seatemp)
    t0["caste"] = deets.getcastefromblood(blood)
    castedefaultheight = slurry.heightspectrum[blood]
    seawrap = fbs.wordwrap2(t0["seadesc"], 60)
    rectolor(x, y, 64, 20, colbg, colfg)
    string1 = t0["firname"] + " " + t0["surname"] + ", " + t0["blood"] + " " + t0["sex"]
    string2 = t0["caste"] + ", " + t0["powers"]
    string3 = t0["donator1"] + " / " + t0["donator2"]
    string4 = t0["heightstr"] + "/" + deets.heightstr(castedefaultheight) + ", " + t0["build"] + " build"
    string5 = t0["dwell"]
    string6 = "LHorn: " + t0["hornLdesc"]
    string7 = "RHorn: " + t0["hornRdesc"]
    string8 = t0["sea"]
    string9 = seawrap[0]
    string10 = "  " + seawrap[1]
    string11 = "  " + seawrap[2]
    string12 = "  " + seawrap[3]
    string13 = "."
    string14 = t0["hair"] + " hair"
    string15 = t0["skin"] + " skin"
    string16 = t0["mouth"]
    string17 = "."
    string18 = "."
    string19 = "."
    string20 = "."
    tcod.console_print_frame(0, x, y, 65, 21, True, 13, string1)
    draw(x + 2, y + 1, string2)
    draw(x + 2, y + 2, string3)
    draw(x + 2, y + 3, string4)
    draw(x + 2, y + 4, string5)
    draw(x + 2, y + 5, string6)
    draw(x + 2, y + 6, string7)
    draw(x + 2, y + 7, string8)
    draw(x + 2, y + 8, string9)
    draw(x + 2, y + 9, string10)
    draw(x + 2, y + 10, string11)
    draw(x + 2, y + 11, string12)
    draw(x + 2, y + 12, string13)
    draw(x + 2, y + 13, string14)
    draw(x + 2, y + 14, string15)
    draw(x + 2, y + 15, string16)
    draw(x + 2, y + 16, string17)
    draw(x + 2, y + 17, string18)
    draw(x + 2, y + 18, string19)
    draw(x + 2, y + 19, string20)
    return


# The display for individual screens.
def bloodpage():  # interface - page of blood color examples
    # screencurrent.name = bloodpage
    global spectrum
    z = spectrum
    spectrum.sort(key=deets.getcastenumstr, )
    h = 1
    w = 1
    numtotal = 0
    for x in z:
        if numtotal == 15 or numtotal == 30 or numtotal == 45 or numtotal == 60 or numtotal == 75 or numtotal == 90 or numtotal == 105 or numtotal == 120 or numtotal == 135:
            w = w + 13
            h = 1
        h = h + 3
        displayname = x
        (rgb1, rgb2, rgb3) = colg.bloodtorgb(x)
        displaycol = (rgb1, rgb2, rgb3)
        # ----- To show bloodcode + Castenum
        castename = deets.getcastefromcolor(rgb1, rgb2, rgb3)
        rectolor(w, h, 12, 2, displaycol)
# ----- To show bloodcode + Caste
        draw(w + 1, h + 1, displayname)
        draw(w + 5, h + 1, castename)
# ----- To show rgb coords + bloodcode
#        colname = str(displaycol.r) + "." + str(displaycol.g) + "." + str(displaycol.b)
#        draw(w, h+1, displayname + " " + colname)
# ----- To show Hue + Caste
#        hue = round(colg.rgbtohue(displaycol.r, displaycol.g, displaycol.b))
#        draw(w + 1, h + 1, str(hue) + "-" + castename)
        numtotal = numtotal + 1
    return


# The display function for various screens
def namepage():
    x = 12
    y = 10
    a = 0
    while a < 330:
        t0 = names.newname()
        draw(x, y, t0)
        a = a + 1
        y = y + 1
        if a == 30 or a == 60 or a == 90 or a == 120 or a == 150 or a == 180 or a == 210 or a == 240 or a == 270 or a == 300 or a == 330:
            x = x + 10
            y = 10


def loadingzone():  # interface - page to load trolls from file
    tcod.console_print_frame(0, 1, 1, 35, 5, True, 13, "Instructions")
    draw(3, 2, "Arrow keys to navigate.")
    draw(3, 3, "Press 1 to load to slot 1.")  # currently nonfunctional
    draw(3, 4, "      2 to load to slot 2.")

    global pageloadtroll
    z = os.listdir("Caverns/AncestralCave/")
    tcod.console_set_default_foreground(0, tcod.Color(250, 250, 200))
    castlist = [""]
    h = 7
    w = 1
    numtotal = 0
    # First load them into the cast-list.
    for arb in z:
        temp = arb
        if 20 < len(temp) < 35:
            if temp[3] == "." and temp[5] == "." and temp[12] == "." and temp[19] == ".":
                castlist.insert(numtotal, temp)
                numtotal = numtotal + 1
    numtotal = 0

    # Print out the data you now have
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
                rectolor(w, h, 15, 1, displaycol)
                displayname = temp[6] + "." + temp[13:19] + ", " + bloodcol
                if btncurrent != numtotal + 100:
                    tcod.console_set_default_foreground(0, tcod.Color(10, 10, 10))
                    draw(w + 1, h + 1, displayname)
                    tcod.console_set_default_foreground(0, tcod.Color(250, 250, 200))
                if btncurrent == numtotal + 100:
                    draw(w + 1, h + 1, displayname)
    pageloadtroll.maxbtn = numtotal + 100
    # pageloadtroll artificial maxbtn limiter
    if pageloadtroll.maxbtn > 360:
        pageloadtroll.maxbtn = 360
    pageloadtroll.minbtn = 101
    global screencurrent
    screencurrent = pageloadtroll


def trollmakepage():  # interface
    global troll1, troll2, troll3
    displaytroll(1, 7, troll1)
    displaytroll(1, 29, troll2)
    displaytroll(66, 17, troll3)
    return


# GLOBALS

screen_width = 160
screen_height = 50
versionnum = "0.2.3"
font_path = 'terminal8x12_gs_tc.png'
font_flags = tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD
tcod.console_set_custom_font(font_path, font_flags)
window_title = "Dancestry " + versionnum
fullscreen = False
tcod.console_init_root(screen_width, screen_height, window_title, fullscreen)
libbie = slurry.getpremadetroll(3)
lester = slurry.getpremadetroll(2)
troll1 = libbie
troll2 = lester
troll3 = deets.trollblank
spectrum = slurry.spectrumfull
btncurrent = 1

screencurrent = ScrPage()
# screens: maketroll, loadingzone, bloodpage, donationpage,
pageloadtroll = ScrPage("loadingzone", 101, 360, False, True)  # There is an artificial maxbtn limiter in loadtroll()
pagemaketroll = ScrPage("maketroll", 51, 55, True, False)
pageblood = ScrPage("bloodpage", 51, 57, True, False)
pagename = ScrPage("namepage", 101, 101, False, False)
# Invoke Main
main()
