import genome as gene
import random
from formattingbs import randsel

# This file contains:
# -- source data to produce random trolls from slurry
# -- source data for mutations in genesourced trolls
# -- bias-by-caste for height, aquatic traits, etc
# -- which blood codes are default
# -- spectrum groupings (high, mid, low, reds, blues, greens..)
# -- spectrums with by-caste entries and mutant entries


# START OF GENES
def genesea(inp):
    # Move all these settings into a .txt file that it gets loaded from at start of program?
    # That would be a memory and CPU hog, unless I put it in a .py in a cavern subfolder . . .
    # Not today, but a possible tidying step in the future.  For now, one slurry file.
    # Blank Setting
    blank = {
        "controls": {  # SS: as seadweller.  Ss/sS: check genes.  ss: as landdweller.
            0: "",  # Ears, fins, wfingers, wtoes
            1: "",  # gillneck, gillneckt, gillribs, gillribt, gillface, gillfacet, salt, air
            2: "",  # bladders
            3: "",  # biolum, teeth    # move teeth doubling gene?
            4: "",  # dorsal/bodyfins,  eyelids, # move doubled eyelid gene elsewhere?
            },
        "bladders": "",    # BB several, Bb one, bb none.
        "ears": "",        # EE full, Ee / eE half, ee none.
        "cheekfins": "",   # CC full, Cc / cC half, cc none.
                    # Make subgenes for earfin size, number of tines, etc.
        "wfingers": "",    # WW full, Ww / wW half, ww none.  webbing
        "wtoes": "",       # WW full, Ww / wW half, ww none.  webbing
        "dorsalfins": "",  # FF big, Ff / fF small, ff none.
        "biolum": "",      # BB full, Bb / bB partial, bb none.
                    # Create subgenes for patterning, brightness, voluntary/reflexive...
                    # conscious/unconscious, steady state / bloodflow,
                    # fin glow, eye glow, stripes, freckles, ...
        "gillneck": {"main": "",   # GG Full, Gg/gG half, gg none
                     "type": ""},  # i internal, e external
        "gillribs": {"main": "",   # GG Full, Gg/gG half, gg none
                     "type": ""},  # i internal, e external
        "gillface": {"main": "",   # GG Full, Gg/gG half, gg none
                     "type": ""},  # i internal, e external
        "toothdouble": "",  # Move to Teeth.  tt land, TT barracuda, Tt blend, D doubled, d singled.
        "eyelids": "",      # Move to Eyes.   EE lids, Ee/eE permanent transparent layer, ee normal land.
        "salt": "",         # Move to Organs. Ss salt, Bb brackish, Ff freshwater.
        "air": "",          # Move to Organs. Can you breathe air?  aaaa = no, anything else = yes.
    }
    # Primary settings
    land = {
        "controls": {0: "ss", 1: "ss", 2: "ss", 3: "ss", 4: "ss"},
        "bladders": "bb", "ears": "EE", "cheekfins": "cc",
        "wfingers": "ww", "wtoes": "ww", "dorsalfins": "ff", "biolum": "bb",
        "gillneck": {"main": "gg", "type": "i"},
        "gillribs": {"main": "gg", "type": "i"},
        "gillface": {"main": "gg", "type": "i"},
        "toothdouble": "dd", "eyelids": "ee",
        "salt": "sbf", "air": "AAAA"}
    sea = {
        "controls": {0: "SS", 1: "SS", 2: "SS", 3: "SS", 4: "SS"},
        "bladders": "bb", "ears": "ee", "cheekfins": "CC",
        "wfingers": "Ww", "wtoes": "Ww", "dorsalfins": "ff", "biolum": "Bb",
        "gillneck": {"main": "GG", "type": "i"},
        "gillribs": {"main": "GG", "type": "i"},
        "gillface": {"main": "gg", "type": "i"},
        "toothdouble": "Dd", "eyelids": "Ee",
        "salt": "SBF", "air": "AAAA"}
    # Secondaries
    deepsea = {
        "controls": {0: "SS", 1: "SS", 2: "SS", 3: "SS", 4: "SS"},
        "bladders": "BB", "ears": "ee", "cheekfins": "CC",
        "wfingers": "WW", "wtoes": "WW", "dorsalfins": "FF", "biolum": "BB",
        "gillneck": {"main": "GG", "type": "i"},
        "gillribs": {"main": "GG", "type": "i"},
        "gillface": {"main": "GG", "type": "i"},
        "toothdouble": "DD", "eyelids": "EE",
        "salt": "Sbf", "air": "aaaa"},
    river = {
        "controls": {0: "Ss", 1: "Ss", 2: "ss", 3: "ss", 4: "ss"},
        "bladders": "bb", "ears": "Ee", "cheekfins": "cC",
        "wfingers": "Ww", "wtoes": "Ww", "dorsalfins": "ff", "biolum": "bb",
        "gillneck": {"main": "Gg", "type": "i"},
        "gillribs": {"main": "gg", "type": "i"},
        "gillface": {"main": "gg", "type": "i"},
        "toothdouble": "dd", "eyelids": "ee",
        "salt": "sbF", "air": "AAAA"},
    seahidden = {
        "controls": {0: "sS", 1: "ss", 2: "ss", 3: "ss", 4: "ss"},
        "bladders": "bb", "ears": "EE", "cheekfins": "cc",
        "wfingers": "ww", "wtoes": "wW", "dorsalfins": "ff", "biolum": "bb",
        "gillneck": {"main": "gg", "type": "i"},
        "gillribs": {"main": "GG", "type": "i"},
        "gillface": {"main": "gg", "type": "i"},
        "toothdouble": "dd", "eyelids": "ee",
        "salt": "SBF", "air": "AAAA"},
    landsea = {
        "controls": {0: "SS", 1: "SS", 2: "SS", 3: "SS", 4: "SS"},
        "bladders": "bb", "ears": "EE", "cheekfins": "cc",
        "wfingers": "ww", "wtoes": "ww", "dorsalfins": "ff", "biolum": "bb",
        "gillneck": {"main": "gg", "type": "i"},
        "gillribs": {"main": "gg", "type": "i"},
        "gillface": {"main": "gg", "type": "i"},
        "toothdouble": "dd", "eyelids": "ee",
        "salt": "sbf", "air": "AAAA"},
    sealand = {
        "controls": {0: "ss", 1: "ss", 2: "ss", 3: "ss", 4: "ss"},
        "bladders": "bb", "ears": "ee", "cheekfins": "CC",
        "wfingers": "Ww", "wtoes": "Ww", "dorsalfins": "ff", "biolum": "Bb",
        "gillneck": {"main": "GG", "type": "i"},
        "gillribs": {"main": "GG", "type": "i"},
        "gillface": {"main": "gg", "type": "i"},
        "toothdouble": "Dd", "eyelids": "Ee",
        "salt": "SBF", "air": "AAAA"},
    webbed = {
        "controls": {0: "sS", 1: "ss", 2: "ss", 3: "ss", 4: "ss"},
        "bladders": "bb", "ears": "ee", "cheekfins": "CC",
        "wfingers": "WW", "wtoes": "WW", "dorsalfins": "ff", "biolum": "bb",
        "gillneck": {"main": "gg", "type": "i"},
        "gillribs": {"main": "gg", "type": "i"},
        "gillface": {"main": "gg", "type": "i"},
        "toothdouble": "dd", "eyelids": "ee",
        "salt": "sbf", "air": "AAAA"},
    bladder = {
        "controls": {0: "ss", 1: "ss", 2: "Ss", 3: "ss", 4: "ss"},
        "bladders": "BB", "ears": "EE", "cheekfins": "cc",
        "wfingers": "ww", "wtoes": "ww", "dorsalfins": "ff", "biolum": "bb",
        "gillneck": {"main": "gg", "type": "i"},
        "gillribs": {"main": "gg", "type": "i"},
        "gillface": {"main": "gg", "type": "i"},
        "toothdouble": "dd", "eyelids": "ee",
        "salt": "sbf", "air": "AAAA"},
    bodyfins = {
        "controls": {0: "ss", 1: "ss", 2: "ss", 3: "ss", 4: "Ss"},
        "bladders": "bb", "ears": "EE", "cheekfins": "cc",
        "wfingers": "ww", "wtoes": "ww", "dorsalfins": "FF", "biolum": "bb",
        "gillneck": {"main": "gg", "type": "i"},
        "gillribs": {"main": "gg", "type": "i"},
        "gillface": {"main": "gg", "type": "i"},
        "toothdouble": "dd", "eyelids": "ee",
        "salt": "sbf", "air": "AAAA"},
    nonviable = {  # no ears/fins, can't breathe.
        "controls": {0: "Ss", 1: "Ss", 2: "ss", 3: "ss", 4: "ss"},
        "bladders": "bb", "ears": "ee", "cheekfins": "cc",
        "wfingers": "WW", "wtoes": "WW", "dorsalfins": "fF", "biolum": "bb",
        "gillneck": {"main": "GG", "type": "i"},
        "gillribs": {"main": "GG", "type": "i"},
        "gillface": {"main": "GG", "type": "i"},
        "toothdouble": "dd", "eyelids": "EE",
        "salt": "sbf", "air": "aaaa"},

    # The actual meat
    gene = blank   # Initialize it as empty.

    # Each entry given an individual mention in case I want to add individual quirks later.
    if inp == "blank":
        gene = blank
    if inp == "land":
        gene = land
    if inp == "sea":
        gene = sea
    if inp == "deepsea":
        gene = deepsea
    if inp == "river":
        gene = river
    if inp == "seahidden":
        gene = seahidden
    if inp == "landsea":
        gene = landsea
    if inp == "sealand":
        gene = sealand
    if inp == "webbed":
        gene = webbed
    if inp == "bladder":
        gene = bladder
    if inp == "bodyfins":
        gene = bodyfins
    if inp == "nonviable":
        gene = nonviable
    if inp == "RR":  # Maroon
        gene = land
    if inp == "Rr":
        gene = land
    if inp == "rr":  # Bronze
        gene = land
    if inp == "rG":
        gene = land
        gene["toothdouble"] = "dD"
    if inp == "RG":  # Gold
        gene = land
        gene["controls"][3] = "SS"
        gene["biolum"] = "Bb"
        gene["toothdouble"] = "Dd"
        gene["eyelids"] = "Ee"
    if inp == "Rg":
        gene = land
        gene["biolum"] = "bB"
    if inp == "rg":  # Lime
        gene = land
    if inp == "GG":  # Olive
        gene = land
    if inp == "Gg":
        gene = land
        gene["controls"][3] = "SS"
    if inp == "gg":  # Jade
        gene = land
        gene["biolum"] = "BB"
    if inp == "Gb":
        gene = land
        gene["controls"][3] = "SS"
    if inp == "GB":  # Teal
        gene = land
    if inp == "gB":
        gene = land
    if inp == "gb":  # Ceru
        gene = land
    if inp == "BB":  # Bloo
        gene = land
    if inp == "Bb":
        gene = land
    if inp == "bb":  # Indigo
        gene = land
        gene["cheekfins"] = "Cc"
        gene["ears"] = "EE"
        gene["bodyfins"] = "Ff"
        gene["wtoes"] = "Ww"
    if inp == "rB":
        gene = land
        gene["controls"][0] = "SS"
        gene["controls"][1] = "SS"
        gene["cheekfins"] = "Cc"
        gene["ears"] = "Ee"
        gene["wtoes"] = "Ww"
        gene["gillribs"] = sea["gillribs"]
        gene["gillneck"] = sea["gillneck"]
        gene["eyelids"] = sea["eyelids"]
    if inp == "RB":  # Violet
        gene = sea
        gene["salt"] = "SBF"
    if inp == "Rb":
        gene = sea
        gene["wtoes"] = "WW"
        gene["bodyfins"] = "Ff"
        gene["salt"] = "SBf"
        gene["biolum"] = "BB"
    if inp == "rb":  # Tyrian
        gene = sea
        gene["wtoes"] = "WW"
        gene["salt"] = "Sbf"
        gene["biolum"] = "BB"
        gene["gillface"] = sea["gillribs"]
    return gene


def genemouth(inp):
    # Blank Setting
    blank = {
        "wide": 0,  # How many teeth show left/right
        "high": 0,  # Longest tooth that is covered
        "double": "",  # Doubled DD, Dd/dD, dd
        # sym    # TT (average), TF/FT (overwrite), FF (distinct)
        # length # 0 - 9.  0 = gums, 4 = normal, 8 = 2x normal, 9 = giant.
        # types  # Cc choppy/flat, Gg grinding, Pp pointy, serrated (?) other (?)
        #        # CG, CP, GP = RR.
        # tooth position:  0 = center, 4 and 5 = molar.
        "top": {
            "L": {
                "sym": {1: True, 2: True, 3: True, 4: True, 5: True, 6: True},  # Symmetry Overrides
                "length": {1: 4, 2: 4,    3: 4,    4: 4,    5: 4,    6: 4},  # Length
                "type": {1: "",  2: "",   3: "",   4: "",   5: "",   6: ""}},  # Type
            "R": {
                "sym": {1: True, 2: True, 3: True, 4: True, 5: True, 6: True},  # Symmetry Overrides
                "length": {1: 4, 2: 4,    3: 4,    4: 4,    5: 4,    6: 4},  # Length
                "type": {1: "",  2: "",   3: "",   4: "",   5: "",   6: ""}}},  # Type
        "bot": {
            "L": {
                "sym": {1: True, 2: True, 3: True, 4: True, 5: True, 6: True},  # Symmetry Overrides
                "length": {1: 4, 2: 4,    3: 4,    4: 4,    5: 4,    6: 4},  # Length
                "type": {1: "",  2: "",   3: "",   4: "",   5: "",   6: ""}},  # Type
            "R": {
                "sym": {1: True, 2: True, 3: True, 4: True, 5: True, 6: True},  # Symmetry Overrides
                "length": {1: 4, 2: 4,    3: 4,    4: 4,    5: 4,    6: 4},  # Length
                "type": {1: "",  2: "",   3: "",   4: "",   5: "",   6: ""}}}}  # Type
    # Primary Settings
    low = {"wide": 4, "high": 4, "double": "dd",
        "top": {
            "L": {
                "sym": {1: True, 2: True, 3: True, 4: True, 5: True, 6: True},  # Symmetry Overrides
                "length": {1: 4, 2: 4,    3: 4,    4: 4,    5: 4,    6: 4},  # Length
                "type": {1: "C", 2: "C",  3: "C",  4: "P",  5: "G",  6: "G"}},  # Type
            "R": {
                "sym": {1: True, 2: True, 3: True, 4: True, 5: True, 6: True},  # Symmetry Overrides
                "length": {1: 4, 2: 4,    3: 4,    4: 4,    5: 4,    6: 4},  # Length
                "type": {1: "C", 2: "C",  3: "C",  4: "P",  5: "G",  6: "G"}}},  # Type
        "bot": {
            "L": {
                "sym": {1: True, 2: True, 3: True, 4: True, 5: True, 6: True},  # Symmetry Overrides
                "length": {1: 4, 2: 4,    3: 4,    4: 4,    5: 4,    6: 4},  # Length
                "type": {1: "C", 2: "C",  3: "C",  4: "C",  5: "G",  6: "G"}},  # Type
            "R": {
                "sym": {1: True, 2: True, 3: True, 4: True, 5: True, 6: True},  # Symmetry Overrides
                "length": {1: 4, 2: 4,    3: 4,    4: 4,    5: 4,    6: 4},  # Length
                "type": {1: "C", 2: "C",  3: "P",  4: "P",  5: "G",  6: "G"}}}}  # Type
    high = {"wide": 6, "high": 4, "double": "dd",
        "top": {
            "L": {
                "sym": {1: True, 2: True, 3: True, 4: True, 5: True, 6: True},  # Symmetry Overrides
                "length": {1: 4, 2: 4,    3: 5,    4: 4,    5: 4,    6: 4},  # Length
                "type": {1: "P", 2: "P",  3: "P",  4: "P",  5: "P",  6: "G"}},  # Type
            "R": {
                "sym": {1: True, 2: True, 3: True, 4: True, 5: True, 6: True},  # Symmetry Overrides
                "length": {1: 4, 2: 4,    3: 5,    4: 4,    5: 4,    6: 4},  # Length
                "type": {1: "P", 2: "P",  3: "P",  4: "P",  5: "P",  6: "G"}}},  # Type
        "bot": {
            "L": {
                "sym": {1: True, 2: True, 3: True, 4: True, 5: True, 6: True},  # Symmetry Overrides
                "length": {1: 4, 2: 4,    3: 4,    4: 5,    5: 4,    6: 4},  # Length
                "type": {1: "P", 2: "P",  3: "P",  4: "P",  5: "P",  6: "G"}},  # Type
            "R": {
                "sym": {1: True, 2: True, 3: True, 4: True, 5: True, 6: True},  # Symmetry Overrides
                "length": {1: 4, 2: 4,    3: 4,    4: 5,    5: 4,    6: 4},  # Length
                "type": {1: "P", 2: "P",  3: "P",  4: "P",  5: "P",  6: "G"}}}}  # Type
    # Secondaries
    allG = {"wide": 2, "high": 7, "double": "dD",  # Frankly Horrifying
        "top": {
            "L": {
                "sym": {1: True, 2: True, 3: True, 4: True, 5: True, 6: True},  # Symmetry Overrides
                "length": {1: 4, 2: 4,    3: 4,    4: 4,    5: 3,    6: 3},  # Length
                "type": {1: "G", 2: "G",  3: "G",  4: "G",  5: "G",  6: "G"}},  # Type
            "R": {
                "sym": {1: True, 2: True, 3: True, 4: True, 5: True, 6: True},  # Symmetry Overrides
                "length": {1: 4, 2: 4,    3: 4,    4: 4,    5: 3,    6: 3},  # Length
                "type": {1: "G", 2: "G",  3: "G",  4: "G",  5: "G",  6: "G"}}},  # Type
        "bot": {
            "L": {
                "sym": {1: True, 2: True, 3: True, 4: True, 5: True, 6: True},  # Symmetry Overrides
                "length": {1: 4, 2: 4,    3: 4,    4: 4,    5: 5,    6: 5},  # Length
                "type": {1: "G", 2: "G",  3: "G",  4: "G",  5: "G",  6: "G"}},  # Type
            "R": {
                "sym": {1: True, 2: True, 3: True, 4: True, 5: True, 6: True},  # Symmetry Overrides
                "length": {1: 4, 2: 4,    3: 4,    4: 4,    5: 5,    6: 5},  # Length
                "type": {1: "G", 2: "G",  3: "G",  4: "G",  5: "G",  6: "G"}}}}  # Type
    allC = {"wide": 3, "high": 4, "double": "dd",  # Rabbit Overbite
        "top": {
            "L": {
                "sym": {1: True, 2: True, 3: True, 4: True, 5: True, 6: True},  # Symmetry Overrides
                "length": {1: 6, 2: 4,    3: 4,    4: 4,    5: 4,    6: 4},  # Length
                "type": {1: "C", 2: "C",  3: "C",  4: "C",  5: "C",  6: "C"}},  # Type
            "R": {
                "sym": {1: True, 2: True, 3: True, 4: True, 5: True, 6: True},  # Symmetry Overrides
                "length": {1: 8, 2: 6,    3: 4,    4: 4,    5: 4,    6: 4},  # Length
                "type": {1: "C", 2: "C",  3: "C",  4: "C",  5: "C",  6: "C"}}},  # Type
        "bot": {
            "L": {
                "sym": {1: True, 2: True, 3: True, 4: True, 5: True, 6: True},  # Symmetry Overrides
                "length": {1: 4, 2: 5,    3: 4,    4: 4,    5: 4,    6: 4},  # Length
                "type": {1: "C", 2: "C",  3: "C",  4: "C",  5: "C",  6: "C"}},  # Type
            "R": {
                "sym": {1: True, 2: True, 3: True, 4: True, 5: True, 6: True},  # Symmetry Overrides
                "length": {1: 4, 2: 4,    3: 5,    4: 4,    5: 4,    6: 4},  # Length
                "type": {1: "C", 2: "C",  3: "C",  4: "C",  5: "C",  6: "C"}}}}  # Type
    allP = {"wide": 6, "high": 2, "double": "dd",  # GNOMF GNOMF GNOMF hellmouth
        "top": {
            "L": {
                "sym": {1: True, 2: True, 3: True, 4: True, 5: True, 6: True},  # Symmetry Overrides
                "length": {1: 8, 2: 8,    3: 8,    4: 8,    5: 5,    6: 3},  # Length
                "type": {1: "P", 2: "P",  3: "P",  4: "P",  5: "P",  6: "P"}},  # Type
            "R": {
                "sym": {1: True, 2: True, 3: True, 4: True, 5: True, 6: True},  # Symmetry Overrides
                "length": {1: 6, 2: 6,    3: 6,    4: 6,    5: 5,    6: 3},  # Length
                "type": {1: "P", 2: "P",  3: "P",  4: "P",  5: "P",  6: "P"}}},  # Type
        "bot": {
            "L": {
                "sym": {1: True, 2: True, 3: True, 4: True, 5: True, 6: True},  # Symmetry Overrides
                "length": {1: 6, 2: 6,    3: 6,    4: 6,    5: 5,    6: 3},  # Length
                "type": {1: "P", 2: "P",  3: "P",  4: "P",  5: "P",  6: "P"}},  # Type
            "R": {
                "sym": {1: True, 2: True, 3: True, 4: True, 5: True, 6: True},  # Symmetry Overrides
                "length": {1: 8, 2: 8,    3: 8,    4: 8,    5: 5,    6: 3},  # Length
                "type": {1: "P", 2: "P",  3: "P",  4: "P",  5: "P",  6: "P"}}}}  # Type
    length1 = {"wide": 6, "high": 2, "double": "dd",
            "top": {
                "L": {
                    "sym": {1: True, 2: True, 3: True, 4: True, 5: True, 6: True},  # Symmetry Overrides
                    "length": {1: 2, 2: 8,    3: 2,    4: 8,    5: 2,    6: 8},  # Length
                    "type": {1: "P", 2: "P",  3: "P",  4: "P",  5: "P",  6: "P"}},  # Type
                "R": {
                    "sym": {1: True, 2: True, 3: True, 4: True, 5: True, 6: True},  # Symmetry Overrides
                    "length": {1: 8, 2: 2,    3: 8,    4: 2,    5: 8,    6: 2},  # Length
                    "type": {1: "P", 2: "P",  3: "P",  4: "P",  5: "P",  6: "P"}}},  # Type
            "bot": {
                "L": {
                    "sym": {1: True, 2: True, 3: True, 4: True, 5: True, 6: True},  # Symmetry Overrides
                    "length": {1: 8, 2: 2,    3: 8,    4: 2,    5: 8,    6: 2},  # Length
                    "type": {1: "P", 2: "P",  3: "P",  4: "P",  5: "P",  6: "P"}},  # Type
                "R": {
                    "sym": {1: True, 2: True, 3: True, 4: True, 5: True, 6: True},  # Symmetry Overrides
                    "length": {1: 2, 2: 8,    3: 2,    4: 8,    5: 2,    6: 8},  # Length
                    "type": {1: "P", 2: "P",  3: "P",  4: "P",  5: "P",  6: "P"}}}}  # Type
    length2 = {"wide": 2, "high": 8, "double": "Dd",
            "top": {
                "L": {
                    "sym": {1: True, 2: True, 3: True, 4: True, 5: True, 6: True},  # Symmetry Overrides
                    "length": {1: 8, 2: 2,    3: 8,    4: 2,    5: 8,    6: 2},  # Length
                    "type": {1: "P", 2: "P",  3: "P",  4: "P",  5: "P",  6: "P"}},  # Type
                "R": {
                    "sym": {1: True, 2: True, 3: True, 4: True, 5: True, 6: True},  # Symmetry Overrides
                    "length": {1: 2, 2: 8,    3: 2,    4: 8,    5: 2,    6: 8},  # Length
                    "type": {1: "P", 2: "P",  3: "P",  4: "P",  5: "P",  6: "P"}}},  # Type
            "bot": {
                "L": {
                    "sym": {1: True, 2: True, 3: True, 4: True, 5: True, 6: True},  # Symmetry Overrides
                    "length": {1: 2, 2: 8,    3: 2,    4: 8,    5: 2,    6: 8},  # Length
                    "type": {1: "P", 2: "P",  3: "P",  4: "P",  5: "P",  6: "P"}},  # Type
                "R": {
                    "sym": {1: True, 2: True, 3: True, 4: True, 5: True, 6: True},  # Symmetry Overrides
                    "length": {1: 8, 2: 2,    3: 8,    4: 2,    5: 8,    6: 2},  # Length
                    "type": {1: "P", 2: "P",  3: "P",  4: "P",  5: "P",  6: "P"}}}}  # Type
    sym1 = {"wide": 6, "high": 4, "double": "Dd",
            "top": {
                "L": {
                    "sym": {1: False, 2: False, 3: False, 4: False, 5: False, 6: False},  # Symmetry Overrides
                    "length": {1: 6, 2: 4, 3: 4, 4: 4, 5: 4, 6: 4},  # Length
                    "type": {1: "P",  2: "P",   3: "P",   4: "P",   5: "P",   6: "P"}},  # Type
                "R": {
                    "sym": {1: False, 2: False, 3: False, 4: False, 5: False, 6: False},  # Symmetry Overrides
                    "length": {1: 6, 2: 4, 3: 4, 4: 4, 5: 4, 6: 4},  # Length
                    "type": {1: "P",  2: "P",   3: "P",   4: "P",   5: "P",   6: "P"}}},  # Type
            "bot": {
                "L": {
                    "sym": {1: False, 2: False, 3: False, 4: False, 5: False, 6: False},  # Symmetry Overrides
                    "length": {1: 6, 2: 4, 3: 4, 4: 4, 5: 4, 6: 4},  # Length
                    "type": {1: "P",  2: "P",   3: "P",   4: "P",   5: "P",   6: "P"}},  # Type
                "R": {
                    "sym": {1: False, 2: False, 3: False, 4: False, 5: False, 6: False},  # Symmetry Overrides
                    "length": {1: 6, 2: 4, 3: 4, 4: 4, 5: 4, 6: 4},  # Length
                    "type": {1: "P",  2: "P",   3: "P",   4: "P",   5: "P",   6: "P"}}}}  # Type
    sym2 = {"wide": 4, "high": 6, "double": "dD",
            "top": {
                "L": {
                    "sym": {1: False, 2: False, 3: False, 4: False, 5: False, 6: False},  # Symmetry Overrides
                    "length": {1: 8, 2: 8, 3: 8, 4: 8, 5: 5, 6: 3},  # Length
                    "type": {1: "P",  2: "P",   3: "P",   4: "P",   5: "P",   6: "P"}},  # Type
                "R": {
                    "sym": {1: True, 2: True, 3: True, 4: True, 5: True, 6: True},  # Symmetry Overrides
                    "length": {1: 8, 2: 8, 3: 8, 4: 8, 5: 5, 6: 3},  # Length
                    "type": {1: "P",  2: "P",   3: "P",   4: "P",   5: "P",   6: "P"}}},  # Type
            "bot": {
                "L": {
                    "sym": {1: False, 2: False, 3: False, 4: False, 5: False, 6: False},  # Symmetry Overrides
                    "length": {1: 6, 2: 4, 3: 4, 4: 4, 5: 4, 6: 4},  # Length
                    "type": {1: "P",  2: "P",   3: "P",   4: "P",   5: "P",   6: "P"}},  # Type
                "R": {
                    "sym": {1: True, 2: True, 3: True, 4: True, 5: True, 6: True},  # Symmetry Overrides
                    "length": {1: 6, 2: 4, 3: 4, 4: 4, 5: 4, 6: 4},  # Length
                    "type": {1: "P",  2: "P",   3: "P",   4: "P",   5: "P",   6: "P"}}}}  # Type

    # The actual meat
    gene = blank   # Initialize it as empty.

    # Each entry given an individual mention in case I want to add individual quirks later.
    if inp == "blank":
        gene = blank
    if inp == "low":
        gene = low
    if inp == "high":
        gene = high
    if inp == "allG":
        gene = allG
    if inp == "allC":
        gene = allC
    if inp == "allP":
        gene = allP
    if inp == "length1":
        gene = length1
    if inp == "length2":
        gene = length2
    if inp == "sym1":
        gene = sym1
    if inp == "sym2":
        gene = sym2

    if inp == "RR":  # Maroon
        gene = low
    if inp == "Rr":
        gene = low
        gene["top"]["L"]["length"][3] = 5
        gene["top"]["R"]["length"][3] = 5
    if inp == "rr":  # Bronze
        gene = low
        gene["top"]["L"]["length"][3] = 6
        gene["bot"]["L"]["length"][4] = 6
    if inp == "rG":
        gene = low
        gene["top"]["L"]["length"][3] = 5
        gene["top"]["R"]["length"][3] = 5
        gene["bot"]["L"]["length"][4] = 5
        gene["bot"]["R"]["length"][4] = 5
        gene["bot"]["L"]["type"][4] = "P"
    if inp == "RG":  # Gold
        gene = high
        gene["double"] = "Dd"
        gene["top"]["R"]["sym"][1] = False   # Jankass motherfuckers.
        gene["top"]["L"]["sym"][2] = False
        gene["top"]["R"]["sym"][3] = False
        gene["top"]["L"]["sym"][4] = False
        gene["top"]["R"]["sym"][5] = False
        gene["top"]["L"]["sym"][6] = False
        gene["bot"]["L"]["sym"][1] = False
        gene["bot"]["R"]["sym"][2] = False
        gene["bot"]["L"]["sym"][3] = False
        gene["bot"]["R"]["sym"][4] = False
        gene["bot"]["L"]["sym"][5] = False
        gene["bot"]["R"]["sym"][6] = False
        gene["top"]["L"]["length"][4] = 5
        gene["top"]["R"]["length"][4] = 5
        gene["bot"]["L"]["length"][3] = 5
        gene["bot"]["R"]["length"][3] = 5
        gene["top"]["L"]["type"][5] = "G"
        gene["top"]["L"]["type"][6] = "G"
        gene["top"]["R"]["type"][5] = "G"
        gene["top"]["R"]["type"][6] = "G"
    if inp == "Rg":
        gene = low
        gene["top"]["R"]["length"][3] = 6
        gene["bot"]["R"]["length"][4] = 6
    if inp == "rg":  # Lime
        gene = low
        gene["top"]["L"]["sym"][3] = False
        gene["top"]["L"]["sym"][4] = False
        gene["top"]["R"]["length"][3] = 5
        gene["top"]["R"]["length"][4] = 6
        gene["top"]["L"]["length"][3] = 5
        gene["bot"]["R"]["length"][4] = 5
        gene["bot"]["L"]["length"][4] = 5
    if inp == "GG":  # Olive
        gene = low
        gene["top"]["L"]["sym"][1] = False
        gene["top"]["L"]["length"][1] = 6
        gene["top"]["L"]["sym"][2] = False
        gene["top"]["L"]["length"][2] = 6
        gene["top"]["L"]["sym"][3] = False
        gene["top"]["L"]["length"][3] = 6
        gene["top"]["L"]["sym"][4] = False
        gene["top"]["L"]["length"][4] = 6
        gene["top"]["R"]["length"][4] = 5
        gene["bot"]["L"]["length"][4] = 5
        gene["bot"]["R"]["length"][4] = 5
        gene["top"]["L"]["type"][3] = "P"
        gene["top"]["R"]["type"][3] = "P"
        gene["top"]["L"]["type"][4] = "P"
        gene["top"]["R"]["type"][4] = "P"
    if inp == "Gg":
        gene = low
        gene["top"]["L"]["sym"][1] = False
        gene["top"]["L"]["length"][1] = 5
        gene["top"]["L"]["sym"][2] = False
        gene["top"]["L"]["length"][2] = 6
        gene["top"]["L"]["sym"][3] = False
        gene["top"]["L"]["length"][3] = 5
        gene["top"]["L"]["sym"][4] = False
        gene["top"]["L"]["length"][4] = 6
        gene["top"]["R"]["length"][3] = 5
        gene["bot"]["L"]["length"][4] = 5
        gene["bot"]["R"]["length"][4] = 5
        gene["top"]["L"]["type"][3] = "P"
        gene["top"]["R"]["type"][3] = "P"
        gene["top"]["L"]["type"][4] = "C"
        gene["top"]["R"]["type"][4] = "C"
        gene["bot"]["R"]["type"][3] = "P"
        gene["bot"]["R"]["type"][4] = "P"
    if inp == "gg":  # Jade
        gene = low
        gene["top"]["L"]["length"][3] = 8
        gene["top"]["R"]["length"][3] = 8
        gene["top"]["L"]["length"][4] = 5
        gene["top"]["R"]["length"][4] = 5
        gene["top"]["L"]["type"][3] = "P"
        gene["top"]["R"]["type"][3] = "P"
        gene["top"]["L"]["type"][4] = "C"
        gene["top"]["R"]["type"][4] = "C"
        gene["bot"]["R"]["type"][3] = "C"
        gene["bot"]["R"]["type"][4] = "C"
    if inp == "Gb":
        gene = low
        gene["top"]["R"]["length"][3] = 6
        gene["top"]["L"]["length"][4] = 5
        gene["top"]["R"]["length"][4] = 5
        gene["bot"]["R"]["type"][3] = "C"
        gene["bot"]["R"]["type"][4] = "C"
    if inp == "GB":  # Teal
        gene = high
        gene["top"]["L"]["length"][3] = 4
        gene["top"]["R"]["length"][3] = 4
        gene["bot"]["L"]["length"][4] = 4
        gene["bot"]["R"]["length"][4] = 4
        gene["top"]["R"]["type"][6] = 6
        gene["top"]["L"]["type"][6] = 6
    if inp == "gB":
        gene = high
        gene["top"]["L"]["length"][3] = 4
        gene["top"]["R"]["length"][3] = 4
        gene["bot"]["L"]["length"][4] = 4
        gene["bot"]["R"]["length"][4] = 4
        gene["top"]["R"]["type"][6] = 6
        gene["top"]["L"]["type"][6] = 6
    if inp == "gb":  # Ceru
        gene = high
        gene["top"]["L"]["type"][5] = "P"
        gene["top"]["R"]["type"][5] = "P"
        gene["top"]["L"]["length"][3] = 8
        gene["top"]["R"]["length"][3] = 8
        gene["top"]["L"]["length"][2] = 5
        gene["top"]["R"]["length"][2] = 5
        gene["top"]["L"]["length"][1] = 5
        gene["top"]["R"]["length"][1] = 5
    if inp == "BB":  # Bloo
        gene = high
        gene["top"]["L"]["type"][5] = "P"
        gene["top"]["R"]["type"][5] = "P"
        gene["top"]["L"]["length"][6] = 5
        gene["top"]["R"]["length"][6] = 5
        gene["top"]["L"]["length"][5] = 5
        gene["top"]["R"]["length"][5] = 5
        gene["top"]["L"]["length"][4] = 5
        gene["top"]["R"]["length"][4] = 5
        gene["top"]["L"]["length"][3] = 6
        gene["top"]["R"]["length"][3] = 6
        gene["top"]["L"]["length"][2] = 5
        gene["top"]["R"]["length"][2] = 5
        gene["top"]["L"]["length"][1] = 5
        gene["top"]["R"]["length"][1] = 5
        gene["top"]["R"]["type"][6] = "G"
    if inp == "Bb":
        gene = high
        gene["top"]["L"]["length"][1] = 5
        gene["top"]["L"]["length"][2] = 5
    if inp == "bb":  # Indigo
        gene["top"]["L"]["length"][1] = 6
        gene["top"]["R"]["length"][1] = 6
        gene["top"]["L"]["length"][2] = 6
        gene["top"]["R"]["length"][2] = 6
        gene["top"]["L"]["length"][3] = 6
        gene["top"]["R"]["length"][3] = 6
        gene["top"]["L"]["length"][4] = 8
        gene["top"]["R"]["length"][4] = 8
        gene = high
    if inp == "rB":
        gene = high
    if inp == "RB":  # Violet
        gene = high
        gene["bot"]["L"]["type"][5] = "P"
        gene["bot"]["L"]["type"][6] = "P"
        gene["bot"]["R"]["type"][5] = "P"
        gene["bot"]["R"]["type"][6] = "P"
    if inp == "Rb":
        gene = high
        gene["bot"]["L"]["type"][5] = "P"
        gene["bot"]["L"]["type"][6] = "P"
        gene["bot"]["R"]["type"][5] = "P"
        gene["bot"]["R"]["type"][6] = "P"
    if inp == "rb":  # Tyrian
        gene = high
        gene["bot"]["L"]["type"][5] = "P"
        gene["bot"]["L"]["type"][6] = "P"
        gene["bot"]["R"]["type"][5] = "P"
        gene["bot"]["R"]["type"][6] = "P"
    return gene


# For single horn object
def genehorn(linmin=0, linmax=4, lweight=0, cinmin=0, cinmax=8, cweight=0, radial="", dir="", width="", tip=""):
    # genehorn((0,4,0),(0,8,0),"ROTSCI", "FBIO", "wn", "PBbCFHJRSsL")
    # Input 1 : (min, max, number between -4 and +4 to modify)
    # Input 2 : (min, max, number between -9 and +9 to modify)
    # Input 3 : "rand", or str made of "R", "O", "T", "S", "C", or "I".
    # Input 4 : "rand", or str made of "F", "B", "I", "O"
    # Input 5 : "rand", or str made of "w", "n"
    # Input 6 : "rand", or str made of P/B/b/C/F/H/J/R/S/s/L.
    blank = {
        "length": 0,    # 1 = 0-1 handspans, 2 = 1-2 handspans, 3 = 2-3 handspans, 4 = 3+ handspans.
        "curl": 0,      # 1 = straight, 2 = up to 45 degrees, 3 = 90 degrees +/- 45, 4 = S-curve
                        # 5 = 180 +/- 45, 6 = 270 +/- 45, 7 = 360 +/-45, 8 = ampora wave-like curves
        "radial": "",   # R = round, O = Oval, T = triangular, S = spiraling, C = C, I = Irregular
        "dir": "",      # Treat head like a compass; horn curl is point direction compared to base dir
                        # Face = F, Back = B, Towards top-center of head = I, towards shoulders = O.
        "width": "",    # w = wide, n = normal
        "tip": "",      # P(point), B(bump), b(branching), C(cone), F(flat), H(hook), J(jagged)
    }                   # R(round), S(split), s(spade), L(bolt),
    # Length
    length = int(random.randint(linmin, linmax) + lweight)
    if length > 4:
        length = 4
    if length < 1:
        length = 1
    # Curl
    curl = int(random.randint(cinmin, cinmax) + cweight)
    if curl > 8:
        curl = 8
    if curl < 0:
        curl = 0
    # Radial
    if radial == "rand":
        radial = "ROTSCI"
    temp3 = radial
    which = random.randint(0, len(radial) - 1)
    radial = temp3[which]
    # Dir
    if dir == "rand":
        dir = "FBIO"
    temp4 = dir
    which = random.randint(0, len(dir) - 1)
    dir = temp4[which]
    # Width
    if width == "rand":
        width = "wnnnnn"
    temp5 = width
    which = random.randint(0, len(width) - 1)
    dir = temp5[which]
    # Tip
    if tip == "rand":
        tip = "PBbCFHJRSsL"
    temp6 = tip
    which = random.randint(0, len(tip) - 1)
    tip = temp6[which]

    gene = blank

    gene["length"] = length
    gene["curl"] = curl
    gene["radial"] = radial
    gene["dir"] = dir
    gene["width"] = width
    gene["tip"] = tip
    return gene


# For single controls object
def genehcon(select="rand", stunt="rand", ttype="rand", angle="rand", noclip="rand", m1=0, m2=4, m3=0, m4=4, gaps="rand"):
    blank = {
        "select": "",   # XX, 23TDdXx, 1
        "stunt": "",    # XX, SsBbWwNn, ABCDEFGHIJKL
        "type": "",     # XX, KkEeAaPpBb
        "angle": "",    # XX, AA, AS/SA, SS.
        "noclip": "",   # XX, ABCDEFGHIJKL, X
        "mountpt": (1, 2),  # 0,0 = forehead, 2,4 = ear, (2,0) = top of head, (4,0) = back of head)
        "gaps": ""}     # XX,  NnHhOo, Xx
    # Meat
    gene = blank
    # Select
    if select == "rand":
        select = "123TDdXx"
    which1 = random.randint(0, len(select) - 1)
    which2 = random.randint(0, len(select) - 1)
    select = select[which1] + select[which2]
    # Stunt
    if stunt == "rand":
        stunt = "SsBbWwNnAAAAAAAAABBBBBBBBCCCCCCCCDDDDDDDEEEEEEFFFFFGGGGGHHHHIIIIJJJKKL"
    which1 = random.randint(0, len(stunt) - 1)
    which2 = random.randint(0, len(stunt) - 1)
    stunt = stunt[which1] + stunt[which2]
    # type
    if ttype == "rand":
        ttype = "PPPPPPPppBBBBBBBbbKkEEeeAa"
    which1 = random.randint(0, len(ttype) - 1)
    which2 = random.randint(0, len(ttype) - 1)
    which3 = random.randint(0, len(ttype) - 1)
    which4 = random.randint(0, len(ttype) - 1)
    which5 = random.randint(0, len(ttype) - 1)
    which6 = random.randint(0, len(ttype) - 1)
    which = which1 + which2 + which3 + which4 + which5 + which6
    ttype = ttype[which1] + ttype[which2] + ttype[which3] + ttype[which4] + ttype[which5] + ttype[which6]
    # angle
    if angle == "rand":
        angle = "AS"
    which1 = random.randint(0, len(select) - 1)
    which2 = random.randint(0, len(select) - 1)
    angle = angle[which1] + angle[which2]
    # noclip
    if noclip == "rand":
        noclip = "AAAAAAAAABBBBBBBBCCCCCCCCDDDDDDDEEEEEEFFFFFGGGGGHHHHIIIIJJJKKLXXXX"
    which1 = random.randint(0, len(select) - 1)
    which2 = random.randint(0, len(select) - 1)
    noclip = noclip[which1] + noclip[which2]
    # mountpt
    mountpt = (random.randint(m1, m2), random.randint(m3, m4))
    # gaps
    if gaps == "rand":
        gaps = "XXXXXXXXXXxxxxxNNnnHhOo"
    which1 = random.randint(0, len(select) - 1)
    which2 = random.randint(0, len(select) - 1)
    gaps = gaps[which1] + gaps[which2]

    gene["select"] = select
    gene["stunt"] = stunt
    gene["type"] = ttype
    gene["angle"] = angle
    gene["noclip"] = noclip
    gene["mountpt"] = mountpt
    gene["gaps"] = gaps
    return gene


# For a troll's full set of horns.
def genehorns(inp):
    # Blank
    blank = {
        "controls": {
            "type": "",     # XXXXXX, KkEeAaPpBb
            "select": "",   # XX, 23TDdXx, 1
            "stunt": "",    # XX, SsBbWwNn, ABCDEFGHIJKL
            "angle": "",    # XX, AA, AS/SA, SS.
            "noclip": "",   # XX, ABCDEFGHIJKL, X
            "mountpt": (0, 0),  # 0,0 = forehead, 2,4 = ear, (2,0) = top of head, (4,0) = back of head)
            "gaps": ""},    # X,  NnHhOo, Xx
        "left": {
            1: {"length": 0, "curl": 0, "radial": "", "dir": "", "width": "", "tip": ""},
            2: {"length": 0, "curl": 0, "radial": "", "dir": "", "width": "", "tip": ""},
            3: {"length": 0, "curl": 0, "radial": "", "dir": "", "width": "", "tip": ""}},
        "right": {
            1: {"length": 0, "curl": 0, "radial": "", "dir": "", "width": "", "tip": ""},
            2: {"length": 0, "curl": 0, "radial": "", "dir": "", "width": "", "tip": ""},
            3: {"length": 0, "curl": 0, "radial": "", "dir": "", "width": "", "tip": ""}}}
    # Primary Controls
    conrand = genehcon("rand", "rand", "rand", "rand", "rand", 0,4,0,4, "rand")
    conspec = genehcon("11", "ABCDEFGHIJKL", "PB", "SS", "ABCDEFGHIJKL", 1,2,1,3, "Xx")
    conside = genehcon("11", "ABCDEFGHIJKL", "PB", "SA", "ABCDEFGHIJKL", 1,3,2,4, "Xxoohn")
    coffspec = genehcon("123dx", "rand", "PPPPBBBBKE", "SA", "rand", 1,3,1,4, "rand")
    conmult = genehcon("dxdxDDDDDDT", "rand", "rand", "rand", "rand", 0,3,0,3, "rand")
    conwrong = genehcon("dxdxdxdxDDTX", "SsBbWwNnACDEFGHIJKL", "rand", "rand", "XADGJ", 0,4,0,4, "XxNnHhOo")

    # Primary Hornsets
    rand = {
        "left": {
            1: genehorn(0, 4, 0, 0, 8, 0, "rand", "rand", "rand", "rand"),
            2: genehorn(0, 4, 0, 0, 8, 0, "rand", "rand", "rand", "rand"),
            3: genehorn(0, 4, 0, 0, 8, 0, "rand", "rand", "rand", "rand")},
        "right": {
            1: genehorn(0, 4, 0, 0, 8, 0, "rand", "rand", "rand", "rand"),
            2: genehorn(0, 4, 0, 0, 8, 0, "rand", "rand", "rand", "rand"),
            3: genehorn(0, 4, 0, 0, 8, 0, "rand", "rand", "rand", "rand")}}
    standardup = {
        "left": {
            1: genehorn(2, 2, 0, 0, 2, 1, "R", "IIIIIIIO", "n", "PPPPPPPbHHHJRSSSsLL"),
            2: genehorn(1, 3, 1, 0, 3, 0, "RRRRRROOOTTCI", "FBIIIIO", "nnnnnnnw", "PPbHHJRSsL"),
            3: genehorn(1, 2, 0, 0, 4, 0, "RRRRRROOOTTCI", "FBIIIIO", "nnnnnnnw", "PPbFHHJRSsL")},
        "right": {
            1: genehorn(2, 2, 0, 0, 2, 1, "R", "IIIIIIIO", "n", "PPPPPPPbHHHJRSSSsLL"),
            2: genehorn(1, 3, 1, 0, 3, 0, "RRRRRROOOTTCI", "FBIIIIO", "nnnnnnnw", "PPbHHJRSsL"),
            3: genehorn(1, 2, 0, 0, 4, 0, "RRRRRROOOTTCI", "FBIIIIO", "nnnnnnnw", "PPbFHHJRSsL")}}
    miscwiggle = {
        "left": {
            1: genehorn(2, 3, 0, 2, 4, 0, "RRROI", "FBIIIO", "rand", "PPPPPPPBbCFHJRSsL"),
            2: genehorn(1, 4, 0, 2, 4, 0, "RRROTI", "FBIIO", "rand", "PPPPPBbCFHJRSsL"),
            3: genehorn(1, 4, 0, 1, 8, 0, "RRROTCI", "FBIIO", "rand", "PPPBbCFHJRSsL")},
        "right": {
            1: genehorn(2, 3, 0, 2, 4, 0, "RRROI", "FBIIIO", "rand", "PPPPPPPBbCFHJRSsL"),
            2: genehorn(1, 4, 0, 2, 4, 0, "RRROTI", "FBIIO", "rand", "PPPPPBbCFHJRSsL"),
            3: genehorn(1, 4, 0, 1, 8, 0, "RRROTCI", "FBIIO", "rand", "PPPBbCFHJRSsL")}}
    ram = {
        "left": {
            1: genehorn(2, 3, 0, 6, 7, 0, "RRRRROTC", "B", "nw", "PR"),
            2: genehorn(1, 4, 0, 5, 8, 0, "RRRRRROOOTTCI", "BBBBBBBOOIF", "nnw", "PR"),
            3: genehorn(1, 4, 0, 5, 8, 0, "RRRRRROOOTTCI", "BBBBBBBOOIF", "nnw", "PPbFHHJRSsL")},
        "right": {
            1: genehorn(2, 3, 0, 6, 7, 0, "RRRRROTC", "B", "nw", "PR"),
            2: genehorn(1, 4, 0, 5, 8, 0, "RRRRRROOOTTCI", "BBBBBBBOOIF", "nnw", "PR"),
            3: genehorn(1, 4, 0, 5, 8, 0, "RRRRRROOOTTCI", "BBBBBBBOOIF", "nnw", "PPbFHHJRSsL")}}
    bull = {
        "left": {
            1: genehorn(0, 4, 2, 3, 4, 0, "RO", "FFI", "rand", "PPPPRSLJ"),
            2: genehorn(0, 4, 2, 1, 5, 0, "ROTI", "FI", "rand", "PPPPRSLJFH"),
            3: genehorn(0, 4, 2, 1, 5, 0, "ROTI", "FBIO", "wn", "PPPPRSLJFH")},
        "right": {
            1: genehorn(0, 4, 2, 3, 4, 0, "RO", "FFI", "rand", "PPPPRSLJ"),
            2: genehorn(0, 4, 2, 1, 5, 0, "ROTI", "FI", "rand", "PPPPRSLJFH"),
            3: genehorn(0, 4, 2, 1, 5, 0, "ROTI", "FBIO", "wn", "PPPPRSLJFH")}}
    stabnub = {
        "left": {
            1: genehorn(1, 3, -1, 0, 1, 0, "ROTSC", "I", "wwwwwwn", "PPPPPPHJSL"),
            2: genehorn(1, 3, -1, 0, 2, 0, "ROTSC", "IO", "wwwnnn", "PPPPHHJJSL"),
            3: genehorn(1, 3, -1, 0, 4, 0, "ROTSCI", "FBIO", "wn", "PPHHHJJSSLL")},
        "right": {
            1: genehorn(1, 3, -1, 0, 1, 0, "ROTSC", "I", "wwwwwwn", "PPPPPPHJSL"),
            2: genehorn(1, 3, -1, 0, 2, 0, "ROTSC", "IO", "wwwnnn", "PPPPHHJJSL"),
            3: genehorn(1, 3, -1, 0, 4, 0, "ROTSCI", "FBIO", "wn", "PPHHHJJSSLL")}}
    swirl = {
        "left": {
            1: genehorn(2, 4, 0, 1, 8, 0, "TS", "IO", "wn", "PPPPPPPPPPPPPBHSsL"),
            2: genehorn(1, 4, 0, 1, 8, 0, "TSI", "IO", "wn", "PPPPPPPPPPPBHJSsL"),
            3: genehorn(1, 4, 0, 1, 8, 0, "TSI", "FBIO", "wn", "PPPPPPPBFHJRSsL")},
        "right": {
            1: genehorn(2, 4, 0, 1, 8, 0, "TS", "IO", "wn", "PPPPPPPPPPPPPBHSsL"),
            2: genehorn(1, 4, 0, 1, 8, 0, "TSI", "IO", "wn", "PPPPPPPPPPPBHJSsL"),
            3: genehorn(1, 4, 0, 1, 8, 0, "TSI", "FBIO", "wn", "PPPPPPPBFHJRSsL")}}

    # Meat
    gene = blank

    # Special presets
    if inp == "blank":
        gene = blank
        gene["controls"] = genehcon("blank")
    if inp == "rand":
        gene = rand
        gene["controls"] = conrand
    if inp == "standardup":
        gene = standardup
        gene["controls"] = conspec
    if inp == "ram":
        gene = ram
        gene["controls"] = coffspec
    if inp == "bull":
        gene = bull
        gene["controls"] = conside
    if inp == "swirl":
        gene = swirl
        gene["controls"] = coffspec
    if inp == "stabnub":
        gene = stabnub
        gene["controls"] = coffspec
    if inp == "mult":
        gene = rand
        gene["controls"] = conmult
    if inp == "wrong":
        gene = rand
        gene["controls"] = conwrong
    if inp == "lefty":
        gene = rand
        gene["controls"]["select"] = "xX"
    if inp == "righty":
        gene = rand
        gene["controls"]["select"] = "xX"
    if inp == "none":
        gene = rand
        gene["controls"]["select"] = "XX"
    if inp == "double":
        gene = rand
        gene["controls"]["select"] = randsel("DDDDd", 2)
    if inp == "triple":
        gene = rand
        gene["controls"]["select"] = randsel("TTTDd", 2)
    if inp == "uni":
        gene = rand
        gene["controls"] = conrand
        gene["controls"]["mountpt"] = (0, 0)
        gene["controls"]["select"] = "Xx"
        gene["right"][1]["curl"] = int(randsel("11111111111112222222233344567888"))
    if inp == "mohawk":
        gene = rand
        gene["controls"] = conrand
        gene["controls"]["mountpt"] = (1, 0)
        gene["left"][1]["curl"] = int(randsel("111111111111122222222333448"))
        gene["left"][2]["curl"] = int(randsel("111111111111122222222333448"))
        gene["left"][3]["curl"] = int(randsel("111111111111122222222333448"))
        gene["right"][1]["curl"] = int(randsel("111111111111122222222333448"))
        gene["right"][2]["curl"] = int(randsel("111111111111122222222333448"))
        gene["right"][3]["curl"] = int(randsel("111111111111122222222333448"))
        gene["controls"]["stunt"] = randsel("SsWwNnAaCcDdEeFfGg", 2)
        # Main castes section
    if inp == "RR":  # Maroon
        gene = ram
        gene["controls"] = conspec
        gene["controls"]["stunt"] = randsel("AA", 2)
        gene["controls"]["noclip"] = randsel("AA", 2)
    if inp == "Rr":
        gene = miscwiggle
        gene["controls"] = conside
        gene["controls"]["stunt"] = randsel("AB", 2)
        gene["controls"]["noclip"] = randsel("ABX", 2)
    if inp == "rr":  # Bronze
        gene = bull
        gene["controls"] = conside
        gene["controls"]["stunt"] = randsel("BB", 2)
        gene["controls"]["noclip"] = randsel("BB", 2)
    if inp == "rG":
        gene = miscwiggle
        gene["controls"] = coffspec
        gene["controls"]["stunt"] = randsel("BC", 2)
        gene["controls"]["noclip"] = randsel("BCX", 2)
        gene["controls"]["select"] = randsel("xddddddDDt", 2)
    if inp == "RG":  # Gold
        gene = standardup
        gene["controls"] = conspec
        gene["controls"]["stunt"] = randsel("CC", 2)
        gene["controls"]["noclip"] = randsel("CCCCCCX", 2)
        gene["controls"]["select"] = randsel("xdDDDDDDDDT", 2)
    if inp == "Rg":
        gene = miscwiggle
        gene["controls"] = coffspec
        gene["controls"]["stunt"] = randsel("CD", 2)
        gene["controls"]["noclip"] = randsel("CDX", 2)
        gene["controls"]["select"] = randsel("xxxddddDDt", 2)
    if inp == "rg":  # Lime
        gene = standardup
        if random.randint(1, 10) > 7:
            gene["left"][1]["tip"] = "p"
        if random.randint(1, 10) > 7:
            gene["right"][1]["tip"] = "p"
        gene["controls"] = conwrong
        gene["controls"]["stunt"] = randsel("DD", 2)
        gene["controls"]["noclip"] = randsel("DX", 2)
    if inp == "GG":  # Olive
        gene = stabnub
        gene["controls"] = conspec
        gene["controls"]["stunt"] = randsel("EE", 2)
        gene["controls"]["noclip"] = randsel("EE", 2)
    if inp == "Gg":
        gene = miscwiggle
        gene["controls"] = coffspec
        gene["controls"]["stunt"] = randsel("EF", 2)
        gene["controls"]["noclip"] = randsel("EFX", 2)
    if inp == "gg":  # Jade
        gene = standardup
        gene["controls"] = conspec
        gene["controls"]["stunt"] = randsel("FF", 2)
        gene["controls"]["noclip"] = randsel("FF", 2)
    if inp == "Gb":
        gene = miscwiggle
        gene["controls"] = coffspec
        gene["controls"]["stunt"] = randsel("FG", 2)
        gene["controls"]["noclip"] = randsel("FGX", 2)
    if inp == "GB":  # Teal
        gene = stabnub
        if random.randint(1, 10) > 3:
            gene["left"][1]["radial"] = "R"
        if random.randint(1, 10) > 3:
            gene["right"][1]["radial"] = "R"
        if random.randint(1, 10) > 7:
            gene["left"][1]["tip"] = "P"
        if random.randint(1, 10) > 7:
            gene["right"][1]["tip"] = "P"
        if random.randint(1, 10) < 3:
            gene["left"][1]["tip"] = "H"
        if random.randint(1, 10) < 3:
            gene["right"][1]["tip"] = "H"
        gene["controls"] = conspec
        gene["controls"]["stunt"] = randsel("GG", 2)
        gene["controls"]["noclip"] = randsel("GG", 2)
    if inp == "gB":
        gene = miscwiggle
        gene["controls"] = coffspec
        gene["controls"]["stunt"] = randsel("GH", 2)
        gene["controls"]["noclip"] = randsel("GHX", 2)
    if inp == "gb":  # Ceru
        gene = standardup
        if random.randint(1, 10) > 7:
            gene["left"][1]["tip"] = "p"
        if random.randint(1, 10) > 7:
            gene["right"][1]["tip"] = "p"
        gene["controls"] = conspec
        gene["controls"]["stunt"] = randsel("HH", 2)
        gene["controls"]["noclip"] = randsel("HH", 2)
    if inp == "BB":  # Bloo
        gene = standardup
        if random.randint(1, 10) > 5:
            gene["left"][1]["curl"] = 1
        if random.randint(1, 10) > 5:
            gene["right"][1]["curl"] = 1
        gene["controls"] = conspec
        gene["controls"]["stunt"] = randsel("II", 2)
        gene["controls"]["noclip"] = randsel("IIX", 2)
    if inp == "Bb":
        gene = miscwiggle
        gene["controls"] = coffspec
        gene["controls"]["stunt"] = randsel("IJ", 2)
        gene["controls"]["noclip"] = randsel("IJX", 2)
    if inp == "bb":  # Indigo
        gene = swirl
        gene["controls"] = conspec
        gene["controls"]["stunt"] = randsel("JJ", 2)
        gene["controls"]["noclip"] = randsel("JJ", 2)
    if inp == "rB":
        gene = miscwiggle
        if random.randint(1, 10) > 5:
            gene["left"][1]["radial"] = randsel("TS")
        if random.randint(1, 10) > 5:
            gene["right"][1]["radial"] = randsel("TS")
        gene["controls"] = coffspec
        gene["controls"]["stunt"] = randsel("JK", 2)
        gene["controls"]["noclip"] = randsel("JKX", 2)
    if inp == "RB":  # Violet
        gene = miscwiggle
        if random.randint(1, 10) > 5:
            gene["left"][1]["curl"] = int(randsel("1248"))
        if random.randint(1, 10) > 5:
            gene["right"][1]["curl"] = int(randsel("1248"))
        gene["controls"] = conspec
        gene["controls"]["stunt"] = randsel("KK", 2)
        gene["controls"]["noclip"] = randsel("KK", 2)
    if inp == "Rb":
        gene = miscwiggle
        if random.randint(1, 10) > 5:
            gene["left"][1]["curl"] = int(randsel("124"))
        if random.randint(1, 10) > 5:
            gene["right"][1]["curl"] = int(randsel("124"))
        gene["controls"] = coffspec
        gene["controls"]["stunt"] = randsel("KKKKL", 2)
        gene["controls"]["noclip"] = randsel("KKKKLXX", 2)
    if inp == "rb":  # Tyrian
        gene = standardup
        if random.randint(1, 10) > 5:
            gene["left"][1]["curl"] = int(randsel("12"))
        if random.randint(1, 10) > 5:
            gene["left"][1]["dir"] = randsel("OOOI")
        if random.randint(1, 10) > 5:
            gene["right"][1]["dir"] = randsel("OOOI")
        if random.randint(1, 10) > 5:
            gene["right"][1]["curl"] = int(randsel("12"))
        gene["controls"] = conspec
        gene["controls"]["stunt"] = randsel("KL", 2)
        gene["controls"]["noclip"] = randsel("KL", 2)
    return gene


# ------------------------------------
# Partially finished Zone
# ------------------------------------


# Incomplete
# needs bio functions for producing and blending these
def geneface():
    gene = {
        "hair": {"back": "", "mid": "", "line": "", "front": ""},
        "jawline": "",
        "cheek": "",
        "chin": "",
        "eyebrow": "",  # Move all eye bits to a subgene?
        "eyeshape": "",
        "eyelash": ""
    }
    return gene


# Incomplete
# needs bio functions for producing and blending these
def geneeyeobj():
    gene = {
        "active": "",       # eye present or unexpressed
        "shape": "",        # almond-shaped, narrow slits, big wide round, boxy
        "multipupil": "",   # multipupil?  Y/N?  PP = Y, all else = no
        "onecol": "",       # solid color eye?  CC = Y, all else = no
        "col": (0, 0, 0),   # color of glow / solid for this eye
        "glow": "",         # eye glow?
        "sym": "TT",        # symmetry, blend Y eyes together, N's together, Y's overwrite N's.
        "pupilnum": 1,      # number pupils in this eye
        "pupilshape": ""    # R = round, capital dominant, lowercase not dominant
                            # Octopus, goat, round, triangle, symbols, oval, slit pupil, diamond, star, ?
    }
    return gene


# Incomplete
# needs bio functions for producing and blending these
def geneeyes():
    gene = {
        "eye1": geneeyeobj(),
        "eye2": geneeyeobj(),
        "eye3": geneeyeobj(),
        "eye4": geneeyeobj(),
        "eye5": geneeyeobj(),
        "focus": "",            # nearsight, farsight, astigmatism
        "colorsense": "",       # red/green colorblind, tetrachromaticism, infravision, ultraviolet, etc.
        "movevision": "",       # How well the vision tracks movement
        "lightvision": "",      # Daylight sight, vs. eye damage taken from daylight
        "darkvision": "",       # How well see in the dark?
        "polarityvision": "",   # Can you see polarization of light?
        "xfoldvision": "",      # Fancy bullshit vision senses
        "independence": "",     # Can each eye move independently? (cross-eyed, lazy eye, gecko eye)
    }
    return gene


spectrumgeneseasocial = {
    "RR": genesea("land"),  # Maroon
    "Rr": genesea("land"),
    "rr": genesea("land"),  # Bronze
    "Rg": genesea("land"),
    "RG": genesea("land"),  # Gold
    "rG": genesea("land"),
    "rg": genesea("land"),  # Lime
    "GG": genesea("land"),  # Olive
    "Gg": genesea("land"),
    "gg": genesea("land"),  # Jade
    "Gb": genesea("land"),
    "GB": genesea("land"),  # Teal
    "gB": genesea("land"),
    "gb": genesea("land"),  # Ceru
    "BB": genesea("land"),  # Bloo
    "Bb": genesea("land"),
    "bb": genesea("land"),  # Indigo
    "rB": genesea("land"),
    "RB": genesea("sea"),  # Violet
    "Rb": genesea("sea"),
    "rb": genesea("sea"),  # Tyrian
    # No mutants listed.  This is what every caste is Expected to be.
    }

# Incorporate this into the Build.
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

# Replace this with dwell analysis of genestrand
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
    "mm": {"clout": 0, "acumen": 0, "grit": 0, "alacrity": 0,           # Mutant
           "hunch": 0, "resolve": 0, "moxie": 0, "psyche": 0, "pts": 2},

    "RR": {"clout": -1, "acumen": 0, "grit": 0, "alacrity": 0,          # Maroon
           "hunch": 2, "resolve": 0, "moxie": 0, "psyche": 1, "pts": 0},
    "Rr": {"clout": -1, "acumen": 0, "grit": 0, "alacrity": 0,  #
           "hunch": 1, "resolve": 0, "moxie": 1, "psyche": 1, "pts": 0},
    "rr": {"clout": -1, "acumen": 0, "grit": 0, "alacrity": 0,          # Bronze
           "hunch": 0, "resolve": 0, "moxie": 2, "psyche": 1, "pts": 0},
    "Rg": {"clout": -1, "acumen": 1, "grit": 0, "alacrity": 0,  #
           "hunch": 0, "resolve": 0, "moxie": 1, "psyche": 1, "pts": 0},
    "RG": {"clout": -1, "acumen": 1, "grit": 0, "alacrity": 0,          # Gold
           "hunch": 0, "resolve": 0, "moxie": 0, "psyche": 2, "pts": 0},
    "rG": {"clout": -1, "acumen": 1, "grit": 0, "alacrity": 0,  #
           "hunch": 0, "resolve": 0, "moxie": 0, "psyche": 2, "pts": 0},
    "rg": {"clout": -1, "acumen": 0, "grit": -1, "alacrity": 0,         # Lime
           "hunch": 0, "resolve": 0, "moxie": 0, "psyche": 3, "pts": 0},

    "GG": {"clout": 0, "acumen": 0, "grit": 0, "alacrity": 1,           # Olive
           "hunch": 1, "resolve": 0, "moxie": 0, "psyche": 0, "pts": 0},
    "Gg": {"clout": 0, "acumen": 0.25, "grit": 0.25, "alacrity": 0.25,  #
           "hunch": 0.25, "resolve": 0, "moxie": 0, "psyche": 0, "pts": 0},
    "gg": {"clout": 0, "acumen": 1, "grit": 1, "alacrity": 0,           # Jade
           "hunch": 0, "resolve": 0, "moxie": 0, "psyche": 0, "pts": 0},
    "Gb": {"clout": 0, "acumen": 1, "grit": 0.5, "alacrity": 0,  #
           "hunch": 0, "resolve": 0, "moxie": 0.5, "psyche": 0, "pts": 0},
    "GB": {"clout": 0, "acumen": 1, "grit": 0, "alacrity": 0,           # Teal
           "hunch": 0, "resolve": 0, "moxie": 1, "psyche": 0, "pts": 0},
    "gB": {"clout": 0, "acumen": 0.5, "grit": 0, "alacrity": 0,  #
           "hunch": 0.5, "resolve": 0, "moxie": 1, "psyche": 0, "pts": 0},
    "gb": {"clout": 0, "acumen": 0, "grit": 0, "alacrity": 0,           # Ceru
           "hunch": 1, "resolve": 0, "moxie": 1, "psyche": 0, "pts": 0},

    "BB": {"clout": 1, "acumen": 1, "grit": 0, "alacrity": -1,          # Bloo
           "hunch": 0, "resolve": 1, "moxie": 0, "psyche": 0, "pts": 0},
    "Bb": {"clout": 1, "acumen": 0, "grit": 1, "alacrity": 0,  #
           "hunch": 0, "resolve": 1, "moxie": -1, "psyche": 0, "pts": 0},
    "bb": {"clout": 1, "acumen": -1, "grit": 1, "alacrity": 0,          # Indigo
           "hunch": 0, "resolve": 1, "moxie": 0, "psyche": 0, "pts": 0},
    "rB": {"clout": 1, "acumen": 0, "grit": 1, "alacrity": 0,  #
           "hunch": 0, "resolve": 1, "moxie": -1, "psyche": -1, "pts": 0},
    "RB": {"clout": 1, "acumen": 0, "grit": 1, "alacrity": 0,           # Violet
           "hunch": 0, "resolve": 1, "moxie": 0, "psyche": -2, "pts": 0},
    "Rb": {"clout": 1, "acumen": 0, "grit": 1, "alacrity": 0,  #
           "hunch": 0, "resolve": 1, "moxie": 0, "psyche": -4, "pts": 0},
    "rb": {"clout": 1, "acumen": 0, "grit": 1, "alacrity": 0,           # Tyrian
           "hunch": 0, "resolve": 1, "moxie": 0, "psyche": -6, "pts": 0},
}

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
