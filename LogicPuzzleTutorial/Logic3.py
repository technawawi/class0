# CUSTOM FUNCTION
def crange(a,b):
  return range(a, b + 1)

def printNoLine(a):
  print(a, end="")

# SOAL 1 / FIBONACCI
# 1,1,2,3,5,8,13 (angka yang ditambah sebelumnya dan menghasilkan selanjutnya disebut fibonacci)
# def fibonacci(a):
#   if a <= 2:
#     return 1
#   else:
#     return fibonacci(a - 1) + fibonacci(a - 2)
  
# for n in crange(1,10):
#   printNoLine(n)
#   printNoLine(" Fibonaccinya adalah ")
#   print(fibonacci(n))

# SOAL 2 / FIBONACCI 3
# def fibonacci3(a):
#   if a <= 3:
#     return 1
#   else:
#     return fibonacci3(a - 1) + fibonacci3(a - 2) + fibonacci3(a - 3)
  
# for n in crange(1,9):
#   printNoLine(n)
#   printNoLine(" Fibonaccinya adalah ")
#   print(fibonacci3(n))

# SOAL 3 / FPB & KPK
# FPB adalah bilangan terbesar yang bisa membagi dua atau lebih angka tanpa sisa
# def fpb(a,b):
#   if b == 0:
#     return a
#   else:
#     return fpb(b, a % b)
  
# print("Faktor Persekutuan Terbesar dari 120 dengan 36 adalah: ",fpb(6, 12))

# KPK adalah bilangan terkecil yang merupakan kelipatan bersama dari dua atau lebih angka. 
# def kpk(a,b):
#   return a * b // fpb(a, b)

# printNoLine("Kelipatan Persekutuan Terkecil dari 120 dengan 36 adalah: ")
# print(kpk(120, 36))

# SOAL 4
# for y in crange(1,9):
#   for x in crange(1,9):
#     if x == y:
#       odd = x * 2 - 1
#       printNoLine(odd)
#     elif x == 9 - (y-1):
#       even = x * 2 - 2
#       printNoLine(even)
#     elif x >= y and x <= 9 - (y-1):
#       printNoLine("A")
#     elif x <= y and x >= 9 - (y-1):
#       printNoLine("C")
#     elif x <= y and x <= 9 - (y-1):
#       printNoLine("D")
#     elif x >= y and x >= 9 - (y-1):
#       printNoLine("B")
#     else:
#       printNoLine(" ")
#   print()

# SOAL 5
# fungsi abs berguna untuk menghilangkan minus pada angka-angka minus -1 0 1 => 1 0 1

bound = 9 // 2

def fibonacci(a):
  if a <= 2:
    return 1
  else:
    return fibonacci(a - 1) + fibonacci(a - 2)

# for y in crange(-bound, bound):
#   for x in crange (-bound, bound):
#     absolutedX = abs(x)
#     absolutedY = abs(y)
#     result = absolutedX if absolutedX > absolutedY else absolutedY
#     result = 4 - result + 1
#     printNoLine(fibonacci(result))
#   print()

# 111111111
# 111111111
# 112222211
# 112333211
# 112353211
# 112333211
# 112222211
# 111111111
# 111111111

# SOAL 6
# for y in crange(-bound, bound):
#   for x in crange(-bound, bound):
#     n = abs(x) if abs(x) > abs(y) else abs(y)
#     n = 4 - n + 1
#     if n % 2 == 0:
#       printNoLine(" ")
#     else:
#       printNoLine(n)
#   print()

# SOAL 7
# for y in crange(-bound, bound):
#   for x in crange(-bound, bound):
#     n = abs(x) if abs(x) > abs(y) else abs(y)
#     n = 4 - n + 1
#     if n % 2 == 0:
#       printNoLine(" ")
#     else:
#       c = n // 2 + 1
#       printNoLine(fibonacci(c))
#   print()

  # SOAL 8
alphabet =  "ABC"
for y in crange(-bound, bound):
  for x in crange(-bound, bound):
    n = abs(x) if abs(x) > abs(y) else abs(y)
    n = 4 - n + 1
    if n % 2 == 0:
      index = n // 2 - 1
      printNoLine(alphabet[index])
    else:
      c = n // 2 + 1
      printNoLine(fibonacci(c))
  print()