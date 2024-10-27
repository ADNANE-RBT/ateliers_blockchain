import numpy as np
from typing import List
import hashlib
from NeuralLayer import NeuralLayer

class NeuralHash:
    def __init__(self, input_size: int = 256, hidden_sizes: List[int] = [128, 64, 32], 
                 output_size: int = 16, seed: int = 42):
        """Initialize the Neural Hash function with specified architecture."""
        self.input_size = input_size - 1  # Reserve one spot for salt
        self.output_size = output_size
        self.seed = seed
        
        # Initialize layers
        layer_sizes = [input_size] + hidden_sizes + [output_size]
        self.layers = []
        for i in range(len(layer_sizes) - 1):
            self.layers.append(NeuralLayer(layer_sizes[i], layer_sizes[i+1], seed + i))

        # Initialize salt generator
        np.random.seed(seed)
        self.salt = np.random.randint(0, 2**16, dtype=np.int32)

    def preprocess_input(self, text: str) -> np.ndarray:
        """Convert input text to numeric vector and pad/truncate as needed."""
        try:
            # Convert text to ASCII values
            ascii_values = np.array([ord(c) for c in text], dtype=np.float32)
            
            # Pad or truncate to match input_size (leaving room for salt)
            if len(ascii_values) < self.input_size:
                padding = np.zeros(self.input_size - len(ascii_values))
                ascii_values = np.concatenate([ascii_values, padding])
            else:
                ascii_values = ascii_values[:self.input_size]
            
            # Add salt as the last element
            salt_array = np.array([self.salt], dtype=np.float32)
            final_input = np.concatenate([ascii_values, salt_array])
            
            # Normalize the input
            final_input = final_input / 255.0 
            # Normalize ASCII values to [0, 1]
            
            return final_input

        except Exception as e:
            raise ValueError(f"Error preprocessing input: {str(e)}")

    def forward_pass(self, inputs: np.ndarray) -> np.ndarray:
        """Process input through all neural layers."""
        try:
            x = inputs
            for layer in self.layers:
                x = layer.forward(x)
            return x
        except Exception as e:
            raise ValueError(f"Error in forward pass: {str(e)}")

    def final_transform(self, output: np.ndarray) -> bytes:
        """Apply final transformation to ensure irreversibility."""
        try:
            # Convert output to bytes
            output_bytes = output.tobytes()
            
            # Create a mask using SHA-256 of the salt
            salt_bytes = str(self.salt).encode()
            mask_bytes = hashlib.sha256(salt_bytes).digest()[:len(output_bytes)]
            
            # XOR the bytes
            result = bytes(a ^ b for a, b in zip(output_bytes, mask_bytes))
            
            return result
        except Exception as e:
            raise ValueError(f"Error in final transform: {str(e)}")

    def hash(self, text: str) -> str:
        """Generate hash for input text."""
        try:
            if not isinstance(text, str):
                raise ValueError("Input must be a string")

            # Preprocess input
            inputs = self.preprocess_input(text)
            
            # Forward pass through neural layers
            output = self.forward_pass(inputs)
            
            # Final transformation
            transformed = self.final_transform(output)
            
            # Generate final hash
            return hashlib.sha256(transformed).hexdigest()[:32]  # 32 characters (128 bits)
        except Exception as e:
            raise ValueError(f"Error generating hash: {str(e)}")
