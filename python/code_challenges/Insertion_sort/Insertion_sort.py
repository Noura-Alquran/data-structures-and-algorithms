def Insertion_sort(list):
    for i in range(1,len(list)):
        j = i - 1
        temp=list[i]

        while j >= 0 and temp < list[j]:
            list[j + 1] = list[j]
            j = j - 1
        list[j+1]=temp

    return list


if __name__ == "__main__":
    list= [8,4,23,42,16,15]
    print(Insertion_sort(list)) #[4, 8, 15, 16, 23, 42]
    list_2=[20,18,12,8,5,-2] #Reverse-sorted
    print(Insertion_sort(list_2)) #[-2, 5, 8, 12, 18, 20]
    list_3=[5,12,7,5,5,7] #Few uniques
    print(Insertion_sort(list_3)) #[5, 5, 5, 7, 7, 12]
    list_4=[2,3,5,7,13,11] #Nearly-sorted
    print(Insertion_sort(list_4)) #[2, 3, 5, 7, 11, 13]
