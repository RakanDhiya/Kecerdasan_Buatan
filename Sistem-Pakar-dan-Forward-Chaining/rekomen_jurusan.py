# REKOMENDASI JURUSAN KULIAH

rules = [
    {
        "if": ["suka_logika", "suka_coding", "matematika_tinggi"],
        "then": "Teknik Informatika",
        "desc": "Cocok untuk yang suka pemrograman & algoritma",
    },
    {
        "if": ["suka_biologi", "suka_menolong", "ipa_tinggi"],
        "then": "Kedokteran",
        "desc": "Cocok untuk yang peduli kesehatan",
    },
    {
        "if": ["suka_organisasi", "suka_hitung", "ekonomi_tinggi"],
        "then": "Manajemen",
        "desc": "Cocok untuk yang suka memimpin & bisnis",
    },
    {
        "if": ["suka_seni", "kreatif", "suka_visual"],
        "then": "Desain Komunikasi Visual",
        "desc": "Cocok untuk yang kreatif & visual",
    },
]

def forward_chaining(fakta):
    return [r for r in rules if all(g in fakta for g in r["if"])]

print("=" * 60)
print(" SISTEM PAKAR REKOMENDASI JURUSAN KULIAH")
print("=" * 60)

print("\nPilih minat Anda (boleh lebih dari satu).")
print("Ketik nomor, pisahkan dengan koma. " "Contoh: 1,3,5\n")

opsi = [
    ("suka_logika", "Suka berpikir logis"),
    ("suka_coding", "Suka ngoding/programming"),
    ("matematika_tinggi", "Nilai matematika tinggi"),
    ("suka_biologi", "Suka pelajaran biologi"),
    ("suka_menolong", "Suka menolong orang"),
    ("ipa_tinggi", "Nilai IPA tinggi"),
    ("suka_organisasi", "Suka berorganisasi"),
    ("suka_hitung", "Suka menghitung/akuntansi"),
    ("ekonomi_tinggi", "Nilai ekonomi tinggi"),
    ("suka_seni", "Suka seni & estetika"),
    ("kreatif", "Merasa diri kreatif"),
    ("suka_visual", "Suka hal-hal visual"),
]

for i, (_, label) in enumerate(opsi, 1):
    print(f" {i:2d}. {label}")

pilihan = input("\nMasukkan pilihan Anda: ")
index_pilihan = [int(x.strip()) - 1 for x in pilihan.split(",") if x.strip().isdigit()]
fakta = [opsi[i][0] for i in index_pilihan if 0 <= i < len(opsi)]

print("\n" + "=" * 60)
print(" HASIL REKOMENDASI JURUSAN")
print("=" * 60)

print("\nMinat Anda:")

for f in fakta:
    print(f" ✓ {f.replace('_', ' ').title()}")

hasil = forward_chaining(fakta)
if hasil:
    print("\n" + "-" * 60)
    for h in hasil:
        print(f"\n★ Jurusan: {h['then']}")
        print(f" Alasan : {h['desc']}")
        print(f" Syarat : {', '.join(h['if'])}")
else:
    print("\n Tidak ada jurusan yang cocok dengan minat Anda.")
    print(" Coba tambahkan minat lain.")