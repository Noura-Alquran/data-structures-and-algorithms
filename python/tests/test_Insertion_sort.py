from code_challenges.Insertion_sort.Insertion_sort import Insertion_sort

def test_insertion_sort():
    assert Insertion_sort([8,4,23,42,16,15]) == [4, 8, 15, 16, 23, 42]
    assert Insertion_sort([20,18,12,8,5,-2]) == [-2, 5, 8, 12, 18, 20]  #Reverse-sorted
    assert Insertion_sort([5,12,7,5,5,7]) == [5, 5, 5, 7, 7, 12] #Few uniques
    assert Insertion_sort ([2,3,5,7,13,11]) == [2, 3, 5, 7, 11, 13]  #Nearly-sorted

