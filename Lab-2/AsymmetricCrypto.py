from typing import Tuple, List, Optional
from keypair import KeyPair
from PrimeGenerator import PrimeGenerator
from MathUtils import MathUtils

class AsymmetricCrypto:
    """
    Classe principale pour la cryptographie asymétrique.

    Attributes:
        key_size (int): La taille des clés (en bits), par défaut 1024.
        key_pair (Optional[KeyPair]): La paire de clés générée.
    """

    
    def __init__(self, key_size: int = 1024):
        self.key_size = key_size
        self.key_pair: Optional[KeyPair] = None

    def generate_keys(self) -> KeyPair:
        """
        Génère une nouvelle paire de clés.

        Returns:
            KeyPair: Un objet contenant la clé publique (e, n) et la clé privée (d, n).
        """

        # Génère deux grands nombres premiers distincts
        p = PrimeGenerator.generate_prime(self.key_size // 2)
        q = PrimeGenerator.generate_prime(self.key_size // 2)
        while p == q:
            q = PrimeGenerator.generate_prime(self.key_size // 2)
        
        n = p * q
        phi = (p - 1) * (q - 1)
        
        # Optimisation: utilise des exposants de chiffrement courants
        e = 65537  # Nombre de Fermat F4
        
        # Calcul de d avec l'algorithme d'Euclide étendu
        _, d, _ = MathUtils.extended_gcd(e, phi)
        d = d % phi
        if d < 0:
            d += phi
        
        self.key_pair = KeyPair(public_key=(e, n), private_key=(d, n))
        return self.key_pair

    def _optimize_message_blocks(self, message: str, n: int) -> List[int]:
        """Optimise le découpage du message en blocs"""
        block_size = (n.bit_length() - 1) // 8
        message_bytes = message.encode('utf-8')
        blocks = []
        
        for i in range(0, len(message_bytes), block_size):
            block = message_bytes[i:i + block_size]
            block_int = int.from_bytes(block, 'big')
            blocks.append(block_int)
        
        return blocks

    def encrypt(self, message: str, public_key: Optional[Tuple[int, int]] = None) -> List[int]:
        """Chiffre le message avec la clé publique"""
        if public_key is None and self.key_pair is None:
            raise ValueError("No public key available. Generate keys first.")
        
        key_to_use = public_key or self.key_pair.public_key
        e, n = key_to_use
        blocks = self._optimize_message_blocks(message, n)
        
        return [pow(block, e, n) for block in blocks]

    def decrypt(self, encrypted_blocks: List[int], private_key: Optional[Tuple[int, int]] = None) -> str:
        """Déchiffre le message avec la clé privée"""
        if private_key is None and self.key_pair is None:
            raise ValueError("No private key available. Generate keys first.")
        
        key_to_use = private_key or self.key_pair.private_key
        d, n = key_to_use
        
        decrypted_blocks = []
        for block in encrypted_blocks:
            decrypted_int = pow(block, d, n)
            block_size = (decrypted_int.bit_length() + 7) // 8
            decrypted_bytes = decrypted_int.to_bytes(block_size, 'big')
            decrypted_blocks.append(decrypted_bytes)
        
        try:
            return b''.join(decrypted_blocks).decode('utf-8')
        except UnicodeDecodeError:
            return "Erreur de déchiffrement"

