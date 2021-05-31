class EmptyQueueException(Exception):
    pass

class Queue():
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)
        if not self.front:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = self.rear.next

    def isEmpty(self):
        if self.front:
            return False
        return True

    def dequeue(self):
        if not self.isEmpty():
            value = self.front.value
            self.front = self.front.next
            return value

        raise EmptyQueueException("queue is empty")



class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.next=None

    def __str__(self):
        return str(self.value)

class BinaryTree:
    def __init__(self,root=None):
        self.root=root

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

    def inOrder(self):
        ## [left][root][right]
        output = []
        if self.root==None:
            return output
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
        output = []
        if self.root==None:
            return output
        def walk(root):
            if root.left:
                walk(root.left)
            if root.right:
                walk(root.right)
            output.append(root.value)
        walk(self.root)
        return output

    def find_maximum_value(self):
        if self.root == None:
            return 0
        maximum_value=self.root.value
        def walk(root):
            nonlocal maximum_value
            if root.value > maximum_value:
                maximum_value=root.value
            if root.left:
                walk(root.left)
            if root.right:
                walk(root.right)
            return maximum_value
        return walk(self.root)


def breadth_first(input):
    # by levels from left to right
        output=[]
        if not input.root:
            return []
        q=Queue()
        q.enqueue(input.root)
        while q.front:
            temp=q.dequeue()
            output=output+[temp.value]
            if temp.left:
                q.enqueue(temp.left)
            if temp.right:
                q.enqueue(temp.right)
        return output



if __name__ == "__main__":
    python/code_challenges/BinaryTree/breadth_first.py
# [2, 7, 5, 2, 6, 9, 5, 11, 4]
