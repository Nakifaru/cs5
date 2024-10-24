# hw8pr1.py
# Lab 8
#
# Name: Michael Mumo
#

# keep this import line...
from cs5png3 import *


#
# A test function...
#
def test_fun():
    """Algorithmic image creation, one pixel at a time.
       This is a test function: it should create
       an image named test.png in the current directory.
    """
    im = PNGImage(300, 200)  # Creates an image of width 300, height 200

    # Nested loops!
    for r in range(200):     # loops over the rows with runner variable r
        for c in range(300): # loops over the columns with c
            if  c == r:   
                im.plotPoint(c, r, (255, 0, 0))
            #else:
            #    im.plotPoint(c, r, (255, 0, 0))
                
    im.saveFile()

#
# start your Lab 8 functions here:
#

def mult(c, n):
    """Mult multiplies c by the positive integer n,
       using only a loop and addition.
    """
    result = 0
    for i in range(n):
        result += c
    return result


# print("mult(105, 3) should be 315 and is", mult(105, 3))
# print(mult(6, 7))
# print(mult(1.5, 28))

def update(c, n):
    """Update starts with z = 0 and runs z = z**2 + c
       for a total of n times. It returns the final z.
    """
    z = 0
    for i in range(n):
        z = z**2 + c
    return z

# print(update(1, 3))
# print(update(-1, 3))
# print(update(1, 10))
# print(update(-1, 10))

def inMSet(c, n):
    """inMSet accepts
            c for the update step of z = z**2+c
            n, the maximum number of times to run that step.
       Then, it returns
            False as soon as abs(z) gets larger than 2.
            True if abs(z) never gets larger than 2 (for n iterations).
    """
    z = 0
    for i in range(n):
        z = z**2 + c
        if abs(z) > 2:
            return False
    return True

# assert inMSet(0 + 0j, 25) == True
# assert inMSet(3 + 4j, 25) == False
# assert inMSet(.3 + -.5j, 25) == True
# assert inMSet(-.7 + .3j, 25) == False
# assert inMSet(.42 + .2j, 25) == True
# assert inMSet(.42 + .2j, 50) == False

def weWantThisPixel(col, row):
    """This function returns True if we want to show
       the pixel at col, row and False otherwise.
    """
    # Changing the and in the next line to or will add more plots in between each
    # plot we had initially

    # After changing I realised it created a grid. This makes sense since a whole 
    # row or column would be a multiple of 10
    if col % 10 == 0  or  row % 10 == 0:
        return True
    else:
        return False

def test():
    """This function demonstrates how
       to create and save a PNG image.
    """
    width = 300
    height = 200
    image = PNGImage(width, height)

    # Create a loop that will draw some pixels.

    for col in range(width):
        for row in range(height):
            if weWantThisPixel(col, row):
                image.plotPoint(col, row)

    # We looped through every image pixel; we now write the file.

    image.saveFile()

def scale(pix, pixMax, floatMin, floatMax):
    """scale accepts
           pix, the CURRENT pixel column (or row).
           pixMax, the total number of pixel columns.
           floatMin, the minimum floating-point value.
           floatMax, the maximum floating-point value.
       scale returns the floating-point value that
           corresponds to pix.
    """

    return floatMin + (pix/pixMax) * (floatMax - floatMin)

# print(scale(100, 200, -2.0, 1.0))
# print(scale(100, 200, -1.5, 1.5))
# print(scale(100, 300, -2.0, 1.0))
# print(scale(25, 300, -2.0, 1.0))
# print(scale(299, 300, -2.0, 1.0))

def mset():
    """Creates a 300x200 image of the Mandelbrot set.
    """

    NUM_ITERATIONS = 25  # Number of updates; will be assigned to n
    XMIN = -2.0          # The smallest real coordinate value
    XMAX =  1.0          # The largest real coordinate value
    YMIN = -1.0          # The smallest imaginary coordinate value
    YMAX =  1.0          # The largest imaginary coordinate value
    FACTOR = 1
    width = 300*FACTOR       # We can update the 1 later to enlarge the image...
    height = 200*FACTOR
    image = PNGImage(width, height)

    # Create a loop to draw some pixels

    for col in range(width):
        x = scale( col, width, XMIN, XMAX)
        for row in range(height):
            y = scale( row, height, YMIN, 1.0)
            c = x + y*1j
            n = NUM_ITERATIONS
            if inMSet(c, n):
                image.plotPoint(col, row, (255, 175, 0))
            else:
                image.plotPoint(col, row, (0, 0, 0))

    image.saveFile()

