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

def test_append(list_test):
    excpected = "{10} -> {Jana} -> {Noura} -> {1222} ->  None"
    actual = f"{list_test}"
    assert excpected == actual

def test_append_to_empty_list(e_list):
    excpected = "{test} ->  None"
    actual = f"{e_list}"
    print(actual)
    assert excpected == actual

def test_insertBefore(before_test):
    excpected = "{10} -> {Jana} -> {Noura} -> {Manal} -> {1222} ->  None"
    actual = f"{before_test}"
    assert excpected == actual

def test_insertAfter(After_test):
    excpected = "{10} -> {Jana} -> {Eman} -> {Noura} -> {Manal} -> {1222} ->  None"
    actual = f"{After_test}"
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
def before_test():
    before_test= LinkedList()
    before_test.insert("Noura")
    before_test.insert("Jana")
    before_test.insert(10)
    before_test.append(1222)
    before_test.insertBefore(1222,"Manal")
    return before_test

@pytest.fixture
def After_test():
    linked = LinkedList()
    linked.insert("Noura")
    linked.insert("Jana")
    linked.insert(10)
    linked.append(1222)
    linked.insertBefore(1222,"Manal")
    linked.insertAfter("Jana","Eman")
    return linked

