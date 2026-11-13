import networkx as nx
import matplotlib.pyplot as plt

# Membuat directed graph
graph = nx.DiGraph()

# Format: (subjek, objek, relasi)
relations = [
    ("Kucing", "Hewan", "adalah"),
    ("Kucing", "Bulu", "memiliki"),
    ("Kucing", "Ikan", "makan"),
    ("Hewan", "Oksigen", "bernapas"),
    ("Ikan", "Air", "hidup_di"),
]

# Menambahkan hubungan
for subject, object_, relation in relations:
    graph.add_edge(subject, object_, label=relation)

# Menentukan posisi node
position = nx.spring_layout(graph, seed=42)

# Menggambar graph
nx.draw(
    graph,
    position,
    with_labels=True,
    node_color="lightblue",
    node_size=2000,
    font_size=10,
    arrows=True,
)

# Mengambil label relasi
edge_labels = nx.get_edge_attributes(graph, "label")

# Menampilkan label relasi
nx.draw_networkx_edge_labels(graph, position, edge_labels=edge_labels)


plt.title("Jaringan Semantik Sederhana")
plt.show()
