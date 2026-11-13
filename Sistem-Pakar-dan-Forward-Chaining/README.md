# Sistem Pakar dan Forward Chaining

Repository ini berisi implementasi beberapa sistem pakar sederhana menggunakan Python. Program menerapkan konsep kecerdasan buatan untuk melakukan diagnosis berdasarkan gejala, menghitung tingkat keyakinan menggunakan Certainty Factor (CF), serta memberikan rekomendasi berdasarkan fakta dan aturan yang telah ditentukan.

## 📂 Struktur File

```text
Sistem-Pakar-dan-Forward-Chaining/
│
├── README.md
├── diagnosis_hama_padi.py
├── diagnosis_motor.py
├── diagnosis_penyakit.py
└── rekomen_jurusan.py
```

## 1. Diagnosis Hama Padi (`diagnosis_hama_padi.py`)

Program ini merupakan sistem pakar sederhana untuk mengidentifikasi kemungkinan hama pada tanaman padi menggunakan metode Backward Chaining.

**Cara Kerja:**
- Menyimpan aturan hubungan antara jenis hama dan gejala dalam Dictionary.
- Pengguna memilih gejala yang ditemukan pada tanaman padi.
- Fungsi `backward_chaining()` memeriksa apakah gejala memenuhi aturan dari hama yang ingin dibuktikan.
- Sistem menampilkan hama yang sesuai dengan fakta yang diberikan.

**Contoh Input:**

```text
Masukkan nomor gejala: 1,2
```

**Output:**

```text
HASIL DIAGNOSIS HAMA

Gejala yang dipilih:
✓ Daun Menguning
✓ Bulir Hampa

Hasil analisis:
✔ Terdeteksi: Wereng
```

**Penjelasan:** Sistem menyimpulkan kemungkinan hama Wereng karena gejala daun menguning dan bulir hampa memenuhi aturan yang telah ditentukan.

## 2. Diagnosis Kerusakan Motor (`diagnosis_motor.py`)

Program ini merupakan sistem pakar untuk mengidentifikasi kemungkinan kerusakan motor menggunakan metode Certainty Factor (CF).

**Cara Kerja:**
- Menyimpan basis pengetahuan berupa jenis kerusakan, gejala, dan nilai keyakinan pakar.
- Pengguna memasukkan tingkat keyakinan terhadap setiap gejala dengan nilai 0.0 sampai 1.0.
- Fungsi `hitung_cf()` menggabungkan nilai CF pakar dan CF pengguna.
- Sistem mengurutkan hasil diagnosis berdasarkan nilai CF tertinggi.
- Fungsi `interpretasi()` menentukan kategori tingkat keyakinan.

**Contoh Input:**

```text
Sulit Starter          : 1.0
Busi Basah             : 1.0
Asap Putih             : 0.0
Oli Berkurang          : 0.0
```

**Contoh Output:**

```text
PERINGKAT DIAGNOSIS:

1. Busi rusak
CF Total : 0.9800 (98.00%)
Status   : Sangat yakin

DIAGNOSIS UTAMA: Busi rusak
TINGKAT KEYAKINAN: 98.00% (Sangat yakin)
```

**Penjelasan:** Sistem menghitung nilai keyakinan berdasarkan kecocokan gejala dengan basis pengetahuan. Kerusakan dengan nilai CF tertinggi menjadi diagnosis utama.

## 3. Diagnosis Penyakit (`diagnosis_penyakit.py`)

Program ini merupakan sistem pakar untuk menentukan kemungkinan penyakit berdasarkan gejala yang dialami pengguna menggunakan metode Certainty Factor.

**Cara Kerja:**
- Menyimpan basis pengetahuan berupa penyakit, gejala, dan nilai CF pakar.
- Pengguna menjawab pertanyaan gejala dengan pilihan Ya atau Tidak.
- Jika menjawab Ya, pengguna memasukkan tingkat keyakinan antara 0.0 sampai 1.0.
- Sistem menghitung nilai CF setiap penyakit.
- Hasil diagnosis diurutkan berdasarkan tingkat keyakinan tertinggi.

**Contoh Input:**

```text
Apakah Anda mengalami Batuk? (y/t): y
Seberapa yakin? (0.0-1.0): 1.0

Apakah Anda mengalami Demam? (y/t): y
Seberapa yakin? (0.0-1.0): 1.0

Apakah Anda mengalami Pilek? (y/t): y
Seberapa yakin? (0.0-1.0): 1.0
```

**Contoh Output:**

```text
Peringkat Diagnosis:

1. Flu 95.20% (Sangat yakin)

DIAGNOSIS UTAMA: Flu
KEYAKINAN: 95.20% (Sangat yakin)
```

**Penjelasan:** Sistem membandingkan gejala yang dimasukkan dengan basis pengetahuan penyakit. Penyakit dengan nilai CF tertinggi ditampilkan sebagai hasil diagnosis utama.

*Catatan: Program ini merupakan simulasi sistem pakar untuk pembelajaran, bukan alat diagnosis medis.*

## 4. Rekomendasi Jurusan Kuliah (`rekomen_jurusan.py`)

Program ini merupakan sistem pakar sederhana untuk memberikan rekomendasi jurusan kuliah berdasarkan minat dan kemampuan pengguna menggunakan metode Forward Chaining.

**Cara Kerja:**
- Menyimpan aturan rekomendasi jurusan dalam bentuk List dan Dictionary.
- Pengguna memilih minat yang sesuai dengan dirinya.
- Pilihan pengguna disimpan sebagai fakta.
- Fungsi `forward_chaining()` mencocokkan fakta dengan seluruh kondisi pada aturan.
- Sistem menampilkan jurusan yang sesuai beserta alasan dan persyaratannya.

**Contoh Input:**

```text
Masukkan pilihan Anda: 1,2,3
```

**Output:**

```text
HASIL REKOMENDASI JURUSAN

Minat Anda:
✓ Suka Logika
✓ Suka Coding
✓ Matematika Tinggi

★ Jurusan: Teknik Informatika
Alasan : Cocok untuk yang suka pemrograman & algoritma
Syarat : suka_logika, suka_coding, matematika_tinggi
```

**Penjelasan:** Sistem memberikan rekomendasi Teknik Informatika karena seluruh fakta yang dipilih pengguna memenuhi kondisi pada aturan yang tersedia.

## 🛠️ Teknologi yang Digunakan

- Python 3
- Dictionary dan List
- Conditional Statement
- Function dan Recursion
- Backward Chaining
- Forward Chaining
- Certainty Factor (CF)

## 🚀 Cara Menjalankan Program

Pastikan Python 3 sudah terinstal di komputer.

Buka terminal pada folder project, kemudian jalankan salah satu program berikut:

```bash
python diagnosis_hama_padi.py
```

```bash
python diagnosis_motor.py
```

```bash
python diagnosis_penyakit.py
```

```bash
python rekomen_jurusan.py
```

Program dapat dijalankan secara terpisah sesuai kebutuhan.

## Kesimpulan

Keempat program menunjukkan penerapan sistem pakar dalam kecerdasan buatan. Backward Chaining digunakan untuk menelusuri kesimpulan berdasarkan target, Forward Chaining digunakan untuk menghasilkan kesimpulan dari fakta yang tersedia, sedangkan Certainty Factor digunakan untuk menghitung tingkat keyakinan terhadap hasil diagnosis.