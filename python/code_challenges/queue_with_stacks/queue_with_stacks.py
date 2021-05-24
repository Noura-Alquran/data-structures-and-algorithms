class EmptyStackException(Exception):
    pass

class Node():
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

    def __str__(self):
        return self.data

    def get_next_node(self):
        return self.next


class Stack():
    def __init__(self,node=None):
        self.top=node

    def push(self, value):
        if self.top == None:
            self.top = Node(value)
        else:
            node = Node(value)
            node.next = self.top
            self.top = node

    def isEmpty(self):
        if self.top:
            return False
        return True

    def pop(self):
        if not self.isEmpty():
            popped_node = self.top
            self.top = self.top.next
            popped_node.next = None
            return popped_node.data
        raise EmptyStackException("stack is empty")

    def peek(self):
        if not self.isEmpty():
            return self.top.data

        raise EmptyStackException("stack is empty")

    def __str__(self):
        top = self.top
        items = []
        while top:
            items.append(str(top.data))
            top = top.next
        return " ".join(items)


class PseudoQueue():
    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()

        self.front = None

    def enqueue(self, value):
        self.stack_1.push(value)

    def dequeue(self ):
        if self.stack_2.top == None:
            if self.stack_1.top== None:
                return "Can't dequeue from empty queue!"
        while not self.stack_1.isEmpty():
            popped = self.stack_1.pop()
            self.stack_2.push(popped)
        result = self.stack_2.pop()
        if self.stack_1.isEmpty():
            while not self.stack_2.isEmpty():
                 self.stack_1.push(self.stack_2.pop())
            return result

    def __str__(self):
        stack= self.stack_1.top
        items = []
        while stack:
            items.insert(0,str(stack.data))
            stack = stack.next
        return " ".join(items)


if __name__== "__main__" :
    pesudoQ= PseudoQueue()
    pesudoQ.enqueue(1)
    pesudoQ.enqueue(2)
    pesudoQ.enqueue(3)
    pesudoQ.enqueue(4)
    print(pesudoQ)
    print(pesudoQ.dequeue())
    print(pesudoQ)






