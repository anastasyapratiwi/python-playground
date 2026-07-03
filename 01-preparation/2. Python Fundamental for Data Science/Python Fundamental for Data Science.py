# Profil Pemateri: XERATIC

print("Hello World")
print(5 + 1)

# Tugas Praktik
print(10 * 2 + 5)
print("Academy DQLab")

# --- Comment pada Python ---

print("Ini adalah sebuah baris kode")
# ini adalah contoh comment dan tidak akan tercetak

# Tugas Praktik
print(10 * 2 + 5)  # fungsi matematika
print("Academy DQLab")  # fungsi mencetak kalimat

# --- Printing Data Type ---
# tipe data Boolean
print(True)

# tipe data String
print("Ayo belajar Python")
print("Belajar Python Sangat Mudah di DQLab")

# tipe data Integer
print(20)

# tipe data Float
print(3.14)

# tipe data List
print([1, 2, 3, 4, 5])
print(["satu", "dua", "tiga"])

# tipe data Tuple
print((1, 2, 3, 4, 5))
print(("satu", "dua", "tiga"))

# tipe data Dictionary
print({"nama": "Budi", "umur": 20})

# tipe data Dictionary dimasukkan ke dalam variabel biodata
biodata = {"nama": "Andi", "umur": 21}  # proses inisialisasi variabel biodata
print(biodata)  # proses pencetakan variabel biodata yang berisi tipe data Dictionary
type(biodata)  # fungsi untuk mengecek jenis tipe data. akan tampil <class 'dict'>

# Tugas Praktik
var_string = "Belajar Python DQLAB"
var_int = 10
var_float = 3.14
var_list = [1, 2, 3, 4]
var_tuple = ("satu", "dua", "tiga")
var_dict = {"nama": "Ali", "umur": 20}

print(var_string)
print(var_int)
print(var_float)
print(var_list)
print(var_tuple)
print(var_dict)

print(type(var_string))
print(type(var_int))
print(type(var_float))
print(type(var_list))
print(type(var_tuple))
print(type(var_dict))

# --- IF Statement ---
i = 10  # inisialisasi variable i yang memiliki nilai 10

if i == 10:  # pengecekan nilai i apakah sama dengan 10
    print("ini adalah angka 10")  # jika TRUE maka akan mencetak kalimat ini

# Tugas Praktik
i = 7  # inisialisasi variable i yang memiliki nilai 10

if i == 10:  # pengecekan nilai i apakah sama dengan 10
    print("ini adalah angka 10")  # jika TRUE maka akan mencetak kalimat ini

# --- IF... ELSE... ---

i = 10  # inisialisasi variable i yang memiliki nilai 10

if i == 10:  # pengecekan nilai i apakah sama dengan 10
    print("ini adalah angka 10")  # jika TRUE maka akan mencetak kalimat ini
else:
    print("bukan angka 10")  # jika FALSE mencetak kalimat ini

i = 5  # inisialisasi variable i yang memiliki nilai 10

if i == 10:  # pengecekan nilai i apakah sama dengan 10
    print("ini adalah angka 10")  # jika TRUE maka akan mencetak kalimat ini
else:
    print("bukan angka 10")  # jika FALSE mencetak kalimat ini

# --- IF ... ELIF ... ELSE ... ---

i = 5
if i == 5:
    print("ini adalah angka 5")
elif i > 5:
    print("lebih besar dari 5")
else:
    print("lebih kecil dari 5")

# Tugas Praktik
i = 7
if i == 5:
    print("ini adalah angka 5")
elif i > 5:
    print("lebih besar dari 5")
else:
    print("lebih kecil dari 5")

i = 3
if i == 5:
    print("ini adalah angka 5")
elif i > 5:
    print("lebih besar dari 5")
else:
    print("lebih kecil dari 5")

# --- NESTED IF ---
"""
if(i<7 and i<3):
Pernyataan ini berarti bahwa i harus bernilai kurang dari 7 dan juga harus kurang dari 3 agar bisa memenuhi pengecekan tersebut.
"""

# Tugas Praktik (Cara pengecekan NESTED IF)
i = 2
if i < 7:
    print("nilai i kurang dari 7")
    if i < 3:
        print("nilai i kurang dari 7 dan kurang dari 3")
    else:
        print("nilai i kurang dari 7 tapi lebih dari 3")

# --- PRAKTIK OPERASI MATEMATIKA ---
a = 10
b = 5
selisih = a - b
jumlah = a + b
kali = a * b
bagi = a / b
print("Hasil penjumlahan a dan b adalah", jumlah)
print("Selisih a dan b adalah :", selisih)
print("Hasil perkalian a dan b adalah :", kali)
print("Hasil pembagian a dan b adalah :", bagi)

# --- OPERASI MODULUS ---
# Sisa dari hasil pembagian

c = 10
d = 5

modulus = c % d
print("Hasil modulus", modulus)

# Tugas Praktik
c = 10
d = 3

modulus = c % d
print("Hasil modulus", modulus)

# --- TUGAS MID PRAKTIK ---
