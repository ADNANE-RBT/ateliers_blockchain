const shajs = require("sha.js"); 

function hash(leftNode, rightNode) {
  return shajs("sha256")
    .update(leftNode + rightNode, "hex")
    .digest("hex");
}

class MerkleTree {
    constructor(height, leaves){
      this.height = height;
      this.leaves = leaves;
    }
    N(level, index){
      if(level === this.height){
        return this.leaves[index];
      }else{

        return hash(
          this.N(level+1, 2*index),
          this.N(level+1, 2*index+1),
        );
      }
    }
    getRoot(){
      return this.N(0,0);
    }
  }


  module.exports = { MerkleTree };


