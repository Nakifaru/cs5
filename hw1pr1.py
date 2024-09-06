# CS5, hw1pr1
# Filename: hw1pr1.py
# Name: Mumo
# Problem description: Second Python lab, problem 1!

pi = [3, 1, 4, 1, 5, 9]
e = [2, 7, 1]

# Example problem (problem 0):  [2, 7, 5, 9]
answer0 = e[0:2] + pi[-2:]  
print("answer0:", answer0)

# Problem 1: creating [7, 1]
answer1 = e[1:3]
print("answer1:", answer1)

# Problem 2: [9, 1, 1]
answer2 = pi[::-2]
print("answer2:", answer2)

# Problem 3: [1, 4, 1, 5, 9]
answer3 = pi[1:]
print("answer3:", answer3)

# Problem 4: [1, 2, 3, 4, 5]
answer4 = e[::-2] + pi[0::2]
print("answer4:", answer4)


# Lab1 string practice

h = 'harvey'
m = 'mudd'
c = 'college'

# Problem 5:  'hey'
answer5 = h[0] + h[4:6]    
print("answer5:", answer5)

# Problem 6:  'collude'
answer6 = c[0:4] + m[1:3] + c[-1]    
print("answer6:", answer6)

# Problem 7:  'arveyudd'
answer7 = h[1:] + m[1:]    
print("answer7:", answer7)

# Problem 8:  'hardeharharhar'
answer8 = h[0:3] + (h+m)[-2: 3: -4] + 3*h[:3]
print("answer8:", answer8)

# Problem 9: 'legomyego'
answer9 = c[3:6] + (c+m)[1::6] + h[-1:-3:-1] + c[-2::-4]
print("answer9:", answer9)

# Problem 10 : 'clearcall'
answer10 = c[0::3] + h[1:3] + (c+h)[0::8] + c[2:4]
print("answer10:", answer10)