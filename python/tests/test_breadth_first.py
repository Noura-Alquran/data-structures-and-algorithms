from code_challenges.BinaryTree.breadth_first import Node ,  BinaryTree, breadth_first

def test_breadth_first():
    input = BinaryTree()
    input.root = Node(2)
    input.root.left = Node(7)
    input.root.right = Node(5)
    input.root.left.right = Node(6)
    input.root.left.left = Node(2)
    input.root.right.right=Node(9)
    input.root.right.right.left=Node(4)
    input.root.left.left.right=Node(5)
    input.root.left.right.left = Node(11)
    expected = [2, 7, 5, 2, 6, 9, 5, 11, 4]
    actual=breadth_first(input)
    assert actual == expected

