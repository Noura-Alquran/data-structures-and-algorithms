import re

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



# def first_repeated_word(string):
#     # split_words =[]
#     # temp = ''
#     # for i in string:
#     #     if i == ' ':
#     #         split_words+=[temp.lower()]
#     #         temp = ''
#     #     else:
#     #         temp += i
#     # if temp:
#     #     split_words+=[temp.lower()]
#     # # print(split_words)
#     # lists=[]
#     # for key in split_words:
#     #     if key in lists:
#     #         return f"First repeated word is -> {key}"
#     #     else:
#     #         lists+=[key]


def first_repeated_word(string):
  if string =="":
    return 'empty string'
  strings=re.sub(r'[^\w\s]','',string).lower().split(' ')
  hash_map =HashTable()
  for word in strings:
    if hash_map.contains(word):
      return word
    else:
      hash_map.add(word,1)
  return 'no repeated word'




if __name__ == "__main__":
    str1="Once upon a time, there was a brave princess who..."
    print(first_repeated_word(str1))
    str2="It was the best of times , it was the worst of times , it was the age of wisdom , it was the age of foolishness , it was the epoch of belief , it was the epoch of incredulity , it was the season of Light , it was the season of Darkness , it was the spring of hope , it was the winter of despair , we had everything before us , we had nothing before us , we were all going direct to Heaven , we were all going direct the other way – in short , the period was so far like the present period , that some of its noisiest authorities insisted on its being received , for good or for evil , in the superlative degree of comparison only..."
    print(first_repeated_word(str2))
    str3="It was a queer, sultry summer , the summer they electrocuted the Rosenbergs , and I didn’t know what I was doing in New York..."
    print(first_repeated_word(str3))
