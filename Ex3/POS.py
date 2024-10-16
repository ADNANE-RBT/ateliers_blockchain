import hashlib
import time
import random

class ProofOfStake:
    def __init__(self, validators):
        self.validators = validators  # A dictionary with validators and their stakes

    # Choose a validator based on their stake
    def select_validator(self):
        total_stake = sum(self.validators.values())
        random_selection = random.uniform(0, total_stake)
        current = 0
        for validator, stake in self.validators.items():
            current += stake
            if current > random_selection:
                return validator

    def validate_block(self, block, validator):
        start_time = time.time()
        block.hash = block.compute_hash()  # In PoS, block is hashed without puzzle-solving
        end_time = time.time()
        return end_time - start_time
