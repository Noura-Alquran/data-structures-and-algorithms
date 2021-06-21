from code_challenges.tree_intersection.tree_intersection import *
import pytest

def test_tree_intersection(test_one):
    expected=[100, 160, 125, 175, 200, 350, 500]
    actual=test_one
    assert actual == expected

def test_one_tree_empty():
    tree1=BinaryTree()
    node=Node(2)
    node.left=Node(1)
    tree2=BinaryTree()
    expected=None
    actual=tree_intersection(tree1,tree2)
    assert actual == expected





@pytest.fixture
def test_one():
    tree1 = Node(150)
    tree1.left = Node(100)
    tree1.left.left = Node(75)
    tree1.left.right = Node(160)
    tree1.left.right.left = Node(125)
    tree1.left.right.right = Node(175)
    tree1.right = Node(250)
    tree1.right.left = Node(200)
    tree1.right.right = Node(350)
    tree1.right.right.left = Node(300)
    tree1.right.right.right = Node(500)
    binary_tree1 = BinaryTree(tree1)
    tree2 = Node(42)
    tree2.left = Node(100)
    tree2.left.left = Node(15)
    tree2.left.right = Node(160)
    tree2.left.right.left = Node(125)
    tree2.left.right.right = Node(175)
    tree2.right = Node(600)
    tree2.right.left = Node(200)
    tree2.right.right = Node(350)
    tree2.right.right.left = Node(4)
    tree2.right.right.right = Node(500)
    binary_tree2 = BinaryTree(tree2)
    return tree_intersection(binary_tree1, binary_tree2)



