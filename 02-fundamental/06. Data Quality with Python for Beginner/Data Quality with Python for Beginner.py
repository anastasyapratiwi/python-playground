# Profil Pemateri: Kevin Stewart, Senior Data Analyst, Traveloka

# --- CHAPTER 1: Data Profiling ---
# --- Importing Data ---
import pandas as pd
import numpy as np
import io
import pandas_profiling
retail_raw = pd.read_csv('https://dqlabcdn.xeratic.com/dqlab-dataset/retail_raw_reduced_data_quality.csv')

# --- Inspeksi tipe data ---
import pandas as pd
import numpy as np
import io
import pandas_profiling
retail_raw = pd.read_csv('https://dqlabcdn.xeratic.com/dqlab-dataset/retail_raw_reduced_data_quality.csv')

# Cetak tipe data di setiap kolom retail_raw
print(retail_raw.dtypes)

# --- Descriptive Statistics - Part 1 ---
# --- Tugas Praktek: ---
import pandas as pd
import numpy as np
import io
import pandas_profiling
retail_raw = pd.read_csv('https://dqlabcdn.xeratic.com/dqlab-dataset/retail_raw_reduced_data_quality.csv')

# Kolom city
length_city = len(retail_raw['city'])
print('Length kolom city:', length_city)

# --- Tugas Praktek: Kolom product_id ---
length_product_id = len(retail_raw['product_id'])
print('Length kolom product_id:', length_product_id)

# --- Descriptive Statistics - Part 2 ---
# --- Tugas Praktek: ---
import pandas as pd
import numpy as np
import io
import pandas_profiling
retail_raw = pd.read_csv('https://dqlabcdn.xeratic.com/dqlab-dataset/retail_raw_reduced_data_quality.csv')

# Count kolom city
count_city = retail_raw['city'].count() 
print('Count kolom count_city:', count_city)

# Tugas praktek: count kolom product_id
count_product_id = retail_raw['product_id'].count()
print('Count kolom product_id:', count_product_id)

# --- Descriptive Statistics - Part 3 ---
# --- Tugas Praktek: ---
import pandas as pd
import numpy as np
import io
import pandas_profiling

retail_raw = pd.read_csv('https://dqlabcdn.xeratic.com/dqlab-dataset/retail_raw_reduced_data_quality.csv')

# Kolom city
length_city = len(retail_raw['city'])
count_city = retail_raw['city'].count()

# Kolom product id
length_product_id = len(retail_raw['product_id'])
count_product_id = retail_raw['product_id'].count()

# Missing value pada kolom city
number_of_missing_values_city = length_city - count_city
ratio_of_missing_values_city = number_of_missing_values_city/length_city
pct_of_missing_values_city = '{0:.1f}%'.format(ratio_of_missing_values_city * 100)
print('Persentase missing value kolom city:', pct_of_missing_values_city)

# --- Tugas praktek: Missing value pada kolom product_id ---
number_of_missing_values_product_id = length_product_id - count_product_id
ratio_of_missing_values_product_id = number_of_missing_values_product_id/length_product_id
pct_of_missing_values_product_id = '{0:.1f}%'.format(ratio_of_missing_values_product_id * 100)
print('Persentase missing value kolom product_id:', pct_of_missing_values_product_id)

# --- Descriptive Statistics - Part 4 ---
# --- Tugas praktek: ---
import pandas as pd
import numpy as np
import io
import pandas_profiling

retail_raw = pd.read_csv('https://dqlabcdn.xeratic.com/dqlab-dataset/retail_raw_reduced_data_quality.csv')

# Deskriptif statistics kolom quantity
print('Kolom quantity')
print('Minimum value: ', retail_raw['quantity'].min())
print('Maximum value: ', retail_raw['quantity'].max())
print('Mean value: ', retail_raw['quantity'].mean())
print('Mode value: ', retail_raw['quantity'].mode())
print('Median value: ', retail_raw['quantity'].median())
print('Standard Deviation value: ', retail_raw['quantity'].std())

# --- Tugas praktek: Deskriptif statistics kolom item_price ---
print('')
print('Kolom item_price')
print('Minimum value: ', retail_raw['item_price'].min())
print('Maximum value: ', retail_raw['item_price'].max())
print('Mean value: ', retail_raw['item_price'].mean())
print('Median value: ', retail_raw['item_price'].median())
print('Standard Deviation value: ', retail_raw['item_price'].std())

# --- Descriptive Statistics - Part 5 ---
# --- Tugas Praktek: ---
import pandas as pd
import numpy as np
import io
import pandas_profiling
retail_raw = pd.read_csv('https://dqlabcdn.xeratic.com/dqlab-dataset/retail_raw_reduced_data_quality.csv')

# Quantile statistics kolom quantity
print('Kolom quantity:')
print(retail_raw['quantity'].quantile([0.25, 0.5, 0.75]))

# Tugas praktek: Quantile statistics kolom item_price
print('')
print('Kolom item_price:')
print(retail_raw['item_price'].quantile([0.25, 0.5, 0.75]))

# --- Descriptive Statistics - Part 6 ---
