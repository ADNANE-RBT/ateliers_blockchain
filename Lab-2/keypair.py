from typing import Tuple
from dataclasses import dataclass

@dataclass
class KeyPair:
    public_key: Tuple[int, int]
    private_key: Tuple[int, int]
    p: int  # Store p and q for CRT optimization
    q: int