# CUSTOM FUNCTION
def crange(a, b):
  return range(a, b + 1)

def printNoLine(a):
  print(a, end="")

# SOAL 1
# Rumus angka ganjil n * 2 - 1 (ingin dimulai dari 1) / n * 2 + 1 (dari 3)

# for y in crange(1,10):
#   for x in crange(1,10):
#     if x == y:
#       odd = x * 2 - 1
#       printNoLine(odd)
#     else:
#       printNoLine(" ")
#   print()

# SOAL 2
# Rumus angka ganjil n * 2 + 2 (ingin dimulai dari 4) / n * 2 - 2 (dari 0)

# for y in crange(1,10):
#   for x in crange(1,10):
#     if x == 10 - (y-1):
#       even = x * 2 - 2
#       printNoLine(even)
#     else:
#       printNoLine(" ")
#   print()

# SOAL 3
# for y in crange(1,9):
#   for x in crange(1,9):
#     if x == y:
#       odd = x * 2 - 1
#       printNoLine(odd)
#     elif x == 9 - (y-1):
#       even = x * 2 - 2
#       printNoLine(even)
#     else:
#       printNoLine(" ")
#   print()

# SOAL 4
# for y in crange(1,9):
#   for x in crange(1,9):
#     if x == y or x == 5:
#       odd = y * 2 - 1
#       printNoLine(odd)
#     elif x == 9 - (y-1) or y == 5:
#       even = x * 2 - 2
#       printNoLine(even)
#     else:
#       printNoLine(" ")
#   print()

# SOAL 5
# for y in crange(1,9):
#   for x in crange(1,9):
#     if x <= y:
#       odd = x * 2 - 1
#       printNoLine(odd)
#     else:
#       printNoLine(" ")
#   print()

# SOAL 6
# for y in crange(1,5):
#   for x in crange(1,5):
#     if x >= 5- (y-1):
#       value = 5 - (y-1)
#       even = value * 2 - 2
#       printNoLine(even)
#     else:
#       printNoLine(" ")
#   print()

# SOAL 7
# for y in crange(1,5):
#   for x in crange(1,5):
#     if x == y:
#       odd = x * 2 - 1
#       printNoLine(odd)
#     elif x == 5 - (y-1):
#       even = x * 2 - 2
#       printNoLine(even)
#     elif x >= y and x <= 5 - (y-1):
#       printNoLine("A")
#     elif x <= y and x >= 5 - (y-1):
#       printNoLine("B")
#     # elif x 
#     else:
#       printNoLine(" ")
#   print()

# SOAL 8
for y in crange(1,5):
  for x in crange(1,5):
    if x == y:
      odd = x * 2 - 1
      printNoLine(odd)
    elif x == 5 - (y-1):
      even = x * 2 - 2
      printNoLine(even)
    elif x <= y and x <= 5 - (y-1):
      printNoLine("A")
    elif x >= y and x >= 5 - (y-1):
      printNoLine("B")
    else:
      printNoLine(" ")
  print()