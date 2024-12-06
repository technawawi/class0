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


catatan tanggal 6 desember 2024

Catatan Pembacaan Kode Python untuk Soal-Soal Logika dan Pola
Soal 1: Deret Fibonacci
Deskripsi: Deret Fibonacci adalah deret angka yang dimulai dengan 0 dan 1, kemudian setiap angka berikutnya adalah hasil penjumlahan dua angka sebelumnya.
Penjelasan Kode:
Fungsi f(n) digunakan untuk menghitung angka Fibonacci pada indeks n.
Kondisi if n <= 2 mengembalikan 1 karena angka pertama dan kedua dalam deret Fibonacci adalah 1.
Jika n > 2, maka fungsi akan memanggil dirinya sendiri (rekursif) untuk menghitung dua angka sebelumnya dan menjumlahkannya.
Loop for n in range(1, 10) digunakan untuk mencetak hasil Fibonacci dari 1 sampai 9.

Soal 2: Deret Modifikasi Fibonacci
Deskripsi: Ini adalah versi modifikasi dari deret Fibonacci, di mana setiap angka adalah hasil penjumlahan tiga angka sebelumnya.
Penjelasan Kode:
Fungsi f(n) diubah sehingga n <= 3 mengembalikan 1, sementara untuk n > 3, fungsi ini menjumlahkan tiga angka sebelumnya.
Fungsi rekursif ini akan terus dipanggil sampai memenuhi syarat dasar (n <= 3).

Soal 3: FPB dan KPK

Deskripsi: Fungsi untuk menghitung Faktor Persekutuan Terbesar (FPB) dan Kelipatan Persekutuan Terkecil (KPK) dari dua bilangan.
Penjelasan Kode:
Fungsi fpb(a, b) menggunakan Algoritma Euclidean untuk menghitung FPB dengan memanfaatkan operasi modulus (%).
Fungsi kpk(a, b) menghitung KPK dengan rumus:

𝐾
𝑃
𝐾
(
𝑎
,
𝑏
)
=
𝑎
×
𝑏
𝐹
𝑃
𝐵
(
𝑎
,
𝑏
)
KPK(a,b)= 
FPB(a,b)
a×b
​
 
Fungsi ini akan menghasilkan KPK dari dua angka yang diberikan.
Soal 4: Pola Kotak (Grid 9x9)
Deskripsi: Program ini menghasilkan pola kotak berbentuk grid 9x9 dengan elemen berbeda di posisi tertentu.
Penjelasan Kode:
Variabel UKURAN = 9 digunakan untuk menentukan ukuran grid.
Nested loops (for x in range(1, UKURAN + 1) dan for y in range(1, UKURAN + 1)) digunakan untuk mencetak setiap elemen dalam grid.
Di dalam setiap iterasi, kondisi if-elif digunakan untuk menentukan karakter apa yang dicetak pada posisi (x, y). Misalnya, jika x == y, maka karakter yang dicetak adalah angka untuk diagonal utama.
Soal 5: Pola Kotak Bertingkat
Deskripsi: Menghasilkan pola kotak bertingkat yang terdiri dari beberapa lapisan, masing-masing dengan angka berbeda.
Penjelasan Kode:
Tepi luar grid dicetak dengan angka 1.
Pada baris/kolom tertentu, angka 2 atau 3 dicetak berdasarkan posisinya, misalnya pada lapisan kedua (baris/kolom 2 dan 8) atau lapisan ketiga (baris/kolom 3 dan 7).
Looping dilakukan dengan dua for untuk mengiterasi baris dan kolom, kemudian mencetak angka sesuai dengan kondisi yang telah ditentukan.
Soal 6: Pola Kotak dengan Zona Tepi
Deskripsi: Menampilkan grid dengan angka di tepi, angka 3 di zona dalam, dan angka 5 di pusat.
Penjelasan Kode:
Fungsi yang digunakan mirip dengan soal 5, tetapi kali ini lebih fokus pada pemberian angka 3 di zona dalam dan angka 5 di tengah grid.
Kondisi if dan elif digunakan untuk memisahkan tepi luar, zona dalam, dan titik tengah, dan mencetak angka yang sesuai.
Soal 7: Pola Kotak dengan Karakter dan Zona
Deskripsi: Mencetak kotak dengan angka di tepi, angka 3 di kotak dalam, dan angka 2 di tengah, serta penggunaan karakter untuk mengisi pola.
Penjelasan Kode:
Looping digunakan untuk memeriksa posisi (x, y) dan mencetak angka atau karakter berdasarkan kondisi tertentu.
Zona yang lebih dalam (seperti kotak dalam) dicetak dengan angka 3 dan titik tengah dicetak dengan angka 2.
Soal 8: Pola Kotak dengan Zona Khusus
Deskripsi: Ini adalah pola yang lebih kompleks, di mana beberapa zona diberi angka atau karakter khusus untuk menciptakan tampilan kotak bertingkat.
Penjelasan Kode:
Tepi luar diberi angka 1, sementara zona lainnya menggunakan karakter atau angka tertentu seperti A, B, dan 2.
Kondisi if-elif digunakan untuk menentukan zona-zona berbeda, dan setiap posisi (x, y) diperiksa apakah cocok dengan kondisi zona tertentu.
Cara Membaca dan Memahami Kode Secara Umum:
Perhatikan Variabel dan Looping:
Setiap kode dimulai dengan mendeklarasikan variabel yang diperlukan (misalnya UKURAN = 9). Kemudian perhatikan penggunaan looping (seperti for) untuk mengiterasi baris dan kolom pada grid atau deret.

Pahami Fungsi:
Fungsi biasanya digunakan untuk melakukan perhitungan atau pengulangan secara terstruktur. Misalnya, dalam soal Fibonacci, fungsi f(n) digunakan untuk menghitung angka Fibonacci menggunakan rekursi.

Kondisi if-else:
Pada pola atau grid, kondisi if-else digunakan untuk memeriksa posisi (x, y) dan mencetak elemen yang sesuai. Pastikan untuk memahami bagaimana setiap kondisi dipisahkan dan apa yang dicetak berdasarkan setiap kondisi.

Modifikasi dan Praktikkan:
Setelah memahami cara kerja kode, cobalah untuk memodifikasi nilai atau kondisi tertentu untuk melihat bagaimana perubahan tersebut mempengaruhi output. Ini adalah cara yang baik untuk memperdalam pemahaman.

