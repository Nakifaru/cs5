# CS5, Lab1 part 2
# Filename: hw1pr2.py
# Name: Mumo Mwendwa
# Problem description: First few functions!


def dbl(x):
    """Result: dbl returns twice its argument
       Argument x: a number (int or float)
       Spam is great, and dbl("spam") is better!
    """
    return 2*x

def tpl(x):
    """Return value: tpl returns thrice its argument
       Argument x: a number (int or float)
    """
    return 3*x

def sq(x):
    """Return value: sq returns the square of its argument
       Argument x: a number (int of float)
    """
    return x * x

def interp(low, hi, fraction):
    """Return value: returns a quarter of the way travelled from low to hi
       Argument low: the startpoint of the journey
       Argument high: the endpoing of the journey
       Argument fraction: the fraction traversed at the time
    """
    return low + (hi - low) * fraction

def checkends(s):
    """Return value: True if first character and last character are similar, else False.
       Argument s: a string
    """
    return s[0] == s[-1]

def has42(d):
    """Return value: True if 42 is a key in the dictionary, else False.
       Argument d: dictionary
    """
    return 42 in d

def hasKey(k, d):
    """Return value: True if k is a key in the d, else False.
       Argument d: dictionary
    """
    return k in d

def flipside(s):
    """Return value: first half of string in the second half.
       Argument s: string
    """
    return s[len(s)//2:] + s[:len(s)//2]

def convertFromSeconds(s):
    """Return value: time in a list of [days, hours, minutes, seconds].
       Argument s: nonnegative integer, number of seconds
    """
    days = s // (24*60*60)  # Number of days
    s = s % (24*60*60)      # The leftover
    hours = s // (60*60)
    s = s % (60*60)
    minutes = s // 60
    seconds = s % 60
    return [days, hours, minutes, seconds]