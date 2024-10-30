
### **block.py** - Block Class

1. **`Block` Class**:
   - **Attributes**:
     - `index`: Position of the block in the chain.
     - `previous_hash`: Hash of the previous block in the chain, ensuring the blocks are linked.
     - `data`: Information stored in the block, such as transaction data.
     - `timestamp`: Time when the block was created.
     - `nonce`: A number that is incremented during the Proof of Work (PoW) to find a valid hash.
     - `hash`: The cryptographic hash of the block’s content, calculated using the `compute_hash` method.
   
   - **Methods**:
     - `compute_hash`: Combines the block’s attributes (index, previous hash, data, timestamp, and nonce) into a single string, hashes it using SHA-256, and returns the resulting hash.
     - `proof_of_work`: Tries to find a hash that starts with a specified number of leading zeros (`difficulty`). Adjusts the `nonce` value repeatedly until the correct hash is found, and returns the time taken to complete this operation.

---

### **pos.py** - Proof of Stake Class

1. **`ProofOfStake` Class**:
   - **Attributes**:
     - `validators`: A dictionary that maps each validator to their respective stake (amount of cryptocurrency held).
   
   - **Methods**:
     - `select_validator`: Randomly selects a validator based on their stake proportion. The more stake a validator has, the higher their probability of being selected to validate a block.
     - `validate_block`: Once a validator is selected, this method validates the block by computing its hash and returns the time taken to validate the block.

---

### **blockchain.py** - Blockchain Class

1. **`Blockchain` Class**:
   - **Attributes**:
     - `chain`: A list that stores the sequence of blocks in the blockchain. The first block is the genesis block, created when the chain is initialized.
   
   - **Methods**:
     - `create_genesis_block`: Creates the first block (genesis block) in the blockchain with index `0`, a default previous hash of `"0"`, and a default data message ("Genesis Block").
     - `get_last_block`: Retrieves the most recent block in the blockchain.
     - `add_block_pow`: Adds a new block using the Proof of Work (PoW) mechanism. It sets the previous hash of the new block, then runs the `proof_of_work` method on the block with a given difficulty, and finally appends the block to the chain.
     - `add_block_pos`: Adds a new block using the Proof of Stake (PoS) mechanism. The `ProofOfStake` class selects a validator to validate the block. The block’s hash is then computed, and the block is appended to the chain.
     - `is_chain_valid`: Ensures that each block in the blockchain is correctly linked by validating that every block’s `hash` matches its computed hash and that each block’s `previous_hash` matches the hash of the preceding block.

---
Here’s the refactored documentation:

---

### **main.py** 

The `main.py` file orchestrates the testing of two consensus mechanisms—**Proof of Work (PoW)** and **Proof of Stake (PoS)**—on a blockchain. The script initializes a blockchain, tests both mechanisms by adding new blocks, records the execution times, and verifies the chain’s validity.

---

### Components of `main.py`

#### **1. Main Function**:
The main function executes tests for both PoW and PoS, records performance, and validates the blockchain.

- **Initialize Blockchain and Tester**:
  - An instance of `BlockchainTester` is created to handle PoW and PoS tests on the blockchain, along with sample transaction data.

- **PoW Testing**:
  - PoW is tested by creating new blocks and setting a range of difficulty levels (e.g., `[2, 4, 6]`).
  - Each block is mined to meet the specified difficulty by solving a cryptographic puzzle.
  - Execution time for each difficulty level is recorded and saved in `pow_results.csv` for comparison.

- **PoS Testing**:
  - PoS is tested with a set of validators and their stakes (e.g., `{"Validator_A": 100, "Validator_B": 50}`).
  - Blocks are added to the blockchain by randomly selecting validators based on their stakes to simulate validation.
  - Execution times are recorded for PoS validation rounds and saved in `pos_results.csv`.

- **Blockchain Validation**:
  - Once PoW and PoS blocks are added, the blockchain’s integrity is checked.
  - The function verifies that each block’s hash correctly links to the previous one, ensuring chain validity.

---

### **Code Execution**:
- **Running `main.py`**:
  - Tests PoW across varying difficulties and PoS with assigned stakes, recording the execution time for both.
  - Saves results to separate CSV files for PoW and PoS (`pow_results.csv` and `pos_results.csv`).
  - Prints whether the blockchain is valid based on the hash integrity of each block in the chain.

