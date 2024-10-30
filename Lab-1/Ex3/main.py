from Block import Block
from BlockChain import Blockchain
from POS import ProofOfStake
import time

def main():
    blockchain = Blockchain()

    # Sample data for new blocks
    data = "Some transaction data"

    # Test different difficulty levels for PoW
    print("Testing Proof of Work (PoW) with varying difficulties:")
    for difficulty in [2, 4, 6]:
        pow_block = Block(index=len(blockchain.chain),
                          previous_hash=blockchain.get_last_block().hash,
                          data=data,
                          timestamp=time.time())
        pow_time = blockchain.add_block_pow(pow_block, difficulty)
        print(f"Block mined with PoW difficulty {difficulty} in {pow_time:.4f} seconds")
        print(f"Hash: {pow_block.hash}")
        print()

    # Test Proof of Stake (PoS) with different validator stakes
    print("Testing Proof of Stake (PoS) with varying validator stakes:")
    validators = {
        "Validator_A": 100,
        "Validator_B": 50,
        "Validator_C": 30,
        "Validator_D": 20,
        "Validator_E": 10
    }
    pos_validator = ProofOfStake(validators)

    for _ in range(3):
        pos_block = Block(index=len(blockchain.chain),
                          previous_hash=blockchain.get_last_block().hash,
                          data=data,
                          timestamp=time.time())
        pos_time = blockchain.add_block_pos(pos_block, pos_validator)
        print(f"Block validated with PoS in {pos_time:.4f} seconds")
        print(f"Hash: {pos_block.hash}")
        print()

    # Chain validation
    if blockchain.is_chain_valid():
        print("Blockchain is valid.")
    else:
        print("Blockchain is not valid.")

if __name__ == "__main__":
    main()