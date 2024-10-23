### **blockfile.py** - Block and Blockchain Classes

1. **`Block` Class**:
   - **Attributes**:
     - `index`: Position of the block in the chain.
     - `previous_hash`: Hash of the previous block in the chain, ensuring the blocks are linked.
     - `data`: Information stored in the block, like transaction data.
     - `timestamp`: Time when the block was created.
     - `nonce`: A number that is incremented during the proof of work to find a valid hash.
     - `hash`: The cryptographic hash of the block’s content, calculated using the `compute_hash` method.
   
   - **Methods**:
     - `compute_hash`: Combines the block’s attributes (index, previous hash, data, timestamp, and nonce) into a single string, hashes it using SHA-256, and returns the resulting hash.
     - `proof_of_work`: This method attempts to find a hash that starts with a specified number of leading zeros (determined by `difficulty`). It adjusts the `nonce` value repeatedly until the correct hash is found, and returns the time taken to complete the operation.

2. **`Blockchain` Class**:
   - **Attributes**:
     - `chain`: A list that stores the sequence of blocks in the blockchain. The first block is the genesis block, created when the chain is initialized.
   
   - **Methods**:
     - `create_genesis_block`: Generates the first block (genesis block) in the blockchain with index 0, a hardcoded previous hash of `"0"`, and a default data message ("Genesis Block").
     - `get_last_block`: Retrieves the most recent block in the blockchain.
     - `add_block`: Adds a new block to the blockchain. Before adding the block, it runs the `proof_of_work` method to compute the valid hash based on the current difficulty level.
     - `is_chain_valid`: Verifies the integrity of the blockchain. It ensures that every block’s hash matches the recomputed hash and that each block’s `previous_hash` matches the hash of the preceding block.

---

### **main.py** - Executing the Blockchain and Proof of Work

1. **Main Function**:
   - In the `main.py` file, the blockchain is instantiated, and multiple blocks are mined with different levels of difficulty.
   - **Difficulty Levels**: A list of difficulty levels is specified (`[2, 3, 4, 5]`), where the difficulty indicates the number of leading zeros required in the block’s hash.
   
   - **Block Addition**: For each difficulty level, a new block is created, and the time required to mine the block (i.e., to find the correct hash) is measured and printed.
   
   - **Blockchain Validation**: After adding all blocks, the blockchain is validated to check whether the integrity of the chain has been maintained.

---

### Code Execution:
- When you run `main.py`, the blockchain starts by creating the genesis block.
- For each subsequent block, the difficulty level increases, making it progressively harder to mine the block (i.e., to find a hash with the required number of leading zeros).
- The output will show the time taken to mine each block at different difficulty levels.
- Finally, the blockchain is validated to ensure that all blocks are correctly linked and the data integrity is maintained.

