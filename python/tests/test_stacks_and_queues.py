import pytest
from stacks_and_queues.stacks_and_queues import Stack,Queue,EmptyStackException,EmptyQueueException

# test 1: Can successfully push onto a stack
def test_stack_push():
    expected = "pass"
    stack = Stack()
    stack.push("pass")
    actual = f"{stack}"
    assert actual == expected

# test 2: Can successfully push multiple values onto a stack
def test_stack_multiple_push(stack_test):
    expected = "1 2 3 4"
    actual = f"{stack_test}"
    assert actual == expected

# test 3: Can successfully pop off the stack
def test_stack_pop(stack_test):
    expected = 1
    actual = stack_test.pop()
    assert actual == expected

# test 4: Can successfully empty a stack after multiple pops
def test_stack_multiple_pop(stack_test):
    for item in range(4):
        stack_test.pop()
    with pytest.raises(EmptyStackException):
        stack_test.pop()

# test 5: Can successfully peek the next item on the stack
def test_stack_peek(stack_test):
    expected = "top"
    stack_test.push("top")
    actual = stack_test.peek()
    assert actual == expected

# test 6: Can successfully instantiate an empty stack
def test_instantiate_empty_stack():
    stack = Stack()
    actual = stack.isEmpty()
    assert actual

# test 7: Calling pop or peek on empty stack raises exception
def test_pop_or_peek_empty_stack():
    stack = Stack()
    with pytest.raises(EmptyStackException):
        stack.peek()
    with pytest.raises(EmptyStackException):
        stack.pop()

# test 8: Can successfully enqueue into a queue
def test_queue_enqueue():
    expected = "5"
    queue = Queue()
    queue.enqueue(5)
    actual = f"{queue}"
    assert actual == expected

# test 9: Can successfully enqueue multiple values into a queue
def test_queue_multiple_enqueue(queue_test):
    expected = "4 3 2 1"
    actual = f"{queue_test}"
    assert actual == expected

# test 10: Can successfully dequeue out of a queue the expected value
def test_queue_dequeue(queue_test):
    expected = 4
    actual = queue_test.dequeue()
    assert actual == expected

# test 11 : Can successfully peek into a queue, seeing the expected value
def test_queue_peek_front(queue_test):
    expected = 4
    actual = queue_test.peek()
    assert actual == expected

# test 12: Can successfully empty a queue after multiple dequeues
def test_queue_multiple_dequeue(queue_test):
    for num in range(4):
        queue_test.dequeue()
    with pytest.raises(EmptyQueueException):
        queue_test.dequeue()

# test 13 : Can successfully instantiate an empty queue
def test_instantiate_empty_queue():
    queue = Queue()
    actual = queue.isEmpty()
    assert actual

# test 14 :Calling dequeue or peek on empty queue raises exception
def test_peek_empty_queue():
    queue = Queue()
    with pytest.raises(EmptyQueueException):
        queue.peek()
    with pytest.raises(EmptyQueueException):
        queue.dequeue()

@pytest.fixture
def stack_test():
    stack = Stack()
    stack.push(4)
    stack.push(3)
    stack.push(2)
    stack.push(1)
    return stack

@pytest.fixture
def queue_test():
    queue = Queue()
    queue.enqueue(4)
    queue.enqueue(3)
    queue.enqueue(2)
    queue.enqueue(1)
    return queue
