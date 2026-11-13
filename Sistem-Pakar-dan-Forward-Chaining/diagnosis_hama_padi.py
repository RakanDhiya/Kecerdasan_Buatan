# DIAGNOSIS HAMA PADI

rules = {
    "Wereng": [["daun_menguning", "bulir_hampa"]],
    "Penggerek Batang": [["batang_berlubang", "daun_menguning"]],
    "Tikus": [["bulir_hampa", "batang_berlubang"]],
    "Walang Sangit": [["daun_terpotong", "bulir_hampa"]],
}

def backward_chaining(target, fakta, visited=None):
    if visited is None:
        visited = set()
    if target in visited:
        return False
    visited.add(target)

    if target in fakta:
        return True
    if target in rules:
        for syarat in rules[target]:
            if all(backward_chaining(s, fakta, visited) for s in syarat):
                return True
    return False

print("=" * 60)
print(" SISTEM PAKAR DIAGNOSIS HAMA PADI")
print("=" * 60)

print("\nPilih gejala yang terlihat di sawah Anda:\n")

opsi_gejala = [
    ("daun_menguning", "Daun padi menguning"),
    ("bulir_hampa", "Bulir padi hampa/kosong"),
    ("batang_berlubang", "Batang padi berlubang"),
    ("daun_terpotong", "Daun padi terpotong"),
]
for i, (_, label) in enumerate(opsi_gejala, 1):
    print(f" {i}. {label}")


pilihan = input("\nMasukkan nomor gejala (pisahkan koma): ")
index_pilihan = [int(x.strip()) - 1 for x in pilihan.split(",") if x.strip().isdigit()]
fakta = [opsi_gejala[i][0] for i in index_pilihan if 0 <= i < len(opsi_gejala)]

print("\n" + "=" * 60)
print(" HASIL DIAGNOSIS HAMA")
print("=" * 60)

print("\nGejala yang dipilih:")

for f in fakta:
    print(f" ✓ {f.replace('_', ' ').title()}")
print("\nHasil analisis:")
terdeteksi = False

for hama in rules:
    if backward_chaining(hama, fakta):
        print(f" ✔Terdeteksi: {hama}")
        terdeteksi = True
if not terdeteksi:
    print(" ✘ Hama tidak teridentifikasi")
