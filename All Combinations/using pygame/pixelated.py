#import Image
from PIL import Image
from PIL import ImageDraw
from math import sqrt
import random
import pygame, sys
from pygame import gfxdraw
# from pygame import Surface


imageSize = 5

def pickColor(color):
    if color < 25:
        color += random.randint(0, 10)
    elif color > 230:
        color += random.randint(-10, 0)
    else:
        color += random.randint(-10, 10)
    return color

def increasing(color):
    if color>245:
        color = 0
    else:
        color += 25 #random.randint(0, 25)
    return color

def beginSame(color, y):
    if y ==0:
        color = 255
    else:
        color = pickColor(color)
    return color

def considerSides(color, average):
    color = average + random.randint(-25,25)
    return color
    

####################################################################################
def normalCoors(oneSide):
    coordinates = []
    ##oneSide = 3
    for i in xrange(oneSide**2):
        x = i/oneSide
        y = i%oneSide
        coordinates.append([x,y])
    return coordinates

def diagCoors(oneSide):
    coordinates = []
    for y in range(oneSide):
        for i in range(y+1):
            coordinates.append([y-i,i])
    y = 1
    while y < oneSide:
        x = oneSide - 1
        tempY = y
        while tempY < oneSide:
            coordinates.append([x,tempY])
            tempY += 1
            x -= 1
        y += 1
    return coordinates
####################################################################################


def makeRandomDiag():
    oneSide =50
    imageSize = oneSide**2
    coordinates = diagCoors(oneSide)
    #coordinates = normalCoors(oneSide)
    for creation in xrange(5):
        R = 0
        G = 0
        B = 0
        avgR = 0
        avgG = 0
        avgB = 0
        img = Image.new("RGB", (oneSide,oneSide), "white")
        pixels = img.load()
        draw = ImageDraw.Draw(img)
        for i in xrange(len(coordinates)):
            if i != 0:
                cR,cG,cB = img.getpixel((coordinates[i-1][0], coordinates[i][1]))
                c2R,c2G,c2B = img.getpixel((coordinates[i][0], coordinates[i][1-1]))
                avgR = (cR+c2R)/2
                avgG = (cG+c2G)/2
                avgB = (cB+c2B)/2
            R = considerSides(R, avgR)
            G = considerSides(G, avgG)
            B = considerSides(B, avgB)
            print R,G,B
            pixels[coordinates[i][0],coordinates[i][1]] = (R,G,B)
        img.save("diagonalPixels" + str(creation) + ".jpg")
    print 'done'

def makeRandomPixels():
    oneSide = 200
    imageSize = oneSide**2
    difference = 0
    #number of images created
    coordinates = normalCoors(oneSide)
    for creation in xrange(5):
        R = 0 #random.randint(0,255)
        G = 0 #random.randint(0,255)
        B = 0 #random.randint(0,255)
        img = Image.new("RGB", (oneSide,oneSide), "white")
        pixels = img.load()
        draw = ImageDraw.Draw(img)
        for spot in coordinates:
            #these make faint stripes
            R = beginSame(R, spot[1])
            G = beginSame(G, spot[1])
            B = beginSame(B, spot[1])
            #these make rainbow waves
            # R = increasing(R)
            # G = increasing(G)
            # B = increasing(B)
            #these make rainbow lines
            # R = pickColor(R)
            # G = pickColor(G)
            # B = pickColor(B)
            pixels[spot[0],spot[1]] = (R,G,B)
            #dont use this its a stupid substitute
##            pixels.putpixel((x,y),(R,G,B))
            
        img.save("2.0combinedPixels" + str(creation) + ".jpg")
    print "done"


def allPixels():
    oneSide = 3
    for i in xrange(2**(oneSide**2)-1):
        surf = pygame.Surface((oneSide,oneSide))
        pixels = Image.new("RGB", (oneSide,oneSide), "white")
        draw = ImageDraw.Draw(pixels)
        pix = pixels.load()
        #binary values for number image
        # would need to be bigger if sides were bigger
        value = '{0:09b}'.format(i)
        print value
        vCount = 0
        for x in xrange(oneSide):
            for y in xrange(oneSide):
                print (x,y),value[vCount]
##              does each row of pixels downward
                if value[vCount] == '1':
                    gfxdraw.pixel(surf, x, y, (0,0,0))
                    #pix[x,y] = (0,0,0)
                else:
                    gfxdraw.pixel(surf, x, y, (255,255,255))
                    #pix[x,y] = (255,255,255)
                # if x == 1 and value[y+3] == '1':
                #     pixels[x,y] = (0,0,0)
                # if x == 2 and value[y+5] == '1':
                #     pixels.putpixel((x,y),(0,0,0))
                    ##pixels[x,y] = (0,0,0)
                vCount += 1
        pygame.image.save(surf, "pixels" + str(i) + ".jpg")
        #pixels.save("pixels" + str(i) + ".jpg")
    print "done"

allPixels()
#makeRandomPixels()
#makeRandomDiag()
