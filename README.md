# class0
Selesaikan video yang ada di dalam modul, dan jika ingin mencatat bisa di push ke link class berikut


catatan 

1. Operator Logika
Operator logika digunakan untuk mengevaluasi beberapa kondisi:

and: True kalau semua kondisi benar.
or: True kalau salah satu kondisi benar.
not: Membalik nilai logis (True jadi False, atau sebaliknya).

x = 5
y = 10

# Semua kondisi benar
print(x > 3 and y < 15)  # True

# Salah satu kondisi benar
print(x > 10 or y > 5)   # True

# Membalik hasil
print(not(x > 3))        # False (karena x > 3 itu True, dibalik jadi False)

Pernyataan Kondisional (if-elif-else)
Ini seperti "jalur keputusan" kita. Program akan memilih berdasarkan kondisi.

Struktur dasar:
if kondisi1:
    # lakukan sesuatu kalau kondisi1 benar
elif kondisi2:
    # lakukan sesuatu kalau kondisi2 benar
else:
    # lakukan sesuatu kalau semua kondisi salah

contoh : umur = 20

if umur < 18:
    print("Anda masih remaja.")
elif umur <= 25:  # sama seperti umur >= 18 and umur <= 25
    print("Anda sudah dewasa muda.")
else:
    print("Anda sudah dewasa.")

# Apa itu Loop?
Loop adalah perulangan untuk menjalankan kode berulang kali, sampai suatu kondisi terpenuhi atau selesai.

Python punya dua jenis loop utama:
for loop: Perulangan dengan jumlah tertentu.
while loop: Perulangan yang berjalan selama kondisinya benar.

for loop dengan logika sederhana
Kita ingin mencetak hanya angka genap dari 1 sampai 10.

contoh: for angka in range(1, 11):  # range(1, 11) = 1 sampai 10
    if angka % 2 == 0:  
    # Mengecek apakah angka genap
        print(angka)

Penjelasan:

- for angka in range(1, 11) artinya perulangan dari 1 sampai 10.
- if angka % 2 == 0 artinya cek apakah angka habis dibagi 2 (genap).
- Hanya angka genap yang dicetak.

Output
2
4
6
8
10

# Menggabungkan Logika dan Loop (Kasus Kompleks)
ingin mencari angka prima dari 1 sampai 10.
Angka prima adalah angka yang hanya bisa dibagi 1 dan dirinya sendiri.

for angka in range(2, 11):  # Angka mulai dari 2 sampai 10
    is_prima = True  # Asumsikan angka prima
    for i in range(2, angka):  # Periksa pembagi dari 2 sampai angka-1
        if angka % i == 0:  # Kalau angka habis dibagi
            is_prima = False  # Angka bukan prima
            break  # Hentikan pemeriksaan
    if is_prima:  # Jika tetap prima
        print(angka, "adalah angka prima")

 Output:
2 adalah angka prima
3 adalah angka prima
5 adalah angka prima
7 adalah angka prima

# Tips Memahami Loop dan Logika
Pahami dasar logika: Gunakan if, break, dan continue untuk mengatur jalannya loop.
Coba buat kasus sederhana: Seperti mencetak angka, mencari angka genap, atau menghentikan loop.
Gunakan print() untuk debugging: Lihat nilai variabel di setiap langkah.
