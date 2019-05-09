import trolldeets as deets
import genome as gene
import random


# This file contains:
# -- hardcoded trolls who have contributed to slurry,
# -- source data to produce random trolls from slurry
# -- source data for mutations in genesourced trolls
# -- which blood codes are default
# -- spectrum groupings (high, mid, low, reds, blues, greens..)
# -- bias-by-caste for height, aquatic traits, etc


def getpremadetroll(x=random.randint(1, 3)):

    t0 = gene.trollobj()

    # Things that aren't really enabled yet.
    # Go through and give each troll a different one once the systems exist.
    strpowers = "None"
    strskin = "grey"
    donator1 = "The Mists"
    donator2 = "Of Time"
    height = "84"  # 7 feet
    strbuild = "thin"
    mouth = genemouthlow
    strhair = "short"
    if (x % 2) == 0:
        strbuild = "big"
        strhair = "long"

    if x == 1:
        t0["firname"] = "Libbie"
        t0["surname"] = "Pickle"
        t0["sex"] = "F"
        t0["blood"] = "RGg"
        t0["sea"] = "sssssbbccEEwwwwffbbSbfggiggiGGittdeeAAAA"
        t0["powers"] = strpowers
        t0["mouth"] = genemouthlow
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
        t0["mouth"] = genemouthhigh
        t0["sea"] = "SSsssbbCcEewWwWffbbsbFGgiGgiggiTtdeeAAAA"
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
        t0["sea"] = "sssSSBBcceeWWWWFFBBsBFGgeGgeGgeTtDEEaaaa"
        t0["mouth"] = genemouthmutant
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
    "rr", "rrr", "rrR", "rrg", "rrG", "rGR", "rGr", "rGB", "RG",
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

spectrummini = [
    "RR", "Rr", "rr", "Rg", "RG", "rG", "rg",
    "GG", "Gg", "gg", "Gb", "GB", "gB", "gb",
    "BB", "Bb", "bb", "rB", "RB", "Rb", "rb"
    ]

spectrumshort = [
    "RR", "rr", "RG", "rg",
    "GG", "gg", "GB", "gb",
    "BB", "bb", "RB", "rb"
    ]

spectrumlow = [
    "RR", "RRr", "RRR", "RRg", "RRG", "RrB", "Rrb", "RRB", "RRb",
    "Rr", "Rrr", "RrR", "Rrg", "RrG", "rrB", "rrb",
    "rr", "rrr", "rrR", "rrg", "rrG", "rGR", "rGr", "rGB",
    "rG", "RGB", "RGb", "RGg", "RGG", "RgR", "Rgr", "RgB", "Rgb",
    "Rg", "Rgg", "RgG", "rgR", "rgr", "rgB", "rgb", "RG",
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
    "rr", "rrr", "rrR", "rrg", "rrG", "rGR", "rGr", "rGB", "RG",
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


geneseamutant = "SsSSsBBCcEewWwWFFBbsBFGgeGgeggiTtDEeaaaa"  # Weird Shit.
genesealand = "sssssbbccEEwwwwffbbsbfggiggiggittdeeAAAA"    # no aquatic traits, no biolum, ears and no fins.
geneseasea = "SSSSSbbCCeeWwWwffBBSBFGGiGGiggiTTdEEAAAA"
# Seadweller active, earfins + no ears, half-webbed fingers/toes,
# no dorsal fins, strong biolum, any water, internal rib/neck gills, no face gills.
genemouthlow = "64ddTTTTTT444444CCCPGG222244TTTTTT444444CCCPGG222244TTTTTT444444CCCCGG222244TTTTTT444444CCPPGG222244"
genemouthhigh = "64ddTTTTTT445444PPPPPP224244TTTTTT445444PPPPPP223244TTTTTT444544PPPPGG222244TTTTTT444544PPPPGG222244"
genemouthmutant = "46DdFFFFFF272727PPPPPP424242FFFFFF727272PPPPPP242424FFFFFF272729PPPPPP242424FFFFFF727272PPPPPP424242"

spectrumheight = {  # 5' = 60, 6' = 72, 7' = 84, 8' = 96, 9' = 108, 10' = 120, 11' = 132
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

spectrumdwell = {
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
    "RR": "sssssbbccEEwwwwffbbsbfggiggiggittdeeAAAA",  # Maroon
    "Rr": "sssssbbccEEwwwwffbbsbfggiggiggittdeeaAAA",
    "rr": "sssssbbccEEwwwwffbbsbfggiggiggittdeeAAAA",  # Bronze
    "rG": "sssssbbccEEwwwwffbbsbfggiggiggittdeeAAaA",
    "RG": "sssSsbbccEEwwwwffbBsbfggiggiggittdEeAAAA",  # Gold
    "Rg": "sssssbbccEEwwwwffbbsbfggiggiggittdeeAaAA",
    "rg": "sssssbbccEEwwwwffbbsbfggiggiggittdeeAAAA",  # Lime
    "GG": "sssssbbccEEwwwwffbbsbfggiggiggittdeeAAAA",  # Olive
    "Gg": "sssssbbccEEwwwwffbbsbfggiggiggittdeeAAAa",
    "gg": "sssssbbccEEwwwwffBBsbfggiggiggittdeeAAAA",  # Jade
    "Gb": "sssSsbbccEEwwwwffbbsbfggiggiggittdeeaAAA",
    "GB": "sssssbbccEEwwwwffbbsbfggiggiggittdeeAAAA",  # Teal
    "gB": "sssssbbccEEwwwwffbbsbfggiggiggittdeeAaAA",
    "gb": "sssssbbccEEwwwwffbbsbfggiggiggittdeeAAAA",  # Ceru
    "BB": "sssssbbccEEwwwwffbbsbfggiggiggittdeeAAAA",  # Bloo
    "Bb": "sssssbbccEEwwwwffbbsbfggiggiggittdeeAAaA",
    "bb": "sssssbbCcEEwwWwFfbbsbfGgiGgiggittdeeAAAA",  # Indigo
    "rB": "SSsssbbCcEewwWwffbbsbfGgiGgiggiTtdEeAaAa",
    "RB": "SSSSSBbCCeeWwWwffBbSbFGGiGGiggiTTdEEAAAA",  # Violet
    "Rb": "SSSSSBbCCeeWwWWFfBBSBFGGiGGiGgitTdEEaaaA",
    "rb": "SSSSSBbCCeeWwWwffBBSbfGGiGGiggiTTdEEAAAA",  # Tyrian
    }

spectrumgenemouth = {
    "RR": "64ddTTTTTT444444CCCPGG222244TTTTTT444444CCCPGG222244TTTTTT444444CCCCGG222244TTTTTT444444CCPPGG222244",  # Maroon
    "Rr": "64ddTTTTTT445444CCCPGG222244TTTTTT445444CCCPGG222244TTTTTT444444CCCCGG224244TTTTTT444444CCPPGG224244",
    "rr": "64ddTTTTTT446444CCCPGG222244TTTTTT444444CCCPGG222244TTTTTT444444CCCCGG222244TTTTTT444644CCPPGG224244",  # Bronze
    "rG": "64ddTTTTTT445444CCCPGG222244TTTTTT445444CCCPGG222244TTTTTT444544CCCPGG222244TTTTTT444544CCPPGG222244",
    "RG": "64dDTFTFTF445544PPPPGG222244FTFTFT445544PPPPGG222244FTFTFT445544PPPPGG222244TFTFTF445544PPPPGG222244",  # Gold
    "Rg": "64ddTTTTTT444444CCCPGG222244TTTTTT446444CCCPGG222244TTTTTT444644CCCCGG224244TTTTTT444444CCPPGG222244",
    "rg": "64ddTTFFTT445644CCCPGG222244TTTTTT445444CCCPGG222244TTTTTT444544CCPPGG222244TTTTTT444544CCPPGG222244",  # Lime
    "GG": "64ddFFFFTT666644CCPPGG222244TTTTTT444544CCPPGG222244TTTTTT444544CCPPGG222244TTTTTT444544CCPPGG222244",  # Olive
    "Gg": "64ddFFFFTT565644CCPCGG222244TTTTTT445444CCPCGG222244TTTTTT444544CCCCGG222244TTTTTT444544CCCCGG222244",
    "gg": "64ddTTTTTT448444CCPCGG222244TTTTTT448444CCPCGG222244TTTTTT444544CCCCGG222244TTTTTT444544CCCCGG222244",  # Jade
    "Gb": "64ddTTTTTT444444CCCPCG222224TTTTTT446444CCCPCG222224TTTTTT444544CCCCGG222244TTTTTT444544CCCCGG222244",
    "GB": "64ddTTTTTT444444PPPPPG222224TTTTTT444444PPPPPG222224TTTTTT444444PPPPGG222244TTTTTT444444PPPPGG222244",  # Teal
    "gB": "64ddTTTTTT444444PPPPPG222224TTTTTT444444PPPPPG222224TTTTTT444444PPPPGG222244TTTTTT444444PPPPGG222244",
    "gb": "64ddTTTTTT558444PPPPPG222224TTTTTT558444PPPPPG222224TTTTTT444544PPPPGG222244TTTTTT444544PPPPGG222244",  # Ceru
    "BB": "64ddTTTTTT556555PPPPPG224224TTTTTT556555PPPPGG224244TTTTTT444544PPPPGG222244TTTTTT444544PPPPGG222244",  # Bloo
    "Bb": "64ddTTTTTT555444PPPPPP222422TTTTTT445444PPPPPP222422TTTTTT444544PPPPGG222244TTTTTT444544PPPPGG222244",
    "bb": "64ddTTTTTT666844PPPPPP222422TTTTTT666844PPPPPP222422TTTTTT444544PPPPGG222244TTTTTT444544PPPPGG222244",  # Indigo
    "rB": "64ddTTTTTT445444PPPPPP224222TTTTTT445444PPPPPP224222TTTTTT444544PPPPGG222244TTTTTT444544PPPPGG222244",
    "RB": "64ddTTTTTT445444PPPPPP222222TTTTTT445444PPPPPP222222TTTTTT444544PPPPPP222222TTTTTT444544PPPPPP222222",  # Violet
    "Rb": "64ddTTTTTT445444PPPPPP222222TTTTTT445444PPPPPP222222TTTTTT444544PPPPPP222222TTTTTT444544PPPPPP222222",
    "rb": "64ddTTTTTT445444PPPPPP222222TTTTTT445444PPPPPP222222TTTTTT444544PPPPPP222222TTTTTT444544PPPPPP222222",  # Tyrian
}

spectrumgeneseasocial = {
    "RR": genesealand,  # Maroon
    "Rr": genesealand,
    "rr": genesealand,  # Bronze
    "Rg": genesealand,
    "RG": genesealand,  # Gold
    "rG": genesealand,
    "rg": genesealand,  # Lime
    "GG": genesealand,  # Olive
    "Gg": genesealand,
    "gg": genesealand,  # Jade
    "Gb": genesealand,
    "GB": genesealand,  # Teal
    "gB": genesealand,
    "gb": genesealand,  # Ceru
    "BB": genesealand,  # Bloo
    "Bb": genesealand,
    "bb": genesealand,  # Indigo
    "rB": genesealand,
    "RB": geneseasea,  # Violet
    "Rb": geneseasea,
    "rb": geneseasea,  # Tyrian
    }
