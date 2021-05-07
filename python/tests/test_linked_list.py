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
    excpected = "{10} -> {Jana} -> {Noura} ->  None"
    actual = f"{list_test}"
    assert excpected == actual


# Will return true when finding a value within the linked list that exists && Will return false when searching for a value in the linked list that does not exist
def test_includes(list_test):
    actual = [list_test.includes(55),list_test.includes("Noura"),list_test.includes(10)]
    excpected = [False, True , True]
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
    return linked_list


