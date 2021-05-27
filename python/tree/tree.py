# Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)

#Create a BinaryTree class and define a method for each of the depth first traversals called preOrder, inOrder, and postOrder which returns an array of the values, ordered appropriately.
class BinaryTree:
    def __init__(self,root=None):
        self.root=root

    def preOrder(self):
        ## [root][left][right]
        if not self.root:
            return []
        output = []
        def walk(root):
            output.append(root.value)
            if root.left:
                walk(root.left)
            if root.right:
                walk(root.right)
        walk(self.root)
        return output

    def inOrder(self):
        ## [left][root][right]
        ## ordered the result
        if not self.root:
            return []
        output = []
        def walk(root):
            if root.left:
                walk(root.left)
            output.append(root.value)
            if root.right:
                walk(root.right)
        walk(self.root)
        return output

    def postOrder(self):
        ## [left][right][root]
        if not self.root:
            return []
        output = []
        def walk(root):
            if root.left:
                walk(root.left)
            if root.right:
                walk(root.right)
            output.append(root.value)
        walk(self.root)
        return output



class BinarySearchTree(BinaryTree):

    # Define a method named add that accepts a value, and adds a new node with that value in the correct location in the binary search tree.
    def add(self,value):
        if not self.root:
            self.root = Node(value)
        else:
            def walk(root):
                if value < root.value:
                    if not root.left:
                        root.left = Node(value)
                        return
                    else:
                        walk(root.left)
                else:
                    if not root.right:
                        root.right = Node(value)
                        return
                    else:
                        walk(root.right)
            return walk(self.root)


    # Define a method named contains that accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once.
    def contains(self,value):
        if not self.root:
            return False
        def walk(root):
            if root:
                if root.value == value:
                    return True
                elif value != root.value:
                    if walk(root.left):
                        return True
                    elif walk(root.right):
                        return True
            return False
        return walk(self.root)




if __name__ == '__main__':
    node1 = Node(1)
    node1.left = Node(2)
    node1.left.right = Node(7)
    node1.left.left = Node(9)
    node1.right = Node(3)
    node1.right.left = Node(4)
    node1.right.right = Node(5)

    binary_tree = BinaryTree(node1)

    print(binary_tree.preOrder()) #[1,2,9,7,3,4,5]
    print(binary_tree.inOrder()) #[9,2,7,1,4,3,5]
    print(binary_tree.postOrder()) #[9,7,2,4,5,3,1]

    bts=BinarySearchTree(node1)
    print(bts.contains(2))
    print(bts.contains(10))

    bts_two=BinarySearchTree()
    bts_two.add(5)
    bts_two.add(9)
    bts_two.add(-2)
    bts_two.add(6)
    bts_two.add(3)
    bts_two.add(8)
    bts_two.add(5)

    assert bts_two.root.value == 5
    assert bts_two.root.left.value == -2
    assert bts_two.root.right.value == 9
    assert bts_two.root.left.right.value == 3
    assert bts_two.root.right.left.left.value == 5
    print('add method pass')






