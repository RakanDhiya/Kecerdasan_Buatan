# DIAGNOSIS PENYAKIT

basis_pengetahuan = {
    "Flu": {"demam": 0.6, "batuk": 0.7, "pilek": 0.8, "sakit_kepala": 0.5},
    "ISPA": {"demam": 0.7, "batuk": 0.8, "sesak_nafas": 0.9, "nyeri_tenggorokan": 0.6},
    "DBD": {"demam": 0.9, "bintik_merah": 0.8, "nyeri_otot": 0.7, "mual": 0.5},
    "Tifus": {"demam": 0.8, "mual": 0.7, "nyeri_perut": 0.8, "lemas": 0.6},
}


def hitung_cf(penyakit, gejala_user):
    cf_list = []
    for gejala, cf_pakar in basis_pengetahuan[penyakit].items():
        if gejala in gejala_user:
            cf = cf_pakar * gejala_user[gejala]
            cf_list.append(cf)
    if not cf_list:
        return 0

    cf_total = cf_list[0]

    for cf in cf_list[1:]:
        cf_total = cf_total + cf * (1 - cf_total)
    return cf_total


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
print(" SISTEM PAKAR DIAGNOSIS PENYAKIT")
print("=" * 60)

print("\nJawab pertanyaan berikut dengan Ya/Tidak.")
print("Jika 'Ya', Anda akan diminta tingkat keyakinan (0.0-1.0).\n")

semua_gejala = set()

for p in basis_pengetahuan.values():
    semua_gejala.update(p.keys())

gejala_user = {}

for g in sorted(semua_gejala):
    nama = g.replace("_", " ").title()
    jawab = input(f"Apakah Anda mengalami {nama}? (y/t): ").lower().strip()

    if jawab == "y":
        while True:
            try:
                cf = float(input(" Seberapa yakin? (0.0-1.0): "))

                if 0 < cf <= 1:
                    gejala_user[g] = cf
                    break
                else:
                    print(" Nilai harus antara 0.0 - 1.0")

            except ValueError:
                print(" Masukkan angka!")


print("\n" + "=" * 60)
print(" HASIL DIAGNOSIS")
print("=" * 60)

if not gejala_user:
    print("\n Tidak ada gejala yang dipilih.")
else:
    hasil = {}

    for penyakit in basis_pengetahuan:
        cf = hitung_cf(penyakit, gejala_user)

        if cf > 0:
            hasil[penyakit] = cf

    if hasil:
        hasil_sorted = sorted(hasil.items(), key=lambda x: x[1], reverse=True)

        print("\nPeringkat Diagnosis:")
        print("-" * 60)

        for i, (penyakit, cf) in enumerate(hasil_sorted, 1):
            bar = "█" * int(cf * 20)

            print(
                f"{i}. {penyakit} "
                f"{cf * 100:.2f}% "
                f"{bar} "
                f"({interpretasi(cf)})"
            )

        utama, cf_utama = hasil_sorted[0]

        print("=" * 60)
        print(f" ★ DIAGNOSIS UTAMA: {utama}")
        print(f" ★ KEYAKINAN: {cf_utama * 100:.2f}% " f"({interpretasi(cf_utama)})")
        print()
        
    else: print("\n Tidak ada penyakit yang cocok.")