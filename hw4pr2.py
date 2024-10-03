def numToBaseB(N, B):
    """Accepts 2 arguments, N, a non-negative integer and a base B, between 2 and 10 inclusive
       Returns a string of N to the base of B
    """
    if N == 0:
        return ''
    return numToBaseB(N//B, B) + str(N%B)

# print(numToBaseB(3116, 9))
# print(numToBaseB(141474, 8))
# print(numToBaseB(42, 8))
# print(numToBaseB(42, 5))
# print(numToBaseB(42, 10))
# print(numToBaseB(42, 2))
# print(numToBaseB(4, 2))
# print(numToBaseB(4, 3))
# print(numToBaseB(4, 4))
# print(numToBaseB(0, 4))
# print(numToBaseB(0, 2))

def baseBToNum(S, B):
    """Accepts 2 arguments, a string S and an integer B between 2 and 10 inclusive. S is a number to the base B.
       Returns an integer
    """
    if S == '':
        return 0
    return B*baseBToNum(S[:-1], B) + int(S[-1])

# print(baseBToNum('5733', 9))
# print(baseBToNum('1474462', 8))
# print(baseBToNum('222', 4))
# print(baseBToNum("101010", 2))
# print(baseBToNum("101010", 3))
# print(baseBToNum("101010", 10))
# print(baseBToNum("11", 2))
# print(baseBToNum("11", 3))
# print(baseBToNum("11", 10))
# print(baseBToNum("", 10))

def baseToBase(B1, B2, s_in_B1):
    """Accepts 3 arguments: B1 and B2, integers between 2 and 10 inclusive
       and s_in_B1, a string representing a number to base B1.
       Returns a string of the number to base B2.
    """
    decimal = baseBToNum(s_in_B1, B1)
    s_in_B2 = numToBaseB(decimal, B2)

    return s_in_B2

# print(baseToBase(2, 10, "11"))
# print(baseToBase(10, 2, "3"))
# print(baseToBase(3, 5, "11"))
# print(baseToBase(2, 3, '101010'))
# print(baseToBase(3, 10, '1120'))
# print(baseToBase(2, 4, '101010'))
# print(baseToBase(2, 10, '101010'))
# print(baseToBase(5, 2, '4321'))
# print(baseToBase(2, 5, '1001001010'))

def add(S, T):
    """Accepts 2 arguments, S and T, strings representing numbers in binary
       Returns the sum of S and T in binary as a string.
    """
    
    S_decimal = baseBToNum(S, 2)
    T_decimal = baseBToNum(T, 2)
    sum_S_and_T = S_decimal + T_decimal
    sum_binary = numToBaseB(sum_S_and_T, 2)
    return sum_binary

# print(add("11", "1"))
# print(add("11", "100"))
# print(add("110", "11"))
# print(add("11100", "11110"))
# print(add("10101", "10101"))

def addB(S, T):
    """Accepts 2 arguments S and T, strings of binary numbers
       Returns the sum of S and T as a string of binary
    """
    # base cases! Check if empty
    if not S:
        return T
    if not T:
        return S

    # There will be four recursive cases--here is the first one:
    if S[-1] == '0' and T[-1] == '0':
        return addB(S[:-1], T[:-1]) + '0'   # 0 + 0 == 0

    # three more recursive cases still to specify...
    if S[-1] == '1' and T[-1] == '0':
        return addB(S[:-1], T[:-1]) + '1'
    
    if S[-1] == '0' and T[-1] == '1':
        return addB(S[:-1], T[:-1]) + '1'
    
    if S[-1] == '1' and T[-1] == '1':
        S = addB(S[:-1], '1')
        return addB(S, T[:-1]) + '0'
    
# print(addB("11100", "11110"))
# print(addB("10101", "10101"))
# print(addB("11", "11"))
# print(addB("11", "100"))

assert addB('11', '100') == '111'
assert addB("11100", "11110") == '111010'
assert addB('110','11') == '1001'
assert addB('110101010','11111111') == '1010101001'
assert addB('1','1') == '10'


def frontNum(S):
    """Accepts an argument S of a string.
       Returns the number of times the element in index 0 occurs consecutively
    """
    if len(S) <= 1:
        return len(S)
    elif S[0] == S[1]:
        return 1 + frontNum(S[1:])
    else:
        return 1
    
# print(frontNum('1110000'))

def compress(S):
    """Accepts one argument S, a string of binary
       Returns S compressed by run length encoding
    """
    if not S:
        return ''
    x = frontNum(S)
    binary = numToBaseB(x, 2)
    padding = '0' * (7-len(binary))
    compressed_section = S[0] + padding + binary
    return compressed_section + compress(S[x:])
    
print(compress('11111'))
print(compress('101010'))
print(compress(42*'0'))

def uncompress(C):
    """Accepts argument C, a compressed binary string by run-length encoding
       Returns a string of the original binary digits
    """
    if not C:
        return ''
    chunk = C[0] * baseBToNum(C[1:8], 2) 
    return chunk + uncompress(C[8:])

# print(uncompress('01000000'))
# print(uncompress('10000101'))
# print(uncompress('100000010000000110000001000000011000000100000001'))
# Stripes = '0'*16 + '1'*16 + '0'*16 + '1'*16
# print(compress(Stripes))
# print(uncompress('00010000100100000001000010010000'))