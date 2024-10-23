from AsymmetricCrypto import AsymmetricCrypto
if __name__ == "__main__":
        print("Démarrage du programme de chiffrement...")
        print("-" * 50)
        
        # Création d'une instance de cryptographie
        crypto = AsymmetricCrypto(key_size=1024)
        
        # Génération des clés
        print("Génération des clés en cours...")
        key_pair = crypto.generate_keys()
        print(f"Clé publique (e,n): {key_pair.public_key}")
        print(f"Clé privée (d,n): {key_pair.private_key}")
        print("-" * 50)
        
        # Message à chiffrer
        message = "Message secret: Bonjour tout le monde!"
        print(f"Message original: {message}")
        
        # Chiffrement
        print("\nChiffrement en cours...")
        encrypted = crypto.encrypt(message)
        print(f"Message chiffré (format nombre): {encrypted}")
        print(f"Message chiffré (format hexadécimal): {[hex(block) for block in encrypted]}")
        
        # Déchiffrement
        print("\nDéchiffrement en cours...")
        decrypted = crypto.decrypt(encrypted)
        print(f"Message déchiffré: {decrypted}")
        
        # Vérification
        print("\nVérification de l'intégrité:")
        print(f"Le message est{'n' if message != decrypted else ''} correctement récupéré: {message == decrypted}")