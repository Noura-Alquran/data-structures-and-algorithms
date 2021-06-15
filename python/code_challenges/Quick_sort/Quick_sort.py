def QuickSort(list, left, right): #left : first index # right:last index
    if left < right:
        position = Partition(list, left, right)
        QuickSort(list, left, position - 1)
        QuickSort(list, position + 1, right)
    return list

def Partition(list, left, right):
    pivot = list[right] # pick last element as pivot
    low = left - 1
    for i  in range(left,right):
        if list[i] <= pivot :
            low += 1
            Swap(list, i, low)

    Swap(list, right, low + 1)
    return low + 1

def Swap(list, i, low):
    temp = list[i]
    list[i] = list[low]
    list[low] = temp






if __name__=="__main__":
    list1=[8,4,23,42,16,15]
    print(QuickSort(list1 ,0,5))
    list_2=[20,18,12,8,5,-2] #Reverse-sorted
    print(QuickSort(list_2,0,5)) #[-2, 5, 8, 12, 18, 20]
    list_3=[5,12,7,5,5,7] #Few uniques
    print(QuickSort(list_3,0,5)) #[5, 5, 5, 7, 7, 12]
    list_4=[2,3,5,7,13,11] #Nearly-sorted
    print(QuickSort(list_4,0,5)) #[2, 3, 5, 7, 11, 13]
