#
# hw8pr3.py
#

# Name: Michael Mumo

import random
import time
import math

#
# a function that throws one dart, returning true  (if it hits the circle)
#                                            false (otherwise)
#
def dart():
    """ Throws one dart between (-1,-1) and (1,1).
        Returns True if it lands in the unit circle; otherwise, False.
    """
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    
    if x**2 + y**2 < 1:
        return True        # HIT (within the unit circle)
    else:
        return False       # miss (landed in one of the corners)
    
def forpi(n):
    """Throws n darts, estimating pi."""
    throws = 0
    hits = 0
    pi = 42
    for throw in range(n):
        throws += 1
        if dart():
            hits += 1
        pi = (4*hits/throws)
        print(str(hits) + ' hits out of ' + str(throws) + ' so that pi is ' + str(pi))

    return pi

def forpi_np(N):
    """Throws N darts, estimating pi."""
    throws = 0
    hits = 0
    pi = 42
    for throw in range(N):
        throws += 1
        if dart():
            hits += 1
        pi = (4*hits/throws)
    return pi

def whilepi(error):
    """Accepts an argument of error, a positive floating-point input
       Returns the number of throws necessary to make the value of pi within error of true pi
    """
    throws = 0
    hits = 0
    pi = 0
    while error < abs(pi - math.pi):
        throws += 1
        if dart():
            hits += 1
        pi = (4*hits/throws)
        print(str(hits) + ' hits out of ' + str(throws) + ' so that pi is ' + str(pi))
    return throws

def whilepi_np(error):
    """Accepts an argument of error, a positive floating-point input
       Returns the number of throws necessary to make the value of pi within error of true pi
    """
    throws = 0
    hits = 0
    pi = 0
    while error < abs(pi - math.pi):
        throws += 1
        if dart():
            hits += 1
        pi = (4*hits/throws)
    return throws

"""
forpi_np(N) over range(1000):
when N = 1, pi = 3.112, LC[0:8] = [3.2, 2.8, 3.6, 4.0, 3.6, 4.0, 3.6, 3.6]
when N = 10, pi = 3.152, LC[0:8] = [3.6, 3.2, 3.6, 2.8, 3.2, 2.4, 3.6, 3.2]
when N = 100, pi = 3.1347199999999997, LC[0:8] = [3.4, 3.04, 3.48, 3.08, 2.96, 2.84, 3.08, 3.12]
when N = 1000, pi = 3.1416200000000005, LC[0:8] = [3.292, 3.168, 3.076, 3.064, 3.18, 3.108, 3.136, 3.096]

for whilepi_np(e) over range(1000):
when e = 1, throws = 1.6, LC[0:8] = [1, 1, 5, 1, 1, 1, 1, 1]
when e = .1 throws = 37.367, LC[0:8] = [20, 42, 17, 5, 5, 5, 94, 5]
when e = .01 throws = 455.518, LC[0:8] = [14, 14, 28, 390, 28, 14, 28, 1136]
when e = .001 throws = 20676.516, LC[0:8] = [973, 27240, 15951, 177, 135, 24977, 289, 8094]

Does forpi or whilepi estimate 𝝅 more efficiently? Why?
forpi estimates pi more efficiently. We are able to define the number of times to loop, defining how long it takes to run the function.

Does forpi or whilepi estimate 𝝅 more accurately? Why?
whilepi estimates pi more accurately. We are able to define how close we want the estimation to be to the known value of pi.
"""