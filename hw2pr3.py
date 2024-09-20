# CS 5 Gold, hw2pr3
# filename: hw2pr3.py
# Name: Michael Mumo
# problem description: List comprehensions



# this gives us functions like sin and cos...
from math import *



# two more functions (not in the math library above)

def dbl(x):
    """Doubler!  argument: x, a number"""
    return 2*x

def sq(x):
    """Squarer!  argument: x, a number"""
    return x**2



# examples for getting used to list comprehensions...

def lc_mult(N):
    """This example accepts an integer N
       and returns a list of integers
       from 0 to N-1, **each multiplied by 2**
    """
    return [2*x for x in range(N)]

def lc_idiv(N):
    """This example accepts an integer N
       and returns a list of integers
       from 0 to N-1, **each divided by 2**
       WARNING: this is INTEGER division...!
    """
    return [x//2 for x in range(N)]

def lc_fdiv(N):
    """This example accepts an integer N
       and returns a list of integers
       from 0 to N-1, **each divided by 2**
       NOTE: this is floating-point division...!
    """
    return [x/2 for x in range(N)]

# printing tests
print( "lc_mult(4)   should be [0, 2, 4, 6] :", lc_mult(4) )   
print( "lc_idiv(4)   should be [0, 0, 1, 1] :", lc_idiv(4) ) 
print( "lc_fdiv(4)   should be [0.0, 0.5, 1.0, 1.5] :", lc_fdiv(4) ) 

# assertion tests
assert lc_mult(4) == [0, 2, 4, 6]
assert lc_idiv(4) == [0, 0, 1, 1]
assert lc_fdiv(4) == [0.0, 0.5, 1.0, 1.5]

# Here is where your functions start for the lab:

# Step 1, part 1
def unitfracs(N):
    """Takes in a number as an argument and returns a list with numbers between 0 and 1 with similar gaps between each other starting with 0.0
    """
    return [x/N for x in range(N)]
# print(unitfracs(5))

def scaledfracs(low, high, N):
    """Returns a list with N numbers with similar gaps between each other starting with low as the first number
    """
    return [low + (high - low)*x for x in unitfracs(N)]
# print(scaledfracs(41, 43, 8))

def sqfracs(low, high, N):
    """Returns a list with N values equally spaced from low to high squared
    """
    return [x**2 for x in scaledfracs(low, high, N)]
# print(sqfracs(0, 10, 5))
# print(sqfracs(10, 20, 10))

def f_of_fracs(f, low, high, N):
    """Returns a list with N values equally spaced between low and high after being passed in function f
    """
    return [f(x) for x in scaledfracs(low, high, N)]
# print(f_of_fracs(sin, 0, pi, 2))

def c(x):
    """c is a semicircular function of radius two"""
    return (4 - x**2)**0.5

def integrate(f, low, high, N):
    """Returns an approximation of the area under the line defined by f between low and high using N rectangles
    """

    # Took some time to figure out why this didn't work in this way. It helped improve my image of integrals.
    # return sum([x * y for x in scaledfracs(low, high, N) for y in f_of_fracs(f, low, high, N)])
    # x = scaledfracs(low, high, N)
    # y = f_of_fracs(f, low, high, N)
    # positions = range(N)
    # areas = [x[position] * y[position] for position in positions]
    # return sum(areas)
    
    height = f_of_fracs(f, low, high, N)  # Creates a list with the heights of the rectangles
    return sum(height) * (high-low)/N # Multiplies the sum of the heights with the width of the rectangles.
print( "integrate(dbl, 0, 10, 4) should be 75 :", integrate(dbl, 0, 10, 4) )
print( "integrate(sq, 0, 10, 4) should be 218.75 :", integrate(sq, 0, 10, 4) )

"""Q1
The integrate will always underestimate the value since the rectangles always leave a portion of a triangle below the line
since the line rises upwards.

An integral that will always be overestimated is one whose line slopes downard such as y = -2x.
"""

def c(x):
    """c is a semicircular function of radius two"""
    return (4 - x**2)**0.5

print (integrate(c, 0, 2, 2))
print(integrate(c, 0, 2, 20))
print(integrate(c, 0, 2, 200))
print(integrate(c, 0, 2, 2000))

"""Q2
integrate(c, 0, 2, 200) is 3.1511769448395266 while integrate(c, 0, 2, 2000) is integrate(c, 0, 2, 2000) is 3.142579505911965.
As N goes to infinity, the value of the integral becomes pi. The area between range 0 and 2 forms a quarter circle, whose area is (pi*r**2)/4.
Since our radius is 2, it's square is 4 which cancels out our denominator 4. Hence our area is defined as pi. As N approaches infininty,
the integral becomes more accurate.
"""