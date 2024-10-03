#
# hw3pr2.py - algorithms and use-it-or-lose-it
#

print("Onward, Algorithms!")

def shiftN(c, N):
    """ returns c, shifted by N spots """
    if N == 0: return c
    return shiftN( shift1(c), N-1 ) 

def shift1(c):
    """ rotate 1 character, c, by 1 place 
        c must be 1 character.
        non-characters don't change!
    """
    if c not in NEXT_CHAR:   # if c is NOT there,
        return c             # just return it unchanged
    else:
        return NEXT_CHAR[c]  # else return the next char
    
def list_to_str(L):
    """L must be a list of characters;
       this function returns a single string made from them.
    """
    if len(L) == 0:
        return ''
    return L[0] + list_to_str(L[1:])
    
NEXT_CHAR = { "a": "b", "A": "B",
            "b": "c", "B": "C",
            "c": "d", "C": "D",
            "d": "e", "D": "E",
            "e": "f", "E": "F",
            "f": "g", "F": "G",
            "g": "h", "G": "H",
            "h": "i", "H": "I",
            "i": "j", "I": "J",
            "j": "k", "J": "K",
            "k": "l", "K": "L",
            "l": "m", "L": "M",
            "m": "n", "M": "N",
            "n": "o", "N": "O",
            "o": "p", "O": "P",
            "p": "q", "P": "Q",
            "q": "r", "Q": "R",
            "r": "s", "R": "S",
            "s": "t", "S": "T",
            "t": "u", "T": "U",
            "u": "v", "U": "V",
            "v": "w", "V": "W",
            "w": "x", "W": "X",
            "x": "y", "X": "Y",
            "y": "z", "Y": "Z",
            "z": "a", "Z": "A",
        }

def encipher (s, N):
    """Takes in s and N as arguements where s is a string and N is number of times to rotate the string characters.
       Returns a string s with it's characters rotated N times. We make use of function helpers shiftN and list_to_str
    """

    shifted =  [shiftN(c, N) for c in s]
    return list_to_str(shifted)

print("encipher('xyza', 1) == 'yzab'", encipher('xyza', 1))
print("encipher('Z A', 1) == 'A B'", encipher('Z A', 1))

assert encipher('xyza', 1) == 'yzab'
assert encipher('Z A', 1) == 'A B'



# table of probabilities for each letter...
def letProb(c):
    """If c is the space character or an alphabetic character,
       we return its monogram probability (for english),
       otherwise we return 1.0.  We ignore capitalization.
       Adapted from
       http://www.cs.chalmers.se/Cs/Grundutb/Kurser/krypto/en_stat.html
       Note: this should really be converted into a dictionary!
    """
    if c == ' ': return 0.1904
    elif c == 'e' or c == 'E':
        return 0.1017
    elif c == 't' or c == 'T':
        return 0.0737
    elif c == 'a' or c == 'A':
        return 0.0661
    elif c == 'o' or c == 'O':
        return 0.0610
    elif c == 'i' or c == 'I':
        return 0.0562
    elif c == 'n' or c == 'N':
        return 0.0557
    elif c == 'h' or c == 'H':
        return 0.0542
    elif c == 's' or c == 'S':
        return 0.0508
    elif c == 'r' or c == 'R':
        return 0.0458
    elif c == 'd' or c == 'D':
        return 0.0369
    elif c == 'l' or c == 'L':
        return 0.0325
    elif c == 'u' or c == 'U':
        return 0.0228
    elif c == 'm' or c == 'M':
        return 0.0205
    elif c == 'c' or c == 'C':
        return 0.0192
    elif c == 'w' or c == 'W':
        return 0.0190
    elif c == 'f' or c == 'F':
        return 0.0175
    elif c == 'y' or c == 'Y':
        return 0.0165
    elif c == 'g' or c == 'G':
        return 0.0161
    elif c == 'p' or c == 'P':
        return 0.0131
    elif c == 'b' or c == 'B':
        return 0.0115
    elif c == 'v' or c == 'V':
        return 0.0088
    elif c == 'k' or c == 'K':
        return 0.0066
    elif c == 'x' or c == 'X':
        return 0.0014
    elif c == 'j' or c == 'J':
        return 0.0008
    elif c == 'q' or c == 'Q':
        return 0.0008
    elif c == 'z' or c == 'Z':
        return 0.0005
    else:
        return 1.0

def getSum(x):
    return sum([letProb(z) for z in x])

def decipher(s):
    """Takes in the argument s of an encrypted string.
       Uses LC to form all possible decryptions of s.
       LoL calls getSum which uses letProb to get the probability of each decryption being an English sentence.
       The sentence that has the greatest probability is returned.
    """
    LC = [encipher(s, n) for n in range(26)]
    print(LC) 

    LoL = [ [getSum(x), x] for x in LC]
    print(LoL)

    print(max(LoL)[1])
    return max(LoL)[1]


def count(e,L):
    """ count(e,L) returns the number of e's in L """
    LC = [ 1 for x in L if x == e ]
    return sum(LC)

def blsort(L):
    """accepts an argument L that is a list of 1 and 0. Returns a list with elements of L in ascending order.
    """

    ones = count(1, L)
    zeros = count(0, L)
    return [0] * zeros + [1] * ones

# print(blsort([1, 0, 1, 0, 1, 0, 1]))
# print(blsort([1, 0, 1]))


def remOne(e,L):
    """Returns a new copy of L with the first e removed."""
    if len(L) == 0: 
        return L
    elif L[0] == e:
        return L[1:]
    else:
        return L[0:1] + remOne(e, L[1:])
    
def gensort(L):
    """Takes in an argument L with a list of numbers.
       Returns a list with elements in L arragned in increasing order.
    """
    if len(L) == 0:
        return []
    small = min(L)
    others = remOne(small, L)
    return [small] + gensort(others)

# print(gensort([7, 9, 4, 3, 0, 5, 2, 6, 1, 8]))


def jscore(S, T):
    """takes in lists S and T as arguments.
       Returns the number of similar letters in S and T.
    """
    if not S or not T:
        return 0
    if S[0] in T:
        return 1 + jscore(S[1:], remOne(S[0], T))
    return jscore(S[1:], T)

# print(jscore('diner', 'syrup'))
# print(jscore('geese', 'elate'))
# print(jscore('gattaca', 'aggtccaggcgc'))
# print(jscore('gattaca', ''))


def exact_change(target_amount, L):
    """takes in 2 arguments, target amount which is an integer and L a list
       returns True if it is possible to get the exactly target sum from the sum of some components of L, else False 
    """
    if target_amount == 0:
        return True
    if target_amount < 0:
        return False
    if sum(L) < target_amount:
        return False

    useIt = exact_change(target_amount - L[0], L[1:])
    loseIt = exact_change(target_amount, L[1:])

    if useIt or loseIt:
        return True
    else:
        return False
    
# print(exact_change(42, [25, 1, 25, 10, 5]), "False")
# print(exact_change(42, [25, 1, 25, 10, 5, 1]), "True")
# print(exact_change(42, [23, 1, 23, 100]), "False")
# print(exact_change(42, [23, 17, 2, 100]), "True")
# print(exact_change(42, [25, 16, 2, 15]), "True")
# print(exact_change(0, [4, 5, 6]), "True")
# print(exact_change(-47, [4, 5, 6]), "False")
# print(exact_change(0, []), "True")
# print(exact_change(42, []), "False")
    

def LCS(S, T):
    """takes 2 arguments S and T which are strings.
       returns the longest common subsequence of letters in the strings.
    """

    if not S or not T:
        return ""

    if S[0] == T[0]:
        return S[0] + LCS(S[1:], T[1:])
    
    result_1 = LCS(S[1:], T)
    result_2 = LCS(S, T[1:])

    if len(result_1) > len(result_2):
        return result_1
    else:
        return result_2

# print(LCS('abcdefghi', 'efghiabcd'))

def make_change(target_amount, L):
    """Takes in two arguments target amount which is an integer and L which is a list
       returns a list of the elements in L that we use to form the exact target amount
    """
    if target_amount == 0:
        return []
    if target_amount < 0:
        return False
    if sum(L) < target_amount:
        return False

    useIt = exact_change(target_amount - L[0], L[1:])
    loseIt = exact_change(target_amount, L[1:])

    if useIt == True:
        return [L[0]] + make_change(target_amount - L[0], L[1:])
    else:
        return [] + make_change(target_amount, L[1:])
    
# print(sorted(make_change(42, [23, 17, 2, 100])))
    
