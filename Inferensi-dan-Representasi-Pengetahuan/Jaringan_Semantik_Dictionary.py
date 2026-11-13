semantic_network = {
    "Kucing": {
        "adalah": ["Hewan"],
        "memiliki": ["Bulu", "Kumis"],
        "makan": ["Ikan", "Daging"],
    },
    "Hewan": {"bernapas": ["Oksigen"], "bergerak": True},
    "Ikan": {"adalah": ["Hewan"], "hidup_di": ["Air"]},
}

def cari_relasi(node, relasi):
    """Mencari objek berdasarkan node dan relasinya."""
    if node in semantic_network:
        if relasi in semantic_network[node]:
            return semantic_network[node][relasi]

    return "Tidak ditemukan"

# Query
print("Kucing adalah:", cari_relasi("Kucing", "adalah"))
print("Kucing makan:", cari_relasi("Kucing", "makan"))
print("Ikan hidup di:", cari_relasi("Ikan", "hidup_di"))
