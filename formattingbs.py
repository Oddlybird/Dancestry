import re

def multisplit(a):
    a = a + "@,@,@,"
    b = a.split("@")
    return b


def trimmulti(a):
    b = re.sub(', , ', ', ', a)
    c = re.sub(',@,@', ',@', b)
    d = re.sub(', , ', ', ', c)
    e = re.sub('@@', '@', d)
    return e


def wordwrap(a, b, c):
    # instring, instring, number of characters to allow
    d = a
    if len(a) < c and len(b) < c:
        d = a + b
        if len(d) > c:
            d = a + "@" + b
    return d
