# Profil Pemateri: Hendra Hadhil Choiri, Data Scientist, Gojek

# --- Chapter 1: Pengenalan Matplotlib dan Persiapan Dataset ---
# --- Pengenalan Dataset ---
import pandas as pd
dataset = pd.read_csv('https://dqlabcdn.xeratic.com/dqlab-dataset/retail_raw_reduced.csv')
print('Ukuran dataset: %d baris dan %d kolom\n' % dataset.shape)
print('Lima data teratas:')
print(dataset.head())

# --- Penambahan Kolom Order Month pada Dataset ---
import pandas as pd
import datetime

dataset = pd.read_csv('https://dqlabcdn.xeratic.com/dqlab-dataset/retail_raw_reduced.csv')

dataset['order_month'] = dataset['order_date'].apply(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))
print(dataset.head())

# --- Penambahan Kolom GMV pada Dataset ---
import pandas as pd
import datetime

dataset = pd.read_csv('https://dqlabcdn.xeratic.com/dqlab-dataset/retail_raw_reduced.csv')
dataset['order_month'] = dataset['order_date'].apply(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))

dataset['gmv'] = dataset['item_price']*dataset['quantity']
print('Ukuran dataset: %d baris dan %d kolom\n' % dataset.shape)
print('Lima data teratas:')
print(dataset.head())

# --- CHAPTER 2: Plot Pertama dengan Matplotlib ---
# --- Membuat Data Agregat ---
import pandas as pd
import datetime

dataset = pd.read_csv('https://dqlabcdn.xeratic.com/dqlab-dataset/retail_raw_reduced.csv')
dataset['order_month'] = dataset['order_date'].apply(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))
dataset['gmv'] = dataset['item_price']*dataset['quantity']

monthly_amount = dataset.groupby('order_month')['gmv'].sum().reset_index()
print(monthly_amount)

# --- Plot Pertama: Membuat Line Chart Trend Pertumbuhan GMV ---
import pandas as pd
import datetime
import matplotlib.pyplot as plt

dataset = pd.read_csv('https://dqlabcdn.xeratic.com/dqlab-dataset/retail_raw_reduced.csv')
dataset['order_month'] = dataset['order_date'].apply(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))
dataset['gmv'] = dataset['item_price']*dataset['quantity']

monthly_amount = dataset.groupby('order_month')['gmv'].sum().reset_index()

plt.plot(monthly_amount['order_month'], monthly_amount['gmv'])
plt.show()

# --- Cara Alternatif: Fungsi .plot() pada pandas Dataframe ---
import pandas as pd
import datetime
import matplotlib.pyplot as plt

dataset = pd.read_csv('https://dqlabcdn.xeratic.com/dqlab-dataset/retail_raw_reduced.csv')
dataset['order_month'] = dataset['order_date'].apply(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))
dataset['gmv'] = dataset['item_price']*dataset['quantity']

dataset.groupby(['order_month'])['gmv'].sum().plot()
plt.show()

# --- CHAPTER 3: Kustomisasi Grafik - Part 1 ---
# --- Mengubah Figure Size ---
import pandas as pd
import datetime
import matplotlib.pyplot as plt

dataset = pd.read_csv('https://dqlabcdn.xeratic.com/dqlab-dataset/retail_raw_reduced.csv')
dataset['order_month'] = dataset['order_date'].apply(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))
dataset['gmv'] = dataset['item_price']*dataset['quantity']

plt.figure(figsize=(15,5))
dataset.groupby(['order_month'])['gmv'].sum().plot()
plt.show()

# --- Menambahkan Title and Axis Labels ---
import pandas as pd
import datetime
import matplotlib.pyplot as plt

dataset = pd.read_csv('https://dqlabcdn.xeratic.com/dqlab-dataset/retail_raw_reduced.csv')
dataset['order_month'] = dataset['order_date'].apply(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))
dataset['gmv'] = dataset['item_price']*dataset['quantity']

plt.figure(figsize=(15, 5))
dataset.groupby(['order_month'])['gmv'].sum().plot()
plt.title('Monthly GMV Year 2019')
plt.xlabel('Order Month')
plt.ylabel('Total GMV')
plt.show()

# --- Kustomisasi Title and Axis Labels ---
import pandas as pd
import datetime
import matplotlib.pyplot as plt

dataset = pd.read_csv('https://dqlabcdn.xeratic.com/dqlab-dataset/retail_raw_reduced.csv')
dataset['order_month'] = dataset['order_date'].apply(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))
dataset['gmv'] = dataset['item_price']*dataset['quantity']

plt.figure(figsize=(15, 5))
dataset.groupby(['order_month'])['gmv'].sum().plot()
plt.title('Monthly GMV Year 2019', loc='center', pad=20, fontsize=20, color='blue')
plt.xlabel('Order Month', fontsize=15)
plt.ylabel('Total Amount', fontsize=15)
plt.show()

# --- Kustomisasi Line dan Point ---
import pandas as pd
import datetime
import matplotlib.pyplot as plt

dataset = pd.read_csv('https://dqlabcdn.xeratic.com/dqlab-dataset/retail_raw_reduced.csv')
dataset['order_month'] = dataset['order_date'].apply(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))
dataset['gmv'] = dataset['item_price']*dataset['quantity']

plt.figure(figsize=(15, 5))
dataset.groupby(['order_month'])['gmv'].sum().plot(color='green', marker='o', linestyle='-.', linewidth=2)
plt.title('Monthly GMV Year 2019', loc='center', pad=20, fontsize=20, color='blue')
plt.xlabel('Order Month', fontsize=15)
plt.ylabel('Total Amount', fontsize=15)
plt.show()

# --- Kustomisasi Grid ---
import pandas as pd
import datetime
import matplotlib.pyplot as plt

dataset = pd.read_csv('https://dqlabcdn.xeratic.com/dqlab-dataset/retail_raw_reduced.csv')
dataset['order_month'] = dataset['order_date'].apply(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))
dataset['gmv'] = dataset['item_price']*dataset['quantity']

plt.figure(figsize=(15, 5))
dataset.groupby(['order_month'])['gmv'].sum().plot(color='green', marker='o', linestyle='-.', linewidth=2)
plt.title('Monthly GMV Year 2019', loc='center', pad=20, fontsize=20, color='blue')
plt.xlabel('Order Month', fontsize=15)
plt.ylabel('Total Amount', fontsize=15)
plt.grid(color='darkgray', linestyle=':', linewidth=0.5)
plt.show()

