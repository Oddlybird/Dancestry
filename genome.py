import random
import re
import colorsys
import colorgarbage as colg
import formattingbs as fbs
import names
import slurry
import traits  # gamelike stats


# Must stay in this file, things get silly if it moves to slurry
# Produces a troll dictionary object
def troll(introll=""):
    if introll == "":
        introll = premadeblood()
    blood = introll
    if introll == "blank":
        blood = "rr"
    bloodshort = blood[0:2]
    horns = {"": ""}
    sea = {"": ""}
    mouth = {"": ""}
    height = 0
    build = ""
    hair = ""
    skin = ""
    powers = ""
    firname = ""
    surname = ""
    sex = ""
    donator1 = ""
    donator2 = ""
    stats = traits.stats(bloodshort)
    if introll == "":
        sea = slurry.genesea(bloodshort)
        horns = slurry.genehorns(bloodshort)
        mouth = slurry.genemouth(bloodshort)
        height = slurry.spectrumheight[bloodshort]
        build = slurry.spectrumbuildtemp[bloodshort]
        hair = slurry.spectrumhairtemp[bloodshort]
        skin = slurry.spectrumskintemp[bloodshort]
        powers = slurry.spectrumpowerstemp[bloodshort]
        stats = traits.statdistrib(traits.stats(bloodshort))
        firname = "FIRNAM"
        surname = defaultnames(bloodshort)
        sex = "N"
        donator1 = "?.?"
        donator2 = "?.?"
    if introll != "" and introll != "blank":
        blood = introll.blood
        sea = introll.sea
        horns = introll["horns"]
        mouth = introll["mouth"]
        height = introll["height"]
        build = introll["build"]
        hair = introll["hair"]
        skin = introll["skin"]
        powers = introll["powers"]
        stats = introll["stats"]
        firname = introll["firname"]
        surname = introll["surname"]
        sex = introll["sex"]
        donator1 = introll["donator1"]
        donator2 = introll["donator2"]
    if introll == "blank":
        sea = slurry.genesea(introll)
        horns = slurry.genehorns(introll)
        mouth = slurry.genemouth(introll)
        height = slurry.spectrumheight[bloodshort]
        build = slurry.spectrumbuildtemp[bloodshort]
        hair = slurry.spectrumhairtemp[bloodshort]
        skin = slurry.spectrumskintemp[bloodshort]
        powers = slurry.spectrumpowerstemp[bloodshort]
        stats = traits.stats(bloodshort)
        firname = "FIRNAM"
        surname = "SURNAM"
        sex = "N"
        donator1 = "?.?"
        donator2 = "?.?"

    strhorns, strhornl, strhornr = describehorns2(horns)

    t0 = {
        "savetype": "12",  # Save Version
        "firname": firname,  # six letters
        "surname": surname,  # six letters
        "sex": sex,          # M/N/F
        "caste": getcastefromblood(blood),
        "dwell": slurry.spectrumdwell[blood],
        # Genes
        "blood": bloodshort,  # RGB rgb
        "stats": stats,
        "mouth": mouth,
        "sea": sea,
        "horns": horns,
        "powers": powers,  # psychic, voodoo, eldritch, none.  specify type later.
                           # Make psychics eyes glow colors?
        "height": height,                     # height in inches
        "heightstr":  heightstr(height),      # human-readable
        "build": build,   # more detailed data later
        "hair": hair,     # more detailed data later.  medium/long.
        "skin": skin,      # freckles, stripes, birthmarks, vitiligo, melanism, albinism, etc.
        # pawfeet, tail, wing, hairstreaks, grubscars, ?
        "donator1": donator1,   # higher caste donator
        "donator2": donator2,   # lower caste donator
#        "seadesc": describesea(blood, sea),
        "hornLdesc": strhornl,
        "hornRdesc": strhornr,
        "hornsdesc": strhorns,
    }
    return t0


# Also must stay here
def getpremadetroll(x=9001):
    if x == 9001:
        x = random.randint(1, 21)
    t0 = troll("blank")
    t0["blood"] = premadeblood()
    shortblood = t0["blood"][0:2]
    # Things that aren't really enabled yet.
    # Go through and give each troll a different one once the systems exist.
    if x == 1:  # Maroon
        t0["firname"] = "Normal"
        t0["blood"] = "RR"
    if x == 2:  # Bronze
        t0["firname"] = "Normal"
        t0["blood"] = "rr"
    if x == 3:  # Gold
        t0["firname"] = "Normal"
        t0["blood"] = "RG"
    if x == 4:  # Lime
        t0["firname"] = "Normal"
        t0["blood"] = "rg"
    if x == 5:  # Olive
        t0["firname"] = "Normal"
        t0["blood"] = "GG"
    if x == 6:  # Jade
        t0["firname"] = "Normal"
        t0["blood"] = "gg"
    if x == 7:  # Teal
        t0["firname"] = "Normal"
        t0["blood"] = "GB"
    if x == 8:  # Ceru
        t0["firname"] = "Normal"
        t0["blood"] = "gb"
    if x == 9:  # Bloo
        t0["firname"] = "Normal"
        t0["blood"] = "BB"
    if x == 10:  # Indigo
        t0["firname"] = "Normal"
        t0["blood"] = "bb"
    if x == 11:  # Violet
        t0["firname"] = "Normal"
        t0["blood"] = "RB"
    if x == 12:  # Tyrian
        t0["firname"] = "Normal"
        t0["blood"] = "rb"
    # Most traits get set to defaults based on blood
    shortblood = t0["blood"]
    shortblood = shortblood[0:2]
    t0["donator1"] = "The Mists"
    t0["donator2"] = "Of Time"
    t0["mouth"] = slurry.genemouth(shortblood)
    t0["horns"] = slurry.genehorns(shortblood)
    t0["height"] = slurry.spectrumheight[shortblood]
    t0["sea"] = slurry.genesea(shortblood)
    t0["sex"] = getsex(t0["blood"])
    t0["surname"] = defaultnames(shortblood)
    # These ones need to be redone when the relevant systems are remade
    t0["skin"] = slurry.spectrumskintemp[shortblood]
    t0["powers"] = slurry.spectrumpowerstemp[shortblood]
    t0["build"] = slurry.spectrumbuildtemp[shortblood]
    t0["hair"] = slurry.spectrumhairtemp[shortblood]
    t0["stats"] = traits.stats(shortblood)

    # Weird Mutants Ho; overwrite caste-based traits.
    if x == 13:
        t0["firname"] = "Lobbah"
        t0["surname"] = "Parkle"
        t0["sex"] = "N"
        t0["blood"] = "bbR"
        t0["sea"] = slurry.genesea("river")
        t0["mouth"] = slurry.genemouth("length2")
        t0["horns"] = slurry.genehorns("uni")
        t0["height"] = 72
        t0["powers"] = "Mutant"
        t0["build"] = "lanky"
        t0["hair"] = "matted"
    if x == 14:
        t0["firname"] = "Mutant"
        t0["horns"] = slurry.genehorns("rand")
    if x == 15:
        t0["firname"] = "Mutant"
        t0["horns"] = slurry.genehorns("bull")
    if x == 16:
        t0["firname"] = "Mutant"
        t0["horns"] = slurry.genehorns("Lefty")
    if x == 17:
        t0["firname"] = "Mutant"
        t0["horns"] = slurry.genehorns("triple")
    if x == 18:
        t0["firname"] = "Mutant"
        t0["horns"] = slurry.genehorns("ram")
    if x == 19:
        t0["firname"] = "Mutant"
        t0["horns"] = slurry.genehorns("wrong")
    if x == 20:
        t0["firname"] = "Mutant"
        t0["horns"] = slurry.genehorns("mult")
    if x == 21:
        t0["firname"] = "Mutant"
        t0["horns"] = slurry.genehorns("none")
    # Even mutants get descriptions based on their individual traits.
    t0["stats"] = slurry.spectrumcorestat[shortblood]
    t0["heightstr"] = heightstr(t0["height"])
    strhornsdesc, strhornl, strhornr = describehorns2(t0["horns"])
    t0["hornsdesc"] = strhornsdesc
    t0["hornLdesc"] = strhornl
    t0["hornRdesc"] = strhornr

    return t0


# Phenotype Classes, containing genes
#        - nested dict -

# genestrand: gender dimorphism, XY, build / body shape
# -- pearshaped, thin rectangle, hourglass, apple, dorito, ...
# -- seadwellers have slightly more fat, lowbloods often skinny
# -- presence/absence of chesticles, bias gender determination with this but not completely
# -- combine height into this
# -- hip, butt, shoulders, chest, waist.
# -- don't bother with X/Y genes.
# -- gender-biased height and musculature
# -- caste-biased height and musculature
# -- gender/caste biased fat stores

# genestrand: face structure, eye hollowness/bug-eyed, chin, nose, eyebrows, eyelashes
# genestrand: psychic, eldritch, voodoo, etc
# genestrand: feral traits - might require entire troll to be passed in so random shit can get altered?
# --- Make Sea into a thing that gets the entire troll passed in?
# genestrand: leg / arm mutations, extra legs/arms
# genestrand: hands/fingers, toes/feet
# genestrand: wings, tails, tentacles
# genestrand: epigenetics.  Contains blood + copies of epigenetic genes.  combine with organs?
# genestrand: organ systems, internal differences based on headcanons, genetic diseased/syndromes/mutations
#           - Vantas color mutation, 3 letters long.  "X" sets that 1 color to 0, another sets a color to 255.
# genestrand: discolorations (hair, skin, blood, hello karkat)
# genestrand: physical / mental stats, that effect traits / interests.
#             match trolls to occupations/interests similar to dwarf therapist
# genestrand: skin issues, scales/fur/feather patches, weird hair textures, strange claws
# ----------: misc other mutations?
# Below are the contents of what used to be called biology.py

# This file contains basic formatting information,
# Functions that are used to combine info from a slurry,
# Functions that manipulate / interact with troll data

# Produce a troll in a set color spectrum, with seeded donators, a seeded ancestor, or neither.
# -- If mutation : parameter that changes the weighting of individual variation vs caste traits
# -- If ancestor : add a pass at the end that sets parameters to make troll member of a Bloodline
def trollgen(kind="", spectrum=slurry.spectrumfull, p1="", p2=""):
    # You can get a decent troll by just going trollgen("mutant"), or trollgen("rand").
    # If some of the inputs are blank, replace them with other stuff.
    rp1 = 0
    rp2 = 0
    rindiv = 0
    rcaste = 0

    if kind == "dancestor":
        # Make a dancestor of p1.
        rp1 = 50        # dancestor/bloodline
        rp2 = 2         # random troll
        # set p2 = random
        rindiv = 99     # do not correct for caste
        rcaste = 1      # not one little bit
    if kind == "blend":
        # Make offspring of p1 and p2
        rp1 = 2     # input troll 1
        rp2 = 2     # input troll 2
        rindiv = 2  # individuality
        rcaste = 4  # caste norms
    if kind == "rand":
        # Generate an arbitrary troll from nothing.
        rp1 = 6     # Random troll
        # set p1 = random
        rp2 = 2     # Random Mutant
        # set p2 = random mutant
        rindiv = 2  # individuality
        rcaste = 6  # caste norms
    if kind == "mutant":
        # Generate an arbitrary troll from nothing.
        rp1 = 2     # Random Mutant
        # set p1 = random mutant
        rp2 = 2     # Random Mutant
        # set p2 = random mutant
        rindiv = 2  # individuality
        rcaste = 4  # caste norms

    # If p1/p2 are either still blank, or still bloodcodes,
    # replace them with default trolls      (of that color)
    if len(p1) < 4:
        p1 = troll(p1)
    if len(p2) < 4:
        p2 = troll(p2)

    # Call maketroll, with the adjusted arguments given above.
    t0 = maketroll(p1, rp1, p2, rp2, kind, rindiv, rcaste, spectrum)
    return t0


def maketroll(p1, rp1, p2, rp2, kind="", rindiv=2, rcaste=4, spectrum=slurry.spectrumfull):
    # Seed1 (donator1), rank-weighting
    # Seed2 (donator2), rank-weighting
    # kind ("dancestor", "blend", "rand", "mutant")
    # rindiv = weighting of individual traits
    # rcaste = weighting of caste-normal traits
    # spectrum = what blood codes the offspring is allowed to have

    # Open an arbitrary troll dict object
    t0 = troll("blank")

    # Donators:  List them appropriately, then load them directly into t0.
    troll1 = p1
    troll2 = p2
    if kind == "dancestor":
        t0["donator1"] = p1["firname"][0] + "." + p1["surname"]
        t0["donator2"] = "?.?"
    else:
        if troll1 == troll("blank"):
            troll1 = troll()
            p1 = troll1
        if troll2 == troll("blank"):
            troll2 = troll()
            p2 = troll2
        # guess that troll num 1 is higher caste
        caste1 = troll1["blood"]
        caste2 = troll2["blood"]
        if caste2 == highercaste(caste1, caste2):
            # if troll num 2 is higher caste, fix it.
            troll1 = p2
            troll2 = p1
        t0["donator1"] = troll1["firname"][0] + "." + p1["surname"]
        t0["donator2"] = troll2["firname"][0] + "." + p2["surname"]
    # End of donation

    # Make Blood
    a = 0
    bloodtempstr = ""
    if kind == "dancestor":             # 95% of the time, make blood match dancestor
        a = random.randint(1, 20)
        if a != 20:
            bloodtempstr = p1["blood"]
    if kind != "dancestor" or a == 20:  # if not dancestor, or if descendant is in the 5%. . .
        a = 0
        fail = 0
        while a < 12:  # You may try 12 times before autoset
            # create blood from donators
            b1 = p1["blood"]
            b2 = p2["blood"]
            i = random.randint(0, len(b1) - 1)  # p1blood, 1st or 2nd letter
            j = random.randint(1, len(b1) - 1)  # p1blood, 2nd or 3rd letter
            k = random.randint(0, len(b2) - 1)  # p2blood, 1st or 2nd letter
            l = random.randint(1, len(b2) - 1)  # p2blood, 2nd or 3rd letter

            bloodtemp = [b1[i], b1[j], b2[k], b2[l]]  # Load 4 letters into list
            random.shuffle(bloodtemp)                 # Shuffle them

            bloodtempstr = bloodtemp[0] + bloodtemp[1]  # Put 2 into a string
            bloodtempstr = bloodsort(bloodtempstr)      # Bloodsort it
            x = random.randint(1, 2)
            if x == 1:  # 50% chance of having a 3rd letter
                bloodtempstr = bloodtempstr + bloodtemp[2]

            # Now check if it is inside the spectrum, and break loop if so
            for arb in spectrum:
                if bloodtempstr == arb:
                    a = 9001
            # If that fails, increment loop.
            fail = fail + 1
            a = a + 1
        if fail >= 12:   # 12 failures = set to random member of spectrum
            bloodtempstr = random.choice(spectrum)
    t0["blood"] = bloodtempstr
    bloodshort = t0["blood"]
    bloodshort = bloodshort[0:2]  # A variable used to look things up in spectrums
    t0["caste"] = getcastefromblood(t0["blood"])
    # End of Blood Segment

    # Height
    if kind == "dancestor":
        compareheight = p1["height"]
        ph3 = 1
    if kind == "blend":
        ph1 = p1["height"] / slurry.spectrumheight[p1["blood"]]
        ph2 = p2["height"] / slurry.spectrumheight[p2["blood"]]
        ph3 = ph1 + ph2 / 2
        compareheight = slurry.spectrumheight[bloodshort]
    if kind == "mutant":
        ph1 = random.randint(85, 115)
        ph2 = random.randint(85, 115)
        ph3 = ph1 + ph2 / 2
        compareheight = slurry.spectrumheight[bloodshort]
    else:
        ph3 = random.randint(95, 105) / 100
        compareheight = slurry.spectrumheight[bloodshort]
    variance = random.randint(1, 4) - 2
    strheight = round(ph3 * compareheight) + variance
    t0["height"] = strheight
    t0["heightstr"]= heightstr(strheight)
    # End of Height

    # Sex
    a = 0
    if kind == "dancestor":
        a = random.randint(1, 20)
        if a != 20:
            t0["sex"] = p1["sex"]
    if kind != "dancestor" or a == 20:
        t0["sex"] = getsex(bloodshort)

    # Names
    if kind == "dancestor":
        t0["firname"] = names.newname()
        t0["surname"] = p1["surname"]
    else:
        t0["firname"] = names.newname()
        t0["surname"] = names.newname()
    # End of Names

    # Temporary Things that will be expanded later:
    # Thing      =                             Ancestor's thing, or a blood-based default Slurry thing
    t0["powers"] = tempinherit(kind, bloodshort, p1["powers"], slurry.spectrumpowerstemp)
    t0["build"] = tempinherit(kind, bloodshort, p1["build"], slurry.spectrumbuildtemp)
    t0["hair"] = tempinherit(kind, bloodshort, p1["hair"], slurry.spectrumhairtemp)
    t0["skin"] = tempinherit(kind, bloodshort, p1["skin"], slurry.spectrumskintemp)
    # End temporary

    # Stats
    t0["stats"] = traits.stats(bloodshort)
    # Gonna need more than this.
    # Eventually feed entire trolldict in there, and pick aptitudes for things.
    # Personality gunk too.
    # End stats

    # Sea
    geneindiv = slurry.genesea("blank")
    genecaste = slurry.genesea[bloodshort]
    weird = ["land", "sea", "deepsea", "river", "seahidden", "landsea", "sealand",
             "webbed", "bladder", "bodyfins", "nonviable"]
    if kind == "dancestor":
        geneindiv = p1["sea"]
        geneindiv = genecombine(geneindiv, slurry.genesea(random.choice(weird)), rp1, rp2)
    elif kind == "mutant":
        geneindiv = slurry.genesea(random.choice(weird))
        geneindiv = genecombine(geneindiv, slurry.genesea(random.choice(weird)))
        geneindiv = genecombine(geneindiv, slurry.genesea(random.choice(weird)))
    else:  # rand, blend
        geneindiv = genecombine(p1["sea"], p2["sea", rp1, rp2])
        geneindiv = genecombine(geneindiv, slurry.genesea(random.choice(weird)), 15, 1)
    # geneindiv is now the source of individuality.  Combine it with caste normal traits.
    t0["sea"] = genecombine(geneindiv, slurry.genesea(bloodshort), rindiv, rcaste)
#    t0["seadesc"] = describesea(bloodshort, t0["sea"])
    t0["dwell"] = describedwell(t0["sea"])
    # End of Sea

    # Mouth
    geneindiv = slurry.genemouth("blank")
    genecaste = slurry.genemouth[bloodshort]
    weird = ["allG", "allC", "allP", "length1", "length2", "sym1", "sym2"
             "low", "allC", "allP", "length1", "length2", "sym2", "low", "high", "high"]
    if kind == "dancestor":
        geneindiv = p1["mouth"]
        geneindiv = genecombine(geneindiv, slurry.genemouth(random.choice(weird)), rp1, rp2)
    elif kind == "mutant":
        geneindiv = slurry.genemouth(random.choice(weird))
        geneindiv = genecombine(geneindiv, slurry.genemouth(random.choice(weird)))
        geneindiv = genecombine(geneindiv, slurry.genemouth(random.choice(weird)))
    else:  # rand, blend
        geneindiv = genecombine(p1["mouth"], p2["mouth", rp1, rp2])
        geneindiv = genecombine(geneindiv, slurry.genemouth(random.choice(weird)), 15, 1)
    # geneindiv is now the source of individuality.  Combine it with caste normal traits.
    t0["mouth"] = genecombine(geneindiv, slurry.genemouth(bloodshort), rindiv, rcaste)
    t0["mouth"] = mouthaverager(t0["mouth"])
    # End of Mouth

    # Horns
    geneindiv = slurry.genehorns("blank")
    genecaste = slurry.genehorns[bloodshort]
    weird = ["rand", "standardup", "ram", "bull", "swirl", "stabnub", "mult", "wrong"
             "lefty", "righty", "none", "double", "triple", "uni", "mohawk"]
    if kind == "dancestor":
        geneindiv = p1["horns"]
        geneindiv = genecombine(geneindiv, slurry.genehorns(random.choice(weird)), rp1, rp2)
    elif kind == "mutant":
        geneindiv = slurry.genehorns(random.choice(weird))
        geneindiv = genecombine(geneindiv, slurry.genehorns(random.choice(weird)))
        geneindiv = genecombine(geneindiv, slurry.genehorns(random.choice(weird)))
    else:  # rand, blend
        geneindiv = genecombine(p1["horns"], p2["horns", rp1, rp2])
        geneindiv = genecombine(geneindiv, slurry.genehorns(random.choice(weird)), 15, 1)
    # geneindiv is now the source of individuality.  Combine it with caste normal traits.
    t0["horns"] = genecombine(geneindiv, slurry.genehorns(bloodshort), rindiv, rcaste)
    t0["horns"] = hornsetaverager(t0["horns"])
    t0["hornsdesc"], t0["hornLdesc"], t0["hornRdesc"] = describehorns2(t0["horns"])
    # End of Horns
    return t0


# Receive either the dancestor's data, or the caste data, or a small chance of neighboring castes.
def tempinherit(kind, blood, ancestral, caste):
    a = 0
    result = ""
    blood = blood[0:2]
    if kind == "dancestor":
        a = random.randint(1, 20)
        if a != 20:
            result = ancestral
    if kind != "dancestor" or a == 20:
        b = 0
        b = random.randint(1, 20)
        if b == 1:
            newblood = premadeblood()
            newblood = newblood[0:2]
            result = caste[newblood]
        elif b == 2 or b == 4 or b == 6 or b == 8:
            c = random.randint(1, 3)
            newblood = neighborcaste(blood, "-", c)
            newblood = newblood[0:2]
            result = caste[newblood]
        elif b == 3 or b == 5 or b == 7 or b == 9:
            c = random.randint(1, 3)
            newblood = neighborcaste(blood, "+", c)
            newblood = newblood[0:2]
            result = caste[newblood]
        else:
            result = caste[blood]
    return result


# Horn Zone
def randhorns(inblood="Rg"):
    outhorn = ""
    inblood = inblood[0:2]
    basehorn = slurry.genehorns(inblood)
    horn1 = genecombine(basehorn, slurry.genehorns(neighborcaste(inblood, "-", 1)))
    horn2 = genecombine(horn1, slurry.genehorns(neighborcaste(inblood, "+", 1)))
    randomhornset = ""
    a = random.randint(0, 20)
    if a == 1:
        randomhornset = slurry.genehorns("rand")
    if a == 2:
        randomhornset = slurry.genehorns("standardup")
    if a == 3:
        randomhornset = slurry.genehorns("ram")
    if a == 4:
        randomhornset = slurry.genehorns("bull")
    if a == 5:
        randomhornset = slurry.genehorns("swirl")
    if a == 6:
        randomhornset = slurry.genehorns("stabnub")
    if a == 7:
        randomhornset = slurry.genehorns("mult")
    if a == 8:
        randomhornset = slurry.genehorns("wrong")
    if a == 9:
        randomhornset = slurry.genehorns("none")
    if a == 10:
        randomhornset = slurry.genehorns("double")
    if a == 11:
        randomhornset = slurry.genehorns("triple")
    if a == 12:
        randomhornset = slurry.genehorns("uni")
    if a == 13:
        randomhornset = slurry.genehorns("mohawk")
    if randomhornset == "":
        randblood = premadeblood()
        randomhornset = slurry.genehorns(randblood[0:2])
    horn3 = genecombine(horn2, randomhornset, 15, 2)
    horn4 = genecombine(horn3, slurry.genehorns(inblood), 5, 2)
    outhorn = horn4
    return outhorn


# Input hornset
def hornblender(horna, hornb, strblood):
    horn1 = genecombine(horna, hornb)
    horn2 = hornsetaverager(horn1)
    horns = genecombine(horn2, slurry.genehorns[strblood[0:2]])
    outhorn = strblood
    while len(outhorn) < 3:
        outhorn = outhorn + "x"
    t0 = outhorn + horns[3:len(horns)]
    t1 = hornsetaverager(t0)
    return t1


# Input 2 individual horns at a time
def hornaverager(hornl, hornr):
    # average horns together some.
    e = random.randint(1, 3)
    # average length; 2/3 same length.
    if e == 1:
        hornl["length"] = hornr["length"]
    if e == 2:
        hornr["length"] = hornl["length"]
    # average curl, 2/3 same curl.
    e = random.randint(1, 3)
    if e == 1:
        hornl["curl"] = hornr["curl"]
    if e == 2:
        hornr["curl"] = hornl["curl"]
    # average Radial.  They WILL have the same cross section shape, it looks silly if they don't.
    e = random.randint(1, 2)
    if e == 1:
        hornl["radial"] = hornr["radial"]
    if e == 2:
        hornr["radial"] = hornl["radial"]
    # average dir, 2/3 chance of matching
    e = random.randint(1, 3)
    if e == 1:
        hornl["dir"] = hornr["dir"]
    if e == 2:
        hornr["dir"] = hornl["dir"]
    # average width :  2/3 chance the width will match.
    e = random.randint(1, 3)
    if e == 1:
        hornl["width"] = hornr["width"]
    if e == 2:
        hornr["width"] = hornl["width"]
    # average point, 2/5 chance of match
    e = random.randint(1, 5)  #
    if e == 1:
        hornl["tip"] = hornr["tip"]
    if e == 2:
        hornr["tip"] = hornl["tip"]
    return hornl, hornr


# Input 1 set horns in dict format.
def hornsetaverager(horns):
    hornsfinal = horns
    # blend horns one and two with eachother
    (hornsfinal["left"][1], hornsfinal["left"][2]) = hornaverager(horns["left"][1], horns["left"][2])
    (hornsfinal["right"][1], hornsfinal["right"][2]) = hornaverager(horns["right"][1], horns["right"][2])
    # blend horn 2 on each side with horn 3 of the opposite side
    (hornsfinal["right"][2], hornsfinal["left"][3]) = hornaverager(horns["right"][2], horns["left"][3])
    (hornsfinal["right"][3], hornsfinal["left"][2]) = hornaverager(horns["right"][3], horns["left"][2])
    # blend L1/R1, L2/R2, L3/R3
    (hornsfinal["left"][1], hornsfinal["right"][1]) = hornaverager(horns["left"][1], horns["right"][1])
    (hornsfinal["left"][2], hornsfinal["right"][2]) = hornaverager(horns["left"][2], horns["right"][2])
    (hornsfinal["left"][3], hornsfinal["right"][3]) = hornaverager(horns["left"][3], horns["right"][3])
    # These steps are in this order on purpose.  It will often take 2+ generations for new traits to bleed
    # from horn 3 down into the visible area.
    return hornsfinal


# Mouf
def mouthblender(mouth1, mouth2, basis):
    moutha = genecombine(mouth1, basis)
    mouthb = genecombine(mouth2, basis)
    mouth3 = genecombine(moutha, mouthb)
    return mouth3


# input one mouth dict
def mouthaverager(mg1):
    mg2 = mg1
    mg2["top"]["L"]["sym"] = genecombine(mg1["top"]["L"]["sym"], mg1["top"]["R"]["sym"])
    mg2["top"]["R"]["sym"] = genecombine(mg1["top"]["L"]["sym"], mg1["top"]["R"]["sym"])
    mg2["bot"]["L"]["sym"] = genecombine(mg1["bot"]["L"]["sym"], mg1["bot"]["R"]["sym"])
    mg2["bot"]["R"]["sym"] = genecombine(mg1["bot"]["L"]["sym"], mg1["bot"]["R"]["sym"])

    mg2["top"]["L"]["length"] = genecombine(mg1["top"]["L"]["length"], mg1["top"]["R"]["length"])
    mg2["top"]["R"]["length"] = genecombine(mg1["top"]["L"]["length"], mg1["top"]["R"]["length"])
    mg2["bot"]["L"]["length"] = genecombine(mg1["bot"]["L"]["length"], mg1["bot"]["R"]["length"])
    mg2["bot"]["R"]["length"] = genecombine(mg1["bot"]["L"]["length"], mg1["bot"]["R"]["length"])

    mg2["top"]["L"]["type"] = genecombine(mg1["top"]["L"]["type"], mg1["top"]["R"]["type"])
    mg2["top"]["R"]["type"] = genecombine(mg1["top"]["L"]["type"], mg1["top"]["R"]["type"])
    mg2["bot"]["L"]["type"] = genecombine(mg1["bot"]["L"]["type"], mg1["bot"]["R"]["type"])
    mg2["bot"]["R"]["type"] = genecombine(mg1["bot"]["L"]["type"], mg1["bot"]["R"]["type"])
    return mg2


# Caste
def getcastefromcolor(r, g, b):  # trolldeets
    (h, s, v) = colorsys.rgb_to_hsv(r, g, b)
    hue = h * 360
    hue = round(hue, 3)
    caste = "-"

    if 0 <= hue < 14:
        caste = "Maroon"
    if 14 <= hue < 25:
        caste = "M/B"
    if 25 <= hue < 37:
        caste = "Bronze"
    if 37 <= hue < 58:
        caste = "B/G"
    if 58 <= hue < 75:
        caste = "Gold"
    if 75 <= hue < 88:
        caste = "G/L"
    if 88 <= hue < 105:
        caste = "Lime"
    if 105 <= hue < 118:
        caste = "L/O"
    if 118 <= hue < 135:
        caste = "Olive"
    if 135 <= hue < 148:
        caste = "O/J"
    if 148 <= hue < 165:
        caste = "Jade"
    if 165 <= hue < 178:
        caste = "J/T"
    if 178 <= hue < 195:
        caste = "Teal"
    if 195 <= hue < 208:
        caste = "T/C"
    if 208 <= hue < 225:
        caste = "Ceru"
    if 225 <= hue < 238:
        caste = "C/B"
    if 238 <= hue < 255:
        caste = "Blue"
    if 255 <= hue < 268:
        caste = "B/I"
    if 268 <= hue < 285:
        caste = "Indigo"
    if 285 <= hue < 298:
        caste = "I/V"
    if 298 <= hue < 315:
        caste = "Violet"
    if 315 <= hue < 328:
        caste = "V/T"
    if 328 <= hue < 345:
        caste = "Tyrian"
    if 345 <= hue < 361:
        caste = "T/M"

    if (r, g, b) == (255, 0, 0):
        caste = "CULL"
    return caste


def getcastefromblood(innie):
    (r, g, b) = colg.bloodtorgb(innie)
    caste = getcastefromcolor(r, g, b)
    return caste


def getcastenum(b):
    (cr, cg, cb) = colg.bloodtorgb(b)
    (h, s, v) = colorsys.rgb_to_hsv(cr, cg, cb)
    hue = h * 360
    hue = round(hue)
    val = v / 100
    caste = round(hue + val, 2)
    return caste


def getcastenumstr(b):
    caste = getcastenum(b)
    caste = round(caste)
    caste = str(caste)
    caste = caste.zfill(5)
    return caste


def highercaste(blood1, blood2):
    # input two bloods, return the higher caste.
    caste1 = getcastenum(blood1)
    caste2 = getcastenum(blood2)
    bloodhigher = blood1  # By default assume the first is higher.
    if caste2 > caste1:  # ..but if it's not, fix that.
        bloodhigher = blood2
    return bloodhigher


def neighborcaste(blood, dir="+", number=1):
    castes = {"RR": 0, "Rr": 1, "rr": 2, "rG": 3, "RG": 4, "Rg": 5, "rg": 6, "GG": 7, "Gg": 8, "gg": 9, "Gb": 10,
              "GB": 11, "gB": 12, "gb": 13, "BB": 14, "Bb": 15, "bb": 16, "rB": 17, "RB": 18, "Rb": 19, "rb": 20,
              }
    givencaste = castes[blood[0:2]]
    if blood == "Cull":
        givencaste = 5
    # Define target we're trying to get to
    targetcaste = -1
    if dir == "+":
        targetcaste = givencaste + number
    if dir == "-":
        targetcaste = givencaste - number
    while targetcaste < 0:
        targetcaste = targetcaste + 20
    while targetcaste > 20:
        targetcaste = targetcaste - 20
    # Find the text version of the number in targetcaste
    neighbor = 0
    for x in castes:
        if castes[x] == targetcaste:
            neighbor = x
    return neighbor


# Blood
def bloodsort(blood):
    a = 0  # count the number of letters stripped out
    sortedblood = ""  # sorted blood code
    for arb in blood:  # for each letter...
        if arb == "R":
            sortedblood = sortedblood + "R"
            a = a + 1
        if a == len(blood) + 1:
            break
    for arb in blood:  # for each letter...
        if arb == "r":
            sortedblood = sortedblood + "r"
            a = a + 1
        if a == len(blood) + 1:
            break
    for arb in blood:  # for each letter...
        if arb == "G":
            sortedblood = sortedblood + "G"
            a = a + 1
        if a == len(blood) + 1:
            break
    for arb in blood:  # for each letter...
        if arb == "g":
            sortedblood = sortedblood + "g"
            a = a + 1
        if a == len(blood) + 1:
            break
    for arb in blood:  # for each letter...
        if arb == "B":
            sortedblood = sortedblood + "B"
            a = a + 1
        if a == len(blood) + 1:
            break
    for arb in blood:  # for each letter...
        if arb == "b":
            sortedblood = sortedblood + "b"
            a = a + 1
        if a == len(blood) + 1:
            break
    return sortedblood


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
    blood = bloodsort(blood)
    x = random.randint(1, 4)
    if x > 2:
        blood = blood + getoneblood()
    return blood


# Misc Surface details (and description functions?)
def getsex(blood):
    sex = " "
    x = random.randint(1, 10)
    if x < 4:
        sex = "M"
    if 4 <= x <= 6:
        sex = "N"
    if x > 6:
        sex = "F"

    (rgb1, rgb2, rgb3) = colg.bloodtorgb(blood)
    hue = colg.rgbtohue(rgb1, rgb2, rgb3)

    x = random.randint(1, 100)
    # jades (hue 150) are more likely to be female.
    if 140 < hue < 160 and x < 25:
        if sex == "N":
            sex = "F"
        if sex == "M":
            sex = "N"
    if 145 < hue < 155 and x < 75:
        if sex == "N":
            sex = "F"
        if sex == "M":
            sex = "N"
    # tyrians (330) are more likely to be female.
    if 320 < hue < 340 and x < 25:
        if sex == "N":
            sex = "F"
        if sex == "M":
            sex = "N"
    if 325 < hue < 335 and x < 75:
        if sex == "N":
            sex = "F"
        if sex == "M":
            sex = "N"
    return sex


def heightstr(h):
    h = int(h)
    feet = h // 12
    inches = h % 12
    hstr = str(feet) + "'" + str(inches)
    hstr = hstr + '"'
    return hstr


def describehorn(inhorn):
    temp = inhorn
    descr = ""
    # Length, default 2
    if temp["length"] == "1":
        descr = "short, "
    if temp["length"] == "4":
        descr = "long, "
    # Width, default n
    if temp["width"] == "w":
        descr = descr + "wide, "
    # Direction, default Inwards
    if temp["dir"] == "F":
        descr = descr + "front "
    if temp["dir"] == "B":
        descr = descr + "backswept "
    if temp["dir"] == "O":
        descr = descr + "outward "
    # curves, default = 2 (slightly curved)
    if temp["curl"] == "1":
        descr = descr + "straight "
    if temp["curl"] == "3":
        descr = descr + "curved "
    if temp["curl"] == "4":
        descr = descr + "S-curved "
    if temp["curl"] == "5":
        descr = descr + "curled "
    if temp["curl"] == "6":
        descr = descr + "curling "
    if temp["curl"] == "7":
        descr = descr + "coiled "
    if temp["curl"] == "8":
        descr = descr + "zig-jag "
    # tip shape
    if temp["tip"] == "B":
        descr = descr + "bump"
    if temp["tip"] == "b":
        descr = descr + "branching"
    if temp["tip"] == "C":
        descr = descr + "cone"
    if temp["tip"] == "F":
        descr = descr + "flat"
    if temp["tip"] == "H":
        descr = descr + "hook"
    if temp["tip"] == "J":
        descr = descr + "jagged"
    if temp["tip"] == "L":
        descr = descr + "bolt"
    if temp["tip"] == "P":
        descr = descr + "point"
    if temp["tip"] == "p":
        descr = descr + "pincher"
    if temp["tip"] == "R":
        descr = descr + "round"
    if temp["tip"] == "S":
        descr = descr + "split"
    if temp["tip"] == "s":
        descr = descr + "spade"
    descr = descr + "-tip "
    # radial, default round
    if temp["radial"] == "O":
        descr = descr + "oval horn"
    if temp["radial"] == "T":
        descr = descr + "edged horn"
    if temp["radial"] == "S":
        descr = descr + "twisting horn"
    if temp["radial"] == "I":
        descr = descr + "irregular horn"
    if temp["radial"] == "C":
        descr = descr + "half-circular horn"
    if temp["radial"] == "R":
        descr = descr + " horn"
        # strip spaces
        descr = re.sub(' +', ' ', descr)
        descr = descr.strip()
    return descr


# Remove, in favor of the graphics only version?
def describehorns2(inhorn):
    if inhorn == slurry.genehorns("blank"):
        me = slurry.genehorns("rand")
    else:
        me = inhorn

    descr = ""
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
    left = ""
    right = ""

    # Horn presence...
    sel = me["controls"]["select"]
    if sel == "TT":
        numhorns = 6
        hornleft1 = me["left"][1]
        hornleft2 = me["left"][2]
        hornleft3 = me["left"][3]
        hornright1 = me["right"][1]
        hornright2 = me["right"][2]
        hornright3 = me["right"][3]
        drh1 = True
        drh2 = True
        drh3 = True
        dlh1 = True
        dlh2 = True
        dlh3 = True
        descr = "tripled horns"
    if sel == "TD":
        numhorns = 5
        hornleft1 = me["left"][1]
        hornleft2 = me["left"][2]
        hornleft3 = me["left"][3]
        hornright1 = me["right"][1]
        hornright2 = me["right"][2]
        drh1 = True
        drh2 = True
        dlh1 = True
        dlh2 = True
        dlh3 = True
        descr = "3 left / 2 right horns"
    if sel == "DT":
        numhorns = 5
        hornleft1 = me["left"][1]
        hornleft2 = me["left"][2]
        hornright1 = me["right"][1]
        hornright2 = me["right"][2]
        hornright3 = me["right"][3]
        drh1 = True
        drh2 = True
        drh3 = True
        dlh1 = True
        dlh2 = True
        descr = "3 right / 2 left horns"
    if sel == "Td":
        numhorns = 4
        hornleft1 = me["left"][1]
        hornleft2 = me["left"][2]
        hornleft3 = me["left"][3]
        hornright1 = me["right"][1]
        drh1 = True
        dlh1 = True
        dlh2 = True
        dlh3 = True
        descr = "3 left / 1 right horn"
    if sel == "Td":
        numhorns = 4
        hornleft1 = me["left"][1]
        hornright1 = me["right"][1]
        hornright2 = me["right"][2]
        hornright3 = me["right"][3]
        drh1 = True
        drh2 = True
        drh3 = True
        dlh1 = True
        descr = "3 right / 1 left horn"
    if sel == "DD":
        numhorns = 4
        hornleft1 = me["left"][1]
        hornleft2 = me["left"][2]
        hornright1 = me["right"][1]
        hornright2 = me["right"][2]
        drh1 = True
        drh2 = True
        dlh1 = True
        dlh2 = True
        descr = "doubled horns"
    if sel == "Dd":
        numhorns = 3
        hornleft1 = me["left"][1]
        hornleft2 = me["left"][2]
        hornright1 = me["right"][1]
        hornright2 = "none"
        drh1 = True
        dlh1 = True
        dlh2 = True
        descr = "a second left horn"
    if sel == "dD":
        numhorns = 3
        hornleft1 = me["left"][1]
        hornleft2 = "none"
        hornright1 = me["right"][1]
        hornright2 = me["right"][2]
        drh1 = True
        drh2 = True
        dlh1 = True
        descr = "a second right horn"
    if sel == "Xx":
        numhorns = 1
        hornright1 = me["right"][1]
        hornright2 = "none"
        hornleft1 = "none"
        hornleft2 = "none"
        drh1 = True
        descr = "no left horn"
    if sel == "xX":
        numhorns = 1
        hornleft1 = me["left"][1]
        hornright2 = "none"
        hornright1 = "none"
        hornleft2 = "none"
        dlh1 = True
        descr = "no right horn"
    if sel == "TX":
        numhorns = 3
        hornleft1 = me["left"][1]
        hornleft2 = me["left"][2]
        hornleft3 = me["left"][3]
        hornright1 = "none"
        hornright2 = "none"
        hornright3 = "none"
        descr = "just 3 left horns"
        dlh1 = True
        dlh2 = True
        dlh3 = True
    if sel == "XT":
        numhorns = 3
        hornright1 = me["right"][1]
        hornright2 = me["right"][2]
        hornright3 = me["right"][3]
        hornleft1 = "none"
        hornleft2 = "none"
        hornleft3 = "none"
        descr = "just 3 right horns"
        drh1 = True
        drh2 = True
        drh3 = True
    if sel == "DX":
        numhorns = 2
        hornleft1 = me["left"][1]
        hornleft2 = me["left"][2]
        hornright1 = "none"
        hornright2 = "none"
        descr = "just two left horns"
        dlh1 = True
        dlh2 = True
    if sel == "XD":
        numhorns = 2
        hornright1 = me["right"][1]
        hornright2 = me["right"][2]
        hornleft1 = "none"
        hornleft2 = "none"
        descr = "just two right horns"
        drh1 = True
        drh2 = True
    if sel == "XX":
        numhorns = 0
        hornright1 = "none"
        hornright2 = "none"
        hornleft1 = "none"
        hornleft2 = "none"
        descr = "no horns at all"
    if numhorns == 22:  # If the troll has the default number of horns
        dlh1 = True
        drh1 = True
        hornleft1 = me["left"][1]    # Set to default.  This also covers when
        hornright1 = me["right"][1]  # either of the genes given are "1"
        hornright2 = "none"
        hornleft2 = "none"
        numhorns = 2
        # Now, if any of the genes are 2's or 3's, overwrite appropriately:
    if sel[0] == "2":
        hornleft1 = me["left"][2]
    if sel[0] == "3":
        hornleft1 = me["left"][3]
    if sel[1] == "2":
        hornright1 = me["right"][2]
    if sel[1] == "3":
        hornright1 = me["right"][3]
    # hornright1, hornright2, hornleft1, hornleft2, and numhorns know what we're describing.
    # descr has a description of how many there are.
    if numhorns == 0:
        return "no horns at all", "none", "none"

    # Odd Mounting
    (mx, my) = me["controls"]["mountpt"]
    if my > 2:
        descr = fbs.lyst(descr, "sidemounted")
    if mx > 2:
        descr = fbs.lyst(descr, "backmounted")
    if my == 0 and numhorns == 1:
        descr = "a centered"
    if my == 0 and numhorns != 1:
        descr = str(numhorns) + " centered horn"
        if numhorns > 1:
            descr = descr + "s"

    # Horn stunting / overwriting
    mstunt = me["controls"]["stunt"]
    if mstunt[0] == "S":
        left = "stunted horn"
        if dlh2:
            left = "two stunted horns"
        if dlh3:
            left = "three stunted horns"
    if mstunt[1] == "S":
        right = "stunted horn"
        if drh2:
            right = "two stunted horns"
        if drh3:
            right = "three stunted horns"
    if mstunt[0] == "B":
        left = "blunted, "
    if mstunt[1] == "B":
        right = "blunted, "
    if mstunt[0] == "W":
        left = "withered, "
    if mstunt[1] == "W":
        right = "withered, "
    if mstunt[0] == "N":
        left = "nub horn"
        if dlh2:
            left = "two nub horns"
            if dlh3:
                left = "three nub horns"
        dlh1 = False
        dlh2 = False
        dlh3 = False
    if mstunt[1] == "N":
        right = "nub horn"
        if drh2:
            right = "two nub horns"
            if drh3:
                right = "three nub horns"
        drh1 = False
        drh2 = False
        drh3 = False

    # Horn type
    ht = ""
    if me["controls"]["type"][0] == "K" or me["controls"]["type"][1] == "K":
        ht = ht + "/Keratin"
    if me["controls"]["type"][0] == "E" or me["controls"]["type"][1] == "E":
        ht = ht + "/Electrosensory"
    if me["controls"]["type"][0] == "A" or me["controls"]["type"][1] == "A":
        ht = ht + "/Antler"
    if me["controls"]["type"][0] == "P" or me["controls"]["type"][1] == "P":
        ht = ht + "/Power"
    if me["controls"]["type"][0] == "B" or me["controls"]["type"][1] == "B":
        ht = ht + "/Balance"
    if ht != "":
        descr = fbs.lyst(descr, ht[1:len(ht)])

    # Angularity
    if me["controls"]["angle"] == "A":
        descr = fbs.lyst(descr, "Angular")
    if me["controls"]["angle"] == "S":
        descr = fbs.lyst(descr, "Smoothly-curved")
    if me["controls"]["angle"] == "B":
        descr = fbs.lyst(descr, "Smooth and Angled")

    # Self-impact test.
    if me["controls"]["noclip"] == "X":
        descr = fbs.lyst(descr, "Potentially clipping")
#    To be in danger, must have X gene, * and *horns shaped in a way that can impact.
#    - spiraling: treat curl as 1 greater than it actually is.
#    - All Curl > 5
#    - Inward,with curl > 2 and length > 1.
#    - Outward, curl > 180 degrees, length > 2
#    - Back direction, curl > 1, length > 1.
#    - side + wide = ear deformity
#    - front + wide = forehead deformity
#    - Side + in = mild skull deformities.


    # Gaps
    gaps = me["controls"]["gaps"]
    if gaps == "NN" or gaps == "Nn" or gaps == "nN" or gaps == "Nh" or gaps == "hN":
        descr = fbs.lyst(descr, "a notch")
    if gaps == "nn" or gaps == "nh":
        descr = fbs.lyst(descr, "small notches")
    if gaps == "HH" or gaps == "Hh" or gaps == "hH" or gaps == "Hn" or gaps == "nH":
        descr = fbs.lyst(descr, "a hole")
    if gaps == "hh" or gaps == "hn":
        descr = fbs.lyst(descr, "small holes")
    if gaps == "OO" or gaps == "Oo" or gaps == "oO":
        descr = fbs.lyst(descr, "hollow")
    if gaps == "oo" or gaps == "oh" or gaps == "on" or gaps == "ho" or gaps == "no":
        descr = fbs.lyst(descr, "porous")

    # Actual horn descriptions go here...
    if dlh1:  # If there's a left horn...
        if hornleft1 != "none":
            left = describehorn(hornleft1)
        if dlh2 and left[0:3] != "two" and left[0:5] != "three" and hornleft2 != "none":
            hornleft2["length"] = 1
            temp = "+ a " + describehorn(hornleft2)
            left = fbs.lyst(left, temp)
        if dlh3 and left[0:3] != "two" and left[0:5] != "three" and hornleft3 != "none":
            hornleft3["length"] = 1
            temp = "+ a " + describehorn(hornleft3)
            left = fbs.lyst(left, temp)
    if drh1:  # If there's a right horn...
        if hornright1 != "none":
            right = describehorn(hornright1)
        if drh2 and right[0:3] != "two" and right[0:5] != "three" and hornright2 != "none":
            hornright2["length"] = 1
            temp = "+ a " + describehorn(hornright2)
            right = fbs.lyst(right, temp)
        if drh3 and right[0:3] != "two" and right[0:5] != "three" and hornright3 != "none":
            hornright3["length"] = 1
            temp = "+ a " + describehorn(hornright3)
            right = fbs.lyst(right, temp)

    return descr, left, right


# Currently not in use.  Remove/alter, replace with graphics.
def describesea(bloodcode, sea):    # slurry.spectrumgenesea, blood[0:2]
    if sea == slurry.genesea("blank"):
        me = slurry.genesea("land")
    else:
        me = sea

    blood = bloodcode[0:2]
    mc = me["controls"]
    cd = slurry.genesea(blood)        # Caste default
#    cc = cd["controls"]
    done = False
    descr = ""
    earfins = ""
    webbing = ""
    gills = ""
    breathes = ""
    bladders = ""
    biolum = ""
    teeth = ""
    eyelids = ""
    bodyfins = ""

    while not done:
        # If someone is arbitrarily set to caste-typical
        if mc[0] == "SS" and mc[1] == "SS" and mc[2] == "SS" and mc[3] == "SS" and mc[4] == "SS":
            dwellvar = slurry.spectrumdwell[blood]
            if dwellvar != "seadweller":
                dwellvar = me.dwell()
            descr = dwellvar
            return descr
        if mc[0] == "ss" and mc[1] == "ss" and mc[2] == "ss" and mc[3] == "ss" and mc[4] == "ss":
            dwellvar = slurry.spectrumdwell[blood]
            if dwellvar != "landdweller":
                dwellvar = me.dwell()
            descr = dwellvar
            return descr
        # If someone cannot breathe at all
        if me["air"] == "aaaa" and mc[1] != "ss" and mc[1] != "SS":
            if me["gillface"]["main"] == "gg" and me["gillneck"]["main"] == "gg" and me["gillribs"]["main"] == "gg":
                descr = "no gills, cannot breathe air"
                return descr
            if me["salt"] == "sbf":
                descr = "cannot breathe air or water"
                return descr
        break

    # Below this point, everyone has Ss or sS, at least one noteworthy difference from cd, and can breathe.
    # Things that add descriptions to the list, but do not end the loop
    if me["air"] != "AAAA" and me["air"] != "aaaa":
        if countaa(me["air"]) > 1:
            descr = descr + "rank " + str(countaa(me["air"]) - 1) + " airless"

    # Epigene #1
    if mc[0] == "Ss" or mc[0] == "sS":  # Webbing, Earfins.
        # limb webbing?  Neck webs?
        # fingers
        fingers = genedesc1(me["wfingers"], cd["wfingers"], "W", "deeply webbed fingers", "w", "unwebbed fingers", "webbed fingers")
        if fingers == "":
            fingers = "xxx"
        # toes
        toes = genedesc1(me["wtoes"], cd["wtoes"], "W", "deeply webbed toes", "w", "unwebbed toes", "webbed toes")
        if toes == "":
            toes = "xxx"
        # webbing combo
        webbing = ""
        # If either is caste-normal:
        if fingers == "xxx" and toes != "xxx":
            webbing = toes
        if toes == "xxx" and fingers != "xxx":
            webbing = fingers
        # if both are abnormal:
        if toes != "xxx" and fingers != "xxx":
            webbing = fingers + " and " + toes
        # if both are abnormal in the same way
        if fingers[0] == "u" and toes[0] == "u":
            webbing = "unwebbed fingers and toes"
        if fingers[0] == "d" and toes[0] == "d":
            webbing = "deeply webbed fingers and toes"
        if fingers[0] == "w" and toes[0] == "w":
            webbing = "webbed fingers and toes"
        # If both are differently webbed
        if fingers[0] == "d" and toes[0] == "w":
            webbing = "webbed toes and deeply webbed fingers"

        # ears, cheekfins, and earfins
        ears = genedesc1(me["ears"], cd["ears"], "E", "full ears", "e", "no ears", "gimpy ears")
        if ears == "":
            ears = "xxx"
        cheekfins = genedesc1(me["cheekfins"], cd["cheekfins"], "C", "fins", "c", "no cheekfins", "gimpy cheekfins")
        if cheekfins == "":
            cheekfins = "xxx"
        # earfins combo
        earfins = ""
        # If either is caste-normal:
        if cheekfins == "xxx" and ears != "xxx":
            earfins = ears
        if ears == "xxx" and cheekfins != "xxx":
            earfins = cheekfins
        # if both are abnormal:
        if ears != "xxx" and cheekfins != "xxx":
            earfins = cheekfins + " and " + ears
        # if both are abnormal in the same way
        if cheekfins[0] == "n" and ears[0] == "n":
            earfins = "no fins or ears"
        if cheekfins[0] == "f" and ears[0] == "f":
            earfins = "full fins and ears"
        if cheekfins[0] == "g" and ears[0] == "g":
            earfins = "gimpy earfins"
        # If both are differently webbed
        if cheekfins[0] == "f" and ears[0] == "g":
            earfins = "earlike fins"
        if cheekfins[0] == "g" and ears[0] == "f":
            earfins = "finlike ears"
    if me.SS[1] == "S":  # Gills and breathing
        # gilltypes
        gillnecktype = ""
        if me["gillneck"]["type"] != cd["gillneck"]["type"]:
            if me["gillneck"]["type"] == "i":
                gillnecktype = "internal"
            if me["gillneck"]["type"] == "e":
                gillnecktype = "external"
        gillribstype = ""
        if me["gillribs"]["type"] != cd["gillribs"]["type"]:
            if me["gillribs"]["type"] == "i":
                gillribstype = "internal"
            if me["gillribs"]["type"] == "e":
                gillribstype = "external"
        gillfacetype = ""
        if me["gillface"]["type"] != cd["gillface"]["type"]:
            if me["gillface"]["type"] == "i":
                gillfacetype = "internal"
            if me["gillface"]["type"] == "e":
                gillfacetype = "external"
        # neckgills
        gillneck = genedesc1(me["gillneck"]["main"], cd["gillneck"]["main"], "G", "full ", "g", "no ", "partial ")
        if gillneck[0:2] != "no" and gillneck != "":
            gillneck = gillneck + gillnecktype + " neckgills"
            if me["gillneck"]["main"] == cd["gillneck"]["main"]:
                gillneck = gillnecktype + " neckgills"
        if gillneck[0:2] == "no":
            gillneck = "no neckgills"
        # rib gills
        gillribs = genedesc1(me["gillribs"]["main"], cd["gillribs"]["main"], "G", "full ", "g", "no ", "partial ")
        if gillribs[0:2] != "no" and gillribs != "":
            gillribs = gillribs + gillribstype + " rib gills"
            if me["gillribs"]["main"] == cd["gillribs"]["main"]:
                gillribs = gillribstype + " rib gills"
        if gillneck[0:2] == "no":
            gillneck = "no rib gills"
        # face gills
        gillface = genedesc1(me["gillface"]["main"], cd["gillface"]["main"], "G", "full ", "g", "no ", "partial ")
        if gillface[0:2] != "no" and gillface != "":
            gillface = gillface + gillfacetype + " facegills"
            if me["gillface"]["main"] == cd["gillface"]["main"]:
                gillface = gillfacetype + " facegills"
        if gillface[0:2] == "no":
            gillface = "no facegills"
        # gill summary!
        gills = ""
        # If at least one gill area is noteworthy in some way...
        if gillneck != "" or gillribs != "" or gillface != "":
            if gillneck != "":
                gills = fbs.lyst(gills, gillneck)
            if gillribs != "":
                gills = fbs.lyst(gills, gillribs)
            if gillribs != "":
                gills = fbs.lyst(gills, gillface)
            # Find ways to shorten this later maybe.  For now it works.
        # breathability
        breathes = ""
        if me["salt"] != cd["salt"] or me["air"] != cd["air"]:
            canb = ""
            cantb = ""
            ws = "salt water"
            wb = "brackwater"
            wf = "freshwater"
            wa = "air"
            if me["salt"][0] == "S":
                canb = fbs.lyst(canb, ws)
            if me["salt"][0] == "s":
                cantb = fbs.lyst(cantb, ws)
            if me["salt"][1] == "B":
                canb = fbs.lyst(canb, wb)
            if me["salt"][1] == "b":
                cantb = fbs.lyst(cantb, wb)
            if me["salt"][2] == "F":
                canb = fbs.lyst(canb, wf)
            if me["salt"][2] == "f":
                cantb = fbs.lyst(cantb, wf)
            if countaa(me["air"]) < 4:
                canb = fbs.lyst(canb, wa)
            if countaa(me["air"]) > 3:
                cantb = fbs.lyst(cantb, wa)
            if canb == "salt water, brackwater, freshwater":
                canb = "water"
            if cantb == "salt water, brackwater, freshwater":
                cantb = "water"
            breathes = "can breathe " + canb
            if cantb != "":
                breathes = breathes + ", but not " + cantb
            if gills == "" and me["salt"] == "sbf" and slurry.spectrumdwell[blood] != "landdweller":
                breathes = "breathes " + canb
            if gills == "" and me["salt"] == "SBF" and slurry.spectrumdwell[blood] != "seadweller":
                breathes = "breathes " + canb
    if mc[2] == "Ss" or mc[2] == "sS":  # Swimbladders.
        bladders = genedesc1(me["bladders"], cd["bladders"], "B", "swim bladders", "b", "no swim bladder", "a swim bladder")
    if mc[3] == "Ss" or mc[3] == "sS":  # Biolum and teeth.
        biolum = genedesc1(me["biolum"], cd["biolum"], "B", "biolum", "b", "no biolum", "partial biolum")
        # teeth
        # Replace or enhance this with caste-specific teeth and teeth mutation   But, for now ...
        teeth = ""
        if me["toothdouble"] != cd["toothdouble"]:
            if me["toothdouble"][2] == "D" and cd["toothdouble"][2] != "D":
                teeth = "doubled "
            if me["toothdouble"][2] == "d" and cd["toothdouble"][2] != "d":
                teeth = "undoubled "
            teeth = teeth + "teeth"
    if mc[4] == "Ss" or mc[4] == "sS":  # Eyelids and body fins
        eyelids = genedesc1(me["eyelids"], cd["eyelids"], "E", "nictating membranes", "e", "single eyelids", "transparent eye cover")
        bodyfins = genedesc1(me["dorsalfins"], cd["dorsalfins"], "F", "body fins", "f", "no body fins", "mini body fins")
    # Summing Up
    if mc[0] == "SS" or mc[0] == "sS" or mc[0] == "Ss":     # Skin
        descr = fbs.lyst(descr, earfins)
        descr = fbs.lyst(descr, webbing)
    if mc[1] == "SS" or mc[1] == "sS" or mc[1] == "Ss":     # Organ systems
        descr = fbs.lyst(descr, gills)
        descr = fbs.lyst(descr, breathes)
    if mc[2] == "SS" or mc[2] == "sS" or mc[2] == "Ss":     # ?
        descr = fbs.lyst(descr, bladders)
    if mc[3] == "SS" or mc[3] == "sS" or mc[3] == "Ss":     # ?
        descr = fbs.lyst(descr, biolum)
        descr = fbs.lyst(descr, teeth)
    if mc[4] == "SS" or mc[4] == "sS" or mc[4] == "Ss":     # ?
        descr = fbs.lyst(descr, eyelids)
        descr = fbs.lyst(descr, bodyfins)

    if descr.strip == "":
        descr = describedwell(cd)

    return descr


def describedwell(sea):
    self = sea
    cont = self["controls"]
    descr = "landdweller"
    if cont[0] == "ss" and cont[1] == "ss" and cont[2] == "ss" and cont[3] == "ss" and cont[4] == "ss":
        descr = "landdweller"
    if cont[0] == "SS" and cont[1] == "SS" and cont[2] == "SS" and cont[3] == "SS" and cont[4] == "SS":
        descr = "seadweller"
    else:
        descr = "beachdweller"
        if self["salt"] == "SBF":
            descr = "seadweller"
        if self["salt"] == "SBf":
            descr = "tidedweller"
        if self["salt"] == "Sbf":
            descr = "deepdweller"
        if self["salt"] == "sbF":
            descr = "riverdweller"
        if self["salt"] == "sBF":
            descr = "ponddweller"
        if self["salt"] == "sBf":
            descr = "deltadweller"
        if self["salt"] == "sbf":
            descr = "surfacedweller"
            # if surface dweller but no gills, landdweller.
            if self["gillface"]["main"] == "gg" and self["gillneck"]["main"] == "gg" and self["gillribs"]["main"] == "gg":
                descr = "landdweller"

    descr = descr.strip()
    if self["air"] == "aaaa":
        descr2 = "non-air " + descr
        descr = descr2
# For now; dweller doesn't need to mention asthma.
#    if self.air != "aaaa" and self.air != "AAAA" and self.SS != "ss" and self.SS != "SS":
#        if countaa(self.air) > 1:
#            descr2 = "breathshort " + descr
#            descr = descr2
    descr = descr.strip()
    return descr


# Gene-level combos and counters
def countaa(inhale):
    a = 0
    if inhale[0] == "a":
        a = a + 1
    if inhale[1] == "a":
        a = a + 1
    if inhale[2] == "a":
        a = a + 1
#    if inhale[3] == "a":
#        a = a + 1
    exhale = a
    return exhale


# Self-referential.
def genecombine(g1, g2, r1=2, r2=2):
    # Feed in the dicts to be combined, gene1 and gene2
    # Feed in the relative rarities (r1, r2), integers where higher = more likely
    # initialize gene3
    g3 = {"": ""}
    # Begin loop counter and loop
    for arb in g1:
        chancegene1 = random.randint(1, r1)  # Roll to see how likely gene1 is
        chancegene2 = random.randint(1, r2)  # same for               gene2
        # boolean
        if isinstance(g1[arb], bool):
            if chancegene1 >= chancegene2:
                g3[arb] = g1[arb]
            else:
                g3[arb] = g2[arb]
        # numbers
        if isinstance(g1[arb], int) or isinstance(g1[arb], float):
            g3[arb] = (g1[arb] + g2[arb]) // 2
        # strings
        if isinstance(g1[arb], str):
            str1 = g1[arb]
            str2 = g2[arb]
            desc = ""
            for x in g1[arb][x]:
                desc = ""
                chancegene1 = random.randint(1, r1)  # Roll to see how likely gene1 is
                chancegene2 = random.randint(1, r2)  # same for               gene2
                if chancegene1 >= chancegene2:
                    desc = desc + str1[x]
                else:
                    desc = desc + str2[x]
            g3[arb] = desc
        # lists, tuples, dicts
        if isinstance(g1[arb], tuple) or isinstance(g1[arb], list) or isinstance(g1[arb], dict):
            str1 = g1[arb]
            str2 = g2[arb]
            for arb2 in str1[arb2]:
                temp = genecombine(str1[arb2], str2[arb2], r1, r2)
                g3[arb][arb2] = temp

    return g3


def genedesc1(my, cy, a, atxt, b, btxt, abtxt, batxt=""):
    if batxt == "":
        batxt = abtxt
    txt = ""
    if my != cy:
        if my == a + a:
            txt = atxt
        if my == b + b:
            txt = btxt
        if my == a + b:
            txt = abtxt
        if my == b + a:
            txt = batxt
    return txt


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


# Move to slurry?
def defaultnames(inblood):
    blood = inblood[0:2]
    name = "Surnam"
    if blood == "RR":
        name = "Maroon"
    if blood == "Rr":
        name = "Marbro"
    if blood == "rr":
        name = "Bronze"
    if blood == "Rg":
        name = "Brogol"
    if blood == "RG":
        name = "-Gold-"
    if blood == "rG":
        name = "Gollim"
    if blood == "rg":
        name = "-Lime-"
    if blood == "GG":
        name = "Olive-"
    if blood == "Gg":
        name = "Olijad"
    if blood == "gg":
        name = "-Jade-"
    if blood == "Gb":
        name = "Jadtea"
    if blood == "GB":
        name = "-Teal-"
    if blood == "gB":
        name = "Teacer"
    if blood == "gb":
        name = "Cerule"
    if blood == "BB":
        name = "-Blue-"
    if blood == "Bb":
        name = "Bluind"
    if blood == "bb":
        name = "Indigo"
    if blood == "rB":
        name = "Indvio"
    if blood == "RB":
        name = "Violet"
    if blood == "Rb":
        name = "Viotyr"
    if blood == "rb":
        name = "Tyrian"
    return name


def eugenics(t0):
    return t0
