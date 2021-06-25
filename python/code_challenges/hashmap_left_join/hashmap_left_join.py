class Node():
  def __init__(self, data=None,next_node=None):
      self.data = data
      self.next_node = next_node

  def __str__(self):
      return self.data

class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def append_to(self,value):
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


class HashTable():
    def __init__(self):
        self.size = 1024
        self.map = [None] * self.size

    # to determine the index of the array
    def hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        index = (hash * 599) % self.size
        return index

     # takes in the key and returns a boolean, indicating if the key exists in the table already.
    def contains(self, key):
        index = self.hash(key)
        if self.map[index]:
            temp = self.map[index].head
            while temp:
                if key == temp.data[0]:
                    return True
                temp = temp.next_node
        return False

    # to add a new key/value pair to a hashtable
    def add(self, key, value):
       index = self.hash(key)
       key_value = [key, value]
       if self.contains(key):
            temp = self.map[index].head
            while temp:
                if key == temp.data[0]:
                    temp.data[1] =  value
                temp = temp.next_node
                return self
       if self.map[index] is None:
           self.map[index] = LinkedList()
       self.map[index].append_to(key_value)
       return self.__str__()

    # takes in the key and returns the value from the table.
    def get(self, key):
        index = self.hash(key)
        if self.map[index]:
            temp = self.map[index].head
            while temp:
                if key == temp.data[0] :
                    return temp.data[1]
                temp = temp.next_node
        return None

    def __str__(self):
        result = ""
        for i in self.map:
            if i is not None:
                temp = i.head
                while temp:
                    result +="{%s} -> " %(temp.data,)
                    temp = temp.next_node
                result+='None'
        return result


def left_join_hash(ht_one,ht_two):
    hash_table = HashTable()
    for elm in ht_one.map :
        if elm :
            hash_table.add(elm.head.data[0], [elm.head.data[1],None])

    for elm in ht_two.map :
        if elm :
            if hash_table.contains(elm.head.data[0]):
                hash_table.add(elm.head.data[0], [ht_one.get(elm.head.data[0]),elm.head.data[1]])

    return hash_table


if __name__ == "__main__":
    
  ht_one = HashTable()
  ht_one.add('fond', 'enamored')
  ht_one.add('wrath', 'anger')
  ht_one.add('diligent', 'employed')
  ht_one.add('guide', 'garp')
  ht_one.add('outfit', 'usher')
  ht_two = HashTable()
  ht_two.add('fond', 'averse')
  ht_two.add('wrath', 'delight')
  ht_two.add('diligent', 'idle')
  ht_two.add('guide', 'follow')
  ht_two.add('flow', 'jam')
    
  print(left_join_hash(ht_one, ht_two))