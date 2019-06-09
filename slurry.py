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
    "Rr": "sssssbbccEEwwwwffbbsbfggiggiggittdeeAAAA",
    "rr": "sssssbbccEEwwwwffbbsbfggiggiggittdeeAAAA",  # Bronze
    "rG": "sssssbbccEEwwwwffbbsbfggiggiggittdeeAAaA",
    "RG": "sssSsbbccEEwwwwffbBsbfggiggiggittdEeAAAA",  # Gold
    "Rg": "sssssbbccEEwwwwffbbsbfggiggiggittdeeAaAA",
    "rg": "sssssbbccEEwwwwffbbsbfggiggiggittdeeAAAA",  # Lime
    "GG": "sssssbbccEEwwwwffbbsbfggiggiggittdeeAAAA",  # Olive
    "Gg": "sssssbbccEEwwwwffbbsbfggiggiggittdeeAAAA",
    "gg": "sssssbbccEEwwwwffBBsbfggiggiggittdeeAAAA",  # Jade
    "Gb": "sssSsbbccEEwwwwffbbsbfggiggiggittdeeaAAA",
    "GB": "sssssbbccEEwwwwffbbsbfggiggiggittdeeAAAA",  # Teal
    "gB": "sssssbbccEEwwwwffbbsbfggiggiggittdeeAAAA",
    "gb": "sssssbbccEEwwwwffbbsbfggiggiggittdeeAAAA",  # Ceru
    "BB": "sssssbbccEEwwwwffbbsbfggiggiggittdeeAAAA",  # Bloo
    "Bb": "sssssbbccEEwwwwffbbsbfggiggiggittdeeAAAA",
    "bb": "sssssbbCcEEwwWwFfbbsbfGgiGgiggittdeeAAAA",  # Indigo
    "rB": "SSsssbbCcEewwWwffbbsbfGgiGgiggiTtdEeAAAa",
    "RB": "SSSSSBbCCeeWwWwffBbSbFGGiGGiggiTTdEEAAAA",  # Violet
    "Rb": "SSSSSBbCCeeWwWWFfBBSBFGGiGGiGgitTdEEaAaA",
    "rb": "SSSSSBbCCeeWwWwffBBSbfGGiGGiggiTTdEEAAAA",  # Tyrian
    "m1": "SSSSSBBCCeeWWWWFFBBSbfGGeGGeGGeTTDEeaaaa",  # Deepdweller
    "m2": "sssssBbCcEeWwWwffbbsbFGGiGGiggittdEEAAAA",  # Recessive Riverdweller
    "m3": "SSssSbbccEEwwWwffbbSBFggiggiGGittdEeAAAA",  # Hidden Amphibian
    "m4": "SSSSSbbccEEwwwwffbbsbfggiggiggittdeeAAAA",  # Land-dweller, technically
    "m5": "sssssBbCCeeWwWwffBbSbFGGiGGiggiTTdEEAAAA",  # Seadweller, technically
    "m6": "SssssbbccEEwwWwffbbsbfggiggiggittdeeAAAA",  # Webbed Toes
    "m7": "ssSssBbccEEwwwwffbbsbfggiggiggittdeeAAAA",  # Swimbladder
    "m8": "ssssSbbccEEwwwwFFbbsbfggiggiggittdeeAAAA",  # Body Fins
    "m9": "Sssssbbcceewwwwffbbsbfggiggiggittdeeaaaa",  # No ears/fins, can't breathe.
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
    "m1": "46DdFFFFFF272727PPPPPPFFFFFF727272PPPPPPFFFFFF272727PPPPPPFFFFFF727272PPPPPP",
    "m2": "63dDFFFFFF727272PPPPPPFFFFFF272727PPPPPPFFFFFF727272PPPPPPFFFFFF272727PPPPPP",
    "m3": "55ddTTTTTT444444CCCPGGTTTTTT444444CCCPGGTTTTTT444444CCCCGGTTTTTT444444CCPPGG",
    "m4": "63ddTTTTTT444444CCCPGGTTTTTT444444CCCPGGTTTTTT444444CCCCGGTTTTTT444444CCPPGG",
    "m5": "72ddTTTTTT444444CCCPGGTTTTTT444444CCCPGGTTTTTT444444CCCCGGTTTTTT444444CCPPGG",

    # Add more mutant mouth types
}

spectrumgenehorn = {
    # "xx": "xxxDDNNTTaxmh22RInS22RInP33RSnP22RInS33RSnP22RInP",# format
    "RR": "RRx11AAPBSCTX26RBnP26RBnB26RBwJ26RBnP26RBnR26RBwb",  # Maroon
    "Rr": "Rrx31aaPBBESO25RSnR24ISnR24RSnR25RSnR25RSnR24ISnB",  #
    "rr": "rrx11AAPBSJSX33RSnP43RSnP43RSnP33RSnP43RSnP43RSnP",  # Bronze
    "rG": "rGxd2aaPBAESo22RInS22RInS24IInS22RInS22RInS24IInb",  #
    "RG": "RGxDDCCPBAJTx22RInP22RInS22RSwH22RInP22RInH22RIwS",  # Gold
    "Rg": "Rgx2dccPBACTn12RSnH12CSnH12RSnH12RSnH12RSnH12RSnH",  #
    "rg": "rgx11ccPBSLTX11RInP11RInP11CInP11RInP14CInP11CInL",  # Lime
    "GG": "GGx11DDPBSETX12OSwb12CSwP12OSwS14OSwS12CSwb12OSwL",  # Olive
    "Gg": "Ggx1dddPBBEtx12RInP12CInL12CInP12RInP12CInL14CInS",  #
    "gg": "ggx11EEPBSCTX22RInH24RInJ22RInH22RInP22RInP22RInP",  # Jade
    "Gb": "Gbxd2ddPBBJth21RInF21RInF24RInF21RInF21RInF21RInF",  #
    "GB": "GBx11DDPBSJTX11RSnP11TSnH11RSnF11RSnR11TSnP11RSnH",  # Teal
    "gB": "gBx3dddPBBJnn21RInH21TInH21RInH21RInH21TInH21RIns",  #
    "gb": "gbx11eePBSCTN22RInp24RInP22RInP22RInH22RInb24RInp",  # Ceru
    "BB": "BBx11FfPBSLTx22RInC21RInF24RInH22RInC21RInF24RInH",  # Bloo
    "Bb": "Bbxd3fFPBBEno21RInH21RInH21RInH21RInH24RInH21RInH",  #
    "bb": "bbx11FFPBSNNX38SInP38TInP38SInP38SInP38TInP38SInP",  # Indigo
    "rB": "rBx2dffPBBLnx28RInP28TInP28RInP28RInP28TInP28SIns",  #
    "RB": "RBx11GGPBASNX28RInP28TInL28RInP28RInP28TInP28TInL",  # Violet
    "Rb": "Rbx13ggPBBLno25RInP24RInL24RIns24RInP24RInP24RInL",  #
    "rb": "rbx11GGPBSUNx22ROnP22ROnP22ROnP22ROnP24ROnP22ROnP",  # Tyrian
    #
    "m1": "rgxXXSspbAXSN11CFnB21COwB31CBwb41IFnb11IOwb24IFwB",  # mutant1
    "m2": "rgxXDsSbpAXBn22OBnb32OFwb42OOwF12OBnF22OFwb32OBwb",  # mutant2
    "m3": "rgxDXBbKkBXUN33OOnC43OBwC13IFwH23OOnH33OBwF43OOwF",  # mutant3
    "m4": "rgxXxbBkKBXMH44OFnF14OOwF24OBwJ34OFnJ44OOwH14OFwH",  # mutant4
    "m5": "rgxxXWwEeBXSh16TBnH26TFwH35TOwp45TBnp15TFwJ25TBwJ",  # mutant5
    "m6": "rgx22wWeEAXBH27TOnJ37TBwJ46TFwR16TOnR26TBwp36TOwp",  # mutant6
    "m7": "rgx33NnAaAXSO38TFnp48TOwp18TBwS27TFnS37TOwR47TFwR",  # mutant7
    "m8": "rgxTTnNaABXBo41SBnS11SFwR28SOws38SBnJ41SFwS11SBwS",  # mutant8
    "m9": "rgxTTWWEPBXBh13SOns23SBwS33SFws43SOns13SBws23SOws",  # mutant9
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

spectrumcorestat = {
    "mm": {"clout": 0, "acumen": 0, "grit": 0, "alacrity": 0,  # Mutant
           "hunch": 0, "resolve": 0, "moxie": 0, "psyche": 0, "pts": 2},

    "RR": {"clout": -1, "acumen": 0, "grit": 0, "alacrity": 0,  # Maroon
           "hunch": 2, "resolve": 0, "moxie": 0, "psyche": 1, "pts": 0},
    "Rr": {"clout": -1, "acumen": 0, "grit": 0, "alacrity": 0,  #
           "hunch": 1, "resolve": 0, "moxie": 1, "psyche": 1, "pts": 0},
    "rr": {"clout": -1, "acumen": 0, "grit": 0, "alacrity": 0,  # Bronze
           "hunch": 0, "resolve": 0, "moxie": 2, "psyche": 1, "pts": 0},
    "Rg": {"clout": -1, "acumen": 1, "grit": 0, "alacrity": 0,  #
           "hunch": 0, "resolve": 0, "moxie": 1, "psyche": 1, "pts": 0},
    "RG": {"clout": -1, "acumen": 1, "grit": 0, "alacrity": 0,  # Gold
           "hunch": 0, "resolve": 0, "moxie": 0, "psyche": 2, "pts": 0},
    "rG": {"clout": -1, "acumen": 1, "grit": 0, "alacrity": 0,  #
           "hunch": 0, "resolve": 0, "moxie": 0, "psyche": 2, "pts": 0},
    "rg": {"clout": -1, "acumen": 0, "grit": -1, "alacrity": 0,  # Lime
           "hunch": 0, "resolve": 0, "moxie": 0, "psyche": 3, "pts": 0},

    "GG": {"clout": 0, "acumen": 0, "grit": 0, "alacrity": 1,  # Olive
           "hunch": 1, "resolve": 0, "moxie": 0, "psyche": 0, "pts": 0},
    "Gg": {"clout": 0, "acumen": 0.25, "grit": 0.25, "alacrity": 0.25,  #
           "hunch": 0.25, "resolve": 0, "moxie": 0, "psyche": 0, "pts": 0},
    "gg": {"clout": 0, "acumen": 1, "grit": 1, "alacrity": 0,  # Jade
           "hunch": 0, "resolve": 0, "moxie": 0, "psyche": 0, "pts": 0},
    "Gb": {"clout": 0, "acumen": 1, "grit": 0.5, "alacrity": 0,  #
           "hunch": 0, "resolve": 0, "moxie": 0.5, "psyche": 0, "pts": 0},
    "GB": {"clout": 0, "acumen": 1, "grit": 0, "alacrity": 0,  # Teal
           "hunch": 0, "resolve": 0, "moxie": 1, "psyche": 0, "pts": 0},
    "gB": {"clout": 0, "acumen": 0.5, "grit": 0, "alacrity": 0,  #
           "hunch": 0.5, "resolve": 0, "moxie": 1, "psyche": 0, "pts": 0},
    "gb": {"clout": 0, "acumen": 0, "grit": 0, "alacrity": 0,  # Ceru
           "hunch": 1, "resolve": 0, "moxie": 1, "psyche": 0, "pts": 0},

    "BB": {"clout": 1, "acumen": 1, "grit": 0, "alacrity": -1,  # Bloo
           "hunch": 0, "resolve": 1, "moxie": 0, "psyche": 0, "pts": 0},
    "Bb": {"clout": 1, "acumen": 0, "grit": 1, "alacrity": 0,  #
           "hunch": 0, "resolve": 1, "moxie": -1, "psyche": 0, "pts": 0},
    "bb": {"clout": 1, "acumen": -1, "grit": 1, "alacrity": 0,  # Indigo
           "hunch": 0, "resolve": 1, "moxie": 0, "psyche": 0, "pts": 0},
    "rB": {"clout": 1, "acumen": 0, "grit": 1, "alacrity": 0,  #
           "hunch": 0, "resolve": 1, "moxie": -1, "psyche": -1, "pts": 0},
    "RB": {"clout": 1, "acumen": 0, "grit": 1, "alacrity": 0,  # Violet
           "hunch": 0, "resolve": 1, "moxie": 0, "psyche": -2, "pts": 0},
    "Rb": {"clout": 1, "acumen": 0, "grit": 1, "alacrity": 0,  #
           "hunch": 0, "resolve": 1, "moxie": 0, "psyche": -4, "pts": 0},
    "rb": {"clout": 1, "acumen": 0, "grit": 1, "alacrity": 0,  # Tyrian
           "hunch": 0, "resolve": 1, "moxie": 0, "psyche": -6, "pts": 0},
}

