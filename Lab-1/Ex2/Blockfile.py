import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data, timestamp):
        self.index = index
        self.previous_hash = previous_hash
        self.data = data
        self.timestamp = timestamp
        self.nonce = 0  
        self.hash = self.compute_hash()

    # calculer le hash du bloc
    def compute_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.data}{self.timestamp}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    # effectuer le Proof of Work
    def proof_of_work(self, difficulty):
        # Le hash doit commencer par 'difficulty' zéros
        start_time = time.time()
        while not self.hash.startswith('0' * difficulty):
            self.nonce += 1
            self.hash = self.compute_hash()
        end_time = time.time()
        execution_time = end_time - start_time
        return execution_time


class Blockchain:
    def __init__(self):
        # La chaîne commence par le bloc de genèse (premier bloc)
        self.chain = [self.create_genesis_block()]

    # Fonction pour créer le bloc de genèse
    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block", time.time())

    # Fonction pour récupérer le dernier bloc de la chaîne
    def get_last_block(self):
        return self.chain[-1]

    # Fonction pour ajouter un nouveau bloc à la chaîne
    def add_block(self, new_block, difficulty):
        new_block.previous_hash = self.get_last_block().hash
        execution_time = new_block.proof_of_work(difficulty)
        self.chain.append(new_block)
        return execution_time

    # Fonction pour vérifier la validité de la chaîne
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Vérifie si le hash du bloc actuel est correct
            if current_block.hash != current_block.compute_hash():
                return False

            # Vérifie si le hash du bloc précédent est correct
            if current_block.previous_hash != previous_block.hash:
                return False
        return True
