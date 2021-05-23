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
        self._items = []

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
    def __len__(self):
        return len(self._items)

class PseudoQueue():
    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()

        self.front = None

    def enqueue(self, value):
        self.stack_1.push(value)


    def dequeue(self):
        if self.stack_2.top == None:
            if self.stack_1.top== None:
                return "Can't dequeue from empty queue!"

        while self.stack_1.top:
            last_stack_1_item = self.stack_1.pop()
            self.stack_2.push(last_stack_1_item)
        return self.stack_2.pop()


    def __str__(self):
         return str(self.stack_1)

if __name__=="__main__":
    pesudoQ= PseudoQueue()
    pesudoQ.enqueue(1)
    pesudoQ.enqueue(2)
    pesudoQ.enqueue(3)
    pesudoQ.enqueue(4)
    print(pesudoQ)
    pesudoQ.dequeue()
    pesudoQ.dequeue()
    print(pesudoQ)
