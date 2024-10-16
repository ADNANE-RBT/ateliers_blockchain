from Blockfile import Blockchain
from Blockfile import Block
import time


def main():
    blockchain = Blockchain()

    data = "Some transaction data"
    difficulty_levels = [2, 3, 4, 5]  # Niveaux de difficulté
    for difficulty in difficulty_levels:
        new_block = Block(index=len(blockchain.chain),
                          previous_hash=blockchain.get_last_block().hash,
                          data=data,
                          timestamp=time.time())
        print(f"\nMining block with difficulty level {difficulty}...")
        execution_time = blockchain.add_block(new_block, difficulty)
        print(f"Block mined with hash: {new_block.hash}")
        print(f"Time taken: {execution_time:.4f} seconds")

    if blockchain.is_chain_valid():
        print("\nBlockchain is valid.")
    else:
        print("\nBlockchain is not valid.")

if __name__ == "__main__":
    main()
