import torch
import torch.nn as nn
import torch.optim as optim

# Data training XOR
X = torch.tensor([
    [0.0, 0.0],
    [0.0, 1.0],
    [1.0, 0.0],
    [1.0, 1.0]
])

target = torch.tensor([
    [0.0],
    [1.0],
    [1.0],
    [0.0]
])

# Membuat arsitektur MLP
model = nn.Sequential(
    nn.Linear(2, 8),
    nn.ReLU(),
    nn.Linear(8, 1),
    nn.Sigmoid()
)

# Konfigurasi training
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# Proses training
for epoch in range(1000):
    optimizer.zero_grad()

    prediction = model(X)
    loss = criterion(prediction, target)

    loss.backward()
    optimizer.step()

# Evaluasi model
with torch.no_grad():
    prediction = model(X)

    print("Hasil Prediksi XOR:")

    for data, result, expected in zip(X, prediction, target):
        print(
            f"{data.tolist()} -> {result.item():.3f} "
            f"(Target: {expected.item():.0f})"
        )