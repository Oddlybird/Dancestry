import colorsys


def rgbtohue(r, g, b):
    (h, s, v) = colorsys.rgb_to_hsv(r, g, b)
    hue = h * 360
    hue = round(hue, 3)
    return hue


def rgbtoval(r, g, b):
    (h, s, v) = colorsys.rgb_to_hsv(r, g, b)
    val = round(v, 3)
    return val


# chibs system
def bloodtorgb(b):
    hue = 0    # // 360
    sat = 0.9
    val = 0.4
    firsttwo = b[0:2]
    if firsttwo == "RR":
        hue = 0
    if firsttwo == "Rr":
        hue = 15
    if firsttwo == "rr":
        hue = 30
    if firsttwo == "rG":
        hue = 45
        val = val + 0.05
    if firsttwo == "RG":
        hue = 60
        val = val + 0.1
    if firsttwo == "Rg":
        hue = 75
        val = val + 0.05
    if firsttwo == "rg":
        hue = 90
        val = val + 0.15
    if firsttwo == "GG":
        hue = 120
        val = val + 0.1
    if firsttwo == "Gg":
        hue = 135
        val = val + 0.05
    if firsttwo == "gg":
        hue = 150
    if firsttwo == "Gb":
        hue = 165
    if firsttwo == "GB":
        hue = 180
    if firsttwo == "gB":
        hue = 195
    if firsttwo == "gb":
        hue = 210
        val = val + 0.05
    if firsttwo == "BB":
        hue = 240
        val = val + 0.05
    if firsttwo == "Bb":
        hue = 255
    if firsttwo == "bb":
        hue = 270
        val = val - 0.05
    if firsttwo == "rB":
        hue = 285
        val = val - 0.1
    if firsttwo == "RB":
        hue = 300
        val = val - 0.1
    if firsttwo == "Rb":
        hue = 315
    if firsttwo == "rb":
        hue = 330

    if len(b) == 2:
        val = val + 0.05
        sat = sat + 0.1
    if len(b) > 2:
        if hasanr(b):
            if hasag(b):
                if b[2] == "R":
                    hue = hue - 6
                    val = val - 0.1
                if b[2] == "r":
                    hue = hue - 3
                    val = val - 0.05
                if b[2] == "G":
                    hue = hue + 6
                    val = val - 0.05
                if b[2] == "g":
                    hue = hue + 3
                    val = val - 0.05
                if b[2] == "B":
                    sat = sat - 0.1
                    val = val - 0.15
                if b[2] == "b":
                    sat = sat - 0.05
                    val = val - 0.1
            if hasab(b):
                if b[2] == "R":
                    hue = hue + 6
                    val = val - 0.1
                if b[2] == "r":
                    hue = hue + 3
                    val = val - 0.05
                if b[2] == "B":
                    hue = hue - 6
                    val = val - 0.1
                if b[2] == "b":
                    hue = hue - 3
                    val = val - 0.05
                if b[2] == "G":
                    sat = sat - 0.1
                    val = val - 0.15
                if b[2] == "g":
                    sat = sat - 0.05
                    val = val - 0.1
            if not hasag(b) and not hasab(b):
                if b[2] == "G":
                    hue = hue + 6
                    val = val - 0.1
                if b[2] == "g":
                    hue = hue + 3
                    val = val - 0.05
                if b[2] == "B":
                    hue = hue - 6
                    val = val - 0.1
                if b[2] == "b":
                    hue = hue - 3
                    val = val - 0.05
                if b[2] == "R":
                    sat = sat + 0.1
                    val = val + 0.15
                if b[2] == "r":
                    sat = sat + 0.05
                    val = val + 0.1
        if not hasanr(b):
            if hasag(b) and hasab(b):
                if b[2] == "G":
                    hue = hue - 6
                    val = val - 0.1
                if b[2] == "g":
                    hue = hue - 3
                    val = val - 0.05
                if b[2] == "B":
                    hue = hue + 6
                    val = val - 0.1
                if b[2] == "b":
                    hue = hue + 3
                    val = val - 0.05
                if b[2] == "R":
                    sat = sat - 0.1
                    val = val - 0.15
                if b[2] == "r":
                    sat = sat - 0.05
                    val = val - 0.1
            if hasab(b) and not hasag(b):
                if b[2] == "R":
                    hue = hue + 6
                    val = val - 0.1
                if b[2] == "r":
                    hue = hue + 3
                    val = val - 0.05
                if b[2] == "G":
                    hue = hue - 6
                    val = val - 0.1
                if b[2] == "g":
                    hue = hue - 3
                    val = val - 0.05
                if b[2] == "B":
                    sat = sat - 0.1
                    val = val - 0.15
                if b[2] == "b":
                    sat = sat - 0.05
                    val = val - 0.1
            if hasag(b) and not hasab(b):
                if b[2] == "R":
                    hue = hue - 6
                    val = val - 0.1
                if b[2] == "r":
                    hue = hue - 3
                    val = val - 0.05
                if b[2] == "B":
                    hue = hue + 6
                    val = val - 0.1
                if b[2] == "b":
                    hue = hue + 3
                    val = val - 0.05
                if b[2] == "G":
                    sat = sat - 0.1
                    val = val - 0.15
                if b[2] == "g":
                    sat = sat - 0.05
                    val = val - 0.1

    while hue > 360:
        hue = hue - 360
    while hue < 0:
        hue = hue + 360
    while sat < 0:
        sat = 0
    while sat > 1:
        sat = 1
    while val < 0.15:
        val = 0.15
    while val > 0.9:
        val = 0.9
    h = hue / 360
    s = sat
    v = val
    (rgb1, rgb2, rgb3) = colorsys.hsv_to_rgb(h, s, v)
    rgb1 = round(rgb1*255)
    rgb2 = round(rgb2*255)
    rgb3 = round(rgb3*255)
    finalcol = (rgb1, rgb2, rgb3)
    return finalcol


# Original
def bloodtorgb_original(b):  # interface, because this is the display color only / specifically.
    # gives you the darker color associated with the code "b" which is a 2-3 letter string.
    rgb1 = 0
    rgb2 = 0
    rgb3 = 0
#    capitals = 0
    rbig = 0
    rlil = 0
    gbig = 0
    glil = 0
    bbig = 0
    blil = 0

    for x in b:
        if x == "r":
            rlil = rlil + 1
        if x == "g":
            glil = glil + 1
        if x == "b":
            blil = blil + 1
        if x == "R":
            rbig = rbig + 1
        if x == "G":
            gbig = gbig + 1
        if x == "B":
            bbig = bbig + 1

    if rlil == 1 and rbig == 0:
        rgb1 = 60
        rlil = 0
    if rlil == 2 and rbig == 0:
        rgb1 = 80
        rlil = 0
    if rbig == 1:
        rgb1 = 100
        rbig = 0
    if rlil == 3 and rbig == 0:
        rgb1 = 100
        rlil = 0
    if rbig == 2:
        rgb1 = 120
        rbig = 0
    if rbig == 3:
        rgb1 = 140
    if rlil == 1:
        rgb1 = rgb1 + 5
    if rlil == 2:
        rgb1 = rgb1 + 15

    if glil == 1 and gbig == 0:
        rgb2 = 60
        glil = 0
    if glil == 2 and gbig == 0:
        rgb2 = 80
        glil = 0
    if gbig == 1:
        rgb2 = 100
    if glil == 3 and gbig == 0:
        rgb2 = 100
        glil = 0
    if gbig == 2:
        rgb2 = 120
    if gbig == 3:
        rgb2 = 140
    if glil == 1:
        rgb2 = rgb2 + 5
    if glil == 2:
        rgb2 = rgb2 + 15

    if blil == 1 and bbig == 0:
        rgb3 = 60
        blil = 0
    if blil == 2 and bbig == 0:
        rgb3 = 80
        blil = 0
    if blil == 3 and bbig == 0:
        rgb3 = 100
        blil = 0
    if bbig == 1:
        rgb3 = 100
    if bbig == 2:
        rgb3 = 120
    if bbig == 3:
        rgb3 = 140
    if blil == 1:
        rgb3 = rgb3 + 5
    if blil == 2:
        rgb3 = rgb3 + 15

    # greys should be brown
    if rgb1 == rgb2 == rgb3:
        rgb1 = rgb1
        rgb2 = rgb2 // 2
        rgb3 = rgb3 // 4

    # Return things to normal color ranges.
    if rgb1 > 255:
        rgb1 = 255
    if rgb2 > 255:
        rgb2 = 255
    if rgb3 > 255:
        rgb3 = 255
    if rgb1 < 0:
        rgb1 = 0
    if rgb2 < 0:
        rgb2 = 0
    if rgb3 < 0:
        rgb3 = 0

    (h, s, v) = colorsys.rgb_to_hsv(rgb1, rgb2, rgb3)
    hue = h * 360
    hue = round(hue, 3)

    # saturation must be at least 0.5
    while s < 0.4:
        s = s + 0.1
        v = v - 0.1
    # in the purple range, things should be darker.
    if 240 < hue < 310:
        v = v - 0.2
    impurity = (hue % 30) / 30
    v = v - impurity
    # value should be between 0.01 and 0.5
    if v < 0.01:
        v = 0.01
    while v > 0.5:
        v = v - 0.2

    h = hue / 360
    (rgb1, rgb2, rgb3) = colorsys.hsv_to_rgb(h, s, v)
    rgb1 = round(rgb1*255)
    rgb2 = round(rgb2*255)
    rgb3 = round(rgb3*255)

    # Vantases are special.
    if b == "rb":
        rgb1 = 255
        rgb2 = 0
        rgb3 = 0

    finalcolor = (rgb1, rgb2, rgb3)
    return finalcolor


def pastel(r, g, b):  # interface (currently nonfunctional)
    (h, s, v) = colorsys.rgb_to_hsv(r, g, b)
    newcolor = colorsys.hsv_to_rgb(h, v, 230)
    return newcolor


def hasanr(b):
    # Purposefully only checks first two letters.
    if len(b) > 0:
        if b[0] == "R" or b[0] == "r":
            return True
    if len(b) > 1:
        if b[1] == "R" or b[1] == "r":
            return True
    return False


def hasag(b):
    # Purposefully only checks first two letters.
    if len(b) > 0:
        if b[0] == "G" or b[0] == "g":
            return True
    if len(b) > 1:
        if b[1] == "G" or b[1] == "g":
            return True
    return False


def hasab(b):
    # Purposefully only checks first two letters.
    if len(b) > 0:
        if b[0] == "B" or b[0] == "b":
            return True
    if len(b) > 1:
        if b[1] == "B" or b[1] == "b":
            return True
    return False
