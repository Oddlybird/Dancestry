import random


def newname():
    working = ""
    # strucs contains the valid name structures.  assign one at random.
    # original strucs = ["PLOPOF", "PLOFFO", "PLONOF", "POPPOL", "POPFOF", "POFLOF", "POFLOF", "PONPLO", "PONFOO",
    # "PONNOP", "PONOPO", "PONOLO", "PONOLO", "POLPOP", "POLPOF", "POLOFO", "POLLON", "POLLOF", "POOPOF", "PLOFPO",
    # "FOFFOP", "FOFOLO", "FONPOF", "FOLPOP", "FOLLOP", "FOLLOF", "NOPPON", "NOPLON", "NOPOPO", "NOPONO", "NOPOLO",
    # "NOLLON", "NOONOF", "NOOLFO", "NOOLON", "LFOLON", "LOPOLO", "LOFOOF", "LOOPON", "OPLOOF", "OLOPOO", "OLOPON", "
    # OLONOO", "ONPOLO"]
    strucs = ["POFLOF", "POONON", "FOFFOL", "NOLFPO", "PONNOP", "FPOLLO", "FOPOLO", "PFOPOO", "FOPOPO", "FOLOPL",
              "POPLON", "POLOFO", "OFPOPO", "OLOPOO", "POFLOF", "FOLLOP", "POLPOP", "PONOLO", "LOFOOF", "NOPONO",
              "PONPLO", "POLPON", "PLONOP", "PLOPOF", "POPOLO", "FOLOOF", "FOOPOP", "PONNOP", "POLOPO", "LOPOPO",
              "LOOPNL", "PONPFO", "POLONO", "NOPLOL", "FOLNOP", "PFOLOP", "NOPOPO", "NOPLON", "POPPOL", "FONPOF",
              "NOPOPO", "NOPLON", "POPPOL", "FONPOF", "NOPFOF", "POPPOL", "PFOLON", "POLOPO", "POLPOL", "PONOOL",
              "POLOOO", "LONOLO", "LONFFO", "PLONOO", "LONPOO", "POFOOF", "POPOLO", "POLONO", "POPOLO", "FPOLFO",
              "NOLLOP", "OLLOLP", "OLPOPO", "LONOLO", "NOOLON", "POLLON", "LOPOLO", "OLONOO", "NOPOPO", "PONOOO",
              "POLOFO", "FLOFPO", "NOOLFO", "PLOPOP", "POOFOO", "LONOPO", "OPONOL", "PONPOP", "FPOLPO", "OPOOPO",
              "OLFONO", "PONPPO", "ONPOPP", "POLPOL", "POFONP", "POLPOP", "FOFOOP", "OPOLOF", "OLLOLP", "POLNOO",
              "NONOOP", "LOOPON", "NOLOON", "POLOPO", "FOLPOP", "LOOPON", "NOLOON", "POLOPO", "FOLPOP", "POLPOF",
              "NOFPOO", "ONOFOO", "POLOPF", "FOPLOF", "POLFON", "POOFLO", "PFOFOP", "NOLFOF", "POLOPO", "PLOFFO",
              "OPOOOF", "FOLOFF", "POLLOF", "PONFOO", "PLONOF", "OLOPON", "OONOFO", "FOFOLO", "NOPPON", "PLOPOO",
              "NOOLOF", "OLPOFN", "POPOFO", "POPOPP", "FOLOOL", "FOLOOL", "NOONOP", "POLOPO", "POOLOP", "POPFOF",
              "FOFFOP", "NOPOLO", "ONPOLO", "POOPOF", "FOFFOP", "NOPOLO", "ONPOLO", "POOPOF", "LFOLON", "POOFOP"]
    a = random.randint(0, len(strucs) - 1)
    structure = strucs[a]
    # translate each letter of the structure into a name, in "working".
    for b in structure:
        if b == "P":
            working = working + getstop()
        if b == "F":
            working = working + getaffricate()
        if b == "L":
            working = working + getliquid()
        if b == "N":
            working = working + getnasal()
        if b == "O":
            working = working + getvowel()
    # "working"   now contains a name
    # "structure" now contains the structure of that name.

    working = qc(working)
    working = working.capitalize()
    return working


def getstop():
    options = "ptkbdgcj"
    a = random.randint(0, len(options) - 1)
    letter = options[a]
    return letter


def getaffricate():
    options = "fszvhshx"
    a = random.randint(0, len(options) - 1)
    letter = options[a]
    return letter


def getliquid():
    options = "lrwy"
    a = random.randint(0, len(options) - 1)
    letter = options[a]
    return letter


def getnasal():
    options = "nnm"
    a = random.randint(0, len(options) - 1)
    letter = options[a]
    return letter


def getvowel():
    options = "aeiou"
    a = random.randint(0, len(options) - 1)
    letter = options[a]
    return letter


def qc(qcin):
    # Quality Control
    qcout = qcin
    a = 0
    while a <= len(qcin):
        # first letters
        if a == 0:
            # #jl -> #ch
            if qcin[a] == "j" and qcin[a + 1] == "l":
                qcout = setletter(a, "c", qcout)
                qcout = setletter(a+1, "h", qcout)
        # three letter strings
        if a <= len(qcin) - 3:
            # vowel + vowel + vowel -> vowel + r + vowel
            if isvowel(qcin[a]) and isvowel(qcin[a + 1]) and isvowel(qcin[a + 2]):
                qcout = setletter(a+1, getliquid(), qcout)
            # (c,k,x) + u + vowel -> qu + vowel
            if qcin[a] == "c" or qcin[a] == "k" or qcin[a] == "x":
                if qcin[a + 1] == "u" and isvowel(qcin[a + 2]):
                    qcout = setletter(a, "q", qcout)
        # two-letter strings
        if a <= len(qcin) - 2:
            # fh -> ph
            if qcin[a:a + 1] == "fh":
                qcout = setletter(a, "p", qcout)
            # sf -> ss
            if qcin[a:a + 1] == "sf":
                qcout = setletter(a+1, "s", qcout)
            # (yh, ih) -> oh
            if qcin[a:a + 1] == "yh" or qcin[a:a + 1] == "ih":
                qcout = setletter(a, "o", qcout)
            # (yw, iw) -> yl, il
            if qcin[a:a + 1] == "yw" or qcin[a:a + 1] == "iw":
                qcout = setletter(a+1, "l", qcout)
            # (yh, ih) -> oh
            if qcin[a:a + 1] == "wz":
                qcout = setletter(a+1, "h", qcout)
        a = a + 1

#    scrabble = 0  # use this later
    return qcout


def isvowel(suspectedv):
    if suspectedv == "a" or suspectedv == "e" or suspectedv == "i" or suspectedv == "o" or suspectedv == "u":
        return True
    return False


def setletter(a, change, inputnam):
    letter1 = inputnam[0]
    letter2 = inputnam[1]
    letter3 = inputnam[2]
    letter4 = inputnam[3]
    letter5 = inputnam[4]
    letter6 = inputnam[5]
    outputnam = letter1 + letter2 + letter3 + letter4 + letter5 + letter6

    if a == 0:
        outputnam = change + letter2 + letter3 + letter4 + letter5 + letter6
    if a == 1:
        outputnam = letter1 + change + letter3 + letter4 + letter5 + letter6
    if a == 2:
        outputnam = letter1 + letter2 + change + letter4 + letter5 + letter6
    if a == 3:
        outputnam = letter1 + letter2 + letter3 + change + letter5 + letter6
    if a == 4:
        outputnam = letter1 + letter2 + letter3 + letter4 + change + letter6
    if a == 5:
        outputnam = letter1 + letter2 + letter3 + letter4 + letter5 + change

    return outputnam


