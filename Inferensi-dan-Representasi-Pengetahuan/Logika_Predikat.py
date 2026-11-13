def diagnosa(gejala):
    """Menentukan kemungkinan penyakit berdasarkan gejala."""

    if "demam" in gejala and "batuk" in gejala:
        return "Kemungkinan Flu"

    if "demam" in gejala and "ruam" in gejala:
        return "Kemungkinan DBD"

    if "pusing" in gejala and "mual" in gejala:
        return "Kemungkinan Maag"

    return "Tidak terdeteksi"


# Input pengguna
gejala_user = ["demam", "batuk", "pilek"]

# Proses diagnosis
hasil = diagnosa(gejala_user)

# Output
print(f"Gejala: {gejala_user}")
print(f"Diagnosa: {hasil}")
