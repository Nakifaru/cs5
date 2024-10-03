# 1 - Warmup-1 > sleep_in
def sleep_in(weekday, vacation):
  if weekday == False or vacation == True:
    return True
  return False

# 2 - Warmup-1 > diff21
def diff21(n):
  if n > 21:
    return 2 * abs(n - 21)
  else:
    return abs(n -21)

# 3 - Warmup-1 > parrot_trouble  
def parrot_trouble(talking, hour):
  if talking == True and (hour < 7 or hour > 20):
    return True
  return False

# 4 - Warmup-1 > makes10
def makes10(a, b):
  if a == 10 or b == 10:
    return True
  if a + b == 10:
    return True
  return False

# 5 - Warmup-1 > near_hundred
def near_hundred(n):
  if abs(200-n) <= 10 or abs(100-n) <= 10:
    return True
  return False

# 6 - Warmup-1 > pos_neg
def pos_neg(a, b, negative):
  if negative == True and a < 0 and b < 0:
    return True
  if negative == False:  
    if a < 0 and b > 0:
      return True
    elif a > 0 and b < 0:
      return True
  return False

# 7 - Warmup-1 > not_string
def not_string(str):
  if str[0:3] != 'not':
    return 'not ' + str
  return str

# 8 - Warmup-1 > missing_char
def missing_char(str, n):
  return str[0:n] + str[n+1:]

# 9 - Warmup-1 > front_back
def front_back(str):
  if len(str) < 2:
    return str
  else:
    return str[-1] + str[1:-1] + str[0]

# 10 - Warmup-1 > front3
def front3(str):
  if len(str) < 3:
    return str * 3
  return str[0:3] * 3

# 11 - Warmup-1 > monkey_trouble
def monkey_trouble(a_smile, b_smile):
  if a_smile == b_smile:
    return True
  return False

# 12 - Warmup-1 > sum_double
def sum_double(a, b):
  if a == b:
    return (a + b) * 2
  return a + b

# 12 - String-1 > hello_name
def hello_name(name):
  return "Hello " + name + "!"

# 13 - String-1 > make_abba
def make_abba(a, b):
  return a + b + b + a

# 14 - String-1 > make_tags
def make_tags(tag, word):
  return "<" + tag + ">" + word + "</" + tag + ">"

#15 - String-1 > make_out_word
def make_out_word(out, word):
  return out[0:len(out)/2 ]  + word + out[len(out)/2:]

#16 - String-1 > extra_end
def extra_end(str):
  return str[-2:] * 3

# 17 - String-1 > first_two
def first_two(str):
  if len(str) < 2:
    return str
  return str[:2]

# 18 - String-1 > first_half 
def first_half(str):
  return str[0:len(str)/2]

# 19 - String-1 > without_end
def without_end(str):
  return str[1:-1]

# 20 - String-1 > combo_string
def combo_string(a, b):
  if len(a) < len(b):
    return a + b + a
  return b + a + b

# 21 - String-1 > non_start
def non_start(a, b):
  return a[1:] + b[1:]

# 22 - String-1 > left2
def left2(str):
  return str[2:] + str[0:2]

# 23 - Logic-1 > cigar_party
def cigar_party(cigars, is_weekend):
  if is_weekend == False and 40 <= cigars <= 60:
    return True
  if is_weekend == True and cigars >= 40:
    return True
  return False

# 24 - Logic-1 > date_fashion
def date_fashion(you, date):
  if you <= 2 or date <= 2:
    return 0
  if you >= 8 or date >= 8:
    return 2
  return 1

#25 - Logic-2 > make_bricks
def make_bricks(small, big, goal):
  if goal > big*5 + small:
    return False
  if goal % 5 > small:
    return False
  return True

#26 - Logic-2 > lone_sum
def lone_sum(a, b, c):
  sum = a + b + c
  if a == b or a == c:
    sum = sum - a
  if a == b or b == c:
    sum = sum - b
  if c == a or c == b:
    sum = sum - c
  return sum
