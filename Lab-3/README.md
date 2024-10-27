# Neural-Inspired Hash Function 

## Overview
The Neural-Inspired Hash Function is a novel approach to cryptographic hashing that combines neural network principles with traditional hashing techniques. It creates a fixed-size hash output from variable-length input text using a multi-layer neural network architecture.

## Architecture

### Components
1. **NeuralLayer Class**
   - Handles individual neural network layers
   - Implements weights, biases, and ReLU activation
   - Performs forward propagation through the layer

2. **NeuralHash Class**
   - Main hash function implementation
   - Manages the neural network architecture
   - Handles input preprocessing and final hash generation

3. **HashTester Class**
   - Provides testing utilities for hash function properties
   - Tests determinism, uniqueness, fixed length output, and speed

### Default Configuration
- Input size: 256 neurons (255 for input + 1 for salt)
- Hidden layers: [128, 64, 32] neurons
- Output size: 16 neurons
- Final hash length: 32 characters (128 bits)

## Process Flow

### Input Processing
1. Text input is converted to ASCII values
2. Values are padded/truncated to match input size
3. Salt is added for additional security
4. Input is normalized to range [0, 1]

### Neural Network Processing
1. Forward propagation through multiple layers
2. ReLU activation between layers
3. Final layer produces fixed-size output

### Hash Generation
1. Neural network output is transformed
2. XOR operation with salt-based mask
3. Final SHA-256 transformation
4. Truncation to 32 characters
