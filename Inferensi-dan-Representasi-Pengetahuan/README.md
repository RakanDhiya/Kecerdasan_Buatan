# Inferensi dan Representasi Pengetahuan

Repository ini berisi beberapa implementasi konsep inferensi dan representasi pengetahuan menggunakan bahasa pemrograman Python. Program-program di dalamnya menunjukkan bagaimana komputer dapat merepresentasikan fakta, menerapkan aturan logika, serta menghasilkan kesimpulan berdasarkan pengetahuan yang tersedia.

## 📂 Struktur File

```text
Inferensi-dan-Representasi-Pengetahuan/
│
├── README.md
├── inferensi_formal.py
├── jaringan_semantik_dictionary.py
├── jaringan_semantik_networkx.py
├── logika_predikat.py
├── logika_proposisi.py
└── penalaran_sederhana_semantik.py
```

## 1. Inferensi Formal (`inferensi_formal.py`)

Program ini menggunakan library SymPy untuk melakukan pengujian terhadap suatu kesimpulan berdasarkan aturan logika.

**Cara Kerja:**
- Membuat dua simbol proposisi, yaitu `hujan` dan `basah`.
- Membuat aturan bahwa jika hujan, maka jalan basah.
- Menetapkan fakta bahwa hujan sedang terjadi.
- Menguji apakah hujan dapat terjadi tanpa menyebabkan jalan basah.

**Output:**

```text
Apakah mungkin hujan tapi tidak basah? False
Kesimpulan: jalan PASTI basah.
```

**Penjelasan:** Hasil `False` menunjukkan bahwa tidak ditemukan kemungkinan hujan terjadi tanpa jalan menjadi basah berdasarkan aturan yang diberikan.

## 2. Jaringan Semantik Dictionary (`jaringan_semantik_dictionary.py`)

Program ini merepresentasikan pengetahuan dalam bentuk Dictionary Python yang berisi hubungan antarobjek.

**Cara Kerja:**
- Membuat objek seperti Kucing, Hewan, dan Ikan.
- Menentukan hubungan menggunakan relasi seperti `adalah`, `memiliki`, dan `makan`.
- Menggunakan fungsi `cari_relasi()` untuk mencari informasi berdasarkan objek dan relasi tertentu.

**Output:**

```text
Kucing adalah: ['Hewan']
Kucing makan: ['Ikan', 'Daging']
Ikan hidup di: ['Air']
```

**Penjelasan:** Program dapat menampilkan hubungan antarobjek berdasarkan informasi yang tersimpan dalam Dictionary.

## 3. Jaringan Semantik NetworkX (`jaringan_semantik_networkx.py`)

Program ini menggunakan library NetworkX dan Matplotlib untuk menggambarkan hubungan antarobjek dalam bentuk graf berarah.

**Cara Kerja:**
- Membuat graf menggunakan `nx.DiGraph()`.
- Menambahkan objek dan hubungan antarobjek.
- Menentukan posisi setiap node.
- Menggambar graf beserta label hubungan menggunakan Matplotlib.

**Output:**

Program menampilkan visualisasi jaringan semantik yang menunjukkan hubungan antara Kucing, Hewan, Bulu, Ikan, Oksigen, dan Air.

## 4. Logika Predikat (`logika_predikat.py`)

Program ini menerapkan logika berbasis kondisi untuk menentukan kemungkinan diagnosis berdasarkan gejala yang diberikan.

**Cara Kerja:**
- Membuat fungsi `diagnosa()` untuk memeriksa kumpulan gejala.
- Menggunakan kondisi `if` untuk mencocokkan gejala.
- Menghasilkan diagnosis berdasarkan aturan yang telah ditentukan.

**Output:**

```text
Gejala: ['demam', 'batuk', 'pilek']
Diagnosa: Kemungkinan Flu
```

**Penjelasan:** Program mencocokkan gejala demam dan batuk dengan aturan yang tersedia sehingga menghasilkan kemungkinan diagnosis flu.

## 5. Logika Proposisi (`logika_proposisi.py`)

Program ini menerapkan logika proposisi menggunakan nilai Boolean untuk menentukan kesimpulan berdasarkan fakta dan aturan.

**Cara Kerja:**
- Menetapkan fakta `hujan = True`.
- Menetapkan kondisi awal `jalan_basah = False`.
- Menggunakan kondisi `if hujan` untuk mengubah nilai jalan basah menjadi `True`.

**Output:**

```text
Apakah jalan basah? True
```

**Penjelasan:** Karena fakta menyatakan bahwa hujan sedang terjadi, aturan program mengubah kondisi jalan menjadi basah.

## 6. Penalaran Sederhana Semantik (`penalaran_sederhana_semantik.py`)

Program ini menerapkan konsep pewarisan sifat (inheritance) dalam jaringan semantik.

**Cara Kerja:**
- Menggunakan struktur Dictionary untuk menyimpan pengetahuan.
- Membuat fungsi `memiliki_sifat()` untuk memeriksa sifat suatu objek.
- Jika sifat tidak ditemukan secara langsung, program mencari parent melalui relasi `adalah`.
- Menggunakan rekursi untuk memeriksa sifat yang diwariskan dari parent.

**Output:**

```text
Kucing bernapas? True
```

**Penjelasan:** Kucing memiliki hubungan `adalah` dengan Hewan. Karena Hewan memiliki sifat bernapas, Kucing juga dianggap mewarisi sifat tersebut.

## 🛠️ Teknologi dan Library

- Python 3
- SymPy
- NetworkX
- Matplotlib

## 🚀 Cara Menjalankan Program

**1. Install library yang dibutuhkan:**

```bash
pip install sympy networkx matplotlib
```

**2. Jalankan salah satu file melalui terminal:**

```bash
python inferensi_formal.py
```

Ganti nama file sesuai program yang ingin dijalankan.

---

## Kesimpulan

Keenam program tersebut menunjukkan penerapan konsep inferensi dan representasi pengetahuan dalam kecerdasan buatan. Mulai dari penggunaan aturan logika untuk menghasilkan kesimpulan hingga representasi hubungan antarobjek menggunakan jaringan semantik.