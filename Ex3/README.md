
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

### **main.py** - Executing Proof of Stake (PoS) and Proof of Work (PoW)

1. **Main Function**:
   - The `main.py` file is the entry point for testing both Proof of Work (PoW) and Proof of Stake (PoS) mechanisms on the blockchain.
   - **PoW Test**:
     - A new block is added to the blockchain using PoW.
     - The difficulty level for mining the block is specified (e.g., `difficulty = 4`), which means the hash must have four leading zeros.
     - The time taken to mine the block is calculated and printed.
   
   - **PoS Test**:
     - The validators and their respective stakes are defined.
     - A block is added to the blockchain using the PoS mechanism, and a validator is randomly selected based on the stakes to validate the block.
     - The time taken for the validation process is calculated and printed.
   
   - **Blockchain Validation**:
     - After the blocks are added using both PoW and PoS, the blockchain is validated to check if the chain is valid, meaning that all blocks are correctly linked and the hash integrity is maintained.

---

### **Code Execution**:
- When you run `main.py`, it will first test the PoW mechanism by creating and mining a block with the specified difficulty level.
- Then, the PoS mechanism will be tested by selecting a validator based on stakes and validating a block.
- The execution time for both PoW and PoS is printed for comparison.
- Finally, the blockchain is validated to ensure the chain’s integrity. 

