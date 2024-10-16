### Code Explanation

Here’s a breakdown of the code and its functionality:

#### 1. **`MerkleTree` Class**:
- **Constructor**: 
  - `constructor(height, leaves)`: Initializes a Merkle Tree with a given height and a list of leaves. The height of the tree defines the number of levels, where each level consists of nodes derived from the leaves at the bottom.
  
- **Methods**:
  - `N(level, index)`: This recursive function returns the node at a given `level` and `index`. If it is at the leaf level (i.e., `level === height`), it returns the leaf at that index. Otherwise, it computes the hash of the concatenation of its left and right children using the `hash` function.
  
  - `getRoot()`: Returns the root of the Merkle Tree, which is the node at the topmost level (`N(0, 0)`).

#### 2. **`hash` function**:
   - `hash(leftNode, rightNode)`: A helper function that computes the SHA-256 hash of two concatenated nodes. This is used to combine nodes at lower levels into their parent node in the Merkle Tree.

#### 3. **Test functions**:
   - `example1()`: This function constructs a Merkle Tree with a height of 3 and a list of leaves, then prints the root of the tree. It demonstrates the Merkle Tree structure without modifying any leaves.
   
   - `example2()`: Similar to `example1()`, but after printing the initial root, it modifies the leaf at index 5 and prints the updated root to show how changing a single leaf alters the entire tree structure.

#### How to run:
1. Create two files:
   - `merkleTree.js` for your `MerkleTree` class implementation.
   - `testMerkleTree.js` for the test cases provided above.

2. To execute the test cases, simply run:
   ```bash
   node testMerkleTree.js
   ```

The output will show the root of the Merkle Tree before and after modifying one of the leaves in `example2()`. This demonstrates how the root of a Merkle Tree reflects the integrity of the entire dataset.

### for more documentation:
https://medium.com/@carterfeldman/a-hackers-guide-to-layer-2-merkle-trees-from-scratch-f682fc31bced