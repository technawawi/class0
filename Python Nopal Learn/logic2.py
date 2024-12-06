#CUSTOM RANGE
#CUSTOM PRINTNLN
def crange(a,b):
  return range(a, b + 1)

def printnln(a):
  print(a, end="")

#  for n in crange(1,9):
#    j = n * 2 - 1
#      print(j)
  
 #SOAL 1 
# for y in crange(1,9):
#   for x in crange(1,9):
#     if x == y:
#       j = x * 2 - 1
#       printnln(j)
#     else:
#       printnln(" ")
#   print()         

#SOAL 2
# for y in crange(1,9):
#   for x in crange(1,9):
#     if x == 9-(y-1):
#        g = x * 2 - 2
#        printnln(g)
#     else:
#        printnln(" ")
#   print()     

#SOAL 3
# for y in crange(1,9):
#   for x in crange(1,9):
#     if x == y:
#       j = x * 2 - 1
#       printnln(j)
#     elif x == 9-(y-1):
#       g = x * 2 - 2
#       printnln(g)
#     else:
#       printnln(" ")
#   print()
#Note UNTUK INI HASIL TENGAHNYA BISA BERUBAH BISA GANJIL ATAU GENAP TERGANTUNG DARI KODE YANG KITA PASANG TERLEBIH DAHULU ATAU KODE DARI IF KALAU GANJIL DULLU MAKA AKAN GANJIL (9) BEGITU JUGA SEBALIKNYA YA 

#SOAL 4
# for y in crange(1,9):
#   for x in crange(1,9):
#     if x == y:
#       j = x * 2 - 1
#       printnln(j)
#     elif x == 9-(y-1):
#       g = x * 2 - 2
#       printnln(g)
#     elif x == 5:
#       j = y * 2 - 1
#       printnln(j)
#     elif y == 5:
#       g = x * 2 - 2
#       printnln(g)
#     else:
#       printnln(" ")
#   print()   
# DISINI ADA CATATAN PENTING YAITU UNTUK MENGISI KOLOM X=5 KITA HARUS MENGGUNAKAN KODE Y*2-1 BUKAN X KARENA KALAU X NANTI HASILNYA 9 DAN ITU TERJADI KARENA PERHITUNGAN SESUAI RUMUS DARI j=5×2−1=10−1=9 JADI BEGITU GES 

#SOAL 5 
# for y in crange(1,9):
#   for x in crange(1,9):
#     if x <= y:
#       j = x * 2 - 1
#       printnln(j)
#     else:
#       printnln(" ")
#   print() 

#SOAL 6
for y in crange(1,9):
  for x in crange(1,9):
    if x >= 9 - (y-1):
      v = 9 - (y-1)
      g = v * 2 - 2 
      printnln(g)
    else:
      printnln(" ")
  print()   
# # NoTe: UNTUK V DISINI BERFUNGSI UNTUK MENGATUR KOLOM ATAU PENEMPATAN ANGKA MANA YANG TERLEBIH DAHULU KELUAR JIKA Y 1 MAKA V NYA 9 DAN JIKA Y9 MAKA VNYA 1  ATAU CONTOHNYA JIKA Y9 MAKA VNYA 0 DAN Y1 MAKA V ATAU GNYA 16   

#SOAL 7

# for y in crange(1,9):
#   for x in crange(1,9):
#     if x == 9-(y-1):
#       g = x * 2 - 2
#       printnln(g)
#     elif x > y and x < 9-(y-1):
#       printnln("A") 
#     elif x == y:
#       j = x * 2 - 1
#       printnln(j)
#     elif x < y and x > 9-(y-1):
#       printnln("B")  
#     else:
#       printnln(" ")

#   print()      
# CTTN= DISINI TIDAK MENGGUNAKAN = DI ELIF 1 & 3 KARENA SUDAH MEMAKAI KODE YANG MEMUNCULKAN ANGKA 1/0 DAN 16/17 ,JADI JIKA KITA PAKAI = MAKA ANGKA ITU TERHITUNG OLEH SEBAB ITU TIDAK PAKAI AGAR TIDAK EROR GUYSS 
# 
#  
# SOAL 8
# for y in crange(1,9):
#   for x in crange(1,9):
#     if x == y:
#       g = x * 2 - 1
#       printnln(g)
#     elif x < y and x < 9-(y-1):
#       printnln("A")
#     elif x > y and x > 9-(y-1):
#       printnln("B")    
#     elif x == 9-(y-1):
#       n = x * 2 - 2
#       printnln(n)
#     else:
#       printnln(" ")
#   print()           

#UNTUK PENJELASAN INI KURANG LEBIH SAMA DENGAN SOAL DIATAS CUMA DIGABUNG SAJA SAMA SOAL 8 LOGIC 1 BEGITU GUYSSS!!!!
