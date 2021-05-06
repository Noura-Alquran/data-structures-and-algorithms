class Node():
  def __init__(self, data=None,next_node=None):
      self.data = data
      self.next_node = next_node
  def __str__(self):
      return self.data

  def set_new_next(self, new_next):
       self.next_node = new_next

class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def insert(self, data): # this implementation of insert is constant O(1)
        data=str(data)
        new_node = Node(data)
        new_node.set_new_next(self.head)
        self.head = new_node

    def includes(self,value):
        value=str(value)
        current = self.head
        value_exists=False
        while current and value_exists is False:
            if current.data == value:
                value_exists = True
            else:
                current = current.next_node
            # if current is None:
            #     raise ValueError("value not in the list")
        return value_exists

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

