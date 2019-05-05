import re


def wordwrap2(instring, wraplength = 20):
    splitup = instring.split(" ")
    result = [ "", "", "", "", "", "", "", "", "", ]
    a = 0
    for arb in splitup:
        if (len(result[a]) + 1 + len(arb)) <= wraplength:
            result[a] = result[a] + " " + arb
            result[a] = result[a].strip()
        if (len(result[a]) + 1 + len(arb)) > wraplength:
            result[a] = result[a].strip()
            a = a + 1
    return result


def lyst(a, b):
    # Combine With Commas And Spaces
    c = ""
    if a == "" and b == "":
        c = ""
    if a == "" and b != "":
        c = b
    if a != "" and b == "":
        c = a
    if a != "" and b != "":
        c = a + ", " + b
    return c


def lyst2(a, b):
    # Combine with spaces, no commas
    c = ""
    if a == "" and b == "":
        c = ""
    if a == "" and b != "":
        c = b
    if a != "" and b == "":
        c = a
    if a != "" and b != "":
        c = a + " " + b
    return c

