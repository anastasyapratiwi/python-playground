# --- Profile Pemateri: Xeratic ---

import pandas as pd

# Load Dataset
df = pd.read_csv('https://dqlabcdn.xeratic.com/dqlab-dataset/HousingData.csv')

# Tampilkan jumlah data duplikat
print(df.duplicated().sum())

# Tampilkan jumlah data yang missing per kolom
print(df.isna().sum())

# Drop baris yang mempunyai baris kosong
df = df.dropna()

# Tampilkan berapa baris dan kolom sisa dari data yang sudah didrop
print(df.shape)
