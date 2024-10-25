from typing import Tuple

class MathUtils:
    """Math utility functions including extended GCD"""
    
    @staticmethod
    def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
        """Extended Euclidean Algorithm to find the modular inverse"""
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = MathUtils.extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y


