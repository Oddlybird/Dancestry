import genome as gene
import pygame
import formattingbs as fbs
# class Jaws:


def thetooth(moufstr):
    mouf = gene.Mouth(moufstr)
    left = ["", "", "", "", "", ""]
    right = ["", "", "", "", "", ""]
    x = 0
    while x < 6:
        if mouf.symtopl[x] == "F" and mouf.symtopr[x] == "F":
            left[x] = mouf.typetopl[x] + mouf.typetopl[x] + mouf.lengthtopl[x]
            right[x] = mouf.typetopr[x] + mouf.typetopr[x] + mouf.lengthtopr[x]
        if mouf.symtopl[x] == "T" and mouf.symtopr[x] == "F":
            left[x] = mouf.typetopl[x] + mouf.typetopl[x] + mouf.lengthtopl[x]
            right[x] = mouf.typetopl[x] + mouf.typetopl[x] + mouf.lengthtopl[x]
        if mouf.symtopl[x] == "F" and mouf.symtopr[x] == "T":
            left[x] = mouf.typetopr[x] + mouf.typetopr[x] + mouf.lengthtopr[x]
            right[x] = mouf.typetopr[x] + mouf.typetopr[x] + mouf.lengthtopr[x]
        if mouf.symtopl[x] == "T" and mouf.symtopr[x] == "T":
            toofleng = str((int(mouf.lengthtopl[x]) + int(mouf.lengthtopr[x])) // 2)
            left[x] = mouf.typetopl[x] + mouf.typetopr[x] + toofleng
            right[x] = mouf.typetopr[x] + mouf.typetopl[x] + toofleng
            while left[x] != right[x]:
                # If the teeth are identical, it'll move on to the next tooth.
                if left[x][0:2] != "PC" and left[x][0:2] != "CP":
                    left[x] = "RR" + toofleng
                    right[x] = "RR" + toofleng
                if left[x][0:2] == "PC" or left[x][0:2] == "CP":
                    left[x] = "PC" + toofleng
                    right[x] = "PC" + toofleng
        x = x + 1
    jawtop = right[5] + right[4] + right[3] + right[2] + right[1] + right[0]
    jawtop = jawtop + left[0] + left[1] + left[2] + left[3] + left[4] + left[5]
    left = ["", "", "", "", "", ""]
    right = ["", "", "", "", "", ""]
    x = 0
    while x < 6:
        if mouf.symbotl[x] == "F" and mouf.symbotr[x] == "F":
            left[x] = mouf.typebotl[x] + mouf.typebotl[x] + mouf.lengthbotl[x]
            right[x] = mouf.typebotr[x] + mouf.typebotr[x] + mouf.lengthbotr[x]
        if mouf.symbotl[x] == "T" and mouf.symbotr[x] == "F":
            left[x] = mouf.typebotl[x] + mouf.typebotl[x] + mouf.lengthbotl[x]
            right[x] = mouf.typebotl[x] + mouf.typebotl[x] + mouf.lengthbotl[x]
        if mouf.symbotl[x] == "F" and mouf.symbotr[x] == "T":
            left[x] = mouf.typebotr[x] + mouf.typebotr[x] + mouf.lengthbotr[x]
            right[x] = mouf.typebotr[x] + mouf.typebotr[x] + mouf.lengthbotr[x]
        if mouf.symbotl[x] == "T" and mouf.symbotr[x] == "T":
            toofleng = str((int(mouf.lengthbotl[x]) + int(mouf.lengthbotr[x])) // 2)
            left[x] = mouf.typebotl[x] + mouf.typebotr[x] + toofleng
            right[x] = mouf.typebotr[x] + mouf.typebotl[x] + toofleng
            while left[x] != right[x]:
                # If the teeth are identical, it'll move on to the next tooth.
                if left[x][0:2] != "PC" and left[x][0:2] != "CP":
                    left[x] = "RR" + toofleng
                    right[x] = "RR" + toofleng
                if left[x][0:2] == "PC" or left[x][0:2] == "CP":
                    left[x] = "PC" + toofleng
                    right[x] = "PC" + toofleng
        x = x + 1
    jawbot = right[5] + right[4] + right[3] + right[2] + right[1] + right[0]
    jawbot = jawbot + left[0] + left[1] + left[2] + left[3] + left[4] + left[5]
    return jawtop, jawbot


def jawprint(mouf):
    jawt, jawb = thetooth(mouf)
    x = 0
    offscreen = pygame.Surface((85, 21))
    offscreen.fill((0, 0, 0))
    toof = pygame.Surface((6, 10))
    toof.fill((0, 0, 0))
    here = 3 * x
    while (here+3) <= len(jawt):
        imgloc = str(jawt[here:here + 3]) + ".PNG"
        toof, toofrect = fbs.load_png(imgloc, "teef")
#        toof = pygame.transform.flip(toof, 1, 0)
        if 2*here >= len(jawt):
            toof = pygame.transform.flip(toof, 1, 0)
        place = ((7*x)+1, 0)
        offscreen.blit(toof, place)
        x = x + 1
        here = 3 * x
    x = 0
    here = 3 * x
    while (here+3) <= len(jawb):
        imgloc = str(jawb[here:here + 3]) + ".PNG"
        toof, toofrect = fbs.load_png(imgloc, "teef")
#        toof = pygame.transform.flip(toof, 1, 0)
        if (2*here) >= len(jawt):
            toof = pygame.transform.flip(toof, 1, 0)
        toof = pygame.transform.flip(toof, 0, 1)
        place = ((7*x)+1, 10)
        offscreen.blit(toof, place)
        x = x + 1
        here = 3 * x
    return offscreen
