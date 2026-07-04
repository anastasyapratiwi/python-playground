# Profil Pemateri: Monika Evelyn Johan, Dosen Universitas Multimedia Nusantara

# --- CHAPTER 1: Pengantar Storytelling dengan Visualisasi menggunakan Python ---
# --- Membaca Dataset ---
# Mengimport library Pandas 
import pandas as pd

# Membaca dan menampilkan dataset
dataset_shopping = pd.read_csv('https://dqlabcdn.xeratic.com/dqlab-dataset/shopping_data.csv', delimiter=',')
print('Menampilkan dataset untuk 5 baris teratas:')
print('------------------------------------------')
print(dataset_shopping.head())

# Melihat tipe data
print('\nMelihat tipe data:')
print('------------------')
dataset_shopping.info()

# Menentukan statistik deskriptif dataset
print('\nStatistik deskriptif:')
print('---------------------')
print(dataset_shopping.describe())

# --- Menentukan Jumlah Pelanggan Berdasarkan Genre ---
# Kode sebelumnya
import pandas as pd

dataset_shopping = pd.read_csv('https://dqlabcdn.xeratic.com/dqlab-dataset/shopping_data.csv', delimiter=',')

## Menghitung jumlah pelanggan berdasarkan Genre
# Mencari pembeli dengan jenis kelamin pria
Male_dataset = dataset_shopping[(dataset_shopping['Genre']=='Male')].reset_index()
jumlah_pria = Male_dataset['Genre'].count()
print('Jumlah Pelanggan Pria =', jumlah_pria)

# Mencari data yang sama pada pembeli dengan jenis kelamin wanita
Female_dataset = dataset_shopping[(dataset_shopping['Genre']=='Female')].reset_index()
jumlah_wanita = Female_dataset['Genre'].count()
print('Jumlah Pelanggan Wanita =', jumlah_wanita)

# Menghitung jumlah pelanggan berdasarkan Genre
jumlah_pelanggan = dataset_shopping.groupby('Genre')['Customer_ID'].count().rename('Jumlah_pelanggan').reset_index()
print('Jumlah pelanggan:\n', jumlah_pelanggan)

# --- Visualisasi Persentase Pelanggan Berdasarkan Genre ---
# Kode sebelumnya
import pandas as pd

dataset_shopping = pd.read_csv('https://dqlabcdn.xeratic.com/dqlab-dataset/shopping_data.csv', delimiter=',')

# Jumlah pelanggan berdasarkan Genre
jumlah_pelanggan = dataset_shopping.groupby('Genre')['CustomerID'].count().rename('Jumlah pelanggan').reset_index()

# Mengimport library Matplotlib
import matplotlib.pyplot as plt

# Menampilkan pie chart pembagian data Male dan Female
plt.pie(jumlah_pelanggan['Jumlah pelanggan'], labels=jumlah_pelanggan['Genre'], autopct='%1.1f%%', startangle=90)
plt.tight_layout()
plt.show()

# --- Menentukan Segmentasi Genre dan Usia ---
# Kode sebelumnya
import pandas as pd

dataset_shopping = pd.read_csv('https://dqlabcdn.xeratic.com/dqlab-dataset/shopping_data.csv', delimiter=',')

## Menghitung rentang usia pelanggan masing - masing Genre
# Membagi kelompok usia
def label_usia(row):
    if row['Age'] < 21:
        return 'remaja'
    if row['Age'] < 40:
        return 'dewasa muda'
    if row['Age'] < 55:
        return 'dewasa'
    return 'pensiun'

# Klasifikasikan kolom 'Age' berdasarkan kelompok usia ke dalam kolom 'Range Usia'
dataset_shopping['Range Usia'] = dataset_shopping.apply(lambda row: label_usia(row), axis=1)

# Kelompokkan dataset berdasarkan 'Genre' dan 'Range Usia' dan dihitung agregasi jumlahnya.
shopping_group = dataset_shopping.groupby(['Genre', 'Range Usia'])['CustomerID'].count().rename('Jumlah Pelanggan')

print(shopping_group)

# --- Visualisasi Segmentasi Genre dan Usia - Pie Chart ---
# Kode sebelumnya
import pandas as pd

dataset_shopping = pd.read_csv('https://dqlabcdn.xeratic.com/dqlab-dataset/shopping_data.csv', delimiter=',')

def label_usia(row):
    if row['Age'] < 21:
        return 'remaja'
    if row['Age'] < 40:
        return 'dewasa muda'
    if row['Age'] < 55:
        return 'dewasa'
    return 'pensiun'

dataset_shopping['Range Usia'] = dataset_shopping.apply (lambda row: label_usia(row), axis=1)

# Kelompokkan dataset berdasarkan 'Genre' dan 'Range Usia' dan dihitung agregasi jumlahnya dan terapkan reset_index()
shopping_group = dataset_shopping.groupby(['Genre', 'Range Usia'])['CustomerID'].count().rename('Jumlah Pelanggan').reset_index()

# Membagi shopping_group ke masing-masing 'Genre'
Male_group = shopping_group[shopping_group['Genre']=='Male']
Female_group = shopping_group[shopping_group['Genre']=='Female']

# Mengimport library Matplotlib
import matplotlib.pyplot as plt

# Buatkan canvas untuk menempatkan pie chart
fig, axs = plt.subplots(1, 2, figsize=(10,5))
   
# Male
axs[0].pie(Male_group['Jumlah Pelanggan'], labels=Male_group['Range Usia'], autopct='%1.1f%%', startangle=90, explode= (0, 0.1, 0, 0))
axs[0].set_title('Persentase Kelompok Usia\nPelanggan Pria')

# Female
axs[1].pie(Female_group['Jumlah Pelanggan'], labels=Female_group['Range Usia'], autopct='%1.1f%%', startangle=90, explode= (0, 0.1, 0, 0))
axs[1].set_title('Persentase Kelompok Usia\nPelanggan Wanita')

plt.tight_layout()
plt.show()

# --- Visualisasi Segmentasi Genre dan Usia - Grouped Bar ---
# Kode sebelumnya
import pandas as pd

dataset_shopping = pd.read_csv('https://dqlabcdn.xeratic.com/dqlab-dataset/shopping_data.csv', delimiter=',')

def label_usia(row):
    if row['Age'] < 21:
        return 'remaja'
    if row['Age'] < 40:
        return 'dewasa muda'
    if row['Age'] < 55:
        return 'dewasa'
    return 'pensiun'

dataset_shopping['Range Usia'] = dataset_shopping.apply(lambda row: label_usia(row), axis=1)

# Kelompokkan dataset berdasarkan 'Genre' dan 'Range Usia' dan dihitung agregasi jumlahnya dan terapkan reset_index()
shopping_group = dataset_shopping.groupby(['Genre', 'Range Usia'])['CustomerID'].count().rename('Jumlah Pelanggan').reset_index()

# Membagi shopping_group ke masing-masing 'Genre'
Male_group = shopping_group[shopping_group['Genre']=='Male']
Female_group = shopping_group[shopping_group['Genre']=='Female']

# Mengimport library Matplotlib
import matplotlib.pyplot as plt

# Menggabungkan tampilan jumlah kelompok usia Male dan Female dengan grouped bar
import numpy as np

labels = shopping_group['Range Usia'].unique()
x = np.arange(len(labels))
width = 0.4 #lebar bar
 
fig, ax = plt.subplots()
Male_bar = ax.bar(x - width/2, Male_group['Jumlah Pelanggan'], width, label = 'Pria')
Female_bar = ax.bar(x + width/2, Female_group['Jumlah Pelanggan'], width, label = 'Wanita')

# Menampilkan angka setiap bar
ax.bar_label(Male_bar, padding=3)
ax.bar_label(Female_bar, padding=3)

ax.set_ylabel('Usia')
ax.set_title('Kelompok Usia Pelanggan')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.tight_layout()
plt.show()

# --- Menentukan Annual Income & Spending Score Berdasarkan Genre dan Usia ---
