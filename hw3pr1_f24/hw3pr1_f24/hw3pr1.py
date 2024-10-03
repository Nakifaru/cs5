# CS5 Gold, Lab 3
# Filename: hw3pr1.py
# Name: Michael Mumo
# Problem description: Lab 3 problem, "Sounds Good!"

import time
import random
import math
import csaudio
from csaudio import *
import wave
wave.big_endian = 0  # if you are having trouble, try commenting out this line...



# a function to get started with a reminder
# about list comprehensions...
def three_ize(L):
    """three_ize is the motto of the green CS 5 alien.
       It's also a function that accepts a list and
       returns a list of elements each three times as large.
    """
    # this is an example of a list comprehension
    LC = [3 * x for x in L]
    return LC


# Function to write #1:  scale
def scale (L, scale_factor):
    return [x * scale_factor for x in L]


# here is an example of a different method
# for writing the three_ize function:
def three_ize_by_index(L):
    """three_ize_by_index has the same behavior as three_ize
       but it uses the INDEX of each element, instead of
       using the elements themselves -- this is much more flexible!
    """
    # we get the length of L first, in order to use it in range:
    N = len(L)
    LC = [3 * L[i] for i in range(N)]
    return LC


# Function to write #2:  add_2
def add_2(L, M):
    """add_2 adds to the numbers in the same index of 2 lists.
       The returned list is as long as the shorter of the two added lists. 
    """
    N = min(len(L), len(M))
    LC = [L[i] + M[i] for i in range(N)]
    return LC

# Function to write #3:  add_3
def add_3(L, M, P):
    """returns a list with the sum of numbers in the same index of 3
       lists. The returned list is the length of the shortest list input. 
    """
    N = min(len(L), len(M), len(P))
    LC = [L[i] + M[i] + P[i] for i in range(N)]
    return LC    


# Function to write #4:  add_scale_2
def add_scale_2(L, M, L_scale, M_scale):
    """ returns a list with the sum of numbers in similar indexes in
        L and M added together after multiplying them by their respective scales.
    """
    N = min(len(L), len(M))
    LC = [L[i] * L_scale + M[i] * M_scale for i in range(N)]
    return LC


# Helper function:  randomize

def randomize(x, chance_of_replacing):
    """randomize accepts an original value, x
       and a fraction named chance_of_replacing.

       With the "chance_of_replacing" chance, it
       should return a random float from -32767 to 32767.

       Otherwise, it should return x (not replacing it).
    """
    r = random.uniform(0, 1)
    if r < chance_of_replacing:
        return random.uniform(-32768, 32767)
    else:
        return x


# Function to write #5:  replace_some
def replace_some(L, chance_of_replacing):
    """Takes in two arguments, a list L and a floating-point value,
        chance of replacing. replace_some uses the helper funciton randomize
        to return a new list with some of the elements replaced.
    """
    return [randomize(x, chance_of_replacing) for x in L]

assert replace_some(range(40, 50), 0) == list(range(40, 50))
assert replace_some([42], 1.0) != [42]

#
# below are functions that relate to sound-processing ...
#


# a function to make sure everything is working
def test():
    """A test function that plays swfaith.wav
       You'll need swfaith.wav in this folder.
    """
    play('swfaith.wav')


# The example changeSpeed function
def changeSpeed(filename, newsr):
    """changeSpeed allows the user to change an audio file's speed.
       Arguments: filename, the name of the original file
                  newsr, the new sampling rate in samples per second
       Result: no return value, but
               this creates the sound file 'out.wav'
               and plays it
    """
    print("Playing the original sound...")
    play(filename)

    samps, sr = readwav(filename)   # get samps and sr from the file!

    print("The first 10 sound-pressure samples are\n", samps[:10])
    print("The number of samples per second is", sr)

    # we don't really need this line, but for consistency...
    newsr = newsr             # from the input! (not needed, a reminder!) 
    newsamps = samps          # same samples as before
    write_wav([newsamps, newsr], "out.wav") # write data to out.wav
    print("\nPlaying new sound...")
    play('out.wav')   # play the new file, 'out.wav'




def flipflop(filename):
    """flipflop swaps the halves of an audio file
       Argument: filename, the name of the original file
       Result: no return value, but
               this creates the sound file 'out.wav'
               and plays it
    """
    print("Playing the original sound...")
    play(filename)

    samps, sr = readwav(filename)   # get samps and sr from the file!

    print("The first 10 sound-pressure samples are\n", samps[:10])
    print("The number of samples per second is", sr)

    print("Computing new sound...")
    # this gets the midpoint and calls it x
    x = len(samps)//2
    newsamps = samps[x:] + samps[:x]
    newsr = sr               # same sr as before

    write_wav([newsamps, newsr], "out.wav") # write data to out.wav
    print("\nPlaying new sound...")
    play('out.wav')   # play the new file, 'out.wav'




# Sound function to write #1:  reverse

def reverse(filename):
    """reverse plays an audio file in reverse
       Argument: filename, the name of the original file
       Result: no return value, but
               this creates the sound file 'out.wav'
               and plays it
    """
    print("Playing the original sound...")
    play(filename)

    samps, sr = readwav(filename)   # get samps and sr from the file!

    print("The first 10 sound-pressure samples are\n", samps[:10])
    print("The number of samples per second is", sr)

    newsamps = samps[::-1]
    newsr = sr               # same sr as before

    write_wav([newsamps, newsr], "out.wav") # write data to out.wav
    print("\nPlaying new sound...")
    play('out.wav')   # play the new file, 'out.wav'


# Sound function to write #2:  volume
def volume(filename, scale_factor):
    """volume plays an audio file at an altered volume
       Argument: filename, the name of the original file
                 scale_factor: the magnitude by which to alter the volume
       Result: no return value, but
               this creates the sound file 'out.wav'
               and plays it
    """
    print("Playing the original sound...")
    play(filename)

    samps, sr = readwav(filename)   # get samps and sr from the file!

    print("The first 10 sound-pressure samples are\n", samps[:10])
    print("The number of samples per second is", sr)

    newsamps = scale(samps, scale_factor)
    newsr = sr

    write_wav([newsamps, newsr], "out.wav") # write data to out.wav
    print("\nPlaying new sound...")
    play('out.wav')   # play the new file, 'out.wav'


# Sound function to write #3:  static
def static(filename, probability_of_static):
    """volume plays an audio file with random static
       Argument: filename, the name of the original file
                 probability_of_static, the chance static occurs at a samp 
       Result: no return value, but
               this creates the sound file 'out.wav'
               and plays it
    """
    print("Playing the original sound...")
    play(filename)

    samps, sr = readwav(filename)   # get samps and sr from the file!

    print("The first 10 sound-pressure samples are\n", samps[:10])
    print("The number of samples per second is", sr)

    newsamps = replace_some(samps, probability_of_static)
    newsr = sr

    write_wav([newsamps, newsr], "out.wav") # write data to out.wav
    print("\nPlaying new sound...")
    play('out.wav')   # play the new file, 'out.wav'


# Sound function to write #4:  overlay
def overlay(filename1, filename2):
    """overlay plays 2 audio files at the same time
       Argument: filename1 and filename2, the names of the original files
       Result: no return value, but
               this creates the sound file 'out.wav'
               and plays it
    """
    print("Playing the first sound...")
    play(filename1)

    print("Playing the second sound...")
    play(filename2)

    samps1, sr1 = readwav(filename1)
    samps2, sr2 = readwav(filename2)

    print("The first 10 sound-pressure of first sample are\n", samps1[:10])
    print("The first 10 sound-pressure of second sample are\n", samps2[:10])
    print("The number of samples per second for first sample is", sr1)
    print("The number of samples per second for second sample is", sr2)

    newsamps = add_scale_2(samps1, samps2, 0.5, 0.5)
    newsr = sr1

    write_wav([newsamps, newsr], "out.wav") # write data to out.wav
    print("\nPlaying new sound...")
    play('out.wav')   # play the new file, 'out.wav'






# Sound function to write #5:  echo

def echo(filename, time_delay):
    """echo plays an audio file with an overlay of itself with a time delay
       Argument: filename1, the name of the original file
                 time_delay, the time in seconds of the delay between the overlay of the sound
       Result: no return value, but
               this creates the sound file 'out.wav'
               and plays it
    """
    print("Playing the sound...")
    play(filename)

    samps, sr = readwav(filename)

    print("The first 10 sound-pressure of sample are\n", samps[:10])
    print("The number of samples per second for sample is", sr)

    samps1 = samps + [0]*int(time_delay * sr) 
    samps2 = [0]*int(time_delay * sr) + samps
 
    newsamps = add_scale_2(samps1, samps2, 1, 1)
    newsr = sr

    write_wav([newsamps, newsr], "out.wav") # write data to out.wav
    print("\nPlaying new sound...")
    play('out.wav')   # play the new file, 'out.wav'


# Helper function for generating pure tones
def gen_pure_tone(freq, seconds):
    """pure_tone returns the y-values of a cosine wave
       whose frequency is freq Hertz.
       It returns nsamples values, taken once every 1/44100 of a second.
       Thus, the sampling rate is 44100 hertz.
       0.5 second (22050 samples) is probably enough.
    """
    # we get to pick our own sampling rate, sr
    sr = 22050
    # how many data samples to create
    nsamples = int(seconds*sr) # rounds down
    # our frequency-scaling coefficient, f
    f = 2*math.pi/sr   # converts from samples to Hz
    # our amplitude-scaling coefficient, a
    a = 32767.0
    
    # now, create the sound!
    samps = [a*math.sin(f*n*freq) for n in range(nsamples)]
    sr = sr   # not needed, but a reminder
    return [samps,sr]


def pure_tone(freq, time_in_seconds):
    """Generates and plays a pure tone of the given frequence."""
    print("Generating tone...")
    samps, sr = gen_pure_tone(freq, time_in_seconds)

    print("The first 10 sound-pressure samples are\n", samps[:10])
    print("The number of samples per second is", sr)

    print("Writing out the sound data...")
    write_wav([samps, sr], "out.wav") # write data to out.wav

    print("Playing new sound...")
    play('out.wav')




# Sound function to write #6:  chord

