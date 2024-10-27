import numpy as np

class NeuralLayer:
    def __init__(self, input_size: int, output_size: int, seed: int):
        """Initialize a neural network layer with weights and biases."""
        np.random.seed(seed)
        self.weights = np.random.randn(input_size, output_size) * 0.01
        self.biases = np.random.randn(output_size) * 0.01

    def forward(self, inputs: np.ndarray) -> np.ndarray:
        """Forward pass through the layer."""
        weighted_sum = np.dot(inputs, self.weights) + self.biases
        return self.relu(weighted_sum)

    @staticmethod
    def relu(x: np.ndarray) -> np.ndarray:
        """ReLU activation function."""
        return np.maximum(0, x)
