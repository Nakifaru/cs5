# CS5, hw4pr1
# Filename: hw4pr1.py
# Name: Michael Mumo
# Problem description: Binary <-> decimal conversions

def isOdd(n):
    """Takes in argument of an integer.
       Returns True if it is odd and False if it is even.
    """
    if n % 2 == 0:
        return False
    return True

print("isOdd(42)    should be  False :", isOdd(42))
print("isOdd(43)    should be  True :", isOdd(43))


def numToBinary(N):
    """Takes in an argument of an integer to the base of ten.
       Returns a string of the number converted to base 2.
    """
    # print(N)
    if N == 0:
        return ''
    return  numToBinary(N//2) + str(N%2)

print("numToBinary(0)      should be  '' :",  numToBinary(0))    
print("numToBinary(42)     should be  '101010' :",  numToBinary(42))


def binaryToNum(S):
    """Takes in a decimal integer as an argument S
       Returns an integer representing S in binary.
    """

    if S == '':
        return 0
    return 2*binaryToNum(S[:-1]) + int(S[-1])
    
print("binaryToNum('')     should be  0 :",  binaryToNum(''))
print("binaryToNum('101010') should be  42 :",  binaryToNum('101010'))

def increment(S):
    """Takes in an argument S, an 8-character string of 0 and 1 representing a binary number
       Returns the next larger number as an 8-character string of binary
    """

    if S == '11111111':
        return '00000000'

    decimal = binaryToNum(S)    #Converts the input to decimal
    next_decimal = decimal + 1  # Uses inbuild python math to increment the decimal 
    next_binary = numToBinary(next_decimal)  # Converts the number back to binary
    next_8_binary = '0' * (8-len(next_binary)) + next_binary   # Adds leading 0s to make z have a length of 8
    return next_8_binary

print("increment('00101001')    should be  00101010 :", increment('00101001'))
print("increment('00000011')    should be  00000100 :", increment('00000011'))
print("increment('11111111')    should be  00000000 :", increment('11111111'))

def count(S, n):
    """Accepts S, an 8-character string of 0 and 1 representing a binary number and n the number of times to increment S
       Prints n times the number incremented by one to a total of n times as an 8-character string of binary 
    """
    
    if n == 0:
        print(S)
    else:
        print(S)
        count(increment(S), n-1)

# count("00000000", 4)
# count("11111110", 5)

def numToTernary(N):
    """Accepts an argument N which is a decimal number
       Returns N converted to Ternary as a string
    """
    # numToTernary(59) returns 2012. From the left, since we have a base of 3
    # converting back to decimal is 2*3**0 + 1*3**1 + 0*3**2 + 2*3**3 which is 59. 
    if N == 0:
        return ''
    return  numToTernary(N//3) + str(N%3)

# print(numToTernary(59))
# print(numToTernary(42))

def ternaryToNum(S):
    """Accepts an argument S, a string of a number to base 3
       Returns S converted to a decimal
    """
    if S == '':
        return 0
    return 3*ternaryToNum(S[:-1]) + int(S[-1]) 

# print(ternaryToNum('12211010'))  


def balancedTernaryToNum(S):
    """Takes in a balanced Ternary with +s, -s, and 0s.
       Makes use of the conversion dictionary to convert elements to their representative value.
       Returns the number in decimal.
    """
    conversion = {
        '+': 1,
        '-': -1,
        '0': 0
    }

    if S == '':
        return 0
    return 3*balancedTernaryToNum(S[:-1]) +  conversion[S[-1]]

# print(balancedTernaryToNum('+---0'))
# print(balancedTernaryToNum('++-0+'))

def numToBalancedTernary(N):
    """Accepts N, a decimal number.
       Returns a string of N converted to a balanced ternary.
    """

    if N == 0:
        return ''
    if N % 3 == 0:
        return numToTernary(N//3) + '0'
    if N % 3 == 1:
        return numToTernary(N//3) + '+'
    if N % 3 == 2:
        return numToTernary((N//3) + 3) + '-'    

print(ternaryToNum('12211010'))
print(ternaryToNum('1120'))
