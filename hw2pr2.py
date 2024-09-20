# CS5 Gold, hw2pr2
# Filename: hw2pr2.py
# Name: Michael Mumo
# Problem description: Sleepwalking student

import random 
import time
import sys 

def rs():
    """rs chooses a random step and returns it.
       Note that a call to rs() requires parentheses.
       Arguments: none at all!
    """
    return random.choice([-1, 1])

def rwpos(start, nsteps):
    """ rwpos models a random walker that
        * starts at the int argument, start
        * takes the int # of steps, nsteps

        rwpos returns the final position of the walker.
    """
    time.sleep(0.1)
    print('location is', start)
    if nsteps == 0:
        return start
    else:
        newpos = start + rs()  # take one step
        return rwpos(newpos, nsteps - 1)
    
# rwpos(42, 2)

def string_walkway( start, low, hi ):
    """ this function constructs a string for the current wandering-situation
    """
    walkway = "_"*(hi-low)    # create a walkway string with (hi-low) underscores

    w = (start-low)           # our sleepwalker's location, w, is start-low
    walkway = walkway[:w] + u"\U0001F680" + walkway[w:]  # put our sleepwalker, "W", there at w

    walkway = u"\U0001F30E" + walkway + 	u"\U0001F315"              # surround with spaces, for now...
    return walkway


def rwsteps(start, low, hi):
    """ rwsteps models a spaceship pilot lost in space which
        * is _currently_ at point start in space between the moon and earth
        * is in a walkway from low to hi
        + returns the # of steps it takes for the astronaut to land on earth or moon
        
        Example Run:    rwsteps( 4, 0, 8 )

        Example outputs:
        In [15]: run hw2pr2.py
        🌎____🚀____🌕
        🌎_____🚀___🌕
        🌎____🚀____🌕
        🌎___🚀_____🌕
        🌎____🚀____🌕
        🌎_____🚀___🌕
        🌎______🚀__🌕
        🌎_____🚀___🌕
        🌎______🚀__🌕
        🌎_______🚀_🌕
        🌎________🚀🌕

        In [16]: run hw2pr2.py
        🌎____🚀____🌕
        🌎_____🚀___🌕
        🌎______🚀__🌕
        🌎_____🚀___🌕
        🌎____🚀____🌕
        🌎___🚀_____🌕
        🌎__🚀______🌕
        🌎_🚀_______🌕
        🌎__🚀______🌕
        🌎_🚀_______🌕
        🌎__🚀______🌕
        🌎_🚀_______🌕
        🌎🚀________🌕
    """
    walkway = string_walkway( start, low, hi ) # create a string with our walker
    print(walkway)                             # print our string  
    time.sleep(0.05)                           # include a dramatic pause

    if start <= low or start >= hi:            # base case: no steps if we're at an end or beyond
        return 0
    else:
        newstart = start + rs()                # take one step, create newstart from old start
        return 1 + rwsteps(newstart, low, hi)  # count one step, recurse for the rest of the trip!




# Fixed building size
exit1 = 0
exit2 = 15

def burning_building( human, fire ):
    """ this function constructs the floor that is on fire

    human_v_fire(4, 10)
    ||_____🏃_____🔥_____||
    ||______🏃_____🔥____||
    ||_____🏃_______🔥___||
    ||____🏃_______🔥____||
    ||___🏃_______🔥_____||
    ||__🏃_________🔥____||
    ||_🏃___________🔥___||
    ||🏃___________🔥____||
    You win! You made it out of the burning builing!


    ||_____🏃_____🔥_____||
    ||____🏃_______🔥____||
    ||___🏃_________🔥___||
    ||__🏃___________🔥__||
    ||_🏃_____________🔥_||
    ||__🏃_____________🔥||
    ||__🏃__🔥___________||
    ||___🏃__🔥__________||
    ||__🏃__🔥___________||
    ||___🏃🔥____________||
    You burned! Game Over


    """
    floor = "_"*(exit2 - exit1) 

    f = (fire - exit1)           
    floor = floor[:f] +	u"\U0001F525" + floor[f:]

    h = (human - exit2)
    floor = floor[:h] + u"\U0001F3C3" + floor[h:]

    floor = "||" + floor + "||"              
    return floor


def human_v_fire(human, fire):
    """Takes in argument of human position and fire position, then runs till the human escapes or burns.
    """
    floor = burning_building(human, fire) 
    print(floor)                              
    time.sleep(0.05)                           

    if human < exit1 or human > exit2:
        print("You win! You made it out of the burning builing!")          
        return
    elif human == fire or fire - human == 1:
        print("You burned! Game Over")
        return 
    elif fire <= exit1 or fire >= exit2:
        return human_v_fire(human, random.randint(1, 9))  #Fire jumps to random position when it gets to the end
    else:
        fire_new = fire + rs()   
        human_new = human + rs()
        return human_v_fire(human_new, fire_new)  # Both position change by one randomly


 