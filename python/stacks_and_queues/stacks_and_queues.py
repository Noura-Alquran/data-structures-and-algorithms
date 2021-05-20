class EmptyStackException(Exception):
    pass

class EmptyQueueException(Exception):
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
            value = self.front.data
            self.front = self.front.next
            return value

        raise EmptyQueueException("queue is empty")


    def peek(self):
        if not self.isEmpty():
            return self.front.data
        raise EmptyQueueException("queue is empty")

    def __str__(self):
        front = self.front
        items = []
        while front:
            items.append(str(front.data))
            front = front.next
        return " ".join(items)


if __name__ == "__main__":
  stack = Stack()
  print(stack)
  stack.push(5)
  print(stack )
  stack.push(4)
  stack.push(3)
  print(stack)
  print(stack.peek())
  stack.pop()
  print(stack)

  queue = Queue()
  print(queue)
  queue.enqueue(1)
  print(queue)
  queue.enqueue(2)
  queue.enqueue(3)
  print(queue)
  queue.dequeue()
  print(queue)
  print(queue.peek())


