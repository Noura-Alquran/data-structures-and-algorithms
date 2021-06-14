def Merge_Sort(list):
    n= len(list)
    if n > 1 :
        mid = int(n/2)
        left =list[0:mid]
        right = list[mid:n]
        Merge_Sort(left)
        Merge_Sort(right)
        Merge (left, right, list)
    return list


def Merge(left, right, list):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            list[k] = left[i]
            i = i + 1
        else :
            list[k] = right[j]
            j = j + 1
            
        k = k + 1

    while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1
 
    while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1


if __name__=="__main__":
    list1=[8,4,23,42,16,15]
    print(Merge_Sort(list1))
    list_2=[20,18,12,8,5,-2] #Reverse-sorted
    print(Merge_Sort(list_2)) #[-2, 5, 8, 12, 18, 20]
    list_3=[5,12,7,5,5,7] #Few uniques
    print(Merge_Sort(list_3)) #[5, 5, 5, 7, 7, 12]
    list_4=[2,3,5,7,13,11] #Nearly-sorted
    print(Merge_Sort(list_4)) #[2, 3, 5, 7, 11, 13]
