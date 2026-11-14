import torch
import torch.nn as nn
import torch.optim as optim

# Data training
X = torch.tensor([[1.0], [2.0], [3.0], [4.0]])
target = torch.tensor([[3.0], [5.0], [7.0], [9.0]])

# Membuat model
model = nn.Linear(1, 1)

criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Proses training
for epoch in range(200):
    optimizer.zero_grad()

    prediction = model(X)
    loss = criterion(prediction, target)

    loss.backward()
    optimizer.step()

# Prediksi data baru
with torch.no_grad():
    test_data = torch.tensor([[5.0]])
    result = model(test_data)

    print(f"Prediksi x=5: {result.item():.2f}")