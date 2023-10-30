# Laporan Proyek Machine Learning
### Nama : Veronika 
### Nim : 211351147
### Kelas : TIF Pagi B

## Domain Proyek

Estimasi harga diamond ini dibuat untuk membantu siapapun yang ingin membeli diamond dan dapat mempersiapkan uang sesuai dengan budget yang mereka punya dengan diamond yang akan mereka dapatkan

## Business Understanding

Pembuatan model untuk memprediksi harga diamond ini diharapkan agar dapat mempermudah siapapun yang ingin membeli diamond dan sudah memiliki kisaran harga yang harus mereka siapkan sesuai dengan diamond yang ingin mereka beli.

Bagian laporan ini mencakup:

### Problem Statements

Menjelaskan pernyataan masalah latar belakang:
- Pembeli yang harus mendatangi toko-toko penjual diamond untuk tau kisaran harga diamond

### Goals

Menjelaskan tujuan dari pernyataan masalah:
- Mempermudah pembeli untuk mengetahui harga kisaran dari diamond yang akan dibeli tanpa harus mendatangi ke setiap toko penjual diamond untuk mengetahui kisaran harga dari diamond tersebut

    ### Solution statements
    - Pembuatan aplikasi estimasi harga diamond yang dapat dipakai oleh setiap orang guna mendapatkan informasi kisaran harga diamond berdasarkan inputan dari karakteristik diamond yang dicari
    - Aplikasi tersebut dibuat menggunakan metode estimasi dengan algoritma Linear Regression dengan minimal akurasi 70% pada tahap evaluasinya

## Data Understanding
Dataset ini diambil dari kaggle yang berisi karakteristik diamond yaitu ukuran, berat, kejernihan berlian dan harga dari berlian dari 50000 baris dan 10 kolom.

Dataset: [Diamonds Price Dataset](https://www.kaggle.com/datasets/amirhosseinmirzaie/diamonds-price-dataset).

Selanjutnya uraikanlah seluruh variabel atau fitur pada data. Sebagai contoh:  

### Variabel-variabel pada Dataset adalah sebagai berikut:
Kolom Deskripsi
- ```carat``` = Berat berlian dalam karat	
- ```cut``` = potongan kualitas pemotongan berlian
- ```color``` = warna berlian dari warna J (terburuk) hingga D (terbaik)
- ```clarity``` = Ukuran kejernihan berlian (dari kiri ke kanan adalah yang terburuk hingga yang terbaik: kejernihan I1, SI2, SI1, VS2, VS1, VVS2, VVS1, IF)
- ```x``` = panjang berlian dalam mm x
- ```y``` = lebar berlian dalam mm y
- ```z``` = kedalaman berlian dalam mm z
- ```depth``` = Persentase kedalaman yang sama dengan kedalaman z / rata-rata (x,y)
- ```table``` = Lebar titik terlebar di bagian atas tabel berlian
- ```price [target variable]``` = harga harga berlian

## Data Preparation
Data preparation yang digunakan dalam pembuatan model ini:
Menentukan atribut yang akan dipakai sebagai X dan Y
```
features = ['carat', 'depth', 'table', 'x', 'y', 'z']
x = df[features]
y = df['price']
x.shape, y.shape
```

## Modeling
Menentukan data training dan testing
```
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=70)
y_test.shape
```
pembuatan model
```
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(x_train, y_train)
pred = lr.predict(x_test)
```

## Evaluation
Tahapan evaluasi yang dipakai yaitu pengecekan akurasi dan r2 score untuk presisinya
```
score = lr.score(x_test, y_test)
print('akurasi model regresi linier =', score)
```
akurasi model regresi linier = 0.8567815493322518

```
from sklearn.metrics import r2_score
r2_DT = r2_score(y_test, pred)
r2_DT

print(f"Precision = {r2_DT}")
```
Precision = 0.8567815493322518

akurasi dan presisi yang didapatkan adalah 85% yang mana model dapat dipakai

## Deployment
Link Aplikasi : [Estimasi Harga Diamond](https://harga-diamond.streamlit.app/)

