# Binary Tree and BST Implementation
* A binary tree is a hierarchical data structure in which each node has at most two children generally referred as left child and right child.
* BST :is a collection of nodes arranged in a way where they maintain BST properties. Each node has a key and an associated value. While searching, the desired key is compared to the keys in BST and if found, the associated value is retrieved.

## Challenge
* Create a **Node class** that has properties for the **value** stored in the node, the **left child node**, and the **right child node**.
* Create a **BinaryTree class**
 - Define a method for each of the depth first traversals called **preOrder**,**inOrder**, and **postOrder** which *returns an array* of the values, ordered appropriately.
* Create a **BinarySearchTree class**
 - Define a method named **add** that accepts a value, and adds a new node with that value in the correct location in the binary search tree.
 - Define a method named **contains** that accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once.

## Approach & Efficiency
### Big O :
* Time >> O(n)
* Space >> O(1)

## Tasks checklist:
- [x] Top-level README “Table of Contents” is updated
- [x] Feature tasks for this challenge are completed
- [x] Unit tests written and passing
- [x] “Happy Path” - Expected outcome
- [x] Expected failure
- [x] Edge Case (if applicable/obvious)
- [x] README for this challenge is complete
- [x] Description, Approach & Efficiency, Solution
- [x] Link to code

## API
* Binary Tree methods:
  1. preOrder() return an array of collection from a pre-order depth first traversal >> [root][left][right]
  2. inOrder() return an array of collection from a in-order depth first traversal >> [left][root][right]
  3. postOrder() return an array of collection from a post-order depth first traversal >> [left][right][root]

* Binary Search Tree methods:
  1. add(value) accepts a value, and adds a new node with that value in the correct location in the binary search tree
  2. contains(value) accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once


* **PR link** : https://github.com/Noura-Alquran/data-structures-and-algorithms/pull/28
