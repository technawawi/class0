# SOAL 1
# for y in range(1,9):
#   for x in range(1,9):
#     if x == y:
#       print("*", end="")
#     else:
#       print(" ", end="")

#   print()

# Membuat custom function untuk mengakali range
def crange(a,b):
  return range(a, b + 1)

# Membuat custom function untuk tidak membuat garis baru
def printNoLine(a):
  print(a, end="")

# SOAL 2
# for y in crange(1,9):
#   for x in crange(1,9):
#     if x == 9 - (y-1):
#       printNoLine("*")
#     else:
#       printNoLine(" ")

#   print()

# SOAL 3
# for y in crange(1,9):
#   for x in crange(1,9):
#     if x == y or x == 9 - (y-1):
#       printNoLine("*")
#     else:
#       printNoLine(" ")

#   print()


# print()
# print()

# Alternatif dari soal 3 dengan menggunakan elif ketimbang or
# for y in crange(1,9):
#   for x in crange(1,9):
#     if x == y:
#       printNoLine("*")
#     elif x == 9 - (y - 1):
#       printNoLine("*")
#     else:
#       printNoLine(" ")

#   print()

# SOAL 4
# for y in crange(1,9):
#   for x in crange(1,9):
#     if x == y:
#       printNoLine("*")
#     elif x == 9 - (y - 1):
#       printNoLine("*")
#     elif y == 5:
#       printNoLine("*")
#     elif x == 5:
#       printNoLine("*")
#     else:
#       printNoLine(" ")

#   print()

# SOAL 5
# for y in range(1,9):
#   for x in range(1,9):
#     if x <= y:
#       printNoLine("*")
#     else:
#       printNoLine(" ")

#   print()

# SOAL 6
# for y in crange(1,9):
#   for x in crange(1,9):
#     if x >= 9 - (y-1):
#       printNoLine("*")
#     else:
#       printNoLine(" ")

#   print()

# SOAL 7
# for y in crange(1,9):
#   for x in crange(1,9):
#     # if x >= y and x <= 9 - (y-1):
#       # printNoLine("*")
#     if x <= y and x >= 9 - (y-1):
#       printNoLine("*")
#     else:
#       printNoLine(" ")

#   print()

# SOAL 8 
# for y in crange(1,9):
#   for x in crange(1,9):
#     if x <= y and x <= 9 - (y-1):
#       printNoLine("*")
#     elif x >= y and x >= 9 - (y-1):
#       printNoLine("*")
#     else:
#       printNoLine(" ")

#   print()

# for y in crange(1,11):
#   for x in crange(1,11):
#     if x <= 11 and y == 1:
#       printNoLine("*")
#     elif x <= 11 and y == 11:
#       printNoLine("*")
#     elif y <= 11 and x == 1:
#       printNoLine("*")
#     elif y <= 11 and x == 11:
#       printNoLine("*")
#     elif x == y:
#       printNoLine("*")
#     elif x == 11 - (y-1):
#       printNoLine("*")
#     elif x == 6 or y == 6:
#       printNoLine("*")
#     else:
#       printNoLine(" ")
#   print()

# for y in crange(1,10):
#   for x in crange(1,10):
#     if x >= y:
#       printNoLine("*")
#     else:
#       printNoLine(" ")
#   print()

