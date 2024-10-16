const CryptoJS = require('crypto-js');

class MerkleTree {
    constructor(leaves) {
        this.leaves = leaves.map(leaf => this.hash(leaf));
        this.tree = this.buildTree(this.leaves);
    }

    hash(data) {
        return CryptoJS.SHA256(data).toString();
    }

    buildTree(leaves) {
        if (leaves.length === 1) {
            return leaves;
        }

        const layer = [];
        for (let i = 0; i < leaves.length; i += 2) {
            const left = leaves[i];
            const right = i + 1 < leaves.length ? leaves[i + 1] : left;
            const combinedHash = this.hash(left + right);
            layer.push(combinedHash);
        }

        return [layer, ...this.buildTree(layer)];
    }

    getRoot() {
        return this.tree[this.tree.length - 1][0];
    }

    getProof(index) {
        let proof = [];
        for (let i = 0; i < this.tree.length - 1; i++) {
            const isRightNode = index % 2 === 0;
            const pairIndex = isRightNode ? index - 1 : index + 1;

            if (pairIndex < this.tree[i].length) {
                proof.push({
                    position: isRightNode ? 'left' : 'right',
                    data: this.tree[i][pairIndex]
                });
            }

            index = Math.floor(index / 2);
        }
        return proof;
    }

    static verify(leaf, proof, root) {
        let computedHash = CryptoJS.SHA256(leaf).toString();

        for (const { position, data } of proof) {
            if (position === 'left') {
                computedHash = CryptoJS.SHA256(data + computedHash).toString();
            } else {
                computedHash = CryptoJS.SHA256(computedHash + data).toString();
            }
        }

        return computedHash === root;
    }
}

module.exports = MerkleTree;