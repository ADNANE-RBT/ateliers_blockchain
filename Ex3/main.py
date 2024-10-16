from Block import Block
from BlockChain import Blockchain
from POS import ProofOfStake
import time

def main():
    blockchain = Blockchain()

    # Sample data for new blocks
    data = "Some transaction data"

    # Difficulty levels for PoW
    difficulty = 4

    # Validators and their stakes for PoS
    validators = {
        "Validator_A": 100,
        "Validator_B": 50,
        "Validator_C": 30
    }
    pos_validator = ProofOfStake(validators)

    # Proof of Work (PoW)
    print("Proof of Work (PoW) Test:")
    pow_block = Block(index=len(blockchain.chain),
                      previous_hash=blockchain.get_last_block().hash,
                      data=data,
                      timestamp=time.time())
    pow_time = blockchain.add_block_pow(pow_block, difficulty)
    print(f"Block mined with PoW in {pow_time:.4f} seconds")
    print(f"Hash: {pow_block.hash}\n")

    # Proof of Stake (PoS)
    print("Proof of Stake (PoS) Test:")
    pos_block = Block(index=len(blockchain.chain),
                      previous_hash=blockchain.get_last_block().hash,
                      data=data,
                      timestamp=time.time())
    pos_time = blockchain.add_block_pos(pos_block, pos_validator)
    print(f"Block validated with PoS in {pos_time:.4f} seconds")
    print(f"Hash: {pos_block.hash}\n")

    # Chain validation
    if blockchain.is_chain_valid():
        print("Blockchain is valid.")
    else:
        print("Blockchain is not valid.")

if __name__ == "__main__":
    main()
