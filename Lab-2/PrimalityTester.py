import random

class PrimalityTester:
    """Classe pour les tests de primalité"""
    
    @staticmethod
    def is_prime(n: int, k: int = 5) -> bool:
        """Test de primalité de Miller-Rabin optimisé"""
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False

        # Écrire n-1 sous la forme d * 2^r
        r, d = 0, n - 1
        while d % 2 == 0:
            r += 1
            d //= 2

        # Test k fois
        for _ in range(k):
            a = random.randrange(2, n - 1)
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(r - 1):
                x = (x * x) % n
                if x == n - 1:
                    break
            else:
                return False
        return True
