# create_scaler.py
from sklearn.preprocessing import StandardScaler
import pickle
import pandas as pd

# Membaca data latih (train) Anda
# Pastikan Anda sudah memuat data latih yang digunakan
train = pd.read_csv('train.csv')  # Sesuaikan dengan nama file Anda

# Tentukan kolom yang akan distandarisasi
columns_to_stdscaller = ['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'EstimatedSalary']

# Buat objek StandardScaler
scaler = StandardScaler()

# Terapkan standarisasi pada data latih
train[columns_to_stdscaller] = scaler.fit_transform(train[columns_to_stdscaller])

# Simpan scaler ke file pkl
with open('scaler.pkl', 'wb') as scaler_file:
    pickle.dump(scaler, scaler_file)
