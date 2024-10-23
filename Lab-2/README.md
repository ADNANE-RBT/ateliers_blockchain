# Documentation de l'Algorithme de Cryptographie Asymétrique
## Inspiré de RSA avec optimisations

## Table des matières
1. [Principe général](#1-principe-général)
2. [Composants mathématiques](#2-composants-mathématiques)
3. [Implémentation détaillée](#3-implémentation-détaillée)
4. [Optimisations](#4-optimisations)


## 1. Principe général

### 1.1 Vue d'ensemble
L'algorithme implémente un système de cryptographie asymétrique où :
- Deux clés sont générées : une publique pour le chiffrement et une privée pour le déchiffrement
- Les messages sont traités par blocs pour gérer les messages de grande taille
- Le système utilise des nombres premiers et des opérations modulaires pour assurer la sécurité

### 1.2 Flux de données
```
Message original → Découpage en blocs → Chiffrement → Blocs chiffrés
Blocs chiffrés → Déchiffrement → Recomposition → Message original
```

## 2. Composants mathématiques

### 2.1 Test de Primalité Miller-Rabin
```python
def is_prime(n: int, k: int = 5) -> bool:
```
- **Objectif** : Tester si un nombre est premier de manière probabiliste
- **Paramètres** :
  - `n` : nombre à tester
  - `k` : nombre d'itérations pour le test (plus k est grand, plus le test est fiable)
- **Principe** : Décompose n-1 en d×2^r et effectue k tests avec des bases aléatoires

### 2.2 Génération de Nombres Premiers
```python
def generate_prime(bits: int) -> int:
```
- **Objectif** : Générer un nombre premier de taille spécifique
- **Méthode** :
  1. Génération d'un nombre aléatoire de la taille souhaitée
  2. Vérification de la primalité avec Miller-Rabin
  3. Répétition jusqu'à trouver un nombre premier

### 2.3 Algorithme d'Euclide Étendu
```python
def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
```
- **Objectif** : Calculer le PGCD et les coefficients de Bézout
- **Retourne** : (gcd, x, y) tels que ax + by = gcd

## 3. Implémentation détaillée

### 3.1 Génération des Clés
```python
def generate_keys(key_size: int = 1024) -> Tuple[Tuple[int, int], Tuple[int, int]]:
```
#### Étapes :
1. Génération de deux nombres premiers p et q
2. Calcul de n = p×q
3. Calcul de φ(n) = (p-1)(q-1)
4. Choix de e = 65537
5. Calcul de d = e^(-1) mod φ(n)
6. Retourne ((e,n), (d,n))

### 3.2 Traitement des Messages
```python
def optimize_message_blocks(message: str, n: int) -> List[int]:
```
- Division du message en blocs de taille optimale
- Conversion des blocs en nombres pour le chiffrement

### 3.3 Chiffrement/Déchiffrement
```python
def encrypt(message: str, public_key: Tuple[int, int]) -> List[int]:
def decrypt(encrypted_blocks: List[int], private_key: Tuple[int, int]) -> str:
```
- Utilisation de l'exponentiation modulaire rapide
- Gestion des conversions entre types de données

## 4. Optimisations

### 4.1 Optimisations Mathématiques
- Utilisation de l'exposant e = 65537 (nombre de Fermat F4)
- Test de Miller-Rabin optimisé
- Exponentiation modulaire rapide avec pow()

### 4.2 Optimisations de Performance
- Découpage intelligent des messages
- Gestion efficace de la mémoire
- Utilisation de types natifs Python

### 4.3 Optimisations de Sécurité
- Vérification de la distinctivité des nombres premiers
- Gestion des erreurs de déchiffrement
- Validation des entrées
