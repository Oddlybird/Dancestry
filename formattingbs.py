import os
import pygame
import random


def randsel(inp="X", length=1):
    x = 0
    which = "X"
    while x < length:
        which = which + inp[random.randint(0, len(inp))]
        x = x + 1
    return which


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


def load_png(name, fold=""):
    """ Load image and return image object"""
    fullname = os.path.join('data', fold, name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error:
        print('Cannot load image: ', fullname)
        raise SystemExit
    return image, image.get_rect()


def pysurface(x, y, col=(0, 0, 0)):
    background = pygame.Surface((x, y))
    background = background.convert()
    background.fill(col)
    return background


def rectolor(surface, x, y, ww, hh, btncolor=(255, 255, 225)):
    (btnr, btng, btnb) = btncolor
    btnr = round(btnr)
    btng = round(btng)
    btnb = round(btnb)
    btncolor = (btnr, btng, btnb)
    rectangle = pysurface(ww, hh, btncolor)
    surface.blit(rectangle, (x, y))
    return surface


def say(thing, col=(255, 255, 255), size=11, bold=False, italic=False):
    font = pygame.font.SysFont("Verdana", size, bold, italic)
    text = font.render(thing, 1, col)
    return text


def btn(text="", w=192, h=24, btncol=(255, 255, 225), txtcol=(50, 50, 0), centered = True, style="Courier"):
    page = pysurface(w, h, btncol)
    font = pygame.font.SysFont(style, 15, True, False)
    words = font.render(text, 1, txtcol)
    textpos = (page.get_width() - words.get_width()) // 2
    if centered == "False":
        textpos = 6
    page.blit(words, (textpos, 0))
    return page
