from NeuralHash import NeuralHash as NH
from HashTester import HashTester as HT


if __name__ == "__main__":
    try:
        # Initialize the hasher, the input array as well as the layers of the nn
        hasher = NH()
        
        # Tests of the data
        test_inputs = [
            "Hello, World!",
            "Neural Hash",
            "This is a test",
            "Different input",
            "Different input",
            "Very different input"
        ]
        
        # Run tests
        print("Running tests...")
        print(f"Determinism Test: {HT.test_determinism(hasher, test_inputs[0])}")
        print(f"Uniqueness Test: {HT.test_uniqueness(hasher, test_inputs)}")
        print(f"Fixed Length Test: {HT.test_fixed_length(hasher, test_inputs)}")
        print(f"Average Speed (seconds): {HT.test_speed(hasher, test_inputs[0]):.6f}")
        
        # Display the example hashes
        print("\nExample Hashes:")
        for text in test_inputs[:]:
            print(f"Input: {text}")
            print(f"Hash: {hasher.hash(text)}\n")
    except Exception as e:
        print(f"Test suite failed: {str(e)}")
