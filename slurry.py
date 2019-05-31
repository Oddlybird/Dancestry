import genome as gene
import random


# This file contains:
# -- source data to produce random trolls from slurry
# -- source data for mutations in genesourced trolls
# -- bias-by-caste for height, aquatic traits, etc
# -- which blood codes are default
# -- spectrum groupings (high, mid, low, reds, blues, greens..)
# -- spectrums with by-caste entries and mutant entries

def eugenics(t0):
    return t0


# Globals go below here.
# CASTE COLOR SETS
spectrumfull = [
    "RR", "RRr", "RRR", "RRg", "RRG", "RrB", "Rrb",
    "Rr", "Rrr", "RrR", "Rrg", "RrG", "rrB", "rrb",
    "rr", "rrr", "rrR", "rrg", "rrG", "rGR", "rGr", "rGB",
    "RG",
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
# END OF CASTE COLOR SETS
# START OF GENES
# Possibly put these constants into the spectrum objects?  spectrumheight["short"], ...
geneseamutant = "SsSSsBBCcEewWwWFFBbsBFGgeGgeggiTtDEeaaaa"  # Weird Shit.
genesealand = "sssssbbccEEwwwwffbbsbfggiggiggittdeeAAAA"    # no aquatic traits, no biolum, ears and no fins.
geneseasea = "SSSSSbbCCeeWwWwffBBSBFGGiGGiggiTTdEEAAAA"
# Seadweller active, earfins + no ears, half-webbed fingers/toes,
# no dorsal fins, strong biolum, any water, internal rib/neck gills, no face gills.
genemouthlow = "64ddTTTTTT444444CCCPGGTTTTTT444444CCCPGGTTTTTT444444CCCCGGTTTTTT444444CCPPGG"
genemouthhigh = "64ddTTTTTT445444PPPPPPTTTTTT445444PPPPPPTTTTTT444544PPPPGGTTTTTT444544PPPPGG"
genemouthmutant = "46DdFTFTFT272727PPPPPPTFTFTF727272PPPPPPFTFTFT272729PPPPPPTFTFTF727272PPPPPP"

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
    # Add a mutant entry or three
    }

spectrumgenemouth = {
    "RR": "64ddTTTTTT444444CCCPGGTTTTTT444444CCCPGGTTTTTT444444CCCCGGTTTTTT444444CCPPGG",  # Maroon
    "Rr": "64ddTTTTTT445444CCCPGGTTTTTT445444CCCPGGTTTTTT444444CCCCGGTTTTTT444444CCPPGG",
    "rr": "64ddTTTTTT446444CCCPGGTTTTTT444444CCCPGGTTTTTT444444CCCCGGTTTTTT444644CCPPGG",  # Bronze
    "rG": "64ddTTTTTT445444CCCPGGTTTTTT445444CCCPGGTTTTTT444544CCCPGGTTTTTT444544CCPPGG",
    "RG": "64dDTFTFTF445544PPPPGGFTFTFT445544PPPPGGFTFTFT445544PPPPGGTFTFTF445544PPPPGG",  # Gold
    "Rg": "64ddTTTTTT444444CCCPGGTTTTTT446444CCCPGGTTTTTT444644CCCCGGTTTTTT444444CCPPGG",
    "rg": "64ddTTFFTT445644CCCPGGTTTTTT445444CCCPGGTTTTTT444544CCPPGGTTTTTT444544CCPPGG",  # Lime
    "GG": "64ddFFFFTT666644CCPPGGTTTTTT444544CCPPGGTTTTTT444544CCPPGGTTTTTT444544CCPPGG",  # Olive
    "Gg": "64ddFFFFTT565644CCPCGGTTTTTT445444CCPCGGTTTTTT444544CCCCGGTTTTTT444544CCCCGG",
    "gg": "64ddTTTTTT448444CCPCGGTTTTTT448444CCPCGGTTTTTT444544CCCCGGTTTTTT444544CCCCGG",  # Jade
    "Gb": "64ddTTTTTT444444CCCPCGTTTTTT446444CCCPCGTTTTTT444544CCCCGGTTTTTT444544CCCCGG",
    "GB": "64ddTTTTTT444444PPPPPGTTTTTT444444PPPPPGTTTTTT444444PPPPGGTTTTTT444444PPPPGG",  # Teal
    "gB": "64ddTTTTTT444444PPPPPGTTTTTT444444PPPPPGTTTTTT444444PPPPGGTTTTTT444444PPPPGG",
    "gb": "64ddTTTTTT558444PPPPPGTTTTTT558444PPPPPGTTTTTT444544PPPPGGTTTTTT444544PPPPGG",  # Ceru
    "BB": "64ddTTTTTT556555PPPPPGTTTTTT556555PPPPGGTTTTTT444544PPPPGGTTTTTT444544PPPPGG",  # Bloo
    "Bb": "64ddTTTTTT555444PPPPPPTTTTTT445444PPPPPPTTTTTT444544PPPPGGTTTTTT444544PPPPGG",
    "bb": "64ddTTTTTT666844PPPPPPTTTTTT666844PPPPPPTTTTTT444544PPPPGGTTTTTT444544PPPPGG",  # Indigo
    "rB": "64ddTTTTTT445444PPPPPPTTTTTT445444PPPPPPTTTTTT444544PPPPGGTTTTTT444544PPPPGG",
    "RB": "64ddTTTTTT445444PPPPPPTTTTTT445444PPPPPPTTTTTT444544PPPPPPTTTTTT444544PPPPPP",  # Violet
    "Rb": "64ddTTTTTT445444PPPPPPTTTTTT445444PPPPPPTTTTTT444544PPPPPPTTTTTT444544PPPPPP",
    "rb": "64ddTTTTTT445444PPPPPPTTTTTT445444PPPPPPTTTTTT444544PPPPPPTTTTTT444544PPPPPP",  # Tyrian
    "low": "64ddTTTTTT444444CCCPGGTTTTTT444444CCCPGGTTTTTT444444CCCCGGTTTTTT444444CCPPGG",
    "high": "64ddTTTTTT445444PPPPPPTTTTTT445444PPPPPPTTTTTT444544PPPPGGTTTTTT444544PPPPGG",
    "mut": "46DdFFFFFF272727PPPPPPFFFFFF727272PPPPPPFFFFFF272729PPPPPPFFFFFF727272PPPPPP",
    "m2": "64dDFFFFFF272727PPPPPPFFFFFF727272PPPPPPFFFFFF272729PPPPPPFFFFFF727272PPPPPP",
    # Add more mutant mouth types
}

spectrumgenehorn = {
    # "xx": "xxxDDNNTTaxmh.22RInS.22RInP.33RSnP.22RInS.33RSnP.22RInP",# format
    "RR": "RRx11AAPBSCTX.25RBnP.25RBnB.25RBwJ.25RBnP.25RBnR.25RBwb",  # Maroon
    "Rr": "Rrx31aaPBBESx.24RSnR.24RSnR.24RSnR.24RSnR.24RSnR.24RSnB",  #
    "rr": "rrx11AAPBSJSX.33RSnP.43RSnP.43RSnP.33RSnP.43RSnP.43RSnP",  # Bronze
    "rG": "rGxd2aaPBAESn.22RInS.22RInS.22RInS.22RInS.22RInS.22RInb",  #
    "RG": "RGxDDCCPBAJTx.22RInP.22RInS.22RSwH.22RInP.22RInH.22RIwS",  # Gold
    "Rg": "Rgx2dccPBACTn.12RSnH.12RSnH.12RSnH.12RSnH.12RSnH.12RSnH",  #
    "rg": "rgx11ccPBSLTX.11RInP.11RInP.11RInP.11RInP.11RInP.11RInP",  # Lime
    "GG": "GGx11DDPBSETX.12OSwb.12OSwP.12OSwS.12OSwS.12OSwb.12OSwP",  # Olive
    "Gg": "Ggx1dddPBBEtx.12RInP.12RInP.12RInP.12RInP.12RInP.12RInS",  #
    "gg": "ggx11EEPBSCTX.22RInH.22RInJ.22RInH.22RInP.22RInP.22RInP",  # Jade
    "Gb": "Gbxd2ddPBBJto.21RInF.21RInF.21RInF.21RInF.21RInF.21RInF",  #
    "GB": "GBx11DDPBSJTX.11RSnP.11RSnH.11RSnF.11RSnR.11RSnP.11RSnH",  # Teal
    "gB": "gBx3dddPBBJnn.21RInH.21RInH.21RInH.21RInH.21RInH.21RIns",  #
    "gb": "gbx11eePBSCTN.22RInp.22RInP.22RInP.22RInH.22RInb.22RInp",  # Ceru
    "BB": "BBx11FfPBSLTx.21RInC.21RInF.21RInH.21RInC.21RInF.21RInH",  # Bloo
    "Bb": "Bbxd3fFPBBEno.21RInH.21RInH.21RInH.21RInH.21RInH.21RInH",  #
    "bb": "bbx11FFPBSNNX.37SInP.37RInP.37SInP.37SInP.37RInP.37SInP",  # Indigo
    "rB": "rBx2dffPBBLnx.27RInP.27RInP.27RInP.27RInP.27RInP.27RIns",  #
    "RB": "RBx11GGPBASNX.27RInP.27RInP.27RInP.27RInP.27RInP.27RInP",  # Violet
    "Rb": "Rbx13ggPBBLno.24RInP.24RInP.24RIns.24RInP.24RInP.24RInP",  #
    "rb": "rbx11GGPBSUNx.22ROnP.22ROnP.22ROnP.22ROnP.22ROnP.22ROnP",  # Tyrian
    "m1": "rgxXXSspbAXSN.11RFnB.21ROwB.31RBwb.41RFnb.11ROwb.21RFwB",  # mutant1
    "m2": "rgxXDsSbpAXBn.22OBnb.32OFwb.42OOwF.12OBnF.22OFwb.32OBwb",  # mutant2
    "m3": "rgxDXBbKkBXUN.33OOnC.43OBwC.13OFwH.23OOnH.33OBwF.43OOwF",  # mutant3
    "m4": "rgxXxbBkKBXMH.44OFnF.14OOwF.24OBwJ.34OFnJ.44OOwH.14OFwH",  # mutant4
    "m5": "rgxxXWwEeBXSh.15TBnH.25TFwH.35TOwp.45TBnp.15TFwJ.25TBwJ",  # mutant5
    "m6": "rgx22wWeEAXBH.26TOnJ.36TBwJ.46TFwR.16TOnR.26TBwp.36TOwp",  # mutant6
    "m7": "rgx33NnAaAXSO.37TFnp.47TOwp.17TBwS.27TFnS.37TOwR.47TFwR",  # mutant7
    "m8": "rgx32nNaABXBo.41SBnS.11SFwR.21SOws.31SBnJ.41SFwS.11SBwS",  # mutant8
    "m9": "rgx23WWEPBXBh.13SOns.23SBwS.33SFws.43SOns.13SBws.23SOws",  # mutant9
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
    # No mutants listed.  This is what every caste is Expected to be.
    }

# These spectrums are incomplete and will be changed later.
spectrumpowerstemp = {
    "RR": "Psychic",  # Maroon
    "Rr": "Psychic",
    "rr": "Psychic",  # Bronze
    "Rg": "Psychic",
    "RG": "Very Psychic",  # Gold
    "rG": "Very Psychic",
    "rg": "Very Psychic",  # Lime
    "GG": "None",  # Olive
    "Gg": "None",
    "gg": "None",  # Jade
    "Gb": "None",
    "GB": "None",  # Teal
    "gB": "None",
    "gb": "None",  # Ceru
    "BB": "None",  # Bloo
    "Bb": "Voodoo",
    "bb": "Voodoo",  # Indigo
    "rB": "Voodoo",
    "RB": "None",  # Violet
    "Rb": "None",
    "rb": "None",  # Tyrian
}

spectrumbuildtemp = {
    "RR": "Curvy",  # Maroon
    "Rr": "Slight",
    "rr": "Lanky",  # Bronze
    "Rg": "Slight",
    "RG": "Thin",  # Gold
    "rG": "Thin",
    "rg": "Athletic",  # Lime
    "GG": "Athletic",  # Olive
    "Gg": "Athletic",
    "gg": "Slender",  # Jade
    "Gb": "Slender",
    "GB": "Twiggy",  # Teal
    "gB": "Twiggy",
    "gb": "Slim",  # Ceru
    "BB": "Athletic",  # Bloo
    "Bb": "Athletic",
    "bb": "Athletic",  # Indigo
    "rB": "Athletic",
    "RB": "Athletic",  # Violet
    "Rb": "Slim",
    "rb": "Slim",  # Tyrian
}

spectrumhairtemp = {
    "RR": "curly",  # Maroon
    "Rr": "long",
    "rr": "fauxhawk",  # Bronze
    "Rg": "short",
    "RG": "short",  # Gold
    "rG": "short",
    "rg": "wavy",  # Lime
    "GG": "short",  # Olive
    "Gg": "short",
    "gg": "short",  # Jade
    "Gb": "short",
    "GB": "short",  # Teal
    "gB": "wavy",
    "gb": "long",  # Ceru
    "BB": "long",  # Bloo
    "Bb": "long",
    "bb": "curly",  # Indigo
    "rB": "curly",
    "RB": "curly",  # Violet
    "Rb": "curly",
    "rb": "curly",  # Tyrian
}

spectrumskintemp = {
    "RR": "grey",  # Maroon
    "Rr": "grey",
    "rr": "grey",  # Bronze
    "Rg": "grey",
    "RG": "grey",  # Gold
    "rG": "grey",
    "rg": "grey",  # Lime
    "GG": "grey",  # Olive
    "Gg": "grey",
    "gg": "grey",  # Jade
    "Gb": "grey",
    "GB": "grey",  # Teal
    "gB": "grey",
    "gb": "grey",  # Ceru
    "BB": "grey",  # Bloo
    "Bb": "grey",
    "bb": "grey",  # Indigo
    "rB": "grey",
    "RB": "grey",  # Violet
    "Rb": "grey",
    "rb": "grey",  # Tyrian
}
