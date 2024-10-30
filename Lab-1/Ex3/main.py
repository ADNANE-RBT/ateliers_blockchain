from Block import Block
from BlockChain import Blockchain
from POS import ProofOfStake
import time
import csv

class BlockchainTester:
    def __init__(self):
        self.blockchain = Blockchain()
        self.data = "Some transaction data"

    def test_pow(self, difficulties):
        results = []
        for difficulty in difficulties:
            pow_block = Block(index=len(self.blockchain.chain),
                              previous_hash=self.blockchain.get_last_block().hash,
                              data=self.data,
                              timestamp=time.time())
            pow_time = self.blockchain.add_block_pow(pow_block, difficulty)
            results.append({
                "Mechanism": "PoW",
                "Difficulty": difficulty,
                "Time": pow_time,
                "Hash": pow_block.hash
            })
        return results

    def test_pos(self, validators):
        pos_validator = ProofOfStake(validators)
        results = []
        for _ in range(3):
            pos_block = Block(index=len(self.blockchain.chain),
                              previous_hash=self.blockchain.get_last_block().hash,
                              data=self.data,
                              timestamp=time.time())
            pos_time = self.blockchain.add_block_pos(pos_block, pos_validator)
            results.append({
                "Mechanism": "PoS",
                "Validators": validators,
                "Time": pos_time,
                "Hash": pos_block.hash
            })
        return results

    def save_results_to_csv(self, filename, results):
        with open(filename, mode='w', newline='') as file:
            fieldnames = list(results[0].keys())
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            for result in results:
                writer.writerow(result)

def main():
    tester = BlockchainTester()

    # Test PoW with different difficulties
    pow_results = tester.test_pow([2, 4, 6])
    tester.save_results_to_csv("pow_results.csv", pow_results)

    # Test PoS with different validator stakes
    validators = {
        "Validator_A": 100,
        "Validator_B": 50,
        "Validator_C": 30,
        "Validator_D": 20,
        "Validator_E": 10
    }
    pos_results = tester.test_pos(validators)
    tester.save_results_to_csv("pos_results.csv", pos_results)

    # Chain validation
    if tester.blockchain.is_chain_valid():
        print("Blockchain is valid.")
    else:
        print("Blockchain is not valid.")

if __name__ == "__main__":
    main()