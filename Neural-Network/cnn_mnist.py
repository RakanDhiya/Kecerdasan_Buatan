import torch
import torch.nn as nn
import torch.optim as optim

from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# Persiapan dataset
transform = transforms.Compose(
    [transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))]
)

train_data = datasets.MNIST(
    root="./data", train=True, download=True, transform=transform
)

train_loader = DataLoader(train_data, batch_size=64, shuffle=True)

# Membuat arsitektur CNN
class CNN(nn.Module):
    def __init__(self):
        super().__init__()

        self.conv1 = nn.Conv2d(1, 16, 3, padding=1)
        self.conv2 = nn.Conv2d(16, 32, 3, padding=1)

        self.pool = nn.MaxPool2d(2, 2)

        self.fc1 = nn.Linear(32 * 7 * 7, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))
        x = self.pool(torch.relu(self.conv2(x)))

        x = x.view(-1, 32 * 7 * 7)

        x = torch.relu(self.fc1(x))
        x = self.fc2(x)

        return x

# Konfigurasi model
model = CNN()

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Proses training
model.train()

for batch_index, (images, labels) in enumerate(train_loader):
    optimizer.zero_grad()

    prediction = model(images)
    loss = criterion(prediction, labels)

    loss.backward()
    optimizer.step()

    if batch_index % 200 == 0:
        print(f"Batch {batch_index}, " f"Loss: {loss.item():.4f}")

print("Pelatihan selesai.")