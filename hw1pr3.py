# CS5,  hw1pr3
# Filename:  hw1pr3.py
#
# Function Frenzy?!
#

#
# vwl example from class
#
def vwl(s):
    """return value: the number of vowels in s 
       arguement s: a string
    """
    if s == '':
        return 0   # no vowels if s is the empty string
    elif s[0] in 'aeiou':
        return 1 + vwl(s[1:])   # count 1 for the vowel s[0]
    else:
        return 0 + vwl(s[1:])   # 0 + is helpful, even if not strictly nec.

# print tests should succeed visibly:
print( "vwl('poptarts')  should be  2 :",  vwl('poptarts') )
print( "vwl('alien')  should be  3 :",  vwl('alien') )

# assert tests should succeed silently:
assert vwl('poptarts') == 2
assert vwl('alien') == 3


def countis(s):
    """return value: the number of alphabet letter i in s 
       arguement s: a string
    """
    if s == '':
        return 0   # no i if s is the empty string
    elif s[0] == 'i':
        return 1 + countis(s[1:])   # count 1 for the i == s[0]
    else:
        return countis(s[1:])   # 0 + is helpful, even if not strictly nec.

# print tests: succeed visibly
print( "countis('poptarts')  should be  0 :",  countis('poptarts') )
print( "countis('aliiien')  should be  3 :",  countis('aliiien') )

# assert tests: succeed silently
assert countis('poptarts') == 0
assert countis('aliiien') == 3


def dropvwl(s):
    """dropvwl returns the non-vowels in s.  Note that "non-vowels" includes
         characters that are not alphabetic.
       Argument: s, which will be a string
       Return value: s with the vowels removed
    """
    if s == '':
        return ''   # return the empty string
    elif s[0] in 'aeiou':
        return '' + dropvwl(s[1:])   # drop s[0], since it's a vowel
    else:
        return s[0] + dropvwl(s[1:])   # keep s[0], since it's NOT a vowel!

# print tests: succeed visibly
print( "dropvwl('poptarts!')  should be  pptrts! :",  dropvwl('poptarts!') )
print( "dropvwl('aliiiens???')  should be  lns??? :",  dropvwl('aliiiens???') )

# assert tests: succeed silently
assert dropvwl('poptarts!') == 'pptrts!'
assert dropvwl('aliiiens???') == 'lns???'


def letterScore(let):
    """letterScore takes a single-character string, and return the value
        of that character as a Scrabble tile.
       Argument: let, a single-character string
       Return value: Scrabble tile value"""
    
    scoreOf =  {'a': 1,  'b': 3,  'c': 3,  'd': 2,  'e': 1,
                'f': 4,  'g': 2,  'h': 4,  'i': 1,  'j': 8,
                'k': 5,  'l': 1,  'm': 3,  'n': 1,  'o': 1,
                'p': 3,  'q': 10, 'r': 1,  's': 1,  't': 1,
                'u': 1,  'v': 4,  'w': 4,  'x': 8,  'y': 4,  
                'z': 10
                }
    if let not in scoreOf:
        return 0
    else:
        return scoreOf[let] 
#
# Tests
#
print( "letterScore('h') should be  4 :",  letterScore('h') )
print( "letterScore('c') should be  3 :",  letterScore('c') )
print( "letterScore('a') should be  1 :",  letterScore('a') )
print( "letterScore('z') should be 10 :",  letterScore('z') )
print( "letterScore('^') should be  0 :",  letterScore('^') )
print( "letterScore('d') should be 2 :",  letterScore('d') )


def scrabbleScore(S):
    """Takes a string S as an argument and returns the Scrabble score of the string.
       Argument: S, string with any characters
       Return value: Scrabble score of the string S
    """
    if S == '':
        return 0 
    else:
        return letterScore(S[0]) + scrabbleScore(S[1:])
#
# Tests
#
print( "scrabbleScore('quetzal')           should be  25 :",  scrabbleScore('quetzal') )
print( "scrabbleScore('jonquil')           should be  23 :",  scrabbleScore('jonquil') )
print( "scrabbleScore('syzygy')            should be  25 :",  scrabbleScore('syzygy') )
print( "scrabbleScore('?!@#$%^&*()')       should be  0 :",  scrabbleScore('?!@#$%^&*()') )
print( "scrabbleScore('')                  should be  0 :",  scrabbleScore('') )
print( "scrabbleScore('abcdefghijklmnopqrstuvwxyz') should be  87 :",  scrabbleScore('abcdefghijklmnopqrstuvwxyz') )


"""print( "scrabbleScore('food')              should be  8 :",  scrabbleScore('food') )
   print( "scrabbleScore('water')             should be  8 :",  scrabbleScore('water') )
"""


def one_dna_to_rna(c):
    """Converts a single-character c from DNA
        nucleotide to its complementary RNA nucleotide
    """
    # dictionary with each conversion
    conversion = { 'A':'U', 'C':'G', 'G':'C', 'T':'A' }
    #
    # check if the input, c, is a key in the dictionary
    if c in conversion:        # is it a key?
        return conversion[c]   # if so, return its value
    else:                      # otherwise
        return ''              # return the empty string
    
def transcribe(S):
    """Takes in a DNA strand in form of a string 
       and returns the complimentary RNA strand.
    """
    if S == '':
        return '' 
    else:
        return one_dna_to_rna(S[0]) + transcribe(S[1:])    
#
# Tests
#
print( "transcribe('ACGTTGCA')             should be  'UGCAACGU' :",  transcribe('ACGTTGCA') )
print( "transcribe('ACG TGCA')             should be  'UGCACGU' :",  transcribe('ACG TGCA') )  # Note that the space disappears
print( "transcribe('GATTACA')              should be  'CUAAUGU' :",  transcribe('GATTACA') )
print( "transcribe('cs5')                  should be  ''  :",  transcribe('cs5') ) # Note that other characters disappear
print( "transcribe('')                     should be  '' :",  transcribe('') )   # Empty strings!

# assert statements!  See below for details...
assert transcribe('ACGTTGCA') == 'UGCAACGU'
assert transcribe('ACG TGCA') == 'UGCACGU'   # Note that the space disappears
assert transcribe('GATTACA')  == 'CUAAUGU'
assert transcribe('cs5')      == ''        # Note that non-DNA other characters disappear


def dot(L, K):
    """Returns the dot product of vector L and K
    """
    if len(L) != len(K) or len(L) == 0 or len(K) == 0:
        return 0.0
    return L[0] * K[0] + dot(L[1:], K[1:])
#
# Tests
#
print( "dot([5, 3], [6, 4])  should be  42.0 :",  dot([5, 3], [6, 4]) )
print( "dot([5, 3], [6])     should be  0.0 :",  dot([5, 3], [6]) )
print( "dot([], [6])         should be  0.0 :",  dot([], [6]) )
print( "dot([], [])          should be  0.0 :",  dot([], []) )
print( "dot([1, 2, 3, 4], [10, 100, 1000, 10000]) should be  43210.0 :",  dot([1, 2, 3, 4], [10, 100, 1000, 10000]) )   


def ind(e, L):
    """Returns the index of the position of e in sequence L.
       If e is not in L returns the length of L.
    """
    if e not in L:
        return len(L)
    
    if L[0] == e:
        return 0
    else:
        return 1 + ind(e, L[1:])

#
# Tests
#
print( "ind(42, [55, 77, 42, 12, 42, 100]) should be  2 :",  ind(42, [55, 77, 42, 12, 42, 100]) )
print( "ind(55, [55, 77, 42, 12, 42, 100]) should be  0 :",  ind(55, [55, 77, 42, 12, 42, 100]) )
print( "ind(42, list(range(0, 100)))       should be  42 :",  ind(42, list(range(0, 100))) )
print( "ind('hi', ['hello', 42, True])     should be  3 :",  ind('hi', ['hello', 42, True]) )
print( "ind('hi', ['well', 'hi', 'there']) should be  1 :",  ind('hi', ['well', 'hi', 'there']) )
print( "ind('i', 'team')                   should be  4 :",  ind('i', 'team') )
print( "ind(' ', 'outer exploration')      should be  5 :",  ind(' ', 'outer exploration')) 
    