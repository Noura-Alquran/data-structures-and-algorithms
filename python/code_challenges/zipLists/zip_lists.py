from Data_Structures.linked_list.linked_list import LinkedList

def zipLists(list_one,list_two):
    #Edge cases when one of the lists is empty
    if not list_one:
        return list_two
    elif not list_two:
        return list_one
    zip_list = LinkedList()
    current_one=list_one
    current_one=current_one.head
    current_two=list_two.head

    while current_one or current_two:
        if current_one:
            zip_list.append(current_one.data)
            current_one=current_one.next_node
        if current_two:
            zip_list.append(current_two.data)
            current_two=current_two.next_node
    return zip_list

if __name__=='__main__':
    list_one=LinkedList()
    list_two=LinkedList()
    list_one.append(25)
    list_one.append(1996)
    list_one.append("birthday")
    list_two.append(5)
    list_two.append("my")
    result=zipLists(list_one,list_two)
    print(result)
