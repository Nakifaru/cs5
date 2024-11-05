#
# hw9pr2.py
#
# Name:
#

# Here is a function for printing 2D arrays
#  (lists-of-lists) of data

def print2d(A):
    """print2d prints a 2D array, A,
       as rows and columns.
       Argument: A, a 2D list of lists.
       Result: None (no return value)
    """
    num_rows = len(A)
    num_cols = len(A[0])

    for r in range(num_rows):
        for c in range(num_cols):
            print(A[r][c], end = ' ')
        print()

    print()

    return None  # This is implied anyway
                 # when no return statement is present

# some tests for print2d
A = [['X', ' ', 'O'], ['O', 'X', 'O']]
print("2-row, 3-column A is")
print2d(A)

A = [['X', 'O'], [' ', 'X'], ['O', 'O'], ['O', 'X']]
print("4-row, 2-column A is")
print2d(A)


# Create a 2D array from a 1D string
def createA(num_rows, num_cols, s):
    """Returns a 2D array with
           num_rows rows and
           num_cols columns
       using the data from s: across the
       first row, then across the second, etc.
       We'll only test it with enough data!
    """
    A = []
    for r in range(num_rows):
        newrow = []
        for c in range(num_cols):
            newrow += [s[0]] # Add that char
            s = s[1:]        # Get rid of that first char
        A += [newrow]
    return A

# A couple of tests for createA:
A = [['X', ' ', 'O'], ['O', 'X', 'O']]
newA = createA(2, 3, 'X OOXO')
assert newA == A
print("Is newA == A? Should be True:", newA == A)

A = [['X', 'O'], [' ', 'X'], ['O', 'O'], ['O', 'X']]
newA = createA(4, 2, 'XO XOOOX')
assert newA == A

def inarow_3east(ch, r_start, c_start, A):
    """Returns true if ch appears 3 times consecutively in A
       from row r_start, column c_start in the east direction
    """

    num_rows = len(A)
    num_cols = len(A[0])

    if r_start < 0 or r_start >= num_rows:
        return False
    if c_start < 0 or c_start > num_cols - 3:
        return False
    for i in range(3):
        if A[r_start][c_start+i] != ch:
            return False
    return True

def inarow_3south(ch, r_start, c_start, A):
    """Returns true if ch appears 3 times consecutively in A
       from row r_start, column c_start in the south direction
    """

    num_rows = len(A)
    num_cols = len(A[0])

    if r_start < 0 or r_start > num_rows - 3:
        return False
    if c_start < 0 or c_start >= num_cols:
        return False
    for i in range(3):
        if A[r_start+i][c_start] != ch:
            return False
    return True

def inarow_3southeast(ch, r_start, c_start, A):
    """Returns true if ch appears 3 times consecutively in A
       from row r_start, column c_start in the southeast direction
    """

    num_rows = len(A)
    num_cols = len(A[0])

    if r_start < 0 or r_start > num_rows - 3:
        return False
    if c_start < 0 or c_start > num_cols - 3:
        return False
    for i in range(3):
        if A[r_start+i][c_start+i] != ch:
            return False
    return True

def inarow_3northeast(ch, r_start, c_start, A):
    """Returns true if ch appears 3 times consecutively in A
       from row r_start, column c_start in the northeast direction
    """

    num_rows = len(A)
    num_cols = len(A[0])

    if r_start < 0 or r_start - 2 < 0:
        return False
    if c_start < 0 or c_start > num_cols - 3:
        return False
    for i in range(3):
        if A[r_start-i][c_start+i] != ch:
            return False
    return True  

# tests of inarow_3east
A = createA(3, 4, 'XXOXXXOOOOOO')
print("\n3east :")
print2d(A)
assert inarow_3east('X', 0, 0, A) == False
assert inarow_3east('O', 2, 1, A) == True
assert inarow_3east('X', 2, 1, A) == False
assert inarow_3east('O', 2, 2, A) == False
print("All 3east tests worked!")

# tests of inarow_3south
A = createA(4, 4, 'XXOXXXOXXOO OOOX')
print("\n3south :")
print2d(A)
assert inarow_3south('X', 0, 0, A) == True
assert inarow_3south('O', 2, 2, A) == False
assert inarow_3south('X', 1, 3, A) == False
assert inarow_3south('O', 42, 42, A) == False
print("All 3south tests worked!")

# tests of inarow_3southeast
A = createA(4, 4, 'XOOXXXOXX XOOOOX')
print("\n3southeast :")
print2d(A)
assert inarow_3southeast('X', 1, 1, A) == True
assert inarow_3southeast('X', 1, 0, A) == False
assert inarow_3southeast('O', 0, 1, A) == True
assert inarow_3southeast('X', 2, 2, A) == False
print("All 3southeast tests worked!")

# tests of inarow_3northeast
A = createA(4, 4, 'XOXXXXOXXOXOOOOX')
print("\n3northeast :")
print2d(A)
assert inarow_3northeast('X', 2, 0, A) == True
assert inarow_3northeast('O', 3, 0, A) == True
assert inarow_3northeast('O', 3, 1, A) == False
assert inarow_3northeast('X', 3, 3, A) == False
print("All 3northeast tests worked!")



def inarow_Neast(ch, r_start, c_start, A, N):
    """Returns true if ch appears N times consecutively in A
       from row r_start, column c_start in the east direction
    """

    num_rows = len(A)
    num_cols = len(A[0])

    if r_start < 0 or r_start >= num_rows:
        return False
    if c_start < 0 or c_start > num_cols - N:
        return False
    for i in range(N):
        if A[r_start][c_start+i] != ch:
            return False
    return True

def inarow_Nsouth(ch, r_start, c_start, A, N):
    """Returns true if ch appears N times consecutively in A
       from row r_start, column c_start in the south direction
    """

    num_rows = len(A)
    num_cols = len(A[0])

    if r_start < 0 or r_start > num_rows - N:
        return False
    if c_start < 0 or c_start >= num_cols:
        return False
    for i in range(N):
        if A[r_start+i][c_start] != ch:
            return False
    return True

def inarow_Nsoutheast(ch, r_start, c_start, A, N):
    """Returns true if ch appears N times consecutively in A
       from row r_start, column c_start in the southeast direction
    """

    num_rows = len(A)
    num_cols = len(A[0])

    if r_start < 0 or r_start > num_rows - N:
        return False
    if c_start < 0 or c_start > num_cols - N:
        return False
    for i in range(N):
        if A[r_start+i][c_start+i] != ch:
            return False
    return True

def inarow_Nnortheast(ch, r_start, c_start, A, N):
    """Returns true if ch appears N times consecutively in A
       from row r_start, column c_start in the northeast direction
    """

    num_rows = len(A)
    num_cols = len(A[0])

    if r_start < 0 or r_start - (N-1) < 0:
        return False
    if c_start < 0 or c_start > num_cols - N:
        return False
    for i in range(3):
        if A[r_start-i][c_start+i] != ch:
            return False
    return True  

# tests of inarow_Neast
A = createA(5, 5, 'XXOXXXOOOOOOXXXX XXXOOOOO')
print("\nNeast :")
print2d(A)
assert inarow_Neast('O', 1, 1, A, 4) == True
assert inarow_Neast('O', 1, 3, A, 2) == True
assert inarow_Neast('X', 3, 2, A, 4) == False
assert inarow_Neast('O', 4, 0, A, 5) == True
print("All Neast tests worked!")


# tests of inarow_Nsouth
A = createA(5, 5, 'XXOXXXOOOOOOXXXXOXXXOOOXO')
print("\nNsouth :")
print2d(A)
assert inarow_Nsouth('X', 0, 0, A, 5) == False
assert inarow_Nsouth('O', 1, 1, A, 4) == True
assert inarow_Nsouth('O', 0, 1, A, 6) == False
assert inarow_Nsouth('X', 4, 3, A, 1) == True
print("All Nsouth tests worked!")


# tests of inarow_Nsoutheast
A = createA(5, 5, 'XOO XXXOXOOOXXXXOXXXOOOXX')
print("\nNsoutheast :")
print2d(A)
assert inarow_Nsoutheast('X', 1, 1, A, 4) == True
assert inarow_Nsoutheast('O', 0, 1, A, 3) == False
assert inarow_Nsoutheast('O', 0, 1, A, 2) == True
assert inarow_Nsoutheast('X', 3, 0, A, 2) == False
print("All Nsoutheast tests worked!")


# tests of inarow_Nnortheast
A = createA(5, 5, 'XOO XXXOXOOOXOXXXOXXXOOXX')
print("\nNnortheast :")
print2d(A)
assert inarow_Nnortheast('X', 4, 0, A, 5) == True
assert inarow_Nnortheast('O', 4, 1, A, 4) == True
assert inarow_Nnortheast('O', 2, 0, A, 2) == False
assert inarow_Nnortheast('X', 0, 3, A, 1) == False
print("All Nnortheast tests worked!")