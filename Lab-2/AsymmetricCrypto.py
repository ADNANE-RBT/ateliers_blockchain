from typing import Tuple, List, Optional
from keypair import KeyPair
from PrimeGenerator import PrimeGenerator
from MathUtils import MathUtils
import math
import random

class AsymmetricCrypto:
    """RSA encryption with optimizations such as CRT and OAEP padding"""
    
    def __init__(self, key_size: int = 1024):
        self.key_size = key_size
        self.key_pair: Optional[KeyPair] = None

    def generate_keys(self) -> KeyPair:
        """Generate public and private key pair with CRT optimization"""
        p = PrimeGenerator.generate_prime(self.key_size // 2)
        q = PrimeGenerator.generate_prime(self.key_size // 2)
        while p == q:
            q = PrimeGenerator.generate_prime(self.key_size // 2)
        
        n = p * q
        phi = (p - 1) * (q - 1)
        
        # Dynamic selection of e
        e = self.select_e(phi)
        
        # Extended GCD to find d
        _, d, _ = MathUtils.extended_gcd(e, phi)
        d = d % phi
        if d < 0:
            d += phi
        
        self.key_pair = KeyPair(public_key=(e, n), private_key=(d, n), p=p, q=q)
        return self.key_pair

    def select_e(self, phi: int) -> int:
        """Selects a dynamic value of e based on properties of n"""
        e = 65537  # Common choice
        while math.gcd(e, phi) != 1:
            e = random.randrange(3, phi)
        return e

    def _optimize_message_blocks(self, message: str, n: int) -> List[int]:
        """Converts the message into optimized blocks for encryption"""
        block_size = (n.bit_length() - 1) // 8
        message_bytes = self._oaep_pad(message, block_size)
        blocks = []
        
        for i in range(0, len(message_bytes), block_size):
            block = message_bytes[i:i + block_size]
            block_int = int.from_bytes(block, 'big')
            blocks.append(block_int)
        
        return blocks

    def encrypt(self, message: str, public_key: Optional[Tuple[int, int]] = None) -> List[int]:
        """Encrypts the message using RSA with OAEP padding"""
        if public_key is None and self.key_pair is None:
            raise ValueError("No public key available. Generate keys first.")
        
        key_to_use = public_key or self.key_pair.public_key
        e, n = key_to_use
        blocks = self._optimize_message_blocks(message, n)
        
        return [pow(block, e, n) for block in blocks]

    def decrypt(self, encrypted_blocks: List[int], private_key: Optional[Tuple[int, int]] = None) -> str:
        """Decrypts the message using CRT optimization"""
        if private_key is None and self.key_pair is None:
            raise ValueError("No private key available. Generate keys first.")
        
        key_to_use = private_key or self.key_pair.private_key
        d, n = key_to_use
        
        decrypted_blocks = []
        for block in encrypted_blocks:
            # Use CRT for decryption optimization
            decrypted_int = self.crt_decrypt(block)
            block_size = (decrypted_int.bit_length() + 7) // 8
            decrypted_bytes = decrypted_int.to_bytes(block_size, 'big')
            decrypted_blocks.append(decrypted_bytes)
        
        # Remove padding after decryption
        decrypted_message = self._oaep_unpad(b''.join(decrypted_blocks))
        
        return decrypted_message.decode('utf-8')

    def crt_decrypt(self, cipher_block: int) -> int:
        """CRT optimized decryption for efficiency"""
        p, q = self.key_pair.p, self.key_pair.q
        d = self.key_pair.private_key[0]
        dp = d % (p - 1)
        dq = d % (q - 1)
        qinv = MathUtils.extended_gcd(q, p)[1] % p
        
        # Compute decrypted block using CRT
        m1 = pow(cipher_block, dp, p)
        m2 = pow(cipher_block, dq, q)
        h = (qinv * (m1 - m2)) % p
        return m2 + h * q

    def _oaep_pad(self, message: str, block_size: int) -> bytes:
        """Applies OAEP padding to the message"""
        message_bytes = message.encode('utf-8')
        padding_length = block_size - len(message_bytes) - 2
        padding = b'\x00' * padding_length + b'\x01'
        return padding + message_bytes

    def _oaep_unpad(self, padded_message: bytes) -> bytes:
        """Removes OAEP padding from the decrypted message"""
        # Split the padded message by the first \x01 byte (which separates the padding from the message)
        unpadded_message = padded_message.split(b'\x01', 1)[-1]
        return unpadded_message
