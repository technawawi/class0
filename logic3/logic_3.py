# LOGIC 3

# deret Finobacci = 0,1,1,2,3,5,8,13
# rumus angka Finobacci dalam python F(n) = F(n-1) + F(n-2) yang mana n > 1

# SOAL 1

def f(n):
  if n <= 2:
    return 1
  else:
    return f(n - 1) + f(n - 2)

for n in range(1, 10):
  print(n, end="")
  print(" Fibonaccinya adalah ", end="")
  print(f(n))

# SOAL 2

def f(n):
  if n <= 3:
    return 1
  else:
    return f(n - 1) + f(n - 2) + f(n - 3)

for n in range(1,10):
  print(n,  end="")
  print(" Finobaccinya adalah ", end="")
  print(f(n))

#SOAL 3

def fpb(a, b):
  if b == 0:
    return a
  else:
    return fpb(b, a % b)

print("FPB 120 dengan 36 adalah")
print(fpb(120, 36))

def kpk(a, b):
  return a * b // fpb(a ,b)
print("KPK dari 120 dan 36 adalah")
print(kpk(120, 36))

# SOAL 4

UKURAN = 9

for x in range(1, UKURAN + 1):
  row = ""
  for y in range(1, UKURAN + 1):
    if x == y:
      row += str(x + y -1) # diagonal utama
    elif x + y == UKURAN + 1:
      row += str((y * 2) - 2) # Digonal kedua
    elif x < y and x + y < UKURAN + 1:
      row += 'A' #segitga yang dikiri atas
    elif x < y and x + y > UKURAN + 1:
      row += 'B' # segitiga yang dikanan atas
    elif x > y and x + y > UKURAN + 1:
      row += 'C' # segitiga yang kanan bawah
    elif x > y and x + y < UKURAN + 1:
      row += 'D' # segitiga kiri bawah
  print(row)

# SOAL 5 

UKURAN = 9

# Loop untuk setiap baris
for x in range(1, UKURAN + 1):
    # Loop untuk setiap kolom dalam baris
    for y in range(1, UKURAN + 1):
        # Tentukan angka yang dicetak berdasarkan posisi (x, y)
        if (x == 1 or x == UKURAN or y == 1 or y == UKURAN or x == 2 or x == 8 or y == 2 or y == 8):
            print('1', end='')
        elif (x in [3, 7] and 3 <= y <= 7) or (y in [3, 7] and 3 <= x <= 7):
            print('2', end='')
        elif (x in [4, 6] and 4 <= y <= 6) or (y in [4, 6] and 4 <= x <= 6):
            print('3', end='')
        elif (x == 5 and y == 5):
            print('5', end='')
        else:
            print(' ', end='')
    print()


# soal 6
UKURAN = 9  

# Loop untuk setiap baris
for x in range(1, UKURAN + 1):
    # String untuk menampung satu baris
    baris = ""
    for y in range(1, UKURAN + 1):
        if x in {1, UKURAN} or y in {1, UKURAN}:  # Tepi luar
            baris += '1'
        elif (x in {3, 7} and 3 <= y <= 7) or (y in {3, 7} and 3 <= x <= 7):  # Kotak dalam
            baris += '3'
        elif x == 5 and y == 5:  # Titik tengah
            baris += '5'
        else:  # Area kosong
            baris += ' '
    # Cetak baris setelah selesai
    print(baris)

# soal 7

UKURAN = 9  
for x in range(1, UKURAN + 1):
    # String untuk menampung satu baris
    line = ""
    for y in range(1, UKURAN + 1):
        # Tepi luar
        if x in {1, UKURAN} or y in {1, UKURAN}:
            line += '1'
        # Kotak dalam
        elif (x in {3, 7} and 3 <= y <= 7) or (y in {3, 7} and 3 <= x <= 7):
            line += '1'
        # Titik tengah
        elif x == 5 and y == 5:
            line += '2'
        # Area kosong
        else:
            line += ' '
    # Cetak baris setelah selesai
    print(line)
print()


# soal 8
UKURAN=9
for x in range(1, UKURAN + 1):
    for y in range(1, UKURAN + 1):
        if x == 1 or x == UKURAN or y == 1 or y == UKURAN:
            print('1', end= '')
        elif (x == 2 or x == 8) and 2 <= y <= 8 or (y == 2 or y == 8) and 2 <= x <= 8:
            print('A', end='')
        elif (x == 4 or x == 6) and 4 <= y <= 6 or (y == 4 or y == 6) and 4 <= x <= 6                          :
            print('B', end='')
        elif x == 5 and y == 5:
            print('2', end= '')
        elif(x == 3 or x == 7) and 3 <= y <= 7 or (y == 3 or y == 7) and 3 <= x <= 7:
            print('1', end='')
        else:
            print(' ', end='')
    print()
