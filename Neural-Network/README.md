# Pengenalan Jaringan Syaraf Tiruan

Repository ini berisi implementasi dasar Jaringan Syaraf Tiruan menggunakan Python dan PyTorch.

## 1. Neuron

**File:** `neuron.py`

Program ini mengimplementasikan neuron sederhana menggunakan PyTorch untuk mempelajari hubungan linear antara input dan output.

Data yang digunakan:
- Input: 1, 2, 3, 4
- Target: 3, 5, 7, 9

**Output:**

Model menghasilkan prediksi untuk input 5 yang diharapkan mendekati angka 11.

## 2. MLP XOR

**File:** `mlp_xor.py`

Program ini menggunakan Multi-Layer Perceptron (MLP) untuk mempelajari operasi logika XOR.

Arsitektur model:
- 2 neuron input.
- 8 neuron pada hidden layer.
- 1 neuron output.
- Aktivasi ReLU dan Sigmoid.
- Optimizer Adam.

**Output:**

Model menghasilkan prediksi yang mendekati:

| Input | Target |
|---|---:|
| 0, 0 | 0 |
| 0, 1 | 1 |
| 1, 0 | 1 |
| 1, 1 | 0 |

## 3. CNN MNIST

**File:** `cnn_mnist.py`

Program ini mengimplementasikan Convolutional Neural Network (CNN) untuk mengenali angka tulisan tangan menggunakan dataset MNIST.

Arsitektur model:
- Convolutional Layer.
- ReLU.
- Max Pooling.
- Fully Connected Layer.
- 10 kelas output (angka 0–9).

**Output:**

Program menampilkan nilai Loss selama proses training dan pesan ketika pelatihan selesai.

```text
Batch 0, Loss: ...
Batch 200, Loss: ...
Batch 400, Loss: ...

Pelatihan selesai.
```

## Teknologi

- Python 3.11
- PyTorch
- Torchvision

## Instalasi

```bash
pip install torch torchvision
```

## Menjalankan Program

```bash
python neuron.py
python mlp_xor.py
python cnn_mnist.py
```