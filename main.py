import json
import os
import trolldeets as deets
import libtcodpy as tcod
import names

# getcaste(b) is a function you can use to get the plaintext of a caste.  Put in the blood-code.
# Will be tagging each function / class / etc
# If I ever figure out modules, that will be which modules they go in.
# tags so far:  #trolldeets, #interface,
# screens:  maketroll, loadingzone, bloodpage, donationpage,
# screens are named ""page, and their ScrPage objects are named page""
# to activate a new main menu button, go to btnselect(), drawmenu(),

# have Trolls (one contributor)
# have Donations (A particular donation by 2 trolls)
# have Slurries (An array of Donations, with some meta-data)


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
    txtcol = tcod.Color(50, 50, 0)
    # Can add a tcod.Color(rrr,ggg,bbb) for:  drawbtn(x,y,"label",background,foreground)
    drawbtn(133, 2, "      MAKE TROLL     ", btnselect(1), txtcol)
    drawbtn(133, 6, "         SAVE        ", btnselect(2), txtcol)
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

    if screencurrent.name == "maketroll":
        drawsmallbtn(1, 1,  "    Create Troll      ", btnselect(51), txtcol)
        drawsmallbtn(1, 3,  "                      ", btnselect(52), txtcol)
        drawsmallbtn(1, 5,  "                      ", btnselect(53), txtcol)
        drawsmallbtn(25, 1, "                      ", btnselect(54), txtcol)
        drawsmallbtn(25, 3, "                      ", btnselect(55), txtcol)
        drawsmallbtn(25, 5, "                      ", btnselect(56), txtcol)
        drawsmallbtn(49, 1, "                      ", btnselect(57), txtcol)
        drawsmallbtn(49, 3, "                      ", btnselect(58), txtcol)
        drawsmallbtn(49, 5, "                      ", btnselect(59), txtcol)

    return


# make the menu buttons work.
def btnselect(x):  # interface - controls which buttons are highlightable.
    # main menu and main submenu only
    global btncurrent, pagename, pageloadtroll, pageblood, pagemaketroll
    btncol = tcod.Color(255, 0, 0)
    if x == btncurrent:
        btncol = tcod.Color(200, 200, 0)
    if x != btncurrent:
        btncol = tcod.Color(120, 120, 0)

    # unused main menu buttons.
    if x == 6 or x == 7 or x == 8 or x == 9 or x == 10 or x == 11:  # Unused Buttons
        btncol = tcod.Color(50, 50, 0)

    # submenu buttons
    # A set of 20 or so working submenu buttons.
    if screencurrent.name == "donationpage":
        if x == 54 or x == 55 or x == 56 or x == 57 or x == 58 or x == 59 or x == 60:  # Unused Buttons
            btncol = tcod.Color(50, 50, 0)
        if x == 61 or x == 62 or x == 63 or x == 64 or x == 65 or x == 66 or x == 67 or x == 68 or x == 69 or x == 70:
            # Unused Buttons
            btncol = tcod.Color(50, 50, 0)
    if screencurrent.name == "maketroll":
        if x == 54 or x == 55 or x == 56 or x == 57 or x == 58 or x == 59 or x == 60:  # Unused Buttons
            btncol = tcod.Color(50, 50, 0)
        if x == 61 or x == 62 or x == 63 or x == 64 or x == 65 or x == 66 or x == 67 or x == 68 or x == 69 or x == 70:
            # Unused Buttons
            btncol = tcod.Color(50, 50, 0)
    # just a ridiculous number of buttons.
    if screencurrent.name == "loadingzone":
        if x > screencurrent.maxbtn:
            btncol = tcod.Color(50, 50, 0)
    return btncol


def usedbuttons(direction):  # interface
    # mainmenu only
    global btncurrent, screencurrent
    if btncurrent < 25:  # mainmenu
        if direction == "+":
            btncurrent = btncurrent + 1
            while btnselect(btncurrent) == tcod.Color(50, 50, 0):
                btncurrent = btncurrent + 1
        if direction == "-":
            btncurrent = btncurrent - 1
            while btnselect(btncurrent) == tcod.Color(50, 50, 0):
                btncurrent = btncurrent - 1
        # loop main menu
        if btncurrent > 12:
            btncurrent = 1
        if btncurrent < 1:
            btncurrent = 12
    # loop submenu.
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
    global troll3, libbie, lester
    key = tcod.console_wait_for_keypress(True)
    if tcod.console_is_key_pressed(tcod.KEY_UP):
        if btncurrent < 9000:
            usedbuttons("-")
    if tcod.console_is_key_pressed(tcod.KEY_DOWN):
        if btncurrent < 9000:
            usedbuttons("+")
    if tcod.console_is_key_pressed(tcod.KEY_LEFT):
        if btncurrent < 25:
            if screencurrent.name == "maketroll":
                btncurrent = 51
            if screencurrent.name == "loadingzone":
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
        if btncurrent > 25:
            if screencurrent.name == "maketroll":
                if btncurrent == 51:
                    troll3 = deets.createtroll()
                    troll3 = deets.createtroll3(libbie,lester)
                    # for now.  Replace this with a function that takes libbie,lester as input
                    # and combines them into a grub.
                    updatescreen()
                    return False
                return False
            # End "main menu" portion of Enter loop.
            # Create a sub-menu here based off which other menu the cursor is in.
            return False
        # the loop for when someone presses enter to choose a button is over.
    if tcod.console_is_key_pressed(tcod.KEY_1):
        if screencurrent.name == "pageloadtroll":
            # load currently selected troll into slot 1.
            return False
        return False
    if tcod.console_is_key_pressed(tcod.KEY_2):
        if screencurrent.name == "pageloadtroll":
            # load currently selected troll into slot 2.
            return False
        return False

    elif key.vk == tcod.KEY_ESCAPE:
        # reenable the above line to make hitting escape close the program.
        return True


# save and load to file.
def savetroll(grub):  # interface     Save Troll
    saveloc = "Caverns/CaveB/" + grub["firname"] + "." + grub["surname"] + "." + grub["blood"] + ".troll"
    c = 1
    int(c)
    while os.path.exists(saveloc):
        c = c + 1
        d = str(c)
        saveloc = "Caverns/CaveB/" + grub["firname"] + "." + grub["surname"] + "." + grub["blood"] + "." + d + ".troll"
    savedtroll = open(saveloc, "wt")
    savedtroll.write("#SaveVersion4#" + "\n")
    y = json.dumps(grub, indent=4)
    savedtroll.write(y)
    savedtroll.close()
    return


def loadtroll(filename):  # interface     Load Troll
    trollobj = deets.createtroll()
    savedtroll = "Caverns/AncestralCave/" + filename + ".troll"
    if os.path.exists(savedtroll):
        loadedtroll = open(savedtroll, "rt")
        if loadedtroll.readline() == "#SaveVersion4#\n":
            y = loadedtroll.read()
            trollobj = json.loads(y)
        elif loadedtroll.readline() != "#SaveVersion4#\n":
            draw(18, 45, "WRONG SAVE TYPE")
        loadedtroll.close()
    return trollobj


# menu-related boxen.
def drawbtn(x, y, label="", btncolor=tcod.Color(255, 255, 225), txtcolor=tcod.Color(50, 50, 0)):  # interface
    rectolor(x, y, 24, 2, btncolor, txtcolor)
    draw(x + 2, y + 1, label)
    return


def drawsmallbtn(x, y, label="", btncolor=tcod.Color(255, 255, 225), txtcolor=tcod.Color(50, 50, 0)):  # interface
    rectolor(x, y, 21, 0, btncolor, txtcolor)
    draw(x, y, label)
    return


def rectolor(x, y, ww, hh, btncolor=tcod.Color(255, 255, 225), txtcolor=tcod.Color(0, 0, 0)):  # interface
    h = 0
    w = 0
    while h <= hh:
        while w <= ww:
            tcod.console_set_char_background(0, x + w, y + h, btncolor, tcod.BKGND_SET)
            tcod.console_set_char_foreground(0, x + w, y + h, txtcolor)
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
    # colbg = tcod.Color(0, 0, 0)
    # colfg = tcod.Color(255, 255, 255)
    # recolor
    colbg = bloodtorgb(t0["blood"])
    colfg = pastel(colbg)
    hornl1 = t0["hornL"]
    hornl2 = deets.Horn(hornl1)
    hornr1 = t0["hornR"]
    hornr2 = deets.Horn(hornr1)
    rectolor(x, y, 64, 20, colbg, colfg)
    string1 = t0["firname"] + " " + t0["surname"] + ", " + t0["blood"] + " " + t0["sex"]
    string2 = t0["caste"] + ", " + t0["powers"]
    string3 = t0["sea"]
    string4 = t0["height"] + ", " + t0["build"] + " build"
    string5 = t0["hair"] + " hair"
    string6 = t0["skin"] + " skin"
    string7 = "LHorn: " + hornl2.desc()
    string8 = "RHorn: " + hornr2.desc()
    tcod.console_print_frame(0, x, y, 65, 21, True, 13, string1)
    draw(x + 2, y + 1, string2)
    draw(x + 2, y + 2, string3)
    draw(x + 2, y + 3, string4)
    draw(x + 2, y + 4, string5)
    draw(x + 2, y + 5, string6)
    draw(x + 2, y + 6, string7)
    draw(x + 2, y + 7, string8)
    return


def bloodtorgb(b):  # interface, because this is the display color only / specifically.
    # gives you the darker color associated with the code "b" which is a 2-3 letter string.
    rgb1 = 0
    rgb2 = 0
    rgb3 = 0
    capitals = 0
    if b[0] == "r" or b[1] == "r":  # recessive colors
        rgb1 = 60
    if b[0] == "g" or b[1] == "g":
        rgb2 = 60
    if b[0] == "b" or b[1] == "b":
        rgb3 = 60
    if b[0] == "R" or b[1] == "R":  # dominant colors
        rgb1 = 120
        capitals = capitals + 1
    if b[0] == "G" or b[1] == "G":
        rgb2 = 120
        capitals = capitals + 1
    if b[0] == "B" or b[1] == "B":
        rgb3 = 120
        capitals = capitals + 1

    # Mutant Fixing : No capital letters = ***slightly*** brighter.
    if capitals == 0:
        if rgb1 != 0:
            rgb1 = rgb1 + 30
        if rgb1 > 210:
            rgb1 = rgb1 - 20
        if rgb2 != 0:
            rgb2 = rgb2 + 30
        if rgb2 > 220:
            rgb2 = rgb2 - 20
        if rgb3 != 0:
            rgb3 = rgb3 + 30
        if rgb3 > 240:
            rgb3 = rgb3 - 20
    # Make dark grubs brighter.
    if rgb1 + rgb2 + rgb3 < 100:
        rgb1 = rgb1 * 2
        rgb2 = rgb2 * 2
        rgb3 = rgb3 * 2
    # Vantases are special.
    if b == "rb":
        rgb1 = 255
        rgb2 = 0
        rgb3 = 0

    # Modulate color by 3rd letter.
    if len(b) == 3:
        if b[2] == "R":
            rgb1 = rgb1 + 25
            rgb2 = rgb2 - 25
            rgb3 = rgb3 - 25
        if b[2] == "G":
            rgb1 = rgb1 - 25
            rgb2 = rgb2 + 25
            rgb3 = rgb3 - 25
        if b[2] == "B":
            rgb1 = rgb1 - 25
            rgb2 = rgb2 - 25
            rgb3 = rgb3 + 25
        if b[2] == "r":
            rgb1 = rgb1 + 25
        if b[2] == "g":
            rgb2 = rgb2 + 25
        if b[2] == "b":
            rgb3 = rgb3 + 25

    # Return things to normal color ranges.
    if rgb1 > 255:
        rgb1 = 255
    if rgb2 > 255:
        rgb2 = 255
    if rgb3 > 255:
        rgb3 = 255
    if rgb1 < 0:
        rgb1 = 0
    if rgb2 < 0:
        rgb2 = 0
    if rgb3 < 0:
        rgb3 = 0

    finalcolor = tcod.Color(rgb1, rgb2, rgb3)
    return finalcolor


def pastel(oldcolor):  # interface (currently nonfunctional)
    # This currently does not function, for unknown reasons.
    # When it starts working, replace the crimson color with a pale offwhite.
    newcolor = tcod.color_lerp(oldcolor, tcod.Color(255, 0, 0), 0.5)
    return newcolor


# The display for individual screens.
def bloodpage():  # interface - page of blood color examples
    # screencurrent.name = bloodpage
    # all the display stuff for this page goes here since it's spammy
    z = ["rb", "rrb", "RRR", "RR", "Rr", "RRr", "Rrr", "rrr", "rr", "rrg", "RRg", "Rrg", "RRG", "Rgb", "Rg", "Rgg",
         "RGr", "RG", "rg", "RGB", "RGb", "rgg", "RGg", "Grr", "RGG", "Gr", "Grg", "Grb", "GGr", "GG", "Gg", "GGg",
         "Ggg", "GGG", "ggg", "gg", "ggb", "GGb", "Ggb", "GGB", "Gb", "Gbb", "gbb", "gb", "GBg", "GBr", "GB", "GBb",
         "GBB", "Bgg", "Bgb", "Bg", "BBg", "BB", "Bb", "BBb", "Bbb", "BBB", "bbb", "bb", "BBr", "Brb", "Brg", "Br",
         "RBB", "Brr", "rbb", "RBb", "RBg", "RB", "RBr", "Rbb", "Rb", "RRB", "RRb", "Rrb"]
    h = 4
    w = 10
    numtotal = 0
    for x in z:
        numtotal = numtotal + 1
        if numtotal == 14 or numtotal == 27 or numtotal == 40 or numtotal == 53 or numtotal == 66 or numtotal == 89:
            w = w + 18
            h = 4
        h = h + 3
        displayname = x
        displaycol = bloodtorgb(x)
        rectolor(w, h, 16, 2, displaycol)
        draw(w + 1, h + 1, displayname)
    return


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
    h = 7
    w = 7
    numtotal = 0
    for arb in z:
        temp = arb
        if 20 < len(temp) < 30:
            if temp[6] == "." and temp[13] == ".":
                numtotal = numtotal + 1
                if numtotal == 21 or numtotal == 41 or numtotal == 61 or numtotal == 81:
                    w = w + 15
                    h = 7
                h = h + 2
                displayname = temp[0:6] + " " + temp[7:13]
                bloodcol = temp[14:17]
                if bloodcol[2] == ".":
                    bloodcol = temp[14:16]
                displaycol = bloodtorgb(bloodcol)
                rectolor(w, h, 14, 1, displaycol)
                if btncurrent != numtotal + 100:
                    tcod.console_set_default_foreground(0, tcod.Color(10, 10, 10))
                    draw(w + 1, h + 1, displayname)
                    tcod.console_set_default_foreground(0, tcod.Color(250, 250, 200))
                if btncurrent == numtotal + 100:
                    draw(w + 1, h + 1, displayname)
    pageloadtroll.maxbtn = numtotal + 100
    if pageloadtroll.maxbtn > 180:
        pageloadtroll.maxbtn = 180
    pageloadtroll.minbtn = 101
    global screencurrent
    screencurrent = pageloadtroll


def trollmakepage():  # interface -- may be combined with showparents.
    displaytroll(1, 7, libbie)
    displaytroll(1, 29, lester)
    displaytroll(66, 17, troll3)
    return


# GLOBALS

screen_width = 160
screen_height = 50
versionnum = "0.2.0"
font_path = 'terminal8x12_gs_tc.png'
font_flags = tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD
tcod.console_set_custom_font(font_path, font_flags)
window_title = "Dancestry " + versionnum
fullscreen = False
tcod.console_init_root(screen_width, screen_height, window_title, fullscreen)
libbie = loadtroll("Libbie.Pickle.RGg")
lester = loadtroll("Lester.Pebble.Brb")
troll3 = deets.createtroll()
btncurrent = 1

screencurrent = ScrPage()
# screens: maketroll, loadingzone, bloodpage, donationpage,
pageloadtroll = ScrPage("loadingzone", 101, 180, False, True)
pagemaketroll = ScrPage("maketroll", 51, 51, True, False)
pageblood = ScrPage("bloodpage", 101, 101, False, True)
pagename = ScrPage("namepage", 101, 101, False, False)
# Invoke Main
main()
