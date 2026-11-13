# Depth First Search (DFS)

Repository ini berisi implementasi algoritma Depth First Search (DFS) menggunakan bahasa pemrograman Python untuk melakukan penelusuran pada struktur Graph.

## 1. DFS Rekursif

**File:** `dfs_rekursif.py`

Program ini mengimplementasikan algoritma Depth First Search menggunakan metode rekursif.

Graph direpresentasikan menggunakan Adjacency List, yaitu struktur data yang menyimpan daftar hubungan antar-node.

Proses pencarian dilakukan dengan mengunjungi sebuah node, menandainya sebagai visited, kemudian menelusuri setiap tetangganya secara rekursif.

**Output:**

```text
Hasil DFS:
ABDECF
```

## 2. DFS Iteratif

**File:** `dfs_iteratif.py`

Program ini mengimplementasikan algoritma Depth First Search menggunakan metode iteratif dengan bantuan struktur data Stack.

Proses pencarian dilakukan dengan:
- Menyimpan node awal ke dalam Stack.
- Mengambil node paling atas dari Stack.
- Memeriksa apakah node sudah dikunjungi.
- Menandai node sebagai visited.
- Memasukkan node tetangga ke dalam Stack.

Program menggunakan `reversed()` agar urutan penelusuran sesuai dengan contoh DFS rekursif.

**Output:**

```text
hasil DFS Iteratif:
ABDECF
```

## 3. Studi Kasus DFS

**File:** `studi_kasus.py`

Program ini merupakan penerapan algoritma DFS iteratif untuk menyelesaikan studi kasus penelusuran Graph.

Graph menggunakan enam node, yaitu A, B, C, D, E, dan F.

Penelusuran dimulai dari node A menggunakan Stack dan himpunan `visited` untuk menghindari kunjungan berulang.

**Output:**

```text
hasil DFS Iteratif:
ABDECF
```

## 4. Teknologi yang Digunakan

- Python 3
- Struktur Data Graph
- Adjacency List
- Stack
- Set

## 5. Cara Menjalankan Program

Jalankan perintah berikut melalui terminal:

```bash
python dfs_rekursif.py
python dfs_iteratif.py
python studi_kasus.py
```

## 6. Kesimpulan

Depth First Search merupakan algoritma pencarian yang menelusuri Graph sedalam mungkin sebelum kembali ke node sebelumnya.

DFS dapat diimplementasikan menggunakan dua metode, yaitu rekursif dengan pemanggilan fungsi secara berulang dan iteratif dengan bantuan Stack.