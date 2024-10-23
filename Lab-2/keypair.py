from typing import Tuple
from dataclasses import dataclass

@dataclass
class KeyPair:
    """Classe pour stocker une paire de clés publique/privée"""
    public_key: Tuple[int, int]
    private_key: Tuple[int, int]

