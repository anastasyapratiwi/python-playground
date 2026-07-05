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

# Mengelompokkan 'Annual Income (k$)' dan 'Spending Score (1-100)' berdasarkan 'Genre' dan 'Range Usia', serta mengambil agregasinya (yaitu nilai rata-rata atau mean) berdasarkan pengelompokan tersebut
group_income = dataset_shopping.groupby(['Genre', 'Range Usia']).mean()[['Annual Income (k$)', 'Spending Score (1-100)']]
print(group_income)

# --- Visualisasi Annual Income Berdasarkan Genre dan Usia ---
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

# Mengelompokkan 'Annual Income (k$)' dan 'Spending Score (1-100)' berdasarkan 'Genre' dan 'Range Usia', serta mengambil agregasinya (yaitu nilai rata-rata atau mean) berdasarkan pengelompokan tersebut
group_income = dataset_shopping.groupby(['Genre', 'Range Usia']).mean()[['Annual Income (k$)', 'Spending Score (1-100)']].reset_index()

# Pisahkan ke dalam masing-masing Genre
male_group = group_income[group_income['Genre']=='Male']
female_group = group_income[group_income['Genre']=='Female']

# Import matplotlib
import matplotlib.pyplot as plt
import numpy as np

labels = group_income['Range Usia'].unique()
x = np.arange(len(labels))

fig = plt.figure(figsize=(8,8))
# Plotkan ke dalam grouped bar chart 
ax1 = plt.subplot(211)
width = 0.4
male_bar = ax1.bar(x - width/2, male_group['Annual Income (k$)'], width, label='Pria')
female_bar = ax1.bar(x + width/2, female_group['Annual Income (k$)'], width, label='Wanita')

# Menampilkan angka setiap bar
ax1.bar_label(male_bar, padding=3, fmt='%.2f')
ax1.bar_label(female_bar, padding=3, fmt='%.2f')
ax1.set_xlabel('Range Usia')
ax1.set_ylabel('Annual Income (k$)')
ax1.set_title('Pendapatan tahunan berdasarkan kelompok usia pelanggan')
ax1.set_xticks(x)
ax1.set_xticklabels(labels)
ax1.legend()

# Plotkan ke dalam pie chart untuk setiap genre
exploding = [0, 0.1, 0, 0]
ax2 = plt.subplot(223)
ax2.pie(male_group['Annual Income (k$)'], labels=male_group['Range Usia'], explode=exploding, autopct='%1.1f%%', startangle=90)
ax2.set_title('Persentase pendapatan tahunan\npelanggan pria berdasarkan\nkelompok usia')

ax2 = plt.subplot(224)
ax2.pie(female_group['Annual Income (k$)'], labels=female_group['Range Usia'], explode=exploding, autopct='%1.1f%%', startangle=90)
ax2.set_title('Persentase pendapatan tahunan\npelanggan wanita berdasarkan\nkelompok usia')

plt.tight_layout()
plt.show()

# --- Visualisasi Spending Score Berdasarkan Genre dan Usia ---
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

# Mengelompokkan 'Annual Income (k$)' dan 'Spending Score (1-100)' berdasarkan 'Genre' dan 'Range Usia', serta mengambil agregasinya (yaitu nilai rata-rata atau mean) berdasarkan pengelompokan tersebut
group_income = dataset_shopping.groupby(['Genre', 'Range Usia']).mean()[['Annual Income (k$)', 'Spending Score (1-100)']].reset_index()

# Pisahkan ke dalam masing-masing Genre
male_group = group_income[group_income['Genre']=='Male']
female_group = group_income[group_income['Genre']=='Female']

# Import matplotlib
import matplotlib.pyplot as plt
import numpy as np

labels = group_income['Range Usia'].unique()
x = np.arange(len(labels))

fig = plt.figure(figsize=(8,8))
# Plotkan ke dalam grouped bar chart 
ax1 = plt.subplot(211)
width = 0.4
male_bar = ax1.bar(x - width/2, male_group['Spending Score (1-100)'], width, label='Pria')
female_bar = ax1.bar(x + width/2, female_group['Spending Score (1-100)'], width, label='Wanita')

# Menampilkan angka setiap bar
ax1.bar_label(male_bar, padding=3, fmt='%.2f')
ax1.bar_label(female_bar, padding=3, fmt='%.2f')
ax1.set_xlabel('Range Usia')
ax1.set_ylabel('Spending Score (1-100)')
ax1.set_title('Skor pengeluaran berdasarkan kelompok usia pelanggan')
ax1.set_xticks(x)
ax1.set_xticklabels(labels)
ax1.legend()

# Plotkan ke dalam pie chart untuk setiap genre
exploding = [0, 0.1, 0, 0]
ax2 = plt.subplot(223)
ax2.pie(male_group['Spending Score (1-100)'], labels=male_group['Range Usia'], explode=exploding, autopct='%1.1f%%', startangle=90)
ax2.set_title('Persentase skor pengeluaran\npelanggan pria berdasarkan\nkelompok usia')

ax2 = plt.subplot(224)
ax2.pie(female_group['Spending Score (1-100)'], labels=female_group['Range Usia'], explode=exploding, autopct='%1.1f%%', startangle=90)
ax2.set_title('Persentase skor pengeluaran\npelanggan wanita berdasarkan\nkelompok usia')

plt.tight_layout()
plt.show()

# --- Data Penjualan ---
# Mengimpor library pandas
import pandas as pd
pd.set_option('display.max_columns', 10)

# Menyimpan data ke dalam dataframe
dataset_retail = pd.read_csv('https://dqlabcdn.xeratic.com/dqlab-dataset/data_retail.csv', delimiter=';')
print('Lima data teratas dataset_retail:')
print('--------------------------------:')
print(dataset_retail.head())

# Mencari total jumlah penjualan dari setiap produk
product_transaction = dataset_retail.groupby('Product').sum().reset_index()
print('\nTotal penjualan untuk setiap produk:')
print('-----------------------------------:')
print(product_transaction)

# --- Visualisasi Data Penjualan ---
# Kode sebelumnya
import pandas as pd

dataset_retail = pd.read_csv('https://dqlabcdn.xeratic.com/dqlab-dataset/data_retail.csv', delimiter=';')

product_transaction = dataset_retail.groupby('Product').sum().reset_index()

# Mengimpor library matplotlib
import matplotlib.pyplot as plt

# Menampilkan visualisasi dari jumlah transaksi tiap produk
fig = plt.figure(figsize=(10,5))

# Plot diagram batang
ax1 = plt.subplot(121)
ax1.bar(product_transaction['Product'], product_transaction['Average_Transaction_Amount'])
ax1.set_ylabel('Rata-rata jumlah transaksi\n(x 1 Milyar)')
ax1.set_title('Total Transaksi Produk')

# Plot persentase dengan pie chart
ax2 = plt.subplot(122)
ax2.pie(product_transaction['Average_Transaction_Amount'], labels=product_transaction['Product'], autopct='%1.1f%%', startangle=90)
ax2.set_title('Persentase Transaksi Produk')

plt.tight_layout()
plt.show()

# --- CHAPTER 3: Mini Project ---
# --- Mini Project Part 1 ---
# Import library pandas
import pandas as pd
pd.set_option('display.max_column', 10)

# Membaca dan menampilkan dataset
dataset_worldbank = pd.read_csv('https://dqlabcdn.xeratic.com/dqlab-dataset/atmajaya/worldbank.csv', delimiter=',', encoding='cp1252')

# Melihat tipe data database worldbank.csv
print('\nInformasi dataset_worldbank:')
print('============================')
dataset_worldbank.info()

# Mengganti baris data yang kosong dengan nilai 0
dataset_worldbank = dataset_worldbank.fillna(0)

# Melihat tipe data database worldbank.csv
print('\nInformasi dataset_worldbank setelah .fillna(0):')
print('===============================================')
dataset_worldbank.info()

# Data worldbank dari tahun ... sampai tahun ...
print('\nData worldbank dari tahun ... sampai tahun ...')
print('==============================================')
print(dataset_worldbank['year'].unique())

# --- Mini Project Part 2 ---
# Kode sebelumnya
import pandas as pd

dataset_worldbank = pd.read_csv('https://dqlabcdn.xeratic.com/dqlab-dataset/atmajaya/worldbank.csv', delimiter=',', encoding='cp1252')

dataset_worldbank = dataset_worldbank.fillna(0)

# Import matplotlib
import matplotlib.pyplot as plt

# GDP negara Indonesia, Malaysia, Singapore, dan Thailand
dataset_indonesia = dataset_worldbank[dataset_worldbank['country']=='Indonesia']
dataset_malaysia = dataset_worldbank[dataset_worldbank['country']=='Malaysia']
dataset_singapore = dataset_worldbank[dataset_worldbank['country']=='Singapore']
dataset_thailand = dataset_worldbank[dataset_worldbank['country']=='Thailand']

fig = plt.figure(figsize=(12, 10))
ax1 = plt.subplot(211)
ax1.plot(dataset_indonesia['year'], dataset_indonesia['realgdppercapita'], label='Indonesia')
ax1.plot(dataset_malaysia['year'], dataset_malaysia['realgdppercapita'], label='Malaysia')
ax1.plot(dataset_singapore['year'], dataset_singapore['realgdppercapita'], label='Singapore')
ax1.plot(dataset_thailand['year'], dataset_thailand['realgdppercapita'], label='Thailand')
ax1.legend()
ax1.grid()
ax1.set_xlabel('Tahun')
ax1.set_ylabel('GDP per kapita')
ax1.set_title('GDP per Kapita untuk Empat Negara ASEAN', fontsize=14)

# 20 negara dengan GDP per kapita tertinggi di tahun 2015
dataset_2015 = dataset_worldbank[dataset_worldbank['year']==2015].nlargest(20, 'realgdppercapita')
ax2 = plt.subplot(212)
ax2.bar(dataset_2015['country'], dataset_2015['realgdppercapita'])
ax2.grid(axis='y')
ax2.set_xlabel('Negara')
ax2.set_ylabel('GDP per kapita')
ax2.set_title('20 Negara dengan GDP per Kapita Tertinggi di 2015', fontsize=14)
plt.xticks(rotation=90)

plt.tight_layout()
plt.show()

# -- Note: For my certificates of completion, check README.md
# -- Thank you.
