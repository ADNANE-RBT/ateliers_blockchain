import random
from PrimalityTester import PrimalityTester 

class PrimeGenerator:
    """Classe pour la génération de nombres premiers"""
    
    @staticmethod
    def generate_prime(bits: int) -> int:
        """Génère un nombre premier de la taille spécifiée en bits"""
        while True:
            n = random.getrandbits(bits) | (1 << bits - 1) | 1
            if PrimalityTester.is_prime(n):
                return n
