import pytest
from code_challenges.queue_with_stacks.queue_with_stacks import Stack ,PseudoQueue

# test 8: Can successfully enqueue into a queue
def test_queue_enqueue():
    expected = "5"
    queue = PseudoQueue()
    queue.enqueue(5)
    actual = f"{queue}"
    assert actual == expected

# test : Can successfully enqueue multiple values into a queue
def test_queue_multiple_enqueue(queue_test):
    expected = "4 3 2 1"
    actual = f"{queue_test}"
    assert actual == expected

# test : Can successfully dequeue out of a queue the expected value
def test_queue_dequeue(queue_test):
    expected = 4
    actual = queue_test.dequeue()
    assert actual == expected



@pytest.fixture
def queue_test():
    queue = PseudoQueue()
    queue.enqueue(4)
    queue.enqueue(3)
    queue.enqueue(2)
    queue.enqueue(1)
    return queue
