from code_challenges.Quick_sort.Quick_sort import *

def test_Quick_Sort():
    assert QuickSort([8,4,23,42,16,15],0,5) == [4, 8, 15, 16, 23, 42]
    assert QuickSort([20,18,12,8,5,-2],0,5) == [-2, 5, 8, 12, 18, 20]  #Reverse-Sorted
    assert QuickSort([5,12,7,5,5,7],0,5) == [5, 5, 5, 7, 7, 12] #Few uniques
    assert QuickSort ([2,3,5,7,13,11],0,5) == [2, 3, 5, 7, 11, 13]  #Nearly-sorted
