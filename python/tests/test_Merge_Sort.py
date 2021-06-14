from code_challenges.Merge_Sort.Merge_Sort import *

def test_Merge_Sort():
    assert Merge_Sort([8,4,23,42,16,15]) == [4, 8, 15, 16, 23, 42]
    assert Merge_Sort([20,18,12,8,5,-2]) == [-2, 5, 8, 12, 18, 20]  #Reverse-Sorted
    assert Merge_Sort([5,12,7,5,5,7]) == [5, 5, 5, 7, 7, 12] #Few uniques
    assert Merge_Sort ([2,3,5,7,13,11]) == [2, 3, 5, 7, 11, 13]  #Nearly-sorted
