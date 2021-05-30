from tree.tree import Node ,BinaryTree,BinarySearchTree
import pytest

## Can successfully instantiate an empty tree
def test_instantiate_an_empty_tree():
    expected =[]
    btt=BinaryTree()
    actual=btt.preOrder()
    assert actual == expected

## Can successfully instantiate a tree with a single root node
def test_instantiate_tree_with_single_root():
    expected =[5]
    node=Node(5)
    btt=BinaryTree(node)
    actual=btt.preOrder()
    assert actual == expected

## Can successfully add a left child and right child to a single root node
def test_tree_add_children_to_single_root():
    expected =[2,5,6]
    node=Node(5)
    node.left=Node(2)
    node.right=Node(6)
    btt=BinaryTree(node)
    actual=btt.inOrder()
    assert actual == expected

## Can successfully return a collection from a preorder traversal
def test_preOrder_traversal(tree_test):
    expected=[1,2,9,7,3,4,5]
    actual=tree_test.preOrder()
    assert actual == expected


## Can successfully return a collection from an inorder traversal
def test_InOrder_traversal(tree_test):
    expected=[9,2,7,1,4,3,5]
    actual=tree_test.inOrder()
    assert actual == expected

## Can successfully return a collection from a postorder traversal
def test_postOrder_traversal(tree_test):
    expected=[9,7,2,4,5,3,1]
    actual=tree_test.postOrder()
    assert actual == expected

# Can successfully add value to the tree in the correct location
def test_add_method_for_BinarySearch_class():
    bts=BinarySearchTree()
    bts.add(5)
    bts.add(9)
    bts.add(-2)
    bts.add(6)
    bts.add(3)
    bts.add(8)
    bts.add(5)
    assert bts.root.value == 5
    assert bts.root.left.value == -2
    assert bts.root.right.value == 9
    assert bts.root.left.right.value == 3
    assert bts.root.right.left.left.value == 5

# Can successfully check if value is in tree at least once
def test_contains_method(tree_test_two):
    expected=True
    actual=tree_test_two.contains(2)
    assert actual == expected

## Code challenge 16
# Can succussfully find the maximum value in the tree
def test_find_max_value_within_tree(tree_test):
    expected=9
    actual=tree_test.find_maximum_value()
    assert actual == expected 





@pytest.fixture
def tree_test():
    node1 = Node(1)
    node1.left = Node(2)
    node1.left.right = Node(7)
    node1.left.left = Node(9)
    node1.right = Node(3)
    node1.right.left = Node(4)
    node1.right.right = Node(5)
    binary_tree = BinaryTree(node1)
    return binary_tree

@pytest.fixture
def tree_test_two():
    node1 = Node(1)
    node1.left = Node(2)
    node1.left.right = Node(7)
    node1.left.left = Node(9)
    node1.right = Node(3)
    node1.right.left = Node(4)
    node1.right.right = Node(5)
    bts = BinarySearchTree(node1)
    return bts
