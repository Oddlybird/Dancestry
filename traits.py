import slurry
import random


def defaultcastestats(blood="mm"):
    blood = blood[0:2]
    statmain = corestatdict()
    statmax = corestatdict()
    castemods = slurry.spectrumcorestat[blood]
    extrapts = castemods["pts"] + random.randint(0, 6) - 2

    for arb in statmain:
        statmain[arb] = castemods[arb]
        if statmain[arb] == 0.5:
            a = random.randint(0, 10)
            if a > 5:
                statmain[arb] = 1
            else:
                statmain[arb] = 0
        if statmain[arb] == 0.25:
            a = random.randint(0, 10)
            if a > 7:
                statmain[arb] = 1
            else:
                statmain[arb] = 0
        statmax[arb] = statmain[arb] + 6

    statsecret = {
        "faith": random.randint(1, 20) - 10,
        "order": random.randint(1, 20) - 10,
        "entropy": random.randint(1, 20) - 10,
        "connection": random.randint(1, 20) - 10,
        "self": random.randint(1, 20) - 10,
        "luck": random.randint(1, 20) - 10,
    }

    dpts = 20 + extrapts
    dorder = "A"    # Average.  Replace later.

    return statmain, statsecret, dpts, dorder, statmax


def corestatdict(inblood=""):
    if inblood == "" or inblood == "blank":
        s = {"clout": 0, "acumen": 0,
             "grit": 0,  "alacrity": 0,
             "hunch": 0, "resolve": 0,
             "moxie": 0, "psyche": 0,
             "pts": 0}
    else:
        src = slurry.spectrumcorestat[inblood]
        s = {"clout": src["clout"],
             "acumen": src["acumen"],
             "grit": src["grit"],
             "alacrity": src["alacrity"],
             "hunch": src["hunch"],
             "resolve": src["resolve"],
             "moxie": src["moxie"],
             "psyche": src["psyche"],
             "pts": src["pts"]}
    return s


def secstatdict(inblood=""):
    s = {
        "faith": 0,
        "order": 0,
        "entropy": 0,
        "connection": 0,
        "self": 0,
        "luck": 0,
        }
#    if inblood != "":
#        src = inblood
#        # There's no difference based on caste, yet.  But if there was, it would go here.
    return s


def stats(blood=""):
    a = random.randint(1, 5)
    dorder = "A"  # G(generalist), S(specialist), A(average), other things.
    if a == 1:
        dorder = "G"
    if a == 2:
        dorder = "S"

    corestat = corestatdict(blood)
    secstat = secstatdict(blood)

    blank = {
        # Core stats
        "statmain": corestat,
        "statmax": corestat,
        # Secret stats
        "statsecret": secstat,
        "aspect": "",
        # distribution stats
        "dorder": dorder,  # distrib order
        "dpts": corestat["pts"],
    }
    return blank


def getaspect(stat):
    faith = stat["statsecret"]["faith"]
    order = stat["statsecret"]["order"]
    entropy = stat["statsecret"]["entropy"]
    connection = stat["statsecret"]["connection"]
    self = stat["statsecret"]["self"]
    luck = stat["statsecret"]["luck"]
    aspectdict = {
        "Rage": faith,
        "Hope": (-1) * faith,
        "Doom": order,
        "Life": (-1) * order,
        "Time": entropy,
        "Space": (-1) * entropy,
        "Blood": connection,
        "Breath": (-1) * connection,
        "Heart": self,
        "Mind": (-1) * self,
        "Void": luck,
        "Light": (-1) * luck,
    }
    greatest = "Rage"
    amt = 0
    for arb1 in aspectdict:
        if aspectdict[greatest] <= aspectdict[arb1]:
            greatest = arb1
            amt = aspectdict[arb1]

    aspect = greatest + "(" + str(amt) + ")"
    return aspect


# stats are listed by caste preference, needs individual preference modifications
# stat distribution style = Average; generalist/specialist currently unused.
def statdistrib(stat, blood):
    # lists of the stat names in order from highest to lowest.
    statmain, smindex = orderstats(stat, "core")
    statmax = slurry.spectrumcorestat[blood]
    for arb in statmax:
        statmax[arb] = statmax[arb] + 6
    # clout, acumen, grit, alacrity, hunch, resolve, moxie, psyche
    pts = stat["dpts"]  # number of points to distribute

    # minimum stat = 1.
    for arb in statmain:
        if statmain[arb] < 1:
            statmain[arb] = 1
    # Individual variance.
    a = random.randint(0, len(smindex) - 1)
    if statmax[smindex[a]] > statmain[smindex[a]]:
        pts = pts - 1
        statmain[smindex[a]] = statmain[smindex[a]] + 1
    a = random.randint(0, len(smindex) - 1)
    if statmax[smindex[a]] > statmain[smindex[a]]:
        pts = pts - 1
        statmain[smindex[a]] = statmain[smindex[a]] + 1
    # sort by new order
    stat["statmain"] = statmain
    statmain, smindex = orderstats(stat, "core")
    # a = random.randint(0, 10)
    # if (a // 3) == 0:
    # if (a // 2) == 0:
    # if (a // 4) == 0:
    # # Make some semirandom alterations to the order of the list.

    if stat.dorder == "A":  # Average
        a = 0
        while pts > 0:  # While there are points
            if statmain[smindex[a]] < statmax[smindex[a]]:
                statmain[smindex[a]] = statmain[smindex[a]] + 1
                pts = pts - 1  # move them from pts to stats 1 at a time
                a = a + 1      # go to next stat
                if a >= len(smindex):  # If you reach end of stat list
                    a = 0              # return to start
            else:
                break
        # pts to distribute now = 0
    if stat.dorder == "G":  # Generalist
        while pts > 0:  # while there are points
            avg = dictavg(statmain)    # Find average
            for a in smindex:   # Check each stat,
                if statmain[a] < statmax[a]:
                    while statmain[a] <= avg:  # If < avg
                        statmain[a] = statmain[a] + 1
                        pts = pts - 1
                else:
                    break
        # improve stat until it > avg by 1
    if stat.dorder == "S":  # Specialist
        while pts > 0:  # while points
            for arbstat in smindex:  # for each stat sorted by rank
                if statmain[arbstat] < statmax[arbstat]:  # Until it = max
                    statmain[arbstat] = statmain[arbstat] + 1
                    pts = pts - 1          # keep dumping points in it
                else:
                    break
    # put values into stat object
    stat["dpts"] = pts
    stat["statmain"] = statmain
    stat["statmax"] = statmax
    return stat


def orderstats(t, flag="core"):
    d1 = {}  # Source dict
    d2 = []  # dest list, to be constructed during function
    if flag == "core" or flag == "main":
        d1 = t["statmain"]
    if flag == "secret":
        d1 = t["statsecret"]
    if flag == "manual":
        d1 = t
    # Actual sorting function
    b = 0  # number of items removed
    for arb1 in d1:  # For every item
        a = 0        # set counter = 0
        for arb2 in d1:                # Compare to every other item
            if d1[arb1] >= d1[arb2]:   # if >=
                a = a + 1              # counter++
                b = b + 1              # counter++
        if a+b >= len(d1):               # If greatest,
            d2.append(arb1)            # Add to end of list
    return d1, d2


def dictavg(dicta={}):
    avg = 0
    for arb in dicta:
        avg = avg + arb
    avg = avg // len(dicta)
    return avg


# list = ["zero", "one", "two", "three"]
# list[0] = "zero"
# for x in list
# len(list)
# list.append("four")  # Add to end
# list.index("four") = 4 # returns the ine number of the first element matching str
# list.insert(1, "temp")
# list.remove("temp") #remove value
# list.pop(1)  (removes specified index or last if unspecified)
# list.del[1]  (removes specified index)
# del list  # delete list
# list.clear() # empty list
# list2 = list1 will create two linked instances.
# list2 = list1.copy()  will create 2 separate objects
# list2 = list(list1)     will make 2 separate objects
# list = list(("zero", "one", "two"))
# list.reverse() reverses order
# list.sort()  # sort alphabetically.

# list.sort(True|False, key=myFunc)
# def myFunc(e):
#     return len(e):

# cars = [
# {'car': 'Ford', 'year': 2005}
# {'car': 'bmw', 'year': 2019}
# ]
# cars.sort(key=myFunc
# def myFunc(e)
# return e['year']

