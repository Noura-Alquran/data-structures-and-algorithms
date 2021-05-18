from Data_Structures.linked_list.linked_list import LinkedList
from code_challenges.zipLists.zip_lists import zipLists
import pytest

# Happy path test
def test_zip_lists(zipLists_test):
    expected="{25} -> {5} -> {1996} -> {my} -> {birthday} ->  None"
    actual=f"{zipLists_test}"
    assert actual==expected

# when one of the lists empty
def test_zip_list_two(edge_test):
    expected="{25} -> {1996} -> {birthday} ->  None"
    actual=f"{edge_test}"
    assert actual==expected



@pytest.fixture
def zipLists_test():
    linked_list_one= LinkedList()
    linked_list_two= LinkedList()
    linked_list_one.append(25)
    linked_list_one.append(1996)
    linked_list_one.append("birthday")
    linked_list_two.append(5)
    linked_list_two.append("my")
    result=zipLists(linked_list_one,linked_list_two)
    return result

@pytest.fixture
def edge_test():
    linked_list_one= LinkedList()
    linked_list_two= LinkedList()
    linked_list_one.append(25)
    linked_list_one.append(1996)
    linked_list_one.append("birthday")
    result=zipLists(linked_list_one,linked_list_two)
    return result
