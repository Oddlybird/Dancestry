import trolldeets as deets
import random

# This file contains:
# -- hardcoded trolls who have contributed to slurry,
# -- source data to produce random trolls from slurry
# -- source data for mutations in genesourced trolls
# -- which blood codes are default
# -- spectrum groupings (high, mid, low, reds, blues, greens..)
# -- bias-by-caste for height, aquatic traits, etc


def getpremadetroll(x=random.randint(1, 3)):

    t0 = deets.trollobj()

    # Things that aren't really enabled yet.
    # Go through and give each troll a different one once the systems exist.
    strpowers = "None"
    strskin = "grey"
    donator1 = "The Mists"
    donator2 = "Of Time"
    strheight = "84"  # 7 feet
    strbuild = "thin"
    strhair = "short"
    if (x % 2) == 0:
        strbuild = "big"
        strhair = "long"

    if x == 1:
        t0["firname"] = "Libbie"
        t0["surname"] = "Pickle"
        t0["sex"] = "F"
        t0["blood"] = "RGg"
        t0["sea"] = "ssbbccEEwwwwffbbSbfggiggiGGittdeeAAAAsss"
        t0["powers"] = strpowers
        t0["hornL"] = "12TFw.point"
        t0["hornR"] = "21SOn.split"
        t0["height"] = 64
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
        t0["sea"] = "SSbbCcEewWwWffbbsbFGgiGgiggiTtdeeAAAAsss"
        t0["powers"] = strpowers
        t0["hornL"] = "46RIn.pincher"
        t0["hornR"] = "37OBn.round"
        t0["height"] = 89
        t0["build"] = strbuild
        t0["hair"] = strhair
        t0["skin"] = strskin
        t0["donator1"] = "The Mists"
        t0["donator2"] = "Of Time"
    if x == 3:
        t0["firname"] = "Lobbah"
        t0["surname"] = "Parkle"
        t0["sex"] = "N"
        t0["blood"] = "bbb"
        t0["sea"] = "ssBBcceeWWWWFFBBsBFGgeGgeGgeTtDEEaaaasSS"
        t0["powers"] = strpowers
        # doubled genes, make just one horn doubled.
        t0["hornL"] = "17OFw.split"
        t0["hornR"] = "17OFw.split"
        t0["height"] = 72
        t0["build"] = strbuild
        t0["hair"] = strhair
        t0["skin"] = strskin
        t0["donator1"] = "The Mists"
        t0["donator2"] = "Of Time"

    h = t0["height"]
    t0["heightstr"] = deets.heightstr(h)

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


# Globals go below here.

spectrumfull = [
    "RR", "RRr", "RRR", "RRg", "RRG", "RrB", "Rrb",
    "Rr", "Rrr", "RrR", "Rrg", "RrG", "rrB", "rrb",
    "rr", "rrr", "rrR", "rrg", "rrG", "rGR", "rGr", "rGB",
    "rG", "RGB", "RGb", "RGg", "RGG", "RgR", "Rgr", "RgB", "Rgb",
    "Rg", "Rgg", "RgG", "rgR", "rgr", "rgB", "rgb",
    "rg", "rgg", "rgG", "GGR", "GGr", "GGG", "GGg",
    "GG", "GGb", "GGB", "GgR", "Ggr", "GgG", "Ggg",
    "Gg", "Ggb", "GgB", "ggR", "ggr", "ggG", "ggg",
    "gg", "ggb", "ggB", "GbG", "Gbg", "GbR", "Gbr",
    "Gb", "Gbb", "GbB", "GBG", "GBg", "GBR", "GBr",
    "GB", "GBb", "GBB", "gBG", "gBg", "gBR", "gBr",
    "gB", "gBb", "gBB", "gbG", "gbg", "gbR", "gbr",
    "gb", "gbb", "gbB", "BBG", "BBg", "BBB", "BBb",
    "BB", "BBr", "BBR", "BbG", "Bbg", "BbB",
    "Bb", "Bbb", "Bbr", "BbR", "bbG", "bbg", "bbb",
    "bb", "bbB", "bbr", "bbR", "rBB", "rBb", "rBg",
    "rB", "rBG", "rBr", "rBR", "RBB", "RBb", "RBG", "RBg",
    "RB", "RBr", "RBR", "RbB", "Rbb", "RbG",
    "Rb", "Rbr", "RbR", "rbB", "rbb", "rbg",
    "rb", "rbG", "rbr", "rbR", "RRB", "RRb",
    ]

spectrumshort = [
    "RR", "Rr", "rr", "Rg", "RG", "rG", "rg",
    "GG", "Gg", "gg", "Gb", "GB", "gB", "gb",
    "BB", "Bb", "bb", "rB", "RB", "Rb", "rb"
    ]

spectrummini = [
    "RR", "rr", "RG", "rg",
    "GG", "gg", "GB", "gb",
    "BB", "bb", "RB", "rb"
    ]

spectrumlow = [
   "RR", "RRr", "RRR", "RRg", "RRG", "RrB", "Rrb", "RRB", "RRb",
   "Rr", "Rrr", "RrR", "Rrg", "RrG", "rrB", "rrb",
    "rr", "rrr", "rrR", "rrg", "rrG", "rGR", "rGr", "rGB",
    "rG", "RGB", "RGb", "RGg", "RGG", "RgR", "Rgr", "RgB", "Rgb",
    "Rg", "Rgg", "RgG", "rgR", "rgr", "rgB", "rgb",
    "rg", "rgg", "rgG",
    ]

spectrummid = [
    "GG", "GGb", "GGB", "GgR", "Ggr", "GgG", "Ggg", "GGG", "GGg",
    "Gg", "Ggb", "GgB", "ggR", "ggr", "ggG", "ggg", "GGR", "GGr",
    "gg", "ggb", "ggB", "GbG", "Gbg", "GbR", "Gbr",
    "Gb", "Gbb", "GbB", "GBG", "GBg", "GBR", "GBr",
    "GB", "GBb", "GBB", "gBG", "gBg", "gBR", "gBr",
    "gB", "gBb", "gBB", "gbG", "gbg", "gbR", "gbr",
    "gb", "gbb", "gbB",
    ]

spectrumhigh = [
    "BBB", "BBb", "BB", "BBr", "BBR", "BbG", "Bbg", "BbB",
    "Bb", "Bbb", "Bbr", "BbR", "bbG", "bbg", "bbb", "BBG", "BBg",
    "bb", "bbB", "bbr", "bbR", "rBB", "rBb", "rBg",
    "rB", "rBG", "rBr", "rBR", "RBB", "RBb", "RBG", "RBg",
    "RB", "RBr", "RBR", "RbB", "Rbb", "RbG",
    "Rb", "Rbr", "RbR", "rbB", "rbb", "rbg",
    "rb", "rbG", "rbr", "rbR",
    ]

spectrumrust = [
   "RR", "RRr", "RRR", "RRg", "RRG", "RrB", "Rrb", "RRB", "RRb",
   "Rr", "Rrr", "RrR", "Rrg", "RrG", "rrB", "rrb",
    "rr", "rrr", "rrR", "rrg", "rrG", "rGR", "rGr", "rGB",
    "rG", "RGB", "RGb", "RGg", "RGG", "RgR", "Rgr", "RgB", "Rgb",
    "Rg",
    ]

spectrumgreens = [
    "Rgg", "RgG", "rgR", "rgr", "rgB", "rgb", "rg", "rgg", "rgG",
    "GG", "GGb", "GGB", "GgR", "Ggr", "GgG", "Ggg", "GGG", "GGg",
    "Gg", "Ggb", "GgB", "ggR", "ggr", "ggG", "ggg", "GGR", "GGr",
    "gg", "ggb", "ggB", "GbG", "Gbg", "GbR", "Gbr",
    "Gb",
    ]

spectrumblues = [
    "Gbb", "GbB", "GBG", "GBg", "GBR", "GBr",
    "GB", "GBb", "GBB", "gBG", "gBg", "gBR", "gBr",
    "gB", "gBb", "gBB", "gbG", "gbg", "gbR", "gbr",
    "gb", "gbb", "gbB",
    "BBB", "BBb", "BB", "BBr", "BBR", "BbG", "Bbg", "BbB",
    "Bb", "BBG", "BBg",
    ]

spectrumpurples = [
    "bbG", "bbg", "bbb", "Bbb", "Bbr", "BbR",
    "bb", "bbB", "bbr", "bbR", "rBB", "rBb", "rBg",
    "rB", "rBG", "rBr", "rBR", "RBB", "RBb", "RBG", "RBg",
    "RB", "RBr", "RBR", "RbB", "Rbb", "RbG",
    "Rb", "Rbr", "RbR", "rbB", "rbb", "rbg",
    "rb", "rbG", "rbr", "rbR",
    ]

def spectrumrand():
    spectrum = [
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
        premadeblood(), premadeblood(), premadeblood(), premadeblood(), premadeblood(),
    ]
    return spectrum

sgenemutant = "SsBBCcEewWwWFFBbsBFGgeGgeggiTtDEeaaaaSSs" # Weird Shit.
sgeneland = "ssbbccEEwwwwffbbsbfggiggiggittdeeAAAAsss"  # no aquatic traits, no biolum, ears and no fins.
sgenesea =  "SSbbCCeeWwWwffBBSBFGGiGGiggiTTdEEAAAASSS"
# Seadweller active, earfins + no ears, half-webbed fingers/toes,
# no dorsal fins, strong biolum, any water, internal rib/neck gills, no face gills.

heightspectrum = {  # 5' = 60, 6' = 72, 7' = 84, 8' = 96, 9' = 108, 10' = 120, 11' = 132
    "RR": 70,  # Maroon
    "Rr": 76,
    "rr": 80,  # Bronze
    "Rg": 90,
    "RG": 96,  # Gold
    "rG": 94,
    "rg": 90,  # Lime
    "GG": 90,  # Olive
    "Gg": 90,
    "gg": 96,  # Jade
    "Gb": 93,
    "GB": 90,  # Teal
    "gB": 93,
    "gb": 96,  # Ceru
    "BB": 100,  # Bloo
    "Bb": 110,
    "bb": 120,  # Indigo
    "rB": 100,
    "RB": 96,  # Violet
    "Rb": 84,
    "rb": 72,  # Tyrian
    }

dwellspectrum = {
    "RR": "landdweller",  # Maroon
    "Rr": "landdweller",
    "rr": "landdweller",  # Bronze
    "Rg": "landdweller",
    "RG": "landdweller",  # Gold
    "rG": "landdweller",
    "rg": "landdweller",  # Lime
    "GG": "landdweller",  # Olive
    "Gg": "landdweller",
    "gg": "landdweller",  # Jade
    "Gb": "landdweller",
    "GB": "landdweller",  # Teal
    "gB": "landdweller",
    "gb": "landdweller",  # Ceru
    "BB": "landdweller",  # Bloo
    "Bb": "landdweller",
    "bb": "landdweller",  # Indigo
    "rB": "landdweller",
    "RB": "seadweller",  # Violet
    "Rb": "seadweller",
    "rb": "seadweller",  # Tyrian
    }

spectrumgenesea = {
    "RR": "ssbbccEEwwwwffbbsbfggiggiggittdeeAAAAsss",  # Maroon
    "Rr": "ssbbccEEwwwwffbbsbfggiggiggittdeeaAAAsss",
    "rr": "ssbbccEEwwwwffbbsbfggiggiggittdeeAAAAsss",  # Bronze
    "Rg": "ssbbccEEwwwwffbbsbfggiggiggittdeeAaAAsss",
    "RG": "ssbbccEEwwwwffbBsbfggiggiggittdEeAAAAsSs",  # Gold
    "rG": "ssbbccEEwwwwffbbsbfggiggiggittdeeAAaAsss",
    "rg": "ssbbccEEwwwwffbbsbfggiggiggittdeeAAAAsss",  # Lime
    "GG": "ssbbccEEwwwwffbbsbfggiggiggittdeeAAAAsss",  # Olive
    "Gg": "ssbbccEEwwwwffbbsbfggiggiggittdeeAAAasss",
    "gg": "ssbbccEEwwwwffBBsbfggiggiggittdeeAAAAsss",  # Jade
    "Gb": "ssbbccEEwwwwffbbsbfggiggiggittdeeaAAAsSs",
    "GB": "ssbbccEEwwwwffbbsbfggiggiggittdeeAAAAsss",  # Teal
    "gB": "ssbbccEEwwwwffbbsbfggiggiggittdeeAaAAsss",
    "gb": "ssbbccEEwwwwffbbsbfggiggiggittdeeAAAAsss",  # Ceru
    "BB": "ssbbccEEwwwwffbbsbfggiggiggittdeeAAAAsss",  # Bloo
    "Bb": "ssbbccEEwwwwffbbsbfggiggiggittdeeAAaAsss",
    "bb": "ssbbCcEEwwWwFfbbsbfGgiGgiggittdeeAAAAsss",  # Indigo
    "rB": "SSbbCcEewwWwffbbsbfGgiGgiggiTtdEeAaAasss",
    "RB": "SSBbCCeeWwWwffBbSbFGGiGGiggiTTdEEAAAASSS",  # Violet
    "Rb": "SSBbCCeeWwWWFfBBSBFGGiGGiGgitTdEEaaaASSS",
    "rb": "SSBbCCeeWwWwffBBSbfGGiGGiggiTTdEEAAAASSS",  # Tyrian
    }

socialspectrumgenesea = {
    "RR": sgeneland,  # Maroon
    "Rr": sgeneland,
    "rr": sgeneland,  # Bronze
    "Rg": sgeneland,
    "RG": sgeneland,  # Gold
    "rG": sgeneland,
    "rg": sgeneland,  # Lime
    "GG": sgeneland,  # Olive
    "Gg": sgeneland,
    "gg": sgeneland,  # Jade
    "Gb": sgeneland,
    "GB": sgeneland,  # Teal
    "gB": sgeneland,
    "gb": sgeneland,  # Ceru
    "BB": sgeneland,  # Bloo
    "Bb": sgeneland,
    "bb": sgeneland,  # Indigo
    "rB": sgeneland,
    "RB": sgenesea,  # Violet
    "Rb": sgenesea,
    "rb": sgenesea,  # Tyrian
    }
