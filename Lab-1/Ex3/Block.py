import hashlib
import time

class Block:
    """
    Represents a single unit of data in the blockchain. Each Block object stores:

    index: Position in the blockchain.
    previous_hash: Hash of the previous block to ensure continuity.
    data: The information stored in the block, e.g., transaction details.
    timestamp: Creation time.
    """
    def __init__(self, index, previous_hash, data, timestamp):
        self.index = index
        self.previous_hash = previous_hash
        self.data = data
        self.timestamp = timestamp
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.data}{self.timestamp}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def proof_of_work(self, difficulty):
        start_time = time.time()
        while not self.hash.startswith('0' * difficulty):
            self.nonce += 1
            self.hash = self.compute_hash()
        end_time = time.time()
        return end_time - start_time