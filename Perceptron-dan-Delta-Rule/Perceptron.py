import numpy as np

class Perceptron:
    def __init__(self, learning_rate=0.1, epochs=100):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = None
        self.bias = 0

    def activation(self, net):
        return 1 if net >= 0.5 else 0

    def fit(self, X, target):
        _, n_features = X.shape

        self.weights = np.zeros(n_features)
        self.bias = 0

        for epoch in range(self.epochs):
            errors = 0

            for x, expected in zip(X, target):
                net = np.dot(self.weights, x) + self.bias
                prediction = self.activation(net)

                if prediction != expected:
                    update = self.learning_rate * (
                        expected - prediction
                    )

                    self.weights += update * x
                    self.bias += update
                    errors += 1

            if errors == 0:
                print(f"Konvergen pada epoch {epoch + 1}")
                break

    def predict(self, X):
        return np.array([
            self.activation(np.dot(self.weights, x) + self.bias)
            for x in X
        ])


# Data training gerbang AND
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

target = np.array([0, 0, 0, 1])

# Training
model = Perceptron(learning_rate=0.1, epochs=100)
model.fit(X, target)

# Hasil prediksi
prediction = model.predict(X)

print("Bobot akhir:", model.weights)
print("Bias:", model.bias)
print("Hasil prediksi:", prediction)
print("Target:", target)