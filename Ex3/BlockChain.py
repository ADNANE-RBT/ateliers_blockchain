import time
from Block import Block
from POS import ProofOfStake

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    # créer le bloc de genèse
    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block", time.time())

    # récupérer le dernier bloc de la chaîne
    def get_last_block(self):
        return self.chain[-1]

    # ajouter un nouveau bloc à la chaîne  
    def add_block_pow(self, new_block, difficulty):
        new_block.previous_hash = self.get_last_block().hash
        execution_time = new_block.proof_of_work(difficulty)
        self.chain.append(new_block)
        return execution_time

    def add_block_pos(self, new_block, pos_validator):
        new_block.previous_hash = self.get_last_block().hash
        execution_time = pos_validator.validate_block(new_block, pos_validator.select_validator())
        self.chain.append(new_block)
        return execution_time

    #  vérifier la validité de la chaîne
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.compute_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True
