#OKE GES JADI KITA DISINI AKAN MEMULAI DI LOGIC 3 

def crange(a, b):
  return range(a, b+1)

def printnln(a):
  print(a, end="")

def fib(a):
  if a <= 2:
    return 1
  else:
    return fib(a-1)+fib(a-2)   

#SOAL 1
# 1,1,2,3,5,8,13,21

# def fib(a):
#   if a <= 2:
#     return 1
#   else:
#     return fib(a-1)+fib(a-2)
  
# for n in crange(1,9):
#   printnln(n)
#   printnln("fibonaccinya adalah")
#   print(fib(n))  
# example FIBNYA ADALAH 5 BERARTI ITU LEBIH DARI 2 DAN ITU MASUKNYA ELSE gJADI HARUS DI TAMBAH 5-1 + 5-2 = berarti fib3(2) + fib4(3)=fib5(5) 

#SOAL 2
# def fib(a):
#   if a <= 3:
#     return 1
#   else:
#     return fib(a-1)+fib(a-2)+fib(a-3)
  
# for n in crange(1,9):
#   print(fib(n)) 

# FUNGSI a<=3 ADALAH UNTUK MENENTUKAN NILAI DERET ANGKA AWAL JIKA KITA MENGSETING 3 MAKA NANTI DERET ANGKA AWAL ANGKA 1 SAMPE 3 BEGITU JUGA JIKA PAKAI 2 JADI CUMA 2 DERET ANGKA 1NYA 

#SOAL 3 
# def fpb(a, b):
#   if b == 0:
#     return a
#   else:
#     return fpb(b, a % b)
  
# printnln("FPB 120 Dengan 36 adalah ")
# print(fpb(120, 36))

# def kpk(a, b):
#   return a * b // fpb(a, b)

# printnln("KPK 120 dengan 36 adalah ")
# print(kpk(120, 36))
#CTTN SENDIRI untuk MENCARI SEBUAH FPB PERLU MENGGUNAKAN MODUL, MODUL ADALAH SEBUAH BILANGAN YANG TERSISA DARI PEMBAGIAN MISAL CONTOH 1.10 & 5= 0 DAN CONTOH 2. 50 & 15 = 5 
# DAN UNTUK MENCARI SEBUAH KPK KITA MENGGUNAKAN ANGKA YANG TELAH DI TENTUKAN YAITU 120 DAN 36 DAN DIBAGI DENGAN HASIL DARI FPB YAITU 12 DAN JADINYA ADALAH 360

#SOAL 4
# for y in crange(1,9):
#   for x in crange(1,9):
#     if x == y: 
#       g = x * 2 - 1
#       printnln(g)
#     elif x == 9-(y-1):
#       n = x * 2 - 2
#       printnln(n)
#     elif x < y and x > 9-(y-1):
#       printnln("C")
#     elif x > y and x < 9-(y-1):
#       printnln("A")
#     elif x < y and x < 9-(y-1):
#       printnln("D")
#     elif x > y and x > 9-(y-1):
#       printnln("B")
#     else:
#       printnln(" ")
#   print()          

#SOAL 5
for y in crange(-4, 4):
  for x in crange(-4, 4):
    ax = abs(x)
    ay = abs(y)
    r = ax if ax > ay else ay
    r = 4 - r + 1
    printnln(fib(r))
  print()  

#SOAL 6
# for y in crange(-4, 4):
#   for x in crange(-4, 4):
#     n = abs(x) if abs(x) > abs(y) else abs(y)
#     n = 4 - n + 1
#     if n % 2 == 0:
#      printnln(" ")
#     else:
#       printnln(n)
#   print()  

#SOAL 7
# for y in crange(-4, 4):
#   for x in crange(-4, 4):
#     n = abs(x) if abs(x) > abs(y) else abs(y)
#     n = 4 - n + 1
#     if n % 2 == 0:
#      printnln(" ")
#     else:
#       c = n // 2 + 1
#       printnln(fib(c))
#   print()  

#SOAL 8
# alph = "ABC"
# for y in crange(-4, 4):
#   for x in crange(-4, 4):
#     n = abs(x) if abs(x) > abs(y) else abs(y)
#     n = 4 - n + 1
#     if n % 2 == 0:
#       i = n // 2 - 1
#       printnln(alph[i])
#     else:
#       c = n // 2 + 1
#       printnln(fib(c))
#   print()  
