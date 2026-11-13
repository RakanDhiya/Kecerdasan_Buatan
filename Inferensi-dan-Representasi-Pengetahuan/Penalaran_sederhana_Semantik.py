semantic_network = {
    "Kucing": {
        "adalah": ["Hewan"],
        "memiliki": ["Bulu", "Kumis"],
        "makan": ["Ikan", "Daging"],
    },
    "Hewan": {"bernapas": ["Oksigen"], "bergerak": True},
    "Ikan": {"adalah": ["Hewan"], "hidup_di": ["Air"]},
}

def memiliki_sifat(node, sifat):
    """
    Mengecek apakah node memiliki sifat tertentu,
    termasuk sifat yang diwarisi dari parent.
    """

    if node not in semantic_network:
        return False

    # Cek sifat secara langsung
    if sifat in semantic_network[node]:
        return True

    # Cari parent melalui relasi 'adalah'
    parent_nodes = semantic_network[node].get("adalah", [])

    # Cek sifat parent
    for parent in parent_nodes:
        if memiliki_sifat(parent, sifat):
            return True

    return False\

def tanya(subjek, sifat):
    """Mengajukan pertanyaan kepada jaringan semantik."""
    return memiliki_sifat(subjek, sifat)

# Pertanyaan
hasil = tanya("Kucing", "bernapas")

print("Kucing bernapas?", hasil)
