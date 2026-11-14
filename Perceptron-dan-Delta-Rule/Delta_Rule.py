import numpy as np

class DeltaRule:
    def __init__(self, learning_rate=0.05, epochs=500):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = None
        self.bias = 0
        self.history = []

    def fit(self, X, target):
        n_samples, n_features = X.shape

        self.weights = np.zeros(n_features)
        self.bias = 0

        for epoch in range(self.epochs):
            total_error = 0

            for x, expected in zip(X, target):
                net = np.dot(self.weights, x) + self.bias
                prediction = net

                error = expected - prediction

                self.weights += self.learning_rate * error * x

                self.bias += self.learning_rate * error

                total_error += error**2

            mse = 0.5 * total_error / n_samples
            self.history.append(mse)

            if mse < 1e-6:
                print(f"Konvergen pada epoch {epoch + 1}, " f"MSE = {mse:.2e}")
                break

    def predict(self, X):
        return np.array([np.dot(self.weights, x) + self.bias for x in X])


# Data training regresi linear
np.random.seed(42)

X = np.random.randn(20, 2)
target = 2 * X[:, 0] + 3 * X[:, 1] + 1

# Training
model = DeltaRule(learning_rate=0.05, epochs=500)
model.fit(X, target)

# Hasil prediksi
prediction = model.predict(X)

print("Bobot akhir:", model.weights)
print("Bias akhir:", model.bias)
print("Target bobot: [2, 3]")
print("Target bias: 1")
print("MSE akhir:", model.history[-1])