const MerkleTree = require('./merkleTree');

// Exemple d'utilisation
const leaves = ['a', 'b', 'c', 'd', 'e'];
const merkleTree = new MerkleTree(leaves);

console.log('Feuilles:', leaves);
console.log('Racine de l\'arbre de Merkle:', merkleTree.getRoot());

// Vérification d'une feuille
const leafIndex = 2; // Indice de la feuille 'c'
const proof = merkleTree.getProof(leafIndex);
const leaf = leaves[leafIndex];
const isValid = MerkleTree.verify(leaf, proof, merkleTree.getRoot());

console.log(`\nVérification de la feuille '${leaf}' :`);
console.log('Preuve:', proof);
console.log('Est valide:', isValid);

// Tentative de vérification avec une feuille incorrecte
const invalidLeaf = 'x';
const isInvalidLeafValid = MerkleTree.verify(invalidLeaf, proof, merkleTree.getRoot());

console.log(`\nVérification de la feuille invalide '${invalidLeaf}' :`);
console.log('Est valide:', isInvalidLeafValid);