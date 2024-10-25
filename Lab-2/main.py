from AsymmetricCrypto import AsymmetricCrypto
if __name__ == "__main__":
        print("Starting the encryption program with optimizations...")
        print("-" * 50)
        
        # Create an instance of the crypto system
        crypto = AsymmetricCrypto(key_size=1024)
        
        # Generate the key pair
        print("Generating keys...")
        key_pair = crypto.generate_keys()
        print(f"Public Key (e,n): {key_pair.public_key}")
        print(f"Private Key (d,n): {key_pair.private_key}")
        print("-" * 50)
        
        # Message to encrypt
        message = "Secret message: Bonjour tout le monde!"
        print(f"Original Message: {message}")
        
        # Encrypt the message
        print("\nEncrypting message...")
        encrypted = crypto.encrypt(message)
        print(f"Encrypted Message (as numbers): {encrypted}")
        
        # Decrypt the message
        print("\nDecrypting message...")
        decrypted = crypto.decrypt(encrypted)
        print(f"Decrypted Message: {decrypted}")
        
        # Verification
        print("\nIntegrity Check:")
        print(f"Message recovered correctly: {message == decrypted}")