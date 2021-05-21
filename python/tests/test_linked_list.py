import pytest
from Data_Structures.linked_list.linked_list import LinkedList


def test_import():
    assert LinkedList
# Can successfully instantiate an empty linked list && The head property will properly point to the first node in the linked list
def test_empty_list(empty_list):
    expected=[None] #None refer to the head of empty list
    actual=[empty_list]
    assert actual==expected

# Can properly insert into the linked list && Can properly return a collection of all the values that exist in the linked list
def test_insert(list_test):
    excpected = "{10} -> {Jana} -> {Noura} -> {1222} ->  None"
    actual = f"{list_test}"
    assert excpected == actual


# Will return true when finding a value within the linked list that exists && Will return false when searching for a value in the linked list that does not exist
def test_includes(list_test):
    actual = [list_test.includes(55),list_test.includes("Noura"),list_test.includes(10)]
    excpected = [False, True , True]
    assert excpected == actual

# Code challenge 6
# Can successfully add a node to the end of the linked list
def test_append(list_test):
    excpected = "{10} -> {Jana} -> {Noura} -> {1222} ->  None"
    actual = f"{list_test}"
    assert excpected == actual

# Can successfully append a node to empty list
def test_append_to_empty_list(e_list):
    excpected = "{test} ->  None"
    actual = f"{e_list}"
    print(actual)
    assert excpected == actual

# Can successfully add multiple nodes to the end of a linked list
def test_append_multiple_nodes(list_test):
    list_test.append(22)
    list_test.append(12)
    excpected = "{10} -> {Jana} -> {Noura} -> {1222} -> {22} -> {12} ->  None"
    actual = f"{list_test}"
    assert excpected == actual

# Can successfully insert a node before a node located i the middle of a linked list
def test_insertBefore(list_test):
    list_test.insertBefore(1222,"Manal")
    excpected = "{10} -> {Jana} -> {Noura} -> {Manal} -> {1222} ->  None"
    actual = f"{list_test}"
    assert excpected == actual

# Can successfully insert a node before the first node of a linked list
def test_insertBefore_first_node(list_test):
    list_test.insertBefore(10,"Mamoun")
    excpected = "{Mamoun} -> {10} -> {Jana} -> {Noura} -> {1222} ->  None"
    actual = f"{list_test}"
    assert excpected == actual

# Can successfully insert after a node in the middle of the linked list
def test_insertAfter(list_test):
    list_test.insertAfter("Jana","Eman")
    excpected = "{10} -> {Jana} -> {Eman} -> {Noura} -> {1222} ->  None"
    actual = f"{list_test}"
    assert excpected == actual

# Can successfully insert a node after the last node of the linked list
def test_insertAfter_last_node(list_test):
    list_test.insertAfter(1222,1996)
    excpected = "{10} -> {Jana} -> {Noura} -> {1222} -> {1996} ->  None"
    actual = f"{list_test}"
    assert excpected == actual

# Code challenge 7
# “Happy Path” where k is not at the end, but somewhere in the middle of the linked list
def test_ll_kthFromEnd(kth_test):
    excpected = 2
    actual=kth_test
    assert excpected == actual

def test_ll_kthFromEnd_one(kth_test_one):
    excpected = 8
    actual=kth_test_one
    assert excpected == actual

# Where the linked list is of a size 1
def test_ll_kthFromEnd_size_one(kth_test_two):
    excpected ="not exist"
    actual=kth_test_two
    assert excpected == actual

# Where k is not a positive integer
def test_ll_kthFromEnd_negative_k(kth_test_three):
    excpected = "incorrect k value"
    actual=kth_test_three
    assert excpected == actual

# Where k is greater than the length of the linked list
def test_ll_kthFromEnd_k_larger(kth_test_four):
    excpected = "not exist"
    actual=kth_test_four
    assert excpected == actual

# Where k and the length of the list are the same
def test_ll_kthFromEnd_k_same_size(kth_test_same):
    excpected = "not exist"
    actual=kth_test_same
    assert excpected == actual

@pytest.fixture
def empty_list():
    linked=LinkedList()

@pytest.fixture
def list_test():
    linked_list = LinkedList()
    linked_list.insert("Noura")
    linked_list.insert("Jana")
    linked_list.insert(10)
    linked_list.append(1222)
    return linked_list

@pytest.fixture
def e_list():
    e_list=LinkedList()
    e_list.append("test")
    return e_list

@pytest.fixture
def kth_test():
    linked_l = LinkedList()
    linked_l.insert(2)
    linked_l.insert(8)
    linked_l.insert(3)
    linked_l.insert(1)
    return linked_l.ll_kthFromEnd(0)

@pytest.fixture
def kth_test_one():
    linked_l = LinkedList()
    linked_l.insert(2)
    linked_l.insert(8)
    linked_l.insert(3)
    linked_l.insert(1)
    return linked_l.ll_kthFromEnd(1)

@pytest.fixture
def kth_test_two():
    linked_l = LinkedList()
    linked_l.insert(2)
    return linked_l.ll_kthFromEnd(0)

@pytest.fixture
def kth_test_three():
    linked_l = LinkedList()
    linked_l.insert(2)
    linked_l.insert(8)
    linked_l.insert(3)
    linked_l.insert(1)
    return linked_l.ll_kthFromEnd(-3)

@pytest.fixture
def kth_test_four():
    linked_l = LinkedList()
    linked_l.insert(2)
    linked_l.insert(8)
    linked_l.insert(3)
    linked_l.insert(1)
    return linked_l.ll_kthFromEnd(6)

@pytest.fixture
def kth_test_same():
    linked_l = LinkedList()
    linked_l.insert(2)
    linked_l.insert(8)
    linked_l.insert(3)
    linked_l.insert(1)
    return linked_l.ll_kthFromEnd(4)
