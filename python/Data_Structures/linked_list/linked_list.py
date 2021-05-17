class Node():
  def __init__(self, data=None,next_node=None):
      self.data = data
      self.next_node = next_node

  def __str__(self):
      return self.data

  def get_next(self):
      return self.next_node

  def set_new_next(self, new_next):
       self.next_node = new_next

class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def insert(self, data): # this implementation of insert is constant O(1)
        # data=str(data)
        new_node = Node(data)
        new_node.set_new_next(self.head)
        self.head = new_node

    def includes(self,value):
        # value=str(value)
        current = self.head
        value_exists=False
        while current and value_exists is False:
            if current.data == value:
                value_exists = True
            else:
                current = current.next_node
        return value_exists

    def append(self,value):
        new_node = Node(value)
        new_node.__str__()
        current = self.head
        if current :
            while current.get_next() != None:
                current = current.get_next()
            current.set_new_next(new_node)
        else:
            self.head=Node(value)
            current=self.head
        return current.__str__()


    def insertBefore(self ,value, newVal):
        new_node = Node(newVal)
        before = self.head
        if not before.data == value:
            old=before
            while before:
                if before.data == value:
                    new_node.next_node = before
                    old.next_node= new_node
                    return
                else:
                    old = before
                    before = before.next_node


    def insertAfter(self ,value, newVal):
        new_node = Node(newVal)
        before=self.head
        if value:
            while before:
                if before.data==value:
                    new_node.next_node=before.next_node
                    before.next_node=new_node
                    return
                before=before.next_node


    def ll_kthFromEnd (self,k):
        current = self.head
        len =0
        if k<0:
            return "incorrect k value"

        while current.next_node:
            current = current.next_node
            len += 1
        if k >= len:
            return "not exist"
        current = self.head
        for j in range(0,len - k):
            current = current.next_node
        return current.data


    def __str__ (self):
        output = ""
        current = self.head
        while current:
            output += "{%s} -> " %(current.data,)
            current = current.next_node
        output += " None"
        return output


if __name__ == "__main__":
  linked_list = LinkedList()
  print(linked_list)
  linked_list.insert("Noura")
  linked_list.insert("Jana")
  linked_list.insert(5)
  print(linked_list)
  print(linked_list.includes("Jana"))
  print(linked_list.includes("Noura"))
  print(linked_list.includes(5))
  print(linked_list.includes(15))

  e_list=LinkedList()
  e_list.append("test")
  print(e_list)
  print(linked_list.ll_kthFromEnd(2))
