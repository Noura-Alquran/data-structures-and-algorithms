class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)
      
class BinaryTree:
    def __init__(self,root=None):
        self.root=root
        self.output=[]

    def preOrder(self):
        ## [root][left][right]
        output=[]
        if self.root == None:
            return output
        def walk(root):
            output.append(root.value)
            if root.left:
                walk(root.left)
            if root.right:
                walk(root.right)
        walk(self.root)
        return output

    
    def __str__(self):
        return str(self.output)


        
def fizzBuzz(node):
    if node:
        if node.value % 3 == 0 and node.value % 5 == 0:
            return'FizzBuzz'
        elif node.value %3 == 0:
            return'Fizz'
        elif node.value % 5 == 0:
            return'Buzz'
        else:
            return str(node.value)


def FizzBuzzTree(tree):
    if not tree.root:
        return []
    new_tree=BinaryTree()
    def walk(node):
        new_tree.output=new_tree.output + [fizzBuzz(node)]
        if node.left:           
            walk(node.left)
        if node.right:
            walk(node.right)
        return new_tree.output

    return walk(tree.root) 

if __name__ == "__main__":
    input = BinaryTree()
    input.root = Node(12)
    input.root.left = Node(7)
    input.root.right = Node(5)
    input.root.left.right = Node(6)
    input.root.left.left = Node(8)
    input.root.right.right=Node(9)
    input.root.right.right.left=Node(4)
    input.root.left.left.right=Node(5)
    input.root.left.right.left = Node(11)
    print(input.preOrder())
    print (FizzBuzzTree(input))
