import numpy as np
from typing import List
import time
from NeuralHash import NeuralHash


class HashTester:
    @staticmethod
    def test_determinism(hasher: NeuralHash, input_text: str) -> bool:
        """Test if the hash function produces the same output for the same input."""
        try:
            hash1 = hasher.hash(input_text)
            hash2 = hasher.hash(input_text)
            return hash1 == hash2
        except Exception as e:
            print(f"Determinism test failed: {str(e)}")
            return False

    @staticmethod
    def test_uniqueness(hasher: NeuralHash, inputs: List[str]) -> bool:
        """Test if different inputs produce different hashes."""
        try:
            hashes = set()
            for text in inputs:
                hash_value = hasher.hash(text)
                if hash_value in hashes:
                    return False
                hashes.add(hash_value)
            return True
        except Exception as e:
            print(f"Uniqueness test failed: {str(e)}")
            return False

    @staticmethod
    def test_fixed_length(hasher: NeuralHash, inputs: List[str]) -> bool:
        """Test if all inputs produce hashes of the same length."""
        try:
            lengths = set()
            for text in inputs:
                hash_value = hasher.hash(text)
                lengths.add(len(hash_value))
            return len(lengths) == 1
        except Exception as e:
            print(f"Fixed length test failed: {str(e)}")
            return False

    @staticmethod
    def test_speed(hasher: NeuralHash, input_text: str, iterations: int = 1000) -> float:
        """Test the speed of the hash function."""
        try:
            start_time = time.time()
            for _ in range(iterations):
                hasher.hash(input_text)
            end_time = time.time()
            return (end_time - start_time) / iterations
        except Exception as e:
            print(f"Speed test failed: {str(e)}")
            return float('inf')
