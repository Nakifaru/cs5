# Warmup-2 > string_times
def string_times(str, n):
  return str * n

# Warmup-2 > front_times
def front_times(str, n):
  if len(str) > 3:
    return str[0:3] * n
  else:
    return str * n
  
# Warmup-2 > string_bits
def string_bits(str):
  return str[0::2]

# Warmup-2 > string_splosion
def string_splosion(str):
  i = 0
  value = ''
  while i < len(str):
    value += str[0:i + 1]
    i += 1
  return value

# Warmup-2 > last2
def last2(str):
  reps = 0
  for i in range(len(str) - 2):
    if str[i] + str[i + 1] == str[-2] + str[-1]:
      reps += 1
  return reps

# Warmup-2 > array_count9
def array_count9(nums):
  nines = 0
  for x in nums:
    if x == 9:
      nines += 1
  return nines

# Warmup-2 > array_front9
def array_front9(nums):
  if len(nums) > 4:
    for i in range(4):
      if nums[i] == 9:
        return True
  if len(nums) < 4:
    for x in nums:
      if x == 9:
        return True
  return False

# Warmup-2 > array123
def array123(nums):
  for i in range(len(nums) - 2):
    if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
      return True
  return False


# Warmup-2 > string_match
def string_match(a, b):
  pair_matches = 0
  for i in range(min(len(a)-1, len(b)-1)):
    if a[i] + a[i+1] == b[i] + b[i+1]:
      pair_matches += 1
  return pair_matches

# String-2 > double_char
def double_char(str):
  result = ''
  for c in str:
    result += c*2
  return result

# String-2 > count_hi
def count_hi(str):
  hi_s = 0
  for i in range(len(str)-1):
    if str[i] + str[i+1] == 'hi':
      hi_s += 1
  return hi_s

# String-2 > cat_dog
def cat_dog(str):
  cats = 0
  dogs = 0
  for i in range(len(str)-2):
    if str[i] + str[i+1] + str[i+2] == 'cat':
      cats += 1
    if str[i] + str[i+1] + str[i+2] == 'dog':
      dogs += 1
  if cats == dogs:
    return True
  return False

# String-2 > count_code
def count_code(str):
  codes = 0
  for i in range(len(str)-3):
    if str[i] == 'c':
      if str[i+1] == 'o':
        if str[i+3] == 'e':
          codes += 1
  return codes

# String-2 > end_other
def end_other(a, b):
  i = -1
  for j in range(min(len(a),len(b))):
    if a[i].lower() != b[i].lower():
      return False
    i -= 1
  return True

# String-2 > xyz_there
def xyz_there(str):
  for i in range(len(str)-2):
    if str[i] + str[i+1] + str[i+2] == 'xyz':
      if i == 0:
        return True
      elif str[i-1] != '.':
        return True
  return False

# List-2 > count_evens
def count_evens(nums):
  evens = 0
  for x in nums:
    if x % 2 == 0:
      evens += 1
  return evens

# List-2 > big_diff
def big_diff(nums):
  largest = nums[0]
  smallest = nums[0]
  for x in nums:
    largest = max(largest, x)
    smallest = min(smallest, x)
  return largest - smallest

# List-2 > centered_average
def centered_average(nums):
  largest = nums[0]
  smallest = nums[0]
  for x in nums:
    largest = max(largest, x)
    smallest = min(smallest, x)
  centred_total = sum(nums) - largest - smallest
  centred_average = centred_total / (len(nums) - 2)
  return centred_average

# List-2 > sum13
def sum13(nums):
  total = 0
  for i in range(len(nums)):
    if nums[i] != 13:
      if i == 0:
        total += nums[i]
      elif nums[i-1] != 13:
        total += nums[i]
  return total 

# List-2 > sum67
def sum67(nums):
  ignore = False
  total = 0
  for x in nums:
    if x == 6:
      ignore = True
    if ignore == False:
      total += x
    if x == 7:
      ignore = False
  return total

# List-2 > has22
def has22(nums):
  for i in range(len(nums)-1):
    if nums[i] == 2:
      if nums[i+1] == 2:
        return True
  return False