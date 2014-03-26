#import Image
from PIL import Image
from PIL import ImageDraw

def allPixels():
    oneSide = 3
    for i in xrange(2**(oneSide**2)):
        pixels = Image.new("RGB", (oneSide,oneSide), "white")
        draw = ImageDraw.Draw(pixels)
        pix = pixels.load()
        #binary values for number image
        # would need to be bigger if sides were bigger
        value = '{0:09b}'.format(i)
        vCount = 0
        for x in xrange(oneSide):
            for y in xrange(oneSide):
                #print (x,y),value[vCount]
##              does each row of pixels downward
                if value[vCount] == '1':
                    #pixels.putpixel((x,y),(0,0,0))
                    pix[x,y] = (0,0,0)
                else:
                    pix[x,y] = (255,255,255)
                # if x == 1 and value[y+3] == '1':
                #     pixels[x,y] = (0,0,0)
                # if x == 2 and value[y+5] == '1':
                #     pixels.putpixel((x,y),(0,0,0))
                    ##pixels[x,y] = (0,0,0)
                vCount += 1
        pixels.save("pixels" + str(i) + ".png")
    print "done"

allPixels()

