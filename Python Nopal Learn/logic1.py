# CUSTOM FUNCTION
def crange(a,b):
  return range(a, b + 1)

def printnln(a):
  print(a, end="")


#SOAL 1
for y in crange(1,9):
  for x in crange(1,9):
    if x == y:
      printnln("*")
    else:
      printnln(" ")
  print()

print()
print()
print()
print()

#SOAL 2
 #ini Jawaban soal 2
for y in crange(1,9):
  for x in crange(1,9):
    if x == 9-(y-1):
      printnln("*")
    else:
      printnln(" ")
  print() 

# print() 
# print() 
# print() 
# print() 



#SOAL 3 
for y in crange(1,9):
  for x in crange(1,9):
    if x == 9 - (y-1) or x == y:
      printnln("*")
    else:
      printnln(" ")

  print()

 #print
 # print
 # print
#ARTERNATIF

for y in crange(1,9):
  for x in crange(1,9):
    if x == 9 - (y-1):
      printnln("*")
    elif x == y:
      printnln("*")
    else:
      printnln(" ")

  print()
#print
#print
 
 #SOAL 4
for y in crange(1,9):
  for x in crange(1,9):
    if x == y:
      printnln("*")
    elif x == 9 - (y-1):
      printnln("*")
    elif x == 5:
      printnln("*")
    elif y == 5:
      printnln("*")
    else:
      printnln(" ")
  
  print()

print()  
print()  
print()  
     

#SOAL 5
for y in crange(1,9):
  for x in crange(1,9):
    if x <= y:
      printnln("*")
    else:
      printnln(" ")

  print()
#KALAU INI ADALAH BINTANG(*) AKAN MUNCUL JIKA NILAI X KURANG DARI Y CONTOH X=2 DAN Y=3 MAKA AKAN MUNNCUL BINTANG GESSSS JADI BEGTIU YA TEMAN TEMANN
print()


#SOAL 6 
# for y in crange(1,9):
#   for x in crange(1,9):
#     if x >= 9 - (y-1):
#       printnln("*")
#     else:
#       printnln(" ")

#   print()
# #DISINI AKAN MUNCUL BINTANG JIKA NILAI X LEBIH BESAR DARI OPERASIONAL 9 - (y-1) CONTOH NILAI X =7 DAN OPERASIONALNYA ADALAH 9 - (Y-1) Y= 5 JADI 9 - (5-1)= 9-4 = 5 NILAI Y(5) DAN NILAI X(7) JADI BEGITU TEMAN TEMAN
# print()
# print()

#SOAL 7
# for y in crange(1,9):
#   for x in crange(1,9):
#     if x >= y and x <= 9 - (y-1):
#       printnln("*")
#     elif x <= y and x >= 9 - (y-1):
#       printnln("*")  
#     else:
#       printnln(" ")

#   print()  
# # JADI KUNCI DARI INI ADALAH KALAU NILAI X LEBIH BESAR DARI Y DAN NILAI X KURANG DARI 10 MAKA AKAN MUNCUL BINTANG MULAI DARI ATAS ATAU BARIS Y1, DAN OPSI 2 JIKA NILAI X KURANG DARI NILAI Y DAN NILAI X LEBIH BESAR DARI NILAI OPERASI 9 - (y-1) MAKA AKAN MUNCUL BINTANG
# print()
# print()   
# print()   


#SOAL 8
# for y in crange(1,9):
#   for x in crange(1,9):
#     if x <= y and x <= 9 - (y-1):
#       printnln("*")
#     elif x >= y and x >= 9 - (y-1):
#       printnln("*")  
#     else:
#       printnln(" ")

#   print()  
#JADI KONDISI DISINI AKAN MUNCUL BINNTANG JIKA NILAI X KURANG DARI Y DAN  NILAI X KURANG DARI OPERASIONAL <= 9 - (y-1) ITU OPSI 1 DAN OPSI 2 ADALAH JIKA NILAI X LEBIH DARI NILAI 9 DAN NILAI X LEBIH BESAR DARI OPERASIONAL 9 - (y-1) MAKA AKAN MUNCUL BINTANG YAA OPSI INI KEBALIKAN DARI OPSI 1 GITU AJA SIH TEMAN TEMAN...
# print()
# print()
# print()

#SEKEDAR NYOBA NYOBA AJA

# for y in crange(1,9):
#   for x in crange(1,9):
#     if x == 1 or x == y or x == 9:
#       printnln("*")
#     else:
#       printnln(" ")
  
#   print()

# print()
# print()

# for y in crange(1,9):
#   for x in crange(1,9):
#     if x == 1 or y == 1 or x == 9 or y == 9:
#       printnln("*")
#     else:
#       printnln(" ")
  
#   print()

# print()
# print()

# for y in crange(1,9):
#   for x in crange(1,9):
#     if x == 1 or y == 1:
#       printnln("*")
#      elif x == 9 and :
#       printnln("*") 
#     else:
#       printnln(" ")
  
#   print()
