# CUSTOM FUNCTION
def crange(a, b):
  return range(a, b + 1)

def printNoLine(a):
  print(a, end="")

def odd(a):
  return a * 2 - 1

def pBound(a):
  return a - 1

# SOAL 1
# print apasi adalah 1, 5 - y
# print angka adalah 1 sampai ganjil(y)

# for y in crange(1,5):
#   for s in crange(1, 5 - y):
#     printNoLine(" ")
#     n = 5 - (y-1)
#   for x in crange(1, odd(y)):
#     printNoLine(x)
#   print()

# SOAL 2
# print spasi adalah 1, y - 1
# print angka adalah 1, 5 - (y-1)

# for y in crange(1, 5):
#   for s in crange(1, y - 1):
#     printNoLine(" ")
#   n = 5 - (y-1)
#   for x in crange(1, odd(n)):
#     printNoLine(x)
#   print()

# SOAL 3
# print spasi adalah 4, 3, 2, 1, 0, 1, 2, 3, 4
# print angka adalah 1, odd(5 - y)

# for y in crange(-4, 4):
#   for s in crange(1, abs(y)):
#     printNoLine(" ")
#   for x in crange(1, odd(5 - abs(y))):
#     printNoLine(x)
#   print()

# SOAL 4
# print spasi adalah 1, 5 - y
# print angka adalah - bound, bound
# bound adalah y - 1

# for y in crange(1,5):
#   for s in crange(1, 5 - y):
#     printNoLine(" ")
#   for x in crange(-pBound(y), pBound(y)):
#     n = y - abs(x)
#     printNoLine(odd(n))
#   print()

# SOAL 5
# for y in crange(1,5):
#   for s in crange(1, y - 1):
#     printNoLine(" ")
#   n = 5 - (y - 1)
#   b = pBound(n)
#   for x in crange(-b, b):
#     c = n - abs(x)
#     printNoLine(odd(c))
#   print()

# SOAL 6
# for y in crange(-4, 4):
#   for s in crange(1, abs(y)):
#     printNoLine(" ")
#   n = 5 - abs(y)
#   b = pBound(n)
#   for x in crange(-b, b):
#     c = n - abs(x)
#     printNoLine(odd(c))
#   print()
