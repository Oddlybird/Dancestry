import trolldeets as deets
import random

# This file contains:
# -- hardcoded trolls who have contributed to slurry,
# -- source data to produce random trolls from slurry
# -- source data for mutations in genesourced trolls
# -- which blood codes are default


def getpremadetroll(x=random.randint(1, 2)):

    t0 = deets.trollobj()

    # Things that aren't really enabled yet.
    # Go through and give each troll a different one once the systems exist.
    strsea = "Landdweller"
    strpowers = "None"
    strskin = "grey"
    donator1 = "The Mists"
    donator2 = "Of Time"
    strheight = "short"
    strbuild = "thin"
    strhair = "short"
    if (x % 2) == 0:
        strheight = "tall"
        strbuild = "big"
        strhair = "long"

    if x == 1:
        t0["firname"] = "Libbie"
        t0["surname"] = "Pickle"
        t0["sex"] = "F"
        t0["blood"] = "RGg"
        strcaste = deets.getcaste("RGg")
        t0["caste"] = strcaste
        t0["sea"] = strsea
        t0["powers"] = strpowers
        t0["hornL"] = "12TFw.point"
        t0["hornR"] = "21SOn.split"
        t0["height"] = strheight
        t0["build"] = strbuild
        t0["hair"] = strhair
        t0["skin"] = strskin
        t0["donator1"] = donator1
        t0["donator2"] = donator2
    if x == 2:
        t0["firname"] = "Lester"
        t0["surname"] = "Pebble"
        t0["sex"] = "M"
        t0["blood"] = "rBb"
        strcaste = deets.getcaste("rBb")
        t0["caste"] = strcaste
        t0["sea"] = strsea
        t0["powers"] = strpowers
        t0["hornL"] = "46RIn.pincher"
        t0["hornR"] = "37OBn.round"
        t0["height"] = strheight
        t0["build"] = strbuild
        t0["hair"] = strhair
        t0["skin"] = strskin
        t0["donator1"] = "The Mists"
        t0["donator2"] = "Of Time"
    return t0


def premadehorn(inhorn=""):
    # be able to specify particular parts of the horn for randomization via the input?
    horn = ""
    if len(inhorn) < 2:
        # length in handspans
        x = random.randint(1, 4)
        horn = str(x)
        # curliness (straight, 45 degree, 90 degree, 180, 270, 360, ampora.)
        x = random.randint(1, 7)
        horn = horn + str(x)
        # Cross-section shape.  R = round, O = oval, T = triangular/edged, S = spiral/twisted like goat.
        x = random.randint(1, 6)
        if x == 1:
            horn = horn + "S"
        if x == 2:
            horn = horn + "T"
        if x == 3:
            horn = horn + "O"
        if x > 3:
            horn = horn + "R"
        # Primary growth direction.  F = forward, B = back, O = outward/side, I = inwards/up/default.
        x = random.randint(1, 6)
        if x == 1:
            horn = horn + "F"
        if x == 2:
            horn = horn + "B"
        if x == 3:
            horn = horn + "O"
        if x > 3:
            horn = horn + "I"
        # Width.  w = nepetalike, n = normal.
        x = random.randint(1, 15)
        if x == 1:
            horn = horn + "w"
        if x > 1:
            horn = horn + "n"
        # Point shape
        # change xmax to match
        x = random.randint(1, 6)
        horn = horn + "."
        if x == 1:
            horn = horn + "cone"
        if x == 2:
            horn = horn + "spade"
        if x == 3:
            horn = horn + "pincher"
        if x == 4:
            horn = horn + "nub"
        if x == 5:
            horn = horn + "jagged"
        if x == 6:
            horn = horn + "flat"
        if x == 7:
            horn = horn + "round"
        if x == 8:
            horn = horn + "hook"
        if x > 8:
            horn = horn + "point"

    return horn


def getoneblood():
    blood = ""
    x = random.randint(1, 15)
    if 1 <= x < 5:
        blood = "R"
    if 5 <= x < 9:
        blood = "r"
    if 9 <= x < 12:
        blood = "G"
    if 12 <= x < 14:
        blood = "g"
    if 14 <= x < 15:
        blood = "B"
    if 15 <= x:
        blood = "b"
    return blood


def premadeblood():
    blood = getoneblood() + getoneblood()
    blood = deets.bloodsort(blood)
    x = random.randint(1, 4)
    if x > 1:
        blood = blood + getoneblood()
    return blood


def eugenics(t0):
    return t0