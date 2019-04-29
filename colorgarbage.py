import libtcodpy as tcod
import colorsys


def rgbtohue(r, g, b):
    (h, s, v) = colorsys.rgb_to_hsv(r, g, b)
    hue = h * 360
    hue = round(hue, 3)
    return hue


def bloodtorgb(b):  # interface, because this is the display color only / specifically.
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

    (h, s, v) = colorsys.rgb_to_hsv(rgb1, rgb2, rgb3)
    hue = h * 360
    hue = round(hue, 3)

    # greys should be brown
    if rgb1 == rgb2 == rgb3:
        rgb1 = rgb1
        rgb2 = rgb2 // 2
        rgb3 = rgb3 // 4
    # in the purple range, things should be darker.
    if 240 < hue < 310:
        v = v - 0.2
    # value should be between 0.2 and 0.5
    if v < 0.2:
        v = 0.2
    if v > 0.4:
        v = 0.4
    # saturation must be at least 0.7
    if s < 0.7:
        s = 0.7

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
