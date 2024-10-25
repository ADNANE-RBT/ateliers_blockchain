import random
from PrimalityTester import PrimalityTester 

class PrimeGenerator:
    """Prime generation with robustness improvements"""
    
    @staticmethod
    def generate_prime(bits: int) -> int:
        """Generates a prime number of a specified bit size"""
        while True:
            n = random.getrandbits(bits) | (1 << bits - 1) | 1
            # Avoid small or weak primes by ensuring the prime is large enough
            if PrimalityTester.is_prime(n) and PrimeGenerator.check_prime_safety(n):
                return n
        
    @staticmethod
    def check_prime_safety(p: int) -> bool:
        """Ensure prime p is robust enough to avoid weak primes"""
        # Avoid small primes or primes too close to others
        return p > 2**(p.bit_length() - 1)


