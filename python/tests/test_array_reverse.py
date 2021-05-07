from code_challenges.array_reverse.array_reverse import reverseArray

def test_reverse_list(list=[1,2,3,4,5,6]):
    expected = list[::-1]
    actual =reverseArray(list)
    assert expected == actual
