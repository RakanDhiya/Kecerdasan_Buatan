# DIAGNOSIS KERUSAKAN MOTOR

basis_pengetahuan = {
    "Busi rusak": {"sulit_starter": 0.8, "busi_basah": 0.9},
    "Ring seher aus": {"asap_putih": 0.85, "oli_berkurang": 0.7},
    "Bearing rusak": {"bergetar_hebat": 0.75, "suara_kasar": 0.8},
    "Kelistrikan bermasalah": {"mati_mendadak": 0.7, "bahan_bakar_lancar": 0.6},
}

def hitung_cf(kerusakan, gejala_user):
    """Menghitung CF kombinasi untuk satu kerusakan"""
    cf_list = []

    for gejala, cf_pakar in basis_pengetahuan[kerusakan].items():
        if gejala in gejala_user:
            cf = cf_pakar * gejala_user[gejala]
            cf_list.append(cf)

    if not cf_list:
        return 0, []

    cf_total = cf_list[0]

    for cf in cf_list[1:]:
        cf_total = cf_total + cf * (1 - cf_total)

    return cf_total, cf_list

def interpretasi(cf):
    if cf >= 0.8:
        return "Sangat yakin"
    elif cf >= 0.6:
        return "Yakin"
    elif cf >= 0.4:
        return "Cukup yakin"
    elif cf >= 0.2:
        return "Sedikit yakin"
    else:
        return "Tidak yakin"

print("=" * 60)
print(" SISTEM PAKAR DIAGNOSIS KERUSAKAN MOTOR")
print("=" * 60)

print("\nSistem akan menanyakan gejala yang Anda alami.")
print("Masukkan tingkat keyakinan (0.0 - 1.0):")
print(" 0.0 = tidak mengalami")
print(" 0.5 = mungkin mengalami")
print(" 1.0 = sangat yakin mengalami\n")

# Kumpulkan semua gejala unik
semua_gejala = set()

for kerusakan in basis_pengetahuan.values():
    semua_gejala.update(kerusakan.keys())

# Input gejala dari user
gejala_user = {}

for g in sorted(semua_gejala):
    while True:
        try:
            nama = g.replace("_", " ").title()
            cf = float(input(f" {nama:25s} (0.0-1.0): "))

            if 0 <= cf <= 1:
                if cf > 0:
                    gejala_user[g] = cf
                break
            else:
                print(" Masukkan nilai antara 0.0 - 1.0")
                
        except ValueError:
            print(" Input tidak valid, masukkan angka!")

print("\n" + "=" * 60)
print(" HASIL DIAGNOSIS")
print("=" * 60)

if not gejala_user:
    print("\n Tidak ada gejala yang diinput. Sistem tidak dapat")
    print(" melakukan diagnosis.")
else:
    print("\nGejala yang Anda alami:")

    for g, cf in gejala_user.items():
        print(f" • {g.replace('_', ' ').title():25s} " f"(CF user = {cf})")

    # Hitung CF tiap kerusakan
    hasil = {}
    for kerusakan in basis_pengetahuan:
        cf, detail = hitung_cf(kerusakan, gejala_user)

        if cf > 0:
            hasil[kerusakan] = (cf, detail)

    if hasil:
        # Urutkan dari CF tertinggi
        hasil_sorted = sorted(hasil.items(), key=lambda x: x[1][0], reverse=True)

        print("\n" + "-" * 60)
        print("PERINGKAT DIAGNOSIS:")
        print("-" * 60)

        for i, (kerusakan, (cf, detail)) in enumerate(hasil_sorted, 1):
            print(f"\n{i}. {kerusakan}")
            print(f" CF Total : {cf:.4f} ({cf * 100:.2f}%)")
            print(f" Status   : {interpretasi(cf)}")
            print(f" Detail   : " f"{[f'{d:.4f}' for d in detail]}")

        # Diagnosis utama
        utama, (cf_utama, _) = hasil_sorted[0]
        print("\n" + "=" * 60)
        print(f" ★ DIAGNOSIS UTAMA: {utama}")
        print(
            f" ★ TINGKAT KEYAKINAN: "
            f"{cf_utama * 100:.2f}% "
            f"({interpretasi(cf_utama)})"
        )
        print("=" * 60)

    else:
        print("\n Tidak ada kerusakan yang cocok dengan gejala Anda.")
