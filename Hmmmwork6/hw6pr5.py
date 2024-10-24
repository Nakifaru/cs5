#
# hw6pr5.py -  Python!
#
#  Gold:   this is "Intro to loops"! (starter code below)
# Black:   this file is not used
#
# Name:
#
def fac(n):
    """Loop-based factorial function
       Argument: a nonnegative integer, n
       Return value: the factorial of n
    """
    result = 1                 # starting value - like a base case
    for x in range(1, n + 1):  # loop from 1 to n, inclusive
        result = result * x    # update the result by mult. by x
    return result              # notice this is AFTER the loop!

#
# Tests for looping factorial
#
print("fac(0) should be 1:", fac(0))
print("fac(5) should be 120:", fac(5)) 


def power(b, p):
    """Arguments: an integer b as a base and p as a power
       Return: b raised to p
    """

    result = 1
    for x in range(1, p + 1):
        result = result * b
    return result

#
# tests for looping power
#
print("power(2, 5): should be 32 ==", power(2, 5))
print("power(5, 2): should be 25 ==", power(5, 2))
print("power(42, 0): should be 1 ==", power(42, 0))
print("power(0, 42): should be 0 ==", power(0, 42))
print("power(0, 0): should be 1 ==", power(0, 0))


def summer(L):
    """Arguments: a list of integers L
       Return: sum of elements of L
    """

    result = 0
    for x in L:
        result = result + x
    return result

print("summer([10,10,10,2,10]): should be 42 ==", summer([10,10,10,2,10]))
print("summer([10,10,10,2]): should be 32 ==", summer([10,10,10,2]))
print("summer([11, 11]): should be 22 ==", summer([11,11]))
print("summer([47]): should be 47 ==", summer([47]))
print("summer([ ]): should be 0 ==", summer([ ]))

def summedOdds(L):
    """Arguments: a list of integers L
       Return: sum of odd elements of L
    """

    result = 0
    for x in L:
        if x % 2 == 1:
            result = result + x
    return result

# tests!
print( "summedOdds([4, 5, 6])      should be 5 :",  summedOdds([4, 5, 6]) )   
print( "summedOdds(range(3, 10))   should be 24 :",  summedOdds(range(3, 10)) )

def summedExcept(exc, L):
    """Arguments: exc, a integer whose value shouldn't be included in the sum, a list of integers L
       Return: sum of elements of L not equal to exc
    """

    result = 0
    for x in L:
        if x != exc:
            result = result + x
    return result

# tests!
print( "summedExcept(5, [4, 5, 6])      should be 10 :",  summedExcept(5, [4, 5, 6]) )   
print( "summedExcept(5, [5, 5, 5])      should be 0 :",  summedExcept(5, [5, 5, 5]) ) 


def summedUpto(exc, L):
    """Arguments: exc, a integer which prompts the return, a list of integers L
       Return: sum of elements of L before encountering exc
    """

    result = 0
    for x in L:
        if x == exc:
            break
        result = result + x
    return result

# tests!
print( "summedUpto(5, [4, 5, 6])      should be 4 :",  summedUpto(5, [4, 5, 6]) )   
print( "summedUpto(5, [4, 6, 5])      should be 10 :",  summedUpto(5, [4, 6, 5]) ) 
print( "summedUpto(5, [4, 6, 32])     should be 42 :",  summedUpto(5, [4, 6, 32]) )


def unique(L):
    """Decide whether all elements in L are unique.
       Argument: L, a list of any elements.
       Return value: True, if all elements in L are unique,
                  or False, if there is any repeated element
    """
    if len(L) == 0:
        return True
    elif L[0] in L[1:]:
        return False
    else:
        return unique(L[1:])  # recursion is OK in this function!

import random

def untilARepeat(high):
    """Use a while loop to guess "hidden", from 0 to 99.
       Argument: hidden, a "hidden" integer from 0 to 99.
       Result: the number of guesses needed to guess hidden.
    """
    guess = random.choice(range(0, high))     # 0 to 99, inclusive
    numguesses = 1                           # We just made one guess, above
    L = []
    while unique(L):
        guess = random.choice(range(0, high)) # Guess again!
        numguesses += 1                      # Add one to our number of guesses
        L = L + [guess]
    return numguesses

"""
Here's what I got when I analyzed 10,000 calls of untilARepeat(365):
In [5]: L = LC

In [6]: sum(L)/len(L)
Out[6]: 25.4784

In [7]: max(L)
Out[7]: 83

In [8]: min(L)
Out[8]: 3

In [9]: 42 in L
Out[9]: True

In [10]: L.count(2)
Out[10]: 0

In [11]: 1 in L
Out[11]: False

In [12]: 142 in L
Out[12]: False
"""


def rs():
    """One random step"""
    return random.choice([-1, 1])

def rwalk(radius):
    """Random walk between -radius and +radius  (starting at 0 by default)"""
    totalsteps = 0          # Starting value of totalsteps (_not_ final value!)
    start = 0               # Start location (_not_ the total # of steps)

    while True:             # Run "forever" (really, until a return or break)
        if start == -radius or start == radius:   
            return totalsteps # Phew!  Return totalsteps (stops the while loop)

        start = start + rs()
        totalsteps += 1     # addn totalsteps 1 (for all who miss Hmmm :-)

        # print("start:", start) # To see what's happening / debugging

    # it can never get here!


"""
First, I created an LC with 10,000 radius-5 random-walk trials, using this line:

   LC = [rwalk(5) for x in range(10000)]

Out of those 10,000 radius-5 trials, the average number of steps
(sum(LC) / len(LC)) needed to reach the boundary was:

++++++++++++
+ 25.0272  +
++++++++++++

+++++++++++++++++++++++
+ Radius   + Average  +
+++++++++++++++++++++++
+    5     + 25.0272  +
+++++++++++++++++++++++
+    6     + 35.5412  +
+++++++++++++++++++++++
+    7     + 49.9962  +
+++++++++++++++++++++++
+    10    + 100.16   +
+++++++++++++++++++++++

If you set a random walker in the middle of an interval with radius radius, on average,
how many steps would you expect the random walker to take before reaching the edge of the interval?
(Not a programming problem, really... a thought problem!)

numsteps = radius * radius

If you set a random walker walking... how far away from the starting point
would you expect our walker to be after numsteps steps?

Covered radius(distance) = numsteps/radius


"""