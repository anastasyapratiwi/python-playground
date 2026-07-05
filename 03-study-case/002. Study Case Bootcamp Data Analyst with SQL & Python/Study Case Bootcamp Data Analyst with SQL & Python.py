# --- Profile Pemateri: Xeratic ---

import pandas as pd

# load dataset
dataset = 'https://dqlabcdn.xeratic.com/dqlab-dataset/SuperStore.csv'
df = pd.read_csv(dataset);

# Pisahkan Customer Name menjadi dua komponen yaitu First_Name dan Last_Name
df[['First_Name', 'Last_Name']] = df['Customer_Name'].str.split(' ', n=1, expand=True)

# tampilkan 5 baris pertama
print(df.head())

# -- Note: For my certificates of completion, check README.md
# -- Thank you.
