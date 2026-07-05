# Profil Pemateri: 
'''
Julio Christian Young
Dosen dan Peneliti bidang Artificial Intelligence 
Universitas Multimedia Nusantara
'''

print("Hello World!")

# --- Lebih Jauh dengan Print ---
print("Halo Dunia")
print("Riset Bahasa Python")

# --- Struktur Program Python - Part 1 ---
# Statement
print("Belajar Python menyenangkan")
print("Halo Dunia")
print("Hello World!")
# Variables & Literals
bilangan1 = 5
bilangan2 = 10
kalimat1 = "Belajar Bahasa Python"
# Operators
print(bilangan1 + bilangan2)

# Tugas Praktik
bilangan1 = 20
bilangan2 = 10
print(bilangan1 - bilangan2)

# Tugas Praktik (Kalkulator Sederhana)
harga_asli = 20000
potongan = 2000
harga_setelah_potongan = harga_asli - potongan
harga_final = harga_setelah_potongan * 1.1
print(harga_final)

# --- PYTHON VARIABLES ---
bil1 = 20
bil2 = 10
print = "Halo Dunia"

# --- Aturan Penamaan Python Variables ---
bil1, bil2 = 3, 4
salam = ("Selamat Pagi",)
penutup = "Salam Sejahtera"

del print

# --- Sequence Type - Part 1 ---
contoh_list = [6, "tujuh", 8, 9.0, 10]
print(contoh_list[0])
print(contoh_list[3])

contoh_list = [6, "tujuh", 8, 9.0, 10]
contoh_list[3] = "empat"
print(contoh_list[3])

# Tugas Praktik
contoh_list = [1, "dua", 3, 4.0, 5]
print(contoh_list[0])
print(contoh_list[3])
contoh_list = [1, "dua", 3, 4.0, 5]
contoh_list[3] = "empat"
print(contoh_list[3])

# --- Sequence Type - Part 2 ---
contoh_tuple = ("Juni", "Juli", "Agustus", "September")
print(contoh_tuple[0])

contoh_tuple = ("Juni", "Juli", "Agustus", "September")

# Tugas Praktik
contoh_tuple = ("Januari", "Februari", "Maret", "April")
print(contoh_tuple[0])
contoh_tuple = ("Januari", "Februari", "Maret", "April")
# contoh_tuple[0] = "Desember"
# Output: TypeError

# --- Set Type ---
contoh_list = ["Theo", "Annette", "Mel", "Handy", "Mel"]
print(contoh_list)

contoh_set = {"Theo", "Annette", "Mel", "Handy", "Mel"}
print(contoh_set)

contoh_frozen_set = {"Theo", "Annette", "Mel", "Handy", "Mel"}
print(contoh_frozen_set)

# Tugas Praktik
contoh_list = ["Dewi", "Budi", "Cici", "Linda", "Cici"]
print(contoh_list)
contoh_set = {"Dewi", "Budi", "Cici", "Linda", "Cici"}
print(contoh_set)
contoh_frozen_set = {"Dewi", "Budi", "Cici", "Linda", "Cici"}
print(contoh_frozen_set)

# --- Mapping Type (Dictionary) ---
person = {"nama": "Theo Lau", "pekerjaan": "Data Analyst"}
print(person["nama"])
print(person["pekerjaan"])

# Tugas Praktik
person = {"nama": "John Doe", "pekerjaan": "Programmer"}
print(person["nama"])
print(person["pekerjaan"])

# Tugas Praktik
sepatu = {"nama": "Sepatu Niko", "harga": 150000, "diskon": 30000}
baju = {"nama": "Baju Unikloh", "harga": 80000, "diskon": 8000}
celana = {"nama": "Celana Lepis", "harga": 200000, "diskon": 60000}
daftar_belanja = [sepatu, baju, celana]

# Data yang dinyatakan ke dalam dictionary
sepatu = {"nama": "Sepatu Niko", "harga": 150000, "diskon": 30000}
baju = {"nama": "Baju Unikloh", "harga": 80000, "diskon": 8000}
celana = {"nama": "Celana Lepis", "harga": 200000, "diskon": 60000}

# Hitunglah harga masing-masing data setelah dikurangi diskon
harga_sepatu = sepatu["harga"] - sepatu["diskon"]
harga_baju = baju["harga"] - baju["diskon"]
harga_celana = celana["harga"] - celana["diskon"]

# Hitung harga total
total_harga = harga_sepatu + harga_baju + harga_celana

# Hitung harga kena pajak
total_pajak = total_harga * 0.1

# Cetak total_harga + total_pajak
print(total_harga + total_pajak)

# --- 6 Operator dalam Python ---
print("--- Arithmetic Operators ---")
print("1. Penambahan (+)")
penambahan = 3 + 2
print(penambahan)

print("2. Pengurangan (-)")
pengurangan = 4 - 2
print(pengurangan)

print("3. Perkalian (*)")
perkalian = 3 * 2
print(perkalian)

print("4. Pembagian (/)")
pembagian = 3 / 2
print(pembagian)

print("5. Modulo/Sisa Bagi (%)")
modulo_sisa_bagi1 = 3 % 2
print(modulo_sisa_bagi1)
modulo_sisa_bagi2 = 8 % 2
print(modulo_sisa_bagi2)

print("6. Pangkat (**)")
pangkat = 3**2
print(pangkat)

print("7. Pembagian Pembulatan Bawah (//)")
pembagian_pembulatan_bawah = 3 // 2
print(pembagian_pembulatan_bawah)

print("--- Assignment Operators ---")
print("1. Penambahan (+=)")
# Cara 1: Pakai += (Nilai x berubah jadi 5)
x = 3
x += 2
penambahan1 = x

# Cara 2: Pakai x + 2 (Nilai x berubah jadi 5)
x = 3
x = x + 2
penambahan2 = x

print(penambahan1 == penambahan2)  # Ini baru hasilnya: True

print("2. Pengurangan (-=)")
# Cara 1: Pakai -= (Nilai x berubah jadi 1)
x = 3
x -= 2
pengurangan1 = x

# Cara 2: Pakai x - 2 (Nilai x berubah jadi 1)
x = 3
x = x - 2
pengurangan2 = x

print(pengurangan1 == pengurangan2)  # Ini baru hasilnya: True

print("3. Perkalian (*=)")
# Cara 1: Pakai *= (Nilai x berubah jadi 6)
x = 3
x *= 2
perkalian1 = x

# Cara 2: Pakai x * 2 (Nilai x berubah jadi 6)
x = 3
x = x * 2
perkalian2 = x

print(perkalian1 == perkalian2)

print("4. Pembagian (/=)")
# Cara 1: Pakai /= (Nilai x berubah jadi 1.5)
x = 3
x /= 2
pembagian1 = x

# Cara 2: Pakai x / 2 (Nilai x berubah jadi 1.5)
x = 3
x = x / 2
pembagian2 = x

print(pembagian1 == pembagian2)

print("5. Modulo/Sisa Bagi (%=)")
# Cara 1: Pakai %= (Nilai x berubah jadi 1)
x = 3
x %= 2
modulo_sisa_bagi1 = x

# Cara 2: Pakai x % 2 (Nilai x berubah jadi 1.5)
x = 3
x = x % 2
modulo_sisa_bagi2 = x

print(modulo_sisa_bagi1 == modulo_sisa_bagi2)

print("6. Pangkat (**=)")
# Cara 1: Pakai **= (Nilai x berubah jadi 9)
x = 3
x **= 2
pangkat1 = x

# Cara 2: Pakai x ** 2 (Nilai x berubah jadi 9)
x = 3
x = x**2
pangkat2 = x

print(pangkat1 == pangkat2)

print("7. Pembagian dengan pembulatan ke bawah (//=)")
# Cara 1: x //= 2 (nilai x berubah jadi 1)
x = 3
x //= 2
pembagian_pembulatan_bawah1 = x

# Cara 2: x // 2 (nilai x berubah jadi 1)
x = 3
x = x // 2
pembagian_pembulatan_bawah2 = x

print(pembagian_pembulatan_bawah1 == pembagian_pembulatan_bawah2)

print("--- Comparison Operators ---")
print("1. Persamaan (==)")
print(33 == 33)
print(34 == 33)

print("2. Pertidaksamaan (!=)")
print(34 != 33)
print(33 != 33)

print("3. Lebih besar dari (>)")
print(34 > 33)
print(33 > 34)

print("4. Lebih kecil dari (<)")
print(33 < 34)
print(34 < 33)

print("5. Lebih besar atau sama dengan (>=)")
print(34 >= 33)
print(34 >= 34)
print(33 >= 34)

print("6. Lebih kecil atau sama dengan (<=)")
print(33 <= 34)
print(33 <= 33)
print(34 <= 33)

print("--- Logical Operators ---")
print("1. and")  # semua nilai harus benar
x = 5
print(x >= 1 and x <= 10)

x = 5
print(x >= 1 and x <= 4)

print("2. or")  # salah satu nilai benar
x = 3
print(x >= 1 or x <= 2)

x = 3
print(x >= 5 or x <= 0)

print("3. not")  # pernyataan nilai salah/kebalikannya
x = 7
print(not (x == 7))
print(not (x >= 10))

print("--- Identity Operators ---")
print("1. is")
x = ["Ani", "Budi"]
y = ["Ani", "Budi"]
a = x
print(a is x)  # True, karena ada persamaannya
print(a is y)  # False, karena tidak ada persamaannya

print("2. is not")
x = ["Ani", "Budi"]
y = ["Ani", "Budi"]
a = x
print(a is not x)  # False, karena ada persamaannya
print(a is not y)  # True, karena tidak ada persamaannya

print("Contoh")
x = 10  # mula-mula x = integer
print(type(x) is int)  # True

x /= 3  # x = float
print(type(x) is int)  # False, karena merupakan float

x /= 3  # x = float
print(type(x) is float)  # True, x = float

print("--- Membership Operators ---")
print("1. in")
# True = anggota sequence/set, False = bukan

x = ["Ani", "Budi", "Cici"]
y = "Cici"
z = "Dodi"
print(y in x)  # True, anggota sequence
print(z in x)  # False, bukan anggota

print("2. not in")
# True = bukan anggota sequence/set, False = adalah anggota

x = ["Ani", "Budi", "Cici"]
y = "Cici"
z = "Dodi"
print(y not in x)  # False, adalah anggota
print(z not in y)  # True, bukan anggota

print("--- Nilai Prioritas Nilai Prioritas Operator dalam Python – Part 1 --- ")
print("Draft")
total_harga = 20000
potongan_harga = 0.5
pajak = 0.1  # pajak dalam persen = 10%
harga_bayar = 1 - potongan_harga  # baris pertama
harga_bayar *= total_harga  # baris kedua
pajak_bayar = pajak * harga_bayar  # baris ketiga
harga_bayar += pajak_bayar  # baris keempat
print(harga_bayar)

print("Python Sederhana")
total_harga = 20000
potongan_harga = 0.5
pajak = 0.1  # pajak dalam persen = 10%
harga_bayar = (1 - potongan_harga) * total_harga  # baris pertama
harga_bayar += harga_bayar * pajak  # baris kedua
print(harga_bayar)

print("Tugas Praktik")
# Kode awal
total_harga = 150000
potongan_harga = 0.3
pajak = 0.1  # pajak dalam persen ~ 10%
harga_bayar = 1 - potongan_harga  # baris pertama
harga_bayar *= total_harga  # baris kedua
pajak_bayar = pajak * harga_bayar  # baris ketiga
harga_bayar += pajak_bayar  # baris ke-4
print("Kode awal - harga_bayar=", harga_bayar)

# Penyederhanaan baris kode dengan menerapkan prioritas operator
total_harga = 150000
potongan_harga = 0.3
pajak = 0.1  # pajak dalam persen ~ 10%
harga_bayar = (1 - potongan_harga) * total_harga  # baris pertama
harga_bayar += harga_bayar * pajak  # baris kedua
print("Penyederhanaan kode - harga_bayar=", harga_bayar)

print("--- Nilai Prioritas Operator dalam Python – Part 2 ---")
print("1. (), nilai prioritas = 10")
# Kiri ke kanan, grouping

print("2. x[index], nilai prioritas = 9")
# Kiri ke kanan, mengakses elemen array

print("3. **, nilai prioritas = 8")
# Kanan ke kiri, pangkat

print("4. +x atau -x, nilai prioritas = 7")
# Kiri ke kanan, tanda bilangan positif/negatif

print("5. * / %, nilai prioritas = 6")
# Kiri ke kanan, perkalian pembagian modulus

print("6. + atau -, nilai prioritas = 5")
# Kiri ke kanan, penambahan atau pengurangan

print(
    "7."
    + "a. is, is not, in, not in;"
    + "b. <=, <, >=, >;"
    + "c. == atau !=,"
    + "nilai prioritas = 4"
)
# Kiri ke kanan, membership operator & comparison operator

print("8. not, nilai prioritas = 3")
# Kiri ke kanan, operator logika legasi (not)

print("9. and, nilai prioritas = 2")
# Kiri ke kanan, operator logika konjungsi (and)

print("10. or, nilai prioritas = 1")
# Kiri ke kanan, operator logika disjungsi (or)

print("Contoh 1")
nilai = (1 - 0.3) * 100
# nilai = 0.7 * 100; kurung duluan
# nilai = 70; baru dikalikan
print(nilai)  # output = 70

print("Contoh 2")
nilai = (3 + 2) ** 2 + (4 + 4) / 2 % 4
print(nilai)  # output = 25

# --- PYTHON CONTROL FLOW ---
# --- Python Conditioning for Decision ---
# Statement if
x = 4
if x % 2 == 0: # jika sisa bagi x dengan 2 sama dengan 0
    print("x habis dibagi dua") # statemen aksi lebih menjorok ke dalam
# Statement if ... elif ... else
x = 7
if x % 2 == 0: # jika sisa bagi x dengan 2 sama dengan 0
    print("x habis dibagi dua")
elif x % 3 == 0: # jika sisa bagi x dengan 3 sama dengan 0
    print("x habis dibagi tiga")
elif x % 5 == 0: # jika sisa bagi x dengan 5 sama dengan 0
    print("x habis dibagi lima")
else:
    print("x tidak habis dibagi dua, tiga ataupun lima")

jam = 13
if jam >= 5 and jam < 12: # selama jam di antara 5 s.d. 12
    print("Selamat pagi!")
elif jam >= 12 and jam < 17: # selama jam di antara 12 s.d. 17
    print("Selamat siang!")
elif jam >= 17 and jam < 19: # selama jam di antara 17 s.d. 19
    print("Selamat sore!")
else: # selain kondisi di atas
    print("Selamat malam!")

# --- Tugas Praktik (Kalkulator Tagihan Mr. Yoyo) ---
tagihan_ke = 'Mr. Yoyo'
warehousing = { 'harga_harian': 1000000, 'total_hari':15 } 
cleansing = { 'harga_harian': 1500000, 'total_hari':10 } 
integration = { 'harga_harian':2000000, 'total_hari':15 } 
transform = { 'harga_harian':2500000, 'total_hari':10 }
sub_warehousing = warehousing["harga_harian"] * warehousing["total_hari"] 
sub_cleansing = cleansing["harga_harian"] * cleansing["total_hari"]
sub_integration = integration["harga_harian"] * integration["total_hari"]
sub_transform = transform["harga_harian"] * transform["total_hari"]
total_harga = sub_warehousing + sub_cleansing + sub_integration + sub_transform
print("Tagihan kepada:") 
print(tagihan_ke)
print("Selamat pagi, anda harus membayar tagihan sebesar:") 
print(total_harga)

# --- Tugas Praktik (dengan if untuk waktu) ---
jam = 17
tagihan_ke = 'Mr. Yoyo'
warehousing = { 'harga_harian': 1000000, 'total_hari':15 } 
cleansing = { 'harga_harian': 1500000, 'total_hari':10 } 
integration = { 'harga_harian':2000000, 'total_hari':15 } 
transform = { 'harga_harian':2500000, 'total_hari':10 }
sub_warehousing = warehousing['harga_harian']*warehousing['total_hari'] 
sub_cleansing = cleansing['harga_harian']*cleansing['total_hari'] 
sub_integration = integration['harga_harian']*integration['total_hari'] 
sub_transform = transform['harga_harian']*transform['total_hari']
total_harga = sub_warehousing+sub_cleansing+sub_integration+sub_transform
print("Tagihan kepada:")
print(tagihan_ke)
if jam > 19:
    print("Selamat malam, anda harus membayar tagihan sebesar:")
elif jam > 17:
    print("Selamat sore, anda harus membayar tagihan sebesar:") 
elif jam > 12:
    print("Selamat siang, anda harus membayar tagihan sebesar:")
else:
    print("Selamat pagi, anda harus membayar tagihan sebesar:") 
print(total_harga)

# --- Python Primitive Loop Control (While & For) ---
# Python while loops – Part 1
# Tagihan
tagihan = [50000, 75000, 125000, 300000, 200000]
# Tanpa menggunakan while loop
total_tagihan = tagihan[0] + tagihan [1] + tagihan[2] + tagihan[3] + tagihan[4]
print(total_tagihan)

# Dengan menggunakan while loop
i = 0 # sebuah variabel untuk mengakses setiap elemen tagihan satu per satu
jumlah_tagihan = len(tagihan) # panjang (jumlah elemen dalam) list tagihan
total_tagihan = 0 # mula-mula, set total_tagihan ke 0
while i < jumlah_tagihan: # selama nilai i kurang dari jumlah_tagihan
    total_tagihan += tagihan[i] # tambahkan tagihan[i] ke total_tagihan
    i += 1 # tambahkan nilai i dengan 1 untuk memproses tagihan selanjutnya.
print(total_tagihan)

# Python while loops – Part 2
# break (keluar dari struktur pengulangan)
# continue untuk melanjutkan proses pengulangan berikutnya. 
tagihan = [50000, 75000, -150000, 125000, 300000, -50000, 200000]
i = 0
jumlah_tagihan = len(tagihan)
total_tagihan = 0
while i < jumlah_tagihan:
    # jika terdapat tagihan ke-i yang bernilai minus (di bawah nol),
    # pengulangan akan dihentikan
    if tagihan[i] < 0:
        total_tagihan = -1
        print("terdapat angka minus dalam tagihan, perhitungan dihentikan!")
        break
    total_tagihan += tagihan[i]
    i += 1
print(total_tagihan)

# Python while loops – Part 3
tagihan = [50000, 75000, -150000, 125000, 300000, -50000, 200000]
i = 0
jumlah_tagihan = len(tagihan)
total_tagihan = 0
while i < jumlah_tagihan:
    # jika terdapat tagihan ke-i yang bernilai minus (di bawah nol),
    # abaikan tagihan ke-i dan lanjutkan ke tagihan berikutnya
    if tagihan[i] < 0:
        i += 1
        continue
    total_tagihan += tagihan[i]
    i += 1
print(total_tagihan)

# Python for loops – Part 1
list_tagihan = [50000, 75000, -150000, 125000, 300000, -50000, 200000]
total_tagihan = 0
for tagihan in list_tagihan: # untuk setiap tagihan dalam list_tagihan
    total_tagihan += tagihan # tambahkan tagihan ke total_tagihan
print(total_tagihan)

# Python for loops – Part 2
list_tagihan = [50000, 75000, -150000, 125000, 300000, -50000, 200000]

# For loops with break
print("For loops with break")
total_tagihan_break = 0
for tagihan in list_tagihan:
    if tagihan < 0:
        print("Terdapat angka minus dalam tagihan, perhitungan dihentikan!")
        break
    total_tagihan_break += tagihan
print("Total tagihan %d." % total_tagihan_break)
print()

# For loops with continue
print("For loops with continue")
total_tagihan_continue = 0
for tagihan in list_tagihan:
    if tagihan < 0:
        print("Terdapat angka minus dalam tagihan, tagihan %d dilewati!" % tagihan)
        continue
    total_tagihan_continue += tagihan
print("Total tagihan %d." % total_tagihan_continue)

# Python for loops – Part 3
#  nested loops, yaitu pengulangan bersarang
list_daerah = ['Malang', 'Palembang', 'Medan']
list_buah = ['Apel', 'Duku', 'Jeruk']
for nama_daerah in list_daerah:
    for nama_buah in list_buah:
        print(nama_buah+" "+nama_daerah)
        # print(f"{nama_buah} dari {nama_daerah}")

# Tugas Praktek (list_cash_flow)
list_cash_flow = [
2500000, 5000000, -1000000, -2500000, 5000000, 10000000,
-5000000, 7500000, 10000000, -1500000, 25000000, -2500000
]
total_pengeluaran, total_pemasukan = 0, 0
for dana in list_cash_flow:
    if dana > 0:
        total_pemasukan += dana
    else:
        total_pengeluaran += dana
total_pengeluaran *= -1
print(total_pengeluaran) 
print(total_pemasukan)

# --- Ekspedisi Pamanku ---
# Data
uang_jalan = 1500000
jumlah_hari = 31
list_plat_nomor = [8993, 2198, 2501, 2735, 3772, 4837, 9152]

# Pengecekan kendaraan dengan nomor pelat ganjil atau genap 
# Deklarasikan kendaraan_genap dan kendaraan_ganjil = 0
kendaraan_genap = 0 
kendaraan_ganjil = 0
for plat_nomor in list_plat_nomor:
    if plat_nomor % 2 == 0: 
        kendaraan_genap += 1 # # Tambah penghitung genap
    else:
        kendaraan_ganjil += 1 # Tambah penghitung ganjil (ingat, kendaraan_ganjil dimulai dari 0, jadi harus dikurangi 1 untuk menambah jumlah kendaraan ganjil)

# Total pengeluaran untuk kendaraan dengan nomor pelat ganjil 
# dan genap dalam 1 bulan
i = 1
total_pengeluaran = 0 # Mulai dari nol rupiah
while i <= jumlah_hari: # hari ke-1 sampai hari ke-31. Jadi batasnya adalah jumlah_hari
    if i % 2 == 0: # Jika hari genap, dikali jumlah kendaraan genap
        total_pengeluaran += (kendaraan_genap * uang_jalan)
    else: # Jika hari ganjil, dikali jumlah kendaraan ganjil
        total_pengeluaran += (kendaraan_ganjil * uang_jalan) 
    i += 1 # Kalau nggak ada ini, Python bakal looping selamanya di hari ke-1

# Cetak total pengeluaran
print(total_pengeluaran)

# -- Note: For my certificates of completion, check README.md
# -- Thank you.
