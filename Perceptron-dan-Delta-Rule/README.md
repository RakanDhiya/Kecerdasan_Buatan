# Perceptron dan Delta Rule

Repository ini berisi implementasi algoritma Perceptron dan Delta Rule dalam Jaringan Syaraf Tiruan menggunakan Python dan NumPy.

## 1. Perceptron

**File:** `perceptron.py`

Program ini mengimplementasikan algoritma Perceptron untuk mempelajari operasi logika AND.

Model melakukan pembaruan bobot dan bias berdasarkan kesalahan prediksi hingga mencapai kondisi konvergen.

**Output:**

```text
Konvergen pada epoch ke-5
Bobot akhir: [0.3 0.3]
Bias akhir: -0.2

Hasil prediksi:
[0 0 0 1]
```

Hasil tersebut menunjukkan bahwa model berhasil mempelajari operasi logika AND.

## 2. Delta Rule

**File:** `delta_rule.py`

Program ini mengimplementasikan algoritma Delta Rule untuk memperbarui bobot berdasarkan selisih antara target dan hasil prediksi.

Model menggunakan fungsi aktivasi linear dan learning rate dalam proses pembelajaran.

**Output:**

Program menampilkan hasil pembelajaran dan prediksi model berdasarkan data yang digunakan.

## Teknologi

- Python 3.11
- NumPy

## Instalasi

```bash
pip install numpy
```

## Menjalankan Program

```bash
python perceptron.py
python delta_rule.py
```