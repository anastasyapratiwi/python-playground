# Profil Pemateri: 
'''
Julio Christian Young
Dosen dan Peneliti bidang Artificial Intelligence 
Universitas Multimedia Nusantara
'''

# --- Chapter 1: Collections manipulation ---
# --- Mengakses List dan Tuple – Part 1 ---
bulan_pembelian = ('Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember')
print(bulan_pembelian[0])
print(bulan_pembelian[5])
print(bulan_pembelian[-1])
print(bulan_pembelian[-2])

# --- Mengakses List dan Tuple – Part 2 ---
bulan_pembelian = ('Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember')

# output pertengahan_tahun Mei, Juni, Juli, Agustus (index 4 - 7)
pertengahan_tahun = bulan_pembelian[4:8]
print(pertengahan_tahun)

# output awal_tahun Januari, Februari, Maret, April, Mei (index 0-4)
awal_tahun = bulan_pembelian[:5]
print(awal_tahun)

# output akhir_tahun September, Oktober, November, Desember (index 8-akhir)
akhir_tahun = bulan_pembelian[8:]
print(akhir_tahun)

# potong list/tuple (indeks negatif), output September, Oktober, November
print(bulan_pembelian[-4:-1])

# Penggabungan Dua atau Lebih List atau Tuple
# menggunakan operator penambahan (+)

list_makanan = ['Gado-gado', 'Ayam Goreng', 'Rendang']
list_minuman = ['Es Teh', 'Es Jeruk', 'Es Campur']
list_menu = list_makanan + list_minuman
print(list_menu)

# --- List Manipulation – Part 1 ---
# Fitur .append()
print(">>> Fitur .append()")
list_makanan = ['Gado-gado', 'Ayam Goreng', 'Rendang']
list_makanan.append('Ketoprak')
print(list_makanan)

# Fitur .clear()
print(">>> Fitur .clear()")
list_makanan = ['Gado-gado', 'Ayam Goreng', 'Rendang']
list_makanan.clear()
print(list_makanan)

# Fitur .copy()
print(">>> Fitur .copy()")
list_makanan1 = ['Gado-gado', 'Ayam Goreng', 'Rendang']
list_makanan2 = list_makanan1.copy()
list_makanan3 = list_makanan1
list_makanan2.append('Opor')
list_makanan3.append('Ketoprak')
print(list_makanan1)
print(list_makanan2)

# Fitur .count()
print(">>> Fitur .count()")
list_score = ['Budi', 'Sud', 'Budi', 'Budi', 'Budi', 'Sud', 'Sud']
score_budi = list_score.count('Budi')
score_sud = list_score.count('Sud')
print(score_budi) # akan menampilkan output 4
print(score_sud) # akan menampilkan output 3

# Fitur .extend()
print(">>> Fitur .extend()")
list_menu = ['Gado-gado', 'Ayam Goreng', 'Rendang']
list_minuman = ['Es Teh', 'Es Jeruk', 'Es Campur']
list_menu.extend(list_minuman)
print(list_menu)

# --- List Manipulation – Part 2 ---
# Fitur .index()
print(">>> Fitur .index()")
list_score = ['Budi','Sud','Budi','Budi','Budi','Sud','Sud']
score_pertama_sud = list_score.index('Sud') + 1
print(score_pertama_sud) # akan menampilkan output 2

# Fitur .insert()
print(">>> Fitur .insert()")
list_score = ['Budi','Sud','Budi','Budi','Sud']
list_score.insert(3, 'Sud')
print(list_score)

# Fitur .pop()
print(">>> Fitur .pop()")
list_menu = ['Gado-gado', 'Ayam Goreng', 'Rendang']
list_menu.pop(1)
print(list_menu)

# Fitur .remove()
print(">>> Fitur .remove()")
list_menu = ['Gado-gado', 'Ayam Goreng', 'Rendang', 'Ketoprak']
list_menu.remove('Rendang')
print(list_menu)

# Fitur .reverse()
print(">>> Fitur .reverse()")
list_menu = ['Gado-gado', 'Ayam Goreng', 'Rendang', 'Ketoprak']
list_menu.reverse()
print(list_menu)

# Fitur .sort()
print(">>> Fitur .sort()")
list_menu = ['Gado-gado', 'Ayam Goreng', 'Rendang', 'Ketoprak']
list_menu.sort() # Default: Ascending
print(list_menu) 
list_menu.sort(reverse=True) # Descending
print(list_menu) 

# --- Tuple Manipulation ---
# Fitur .count()
print(">>> Fitur .count()")
tuple_score = ('Budi', 'Sud', 'Budi', 'Budi', 'Budi', 'Sud', 'Sud')
score_budi = tuple_score.count('Budi')
score_sud = tuple_score.count('Sud')
print(score_budi) # akan menampilkan output 4
print(score_sud) # akan menampilkan output 3

# Fitur .index()
print(">>> Fitur .index()")
tuple_score = ('Budi','Sud','Budi','Budi','Budi','Sud','Sud')
score_pertama_sud = tuple_score.index('Sud')+1
print(score_pertama_sud) # akan menampilkan output 2

# --- Set Manipulation – Part 1 ---
# Fitur .add()
print(">>> Fitur .add()")
set_buah = {'Jeruk','Apel','Anggur'}
set_buah.add('Melon')
print(set_buah)

# Fitur .clear()
print(">>> Fitur .clear()")
set_buah = {'Jeruk','Apel','Anggur'}
set_buah.clear()
print(set_buah) # output = set() atau empty set{}

# Fitur .copy()
print(">>> Fitur .copy()")
set_buah1 = {'Jeruk','Apel','Anggur'}
set_buah2 = set_buah1
set_buah3 = set_buah1.copy()
set_buah2.add('Melon')
set_buah3.add('Kiwi')
print(set_buah1)
print(set_buah2)

# Fitur .update()
print(">>> Fitur .update()")
parcel1 = {'Anggur','Apel','Jeruk'}
parcel2 = {'Apel','Kiwi','Melon'}
parcel1.update(parcel2)
print(parcel1)

# Fitur .pop()
print(">>> Fitur .pop()")
parcel = {'Anggur','Apel','Jeruk'}
buah = parcel.pop()
print(buah)
print(parcel)

# Fitur .remove()
print(">>> Fitur .remove()")
parcel = {'Anggur','Apel','Jeruk'}
parcel.remove('Apel')
print(parcel)

# --- Set Manipulation – Part 2 ---
# Fitur .union()
print(">>> Fitur .union()")
parcel1 = {'Anggur','Apel','Jeruk'}
parcel2 = {'Apel','Kiwi','Melon'}
parcel3 = parcel1.union(parcel2)
print(parcel1)
print(parcel3)

# Fitur .isdisjoint()
print(">>> Fitur .isdisjoint()")
parcel1 = {'Anggur','Apel','Jeruk'}
parcel2 = {'Kiwi','Melon','Pisang'}
parcel3 = {'Apel','Srikaya','Semangka'}
parcel1_parcel2_disjoint = parcel1.isdisjoint(parcel2)
print(parcel1_parcel2_disjoint)
parcel1_parcel3_disjoint = parcel1.isdisjoint(parcel3)
print(parcel1_parcel3_disjoint)

# Fitur .issubset()
print(">>> Fitur .issubset()")
parcel_A = {'Anggur', 'Apel'}
parcel_B = {'Durian','Semangka','Apel'}
parcel_C = {'Anggur', 'Kiwi', 'Apel', 'Jeruk', 'Melon'}
parcel_A_dalam_C = parcel_A.issubset(parcel_C)
parcel_B_dalam_C = parcel_B.issubset(parcel_C)
print(parcel_A_dalam_C)
print(parcel_B_dalam_C)

# Fitur .issuperset()
print(">>> Fitur .issuperset()")
parcel_C_mengandung_A = parcel_C.issuperset(parcel_A)
parcel_C_mengandung_B = parcel_C.issuperset(parcel_B)
print(parcel_C_mengandung_A)
print(parcel_C_mengandung_B)

# Fitur .intersection()
print(">>> Fitur .intersection()")
parcel_A = {'Anggur', 'Kiwi', 'Apel', 'Jeruk', 'Melon'}
parcel_B = {'Apel', 'Jeruk', 'Semangka', 'Durian', 'Tomat'}
parcel_C = parcel_A.intersection(parcel_B)
print(parcel_C)

# Fitur .difference()
print(">>> Fitur .difference()")
parcel_C = parcel_A.difference(parcel_B)
print(parcel_C)

# Fitur .symmetric_difference()
print(">>> Fitur .symmetric_difference()")
parcel_A = {'Anggur', 'Apel', 'Jeruk', 'Melon'}
parcel_B = {'Apel','Jeruk','Semangka','Leci'}
parcel_C = parcel_A.symmetric_difference(parcel_B)
print(parcel_C)

# --- Dictionary Manipulation ---
# Fitur .clear()
print(">>> Fitur .clear()")
info_karyawan = {'nama' : 'Aksara',
                 'nik' : '1211011',
                 'pekerjaan' : 'Data Analyst'}
info_karyawan.clear()
print(info_karyawan)

# Fitur .copy()
print(">>> Fitur .copy()")
info_karyawan1 = {'nama' : 'Aksara',
                  'nik' : '1211011',
                  'pekerjaan' : 'Data Analyst'}
info_karyawan2 = info_karyawan1.copy()
info_karyawan2['nama'] = 'Senja'
info_karyawan2['nik'] = '1211056'
print(info_karyawan1)
print(info_karyawan2)


# Fitur .keys()
print(">>> Fitur .keys()")
info_karyawan = {'nama' : 'Aksara',
                 'nik' : '1211011',
                 'pekerjaan' : 'Data Analyst'}
kunci_akses = list(info_karyawan.keys())
print(kunci_akses) # Outputnya bersifat iterable sehingga dapat digunakan dalam perulangan.

# Fitur .values()
print(">>> Fitur .values()")
value_dict = list(info_karyawan.values())
print(value_dict)

# Fitur .update()
print(">>> Fitur .update()")
info_karyawan.update({'skillset':['Python', 'R']})
print(info_karyawan)

# --- Useful Tips and Tricks ---
# --- Tugas 1 ---
# Tuple
print(">>> Tuple")
tuple_menu = ('Gado-gado','Ayam Goreng','Rendang','Ketoprak')
jumlah_menu = len(tuple_menu)
print(jumlah_menu)

# List
print(">>> List")
list_menu = ['Gado-gado','Ayam Goreng','Rendang','Ketoprak']
jumlah_menu = len(list_menu)
print(jumlah_menu)

# --- Tugas 2 ---
# Konversi tipe data
print(">>> Konversi tipe data")
list_buah = ['Apel', 'Apel', 'Jeruk', 'Markisa', 'Jeruk', 'Markisa', 'Apel']
set_buah = set(list_buah)
print(set_buah)
list_buah = list(set_buah)
list_buah.sort()
print(list_buah)

# Tugas Praktik
# menghitung rata-rata pengeluaran dan pemasukanku selama 9 bulan terakhir

# Data keuangan
keuangan = {
'pengeluaran': [2, 2.5, 2.25, 2.5, 3.2, 2.5, 3.5, 4, 3],
'pemasukan': [7.8, 7.5, 9, 7.6, 7.2, 7.5, 7, 10, 7.5]
}

# Perhitungan rata-rata pemasukan dan rata-rata pengeluaran
total_pengeluaran = 0
total_pemasukan = 0
for biaya in keuangan['pengeluaran']: 
    total_pengeluaran += biaya # Menambah total_pengeluaran dengan tiap biaya
for biaya in keuangan['pemasukan']: 
    total_pemasukan += biaya 
rata_rata_pengeluaran = total_pengeluaran / len(keuangan['pengeluaran']) 
rata_rata_pemasukan = total_pemasukan / len(keuangan['pemasukan'])
print(rata_rata_pengeluaran) 
print(rata_rata_pemasukan)

# --- Chapter 2: String Manipulation dengan Python ---
# --- Tinjauan Ulang String pada Python ---
nama_produk = 'Sepatu Niko'
kategori_produk = "Busana Pria"

# Tanda kutip satu (6 kali)
deskripsi_produk = '''Sepatu Niko merupakan sepatu kasual yang aerodinamis.
Sepatu ini tersedia dalam berbagai macam ukuran. Untuk
informasi lebih lanjut hubungi kami di no. 0832-xxxx-xxxx.
'''
print(deskripsi_produk)

# Tanda kutip dua (6 kali)
komentar_terbaik_produk = """Sepatu Niko nyaman dipakai dan
bahannya tidak mudah kotor.
"""
print(komentar_terbaik_produk)

# Apa itu String Manipulation?
nama_produk = "Sepatu Niko"
nama_produk = nama_produk[:2] + "P" + nama_produk[3:9] + "K" + nama_produk[-1]
print(nama_produk) # Output: SePatu NiKo
print(nama_produk[:7]) # Output: SePatu
print(nama_produk[7:]) # Output: NiKo
print(len(nama_produk)) # Output: 11

# Operator “+” untuk Tipe Data String
nama_depan = 'John'
nama_belakang = 'Doee'
nama_lengkap = nama_depan + ' ' + nama_belakang
print(nama_lengkap) # Output: John Doee

umur = '27 tahun'
alamat = 'Jl. Anggrek No. 100'
nama_umur_alamat = 'Hi, saya ' + nama_lengkap + ' umur ' + umur + ', tinggal di ' + alamat + '.'
print(nama_umur_alamat) # Output: Hi, saya John Doee umur 27 tahun, tinggal di Jl. Anggrek No. 100.

# --- Menghilangkan Spasi di Awal dan/atau di Akhir ---
# Fitur .strip()
print(">>> Fitur .strip()")
kata_sambutan = ' halo, selamat siang! '
kata_sambutan = kata_sambutan.strip()
print(kata_sambutan) # Output: 'halo, selamat siang!'

# Fitur .lstrip()
print(">>> Fitur .lstrip()")
kata_sambutan = ' halo, selamat siang! '
kata_sambutan = kata_sambutan.lstrip()
print(kata_sambutan) # Output: 'halo, selamat siang! '

# Fitur .rstrip()
print(">>> Fitur .rstrip()")
kata_sambutan = ' halo, selamat siang! '
kata_sambutan = kata_sambutan.rstrip()
print(kata_sambutan) # Output: ' halo, selamat siang!'

# --- Mengubah Caps pada String ---
# Fitur .capitalize()
print(">>> Fitur .capitalize()")
judul_buku = 'belajar bahasa Python'
print(judul_buku.capitalize()) # Output: Belajar bahasa python

# Fitur .lower()
print(">>> Fitur .lower()")
judul_buku = 'Belajar Bahasa PYTHON.'
print(judul_buku.lower()) # Output: belajar bahasa python.

# Fitur .upper()
print(">>> Fitur .upper()")
judul_buku = 'Belajar Bahasa PYTHON.'
print(judul_buku.upper()) # Output: BELAJAR BAHASA PYTHON.

# --- Pemecahan, Penggabungan, dan Penggantian String ---
# Fitur .split()
print(">>> Fitur .split()")
frasa = "ani dan budi dan wati dan johan"
karakter = frasa.split("dan")
print(karakter) # Output: ['ani', 'budi', 'wati', 'johan']

kata = frasa.split(" ")
print(kata) # Output: ['ani', 'dan', 'budi', 'dan', 'wati', 'dan', 'johan'] 

# Fitur .join()
print(">>> Fitur .join()")
pemisah = " dan "
karakter = ["Ricky", "Peter", "Jordan"]
frasa = pemisah.join(karakter)
print(frasa) # Output: 'Ricky dan Peter dan Jordan'

frasa = " ".join(karakter)
print(frasa) # Output: 'Ricky Peter Jordan'

# Fitur .replace()
print(">>> Fitur .replace()")
frasa = "apel malang apel yang paling segar, apel sehat, apel nikmat"
frasa = frasa.replace("apel", "jeruk")
print(frasa) # Output: 'jeruk malang jeruk yang paling segar, jeruk sehat, jeruk nikmat'

# --- Menentukan Posisi dan Jumlah Sub-string pada String ---
teks = "Apel malang adalah apel termanis dibanding apel-apel lainnya"

# Fitur .find()
print(">>> Fitur .find()")
print(teks.find("Apel")) # Output: 0 (dikarenakan kalimat diawali dengan kata Apel)
print(teks.find("malang")) # Output: 5 (kata malang muncul dimulai dari indeks ke-5 ketika setiap karakter dalam string direpresentasikan sebagai array.)

# Fitur .count()
print(">>> Fitur .count()")
kemunculan_kata_apel = teks.count("apel")
print(kemunculan_kata_apel) # Output: 3 (Apel diawali huruf kapital dan kata yang dicari diawali huruf kecil)

# --- Menentukan String Apakah Diawali/Diakhiri oleh Sub-string ---
# Fitur .startswith()
print(">>> Fitur .startswith()")
teks = "Apel malang adalah apel termanis dibanding apel-apel lainnya"
print(teks.startswith("Apel")) #True
print(teks.startswith("apel")) #False

# Fitur .endswith()
print(">>> Fitur .endswith()")
print(teks.endswith("lainnya")) #True
print(teks.endswith("apel")) #False

# --- Tugas Praktik (PENGOLAHAN DATA TEKS) ---
judul_artikel = [
"Buah Salak Baik untuk Mata", "Buah Salak Kaya Potasium", 
"Buah Jeruk Kaya Vitamin C", "Buah Salak Kaya Manfaat", 
"Salak Baik untuk Jantung", "Jeruk dapat Memperkuat Tulang", 
"Jeruk Mencegah Penyakit Asma", "Jeruk Memperkuat Gigi", 
"Jeruk Mencegah Kolesterol Jahat", "Salak Mencegah Diabetes", 
"Salak Memperkuat Dinding Usus", "Salak Baik untuk Darah",
"Jeruk Kaya Manfaat untuk Jantung", "Salak si Kecil yang Baik", 
"Jeruk dan Salak Buah Kaya Manfaat", "Buah Jeruk Enak",
"Tips Panen Jeruk Ribuan Kilo", "Tips Bertanam Salak", 
"Salak Manis untuk Berbuka", "Jeruk Baik untuk Wajah"
]
jumlah_artikel_jeruk = 0
jumlah_artikel_salak = 0
for judul in judul_artikel:
    if judul.count("Jeruk") > 0: 
        jumlah_artikel_jeruk += 1
    if judul.count("Salak") > 0:
        jumlah_artikel_salak += 1
print(jumlah_artikel_jeruk) 
print(jumlah_artikel_salak)

# --- Tugas Praktik (Kata Positif) ---
judul_artikel = [
"Buah Salak Baik untuk Mata", "Buah Salak Kaya Potasium", 
"Buah Jeruk Kaya Vitamin C", "Buah Salak Kaya Manfaat", 
"Salak Baik untuk Jantung", "Jeruk dapat Memperkuat Tulang", 
"Jeruk Mencegah Penyakit Asma", "Jeruk Memperkuat Gigi", 
"Jeruk Mencegah Kolesterol Jahat", "Salak Mencegah Diabetes", 
"Salak Memperkuat Dinding Usus", "Salak Baik untuk Darah",
"Jeruk Kaya Manfaat untuk Jantung", "Salak si Kecil yang Baik", 
"Jeruk dan Salak Buah Kaya Manfaat", "Buah Jeruk Enak",
"Tips Panen Jeruk Ribuan Kilo", "Tips Bertanam Salak", 
"Salak Manis untuk Berbuka", "Jeruk Baik untuk Wajah"
]
kata_positif = ["Kaya", "Baik", "Mencegah", "Memperkuat"]
kata_positif_jeruk = 0
kata_positif_salak = 0
for judul in judul_artikel: 
    for kata in kata_positif:
        if judul.count("Jeruk") > 0 and judul.count(kata) > 0: 
            kata_positif_jeruk += 1
        if judul.count("Salak") > 0 and judul.count(kata) > 0:
            kata_positif_salak += 1
print(kata_positif_jeruk) 
print(kata_positif_salak)

# --- Chapter 3: Functions ---
# --- Fungsi Pertama (contoh_fungsi) ---
# Definisikan fungsi
def contoh_fungsi():
    print("Halo Dunia")
    print("Aku sedang belajar bahasa Python")
# Panggil fungsi yang telah didefinisikan
contoh_fungsi()

# --- Fungsi Kedua (fungsi_dengan_argumen membutuhkan dua argumen (nama_depan, nama_belakang)) ---
# Definsikan fungsi 
def fungsi_dengan_argumen(nama_depan, nama_belakang):
    print(nama_depan+" "+nama_belakang)
# Panggil fungsi dengan memasukkan argumen
# nama_depan yaitu "John" dan nama_belakang "Doe"
fungsi_dengan_argumen("John", "Doe")

# --- Fungsi Ketiga ---
# Definsikan fungsi dengan nilai default argument kedua adalah "".
def fungsi_dengan_argumen(nama_depan, nama_belakang = ""):
	print(nama_depan+" "+nama_belakang)
# Panggil fungsi dengan memasukkan argumen nama_depan "John"
fungsi_dengan_argumen("John")
# Panggil fungsi dengan memasukkan argumen
# nama_depan yaitu "John" dan nama_belakang "Doe"
fungsi_dengan_argumen("John", "Doe")

# --- Tugas Praktik ---
# Dua buah data yang tersimpan dalam tipe list
data1 = [70, 70, 70, 100, 100, 100, 120, 120, 150, 150]
data2 = [50, 60, 60, 50, 70, 70, 100, 80, 100, 90]

# Definisikan fungsi hitung_rata_rata
def hitung_rata_rata(data):
    jumlah = 0
    for item in data:
        jumlah += item # Setiap angka dalam data ditambahkan ke 'jumlah'
    rata_rata = jumlah/len(data) # Total dibagi banyaknya data
    return rata_rata

# Hitung nilai rata-rata dari kedua data yang dimiliki
print('Rata-rata data1:')
print(hitung_rata_rata(data1))
print('Rata-rata data2:')
print(hitung_rata_rata(data2))

# Dua buah data yang tersimpan dalam tipe list
data1 = [70, 70, 70, 100, 100, 100, 120, 120, 150, 150]
data2 = [50, 60, 60, 50, 70, 70, 100, 80, 100, 90]

# Fungsi rata-rata data
def hitung_rata_rata(data):
    jumlah = 0
    for item in data:
        jumlah += item
    rata_rata = jumlah/len(data)
    return rata_rata
  
# Definisikan fungsi hitung_standar_deviasi
def hitung_standar_deviasi(data):
    rata_rata_data = hitung_rata_rata(data)
    varians = 0
    for item in data:
        varians += (item - rata_rata_data) ** 2 # Selisihnya itu dikuadratkan (biar kalau hasilnya minus tetep jadi positif).
    varians /= len(data) # mencari "Rata-rata dari kuadrat selisih". Baris ini hukumnya WAJIB karena: Kalau nggak dibagi, cuma punya "Total Kesalahan". Setelah dibagi, Mbak punya "Rata-rata Kesalahan" (Varians).
    standar_deviasi = varians ** (1/2) # Karena tadi sempat dikuadratkan, sekarang "dinetralin" lagi pakai akar kuadrat ($1/2$ itu sama dengan akar).
    return standar_deviasi

# Hitung nilai standar deviasi dari kedua data yang dimiliki
print('Standar deviasi data1:')
print(hitung_standar_deviasi(data1))
print('Standar deviasi data2:')
print(hitung_standar_deviasi(data2))

# --- Tugas Praktik (Tabel Properti) ---
# Data properti
tabel_properti = {
'luas_tanah': [70, 70, 70, 100, 100, 100, 120, 120, 150, 150],
'luas_bangunan': [50, 60, 60, 50, 70, 70, 100, 80, 100, 90],
'jarak': [15, 30, 55, 30, 25, 50, 20, 50, 50, 15],
'harga': [500, 400, 300, 700, 1000, 650, 2000, 1200, 1800, 3000]
}

# Fungsi rata-rata data
def hitung_rata_rata(data):
    jumlah = 0
    for item in data:
        jumlah += item
    rata_rata = jumlah/len(data)
    return rata_rata

# Fungsi hitung_standar_deviasi
def hitung_standar_deviasi(data):
    rata_rata_data = hitung_rata_rata(data)
    varians = 0
    for item in data:
        varians += (item - rata_rata_data) ** 2
        varians /= len(data)
    standar_deviasi = varians ** (1/2)
    return standar_deviasi

# Definisikan fungsi untuk menghitung rata-rata dan standar deviasi
# setiap kolom pada tabel_properti yang diberikan oleh key dict.
def deskripsi_properti(tabel):
    for key in tabel.keys(): # Fungsi .keys() itu gunanya cuma buat ngambil semua daftar Label yang tertempel di depan laci-laci tadi, tanpa ngelihat isinya dulu.
        print('Rata-rata ' + key + ':')
        print(hitung_rata_rata(tabel[key])) # Si key itu cuma nama variabel sementara pas lagi muter (looping).
        print('Standar deviasi ' + key + ':')
        print(hitung_rata_rata(tabel[key]))
        print('')

# Panggil fungsi deskripsi_properti untuk menghitung rata-rata 
# dan standar deviasi setiap kolom pada tabel_properti
deskripsi_properti(tabel_properti)

# --- Chapter 4: Manipulasi Berkas Teks dan Library Matematika pada Python ---
import requests
url = "https://storage.googleapis.com/dqlab-dataset/hello.txt"
response = requests.get(url)

# --- Membaca Berkas Teks – Part 1 ---
# A1. Membaca file hello.txt dengan fungsi read() dan menutup file
# Membaca file hello.txt dengan fungsi read()
print(">>> Membaca file hello.txt dengan fungsi read()")
file = open("hello.txt", "r")
content = file.read()

file.close()
print(content)

# A2. Membaca file hello.txt dengan fungsi readline()
print(">>> Membaca file hello.txt dengan fungsi readline()")
file = open("hello.txt", "r")

first_line = file.readline()
second_line = file.readline() 

file.close()
print(first_line)
print(second_line)

# --- Tugas Praktik ---
import requests
url = "https://storage.googleapis.com/dqlab-dataset/hello.txt"
response = requests.get(url)

# Cetak kode status dari response
print(response) # kode status HTTP 200 = OK dari url tempat file disimpan

# Cetak isi file hello.txt menggunakan method response.iter_lines()
print("\n>> Cetak isi file hello.txt menggunakan method response.iter_lines():")
for baris in response.iter_lines():
	print(baris)

# --- Membaca Berkas Teks – Part 2 ---
# A1. Membaca file hello.txt dengan fungsi readlines()
print(">>> Membaca file hello.txt dengan fungsi readlines()")
file = open("hello.txt", "r")

all_lines = file.readlines()
file.close()
print(all_lines)

# A2. Membaca file hello.txt dengan menerapkan looping (for loops)
print(">>> Membaca file hello.txt dengan menerapkan looping")
file = open("hello.txt", "r")

for line in file:
	print(line)
file.close()

# --- Tugas Praktik ---
import requests
url = "https://storage.googleapis.com/dqlab-dataset/hello.txt"
response = requests.get(url)

# Cetak kode status dari response
print(response)

# Cetak isi file hello.txt menggunakan atribut response.text
print("\n>> Cetak isi file hello.txt menggunakan atribut response.text:")
print(response.text) 

