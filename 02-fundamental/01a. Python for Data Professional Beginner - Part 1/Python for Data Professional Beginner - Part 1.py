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

