# Profil Pemateri: Muhammad Raden Hadi, Data Scientist, Bukalapak

# --- Chapter 2: Pengenalan Numpy dan Pandas ---
# Load Library
# memuat numpy sebagai np
import numpy as np
 
# memuat pandas sebagai pd
import pandas as pd

# Load Dataset
import pandas as pd
# memuat data bernama 'dataset_statistics.csv' dan memasukkan hasilnya ke dalam 'raw_data'
raw_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dataset_statistic.csv", sep=';')

# Inspeksi Data
import pandas as pd
raw_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dataset_statistic.csv", sep=';')

print (raw_data)
# melihat 10 data pada baris pertama
print (raw_data.head(10))

# melihat 5 data pada baris terakhir
print (raw_data.tail())

# Metode Shape
# Berapa banyak baris data dan fitur yang dataset punya?
import pandas as pd
raw_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dataset_statistic.csv", sep=';')

# melihat dimensi dari raw_data
print (raw_data.shape)

# mengambil jumlah data
print (raw_data.shape[0])

# Melihat Kolom Dalam Dataset
import pandas as pd
raw_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dataset_statistic.csv", sep=';')

print(raw_data.columns)

# Metode Isna (Ada berapa banyak data yang hilang dari dataset?)
import pandas as pd
raw_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dataset_statistic.csv", sep=';')

print (raw_data.isna()) # melihat data dari dataset. Nilai kolom akan bernilai False jika tidak terdapat nilai na dan akan bernilai True jika sebaliknya.
print (raw_data.isna().sum()) # menghitung jumlah data yang hilang dari dataset

# Metode Describe (.describe())
# melihat ringkasan dari data misalnya rerata, jumlah, nilai maksimum-minimum dan ukuran lainnya
import pandas as pd
raw_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dataset_statistic.csv", sep=';')

print (raw_data.describe())

# Mencari nilai maksimum dengan method .max() dan nilai minimum dengan method .min()

# Mencari nilai maksimum dari tiap kolom
raw_data.max()
 
# Mencari nilai maksimum dari kolom 'Harga'
raw_data['Harga'].max()
 
# Mencari nilai minimum dari kolom 'Harga'
raw_data['Harga'].min()

# Metode Sum (.sum())
# Jumlah dari semua nilai pada kolom
import pandas as pd
raw_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dataset_statistic.csv", sep=';')

# menghitung jumlah dari semua kolom
print (raw_data.sum())
 
# menghitung jumlah dari semua kolom bertipe data numerik saja
raw_data.sum(numeric_only=True)

# menghitung jumlah dari kolom 'Harga' dan 'Pendapatan'
raw_data[['Harga', 'Pendapatan']].sum()

# --- Manipulasi Dataframe - Memilih Kolom dan Baris ---
import pandas as pd
raw_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dataset_statistic.csv", sep=';')

# Memilih kolom 'Pendapatan' saja
print (raw_data['Pendapatan'])
 
# Memilih kolom 'Jenis Kelamin' dan 'Pendapatan'
print (raw_data[['Jenis Kelamin', 'Pendapatan']])

# --- Metode Loc ---
import pandas as pd
raw_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dataset_statistic.csv", sep=';')

# Mengambil data dari baris pertama (indeks 0) hingga baris ke-9 (indeks 9), yaitu sebanyak 10 baris
print(raw_data[:10])
 
# Mengambil data dari baris ke-4 (indeks 3) hingga baris ke-5 (indeks 4)
print(raw_data[3:5])
 
# Mengambil data dari baris ke-2 (indeks 1), baris ke-4 (indeks 3), dan baris ke-11 (indeks 10)
print(raw_data.loc[[1,3,10]])

# Mengambil kolom 'Jenis Kelamin' dan 'Pendapatan' dari baris ke-2 (indeks 1) hingga baris ke-10 (indeks 9)
print(raw_data[['Jenis Kelamin', 'Pendapatan']][1:10])
 
# Mengambil kolom 'Harga' dan 'Tingkat Kepuasan' dari baris ke-2 (indeks 1), baris ke-11 (indeks 10), dan baris ke-16 (indeks 15)
print(raw_data[['Harga', 'Tingkat Kepuasan']].loc[[1, 10, 15]])

# --- Chapter 3: Ukuran Pusat (Measures of Central Tendency) ---
# --- Rata-rata (Mean) -> .mean() ---
import numpy as np
import pandas as pd
raw_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dataset_statistic.csv", sep=';')

# mengambil hanya data untuk produk 'A'
produk_A = raw_data[raw_data['Produk'] == 'A']
 
# menghitung rerata pendapatan menggunakan method .mean pada objek pandas DataFrame
print (produk_A['Pendapatan'].mean())
 
# menghitung rerata pendapatan menggunakan method .mean pada objek pandas DataFrame dengan numpy
print (np.mean(produk_A['Pendapatan']))

# --- Median -> .median() ---
import numpy as np
import pandas as pd
raw_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dataset_statistic.csv", sep=';')
produk_A = raw_data[raw_data['Produk'] == 'A']

print (raw_data)
# Hitung median dari pendapatan menggunakan pandas
print (produk_A['Pendapatan'].median())
 
# Hitung median dari pendapatan menggunakan numpy
print (np.median(produk_A['Pendapatan']))

# --- Modus -> .value_counts() ---
import pandas as pd
raw_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dataset_statistic.csv", sep=';')

# Melihat jumlah dari masing-masing produk
print(raw_data['Produk'].value_counts())

# --- Kuantil -> .quantile() ---
import numpy as np
import pandas as pd
raw_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dataset_statistic.csv", sep=';')

# mencari median atau 50% dari data menggunakan pandas
raw_data['Pendapatan'].quantile(q = 0.5)
 
# mencari median atau 50% dari data menggunakan numpy
np.quantile(raw_data['Pendapatan'], q = 0.5)

import numpy as np
import pandas as pd
raw_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dataset_statistic.csv", sep=';')

# mencari median atau 50% dari data menggunakan pandas
print(raw_data['Pendapatan'].quantile(q = 0.5))
 
# mencari median atau 50% dari data menggunakan numpy
print(np.quantile(raw_data['Pendapatan'], q = 0.5))

# --- Pandas ---
# Mencari Kuartil 1 (25%)
print(raw_data['Pendapatan'].quantile(0.25))

# Mencari Median via Quantile (50%)
print(raw_data['Pendapatan'].quantile(0.5))

# Mencari Kuartil 3 (75%)
print(raw_data['Pendapatan'].quantile(0.75))

# --- Numpy ---
import numpy as np

# Pake Quantile (skala 0 sampai 1)
q1 = np.quantile(produk_A['Pendapatan'], 0.25)
q3 = np.quantile(produk_A['Pendapatan'], 0.75)

# Pake Percentile (skala 0 sampai 100)
q1_alt = np.percentile(produk_A['Pendapatan'], 25)

# --- Agregasi Data dengan method .agg() ---
import numpy as np
import pandas as pd
raw_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dataset_statistic.csv", sep=';')

# menghitung rerata dan median 'Pendapatan' dan 'Harga'
print(raw_data[['Pendapatan', 'Harga']].agg([np.mean, np.median]))
 
# menghitung rerata dan median Pendapatan dan Harga dari tiap produk
print(raw_data[['Pendapatan', 'Harga', 'Produk']].groupby('Produk').agg([np.mean, np.median]))

# --- Ukuran Sebaran (Measures of Dispersion) ---
# --- Proporsi Kategori ---
import pandas as pd
raw_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dataset_statistic.csv", sep=';')

# cari proporsi tiap Produk
print(raw_data['Produk'].value_counts()/raw_data.shape[0])

# --- Ukuran Sebaran pada Data Interval dan Rasio ---
# Rentang (range) -> max(X)−min(X)
import pandas as pd
raw_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dataset_statistic.csv", sep=';')

# Cari nilai rentang dari kolom 'Pendapatan'
print (raw_data['Pendapatan'].max() - raw_data['Pendapatan'].min())

# --- Variansi -> .var() ---
import numpy as np
import pandas as pd
raw_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dataset_statistic.csv", sep=';')

# menghitung variansi Pendapatan menggunakan method .var() dari pandas
print (raw_data['Pendapatan'].var())
 
# menghitung variansi Pendapatan menggunakan method .var() dari numpy
print (np.var(raw_data['Pendapatan']))

# mengatur variansi populasi dengan method `.var()` dari pandas
print (raw_data['Pendapatan'].var(ddof=0))

# --- Deviasi Baku (Standard Deviation) -> .std() ---
import numpy as np
import pandas as pd
raw_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dataset_statistic.csv", sep=';')

# menghitung deviasi baku sampel pendapatan menggunakan method std() dari pandas
print (raw_data['Pendapatan'].std())
 
# menghitung deviasi baku sampel pendapatan menggunakan method std() dari numpy
print (np.std(raw_data['Pendapatan'], ddof = 1))

# --- Chapter 5: Korelasi ---
import pandas as pd
raw_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dataset_statistic.csv", sep=';')

# menghitung korelasi dari setiap pasang variabel pada raw_data
print (raw_data.corr(numeric_only=True))

# mencari korelasi 'kendall' untuk tiap pasang variabel
print (raw_data.corr(method='kendall', numeric_only=True))
 
# mencari korelasi 'spearman' untuk tiap pasang variabel
print (raw_data.corr(method='spearman', numeric_only=True))
