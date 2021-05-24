class EmptyQueueException(Exception):
    pass

class Node():
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

    def __str__(self):
        return self.data

    def get_next_node(self):
        return self.next

class Queue():
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)
        if not self.front:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = self.rear.next

    def isEmpty(self):
        if self.front:
            return False
        return True

    def dequeue(self):
        if not self.isEmpty():
            value = self.front.data
            self.front = self.front.next
            return value

        raise EmptyQueueException("queue is empty")


    def peek(self):
        if not self.isEmpty():
            return self.front.data
        raise EmptyQueueException("queue is empty")

    def __str__(self):
        front = self.front
        items = []
        while front:
            items.append(str(front.data))
            front = front.next
        return " ".join(items)

class Cat():
    def __init__(self, name):
        self.name = name
        self.type = "cat"

class Dog():
    def __init__(self, name):
        self.name = name
        self.type = "dog"


class AnimalShelter:
    def __init__(self):
        self.cat = Queue()
        self.dog = Queue()

    def enqueue(self, pet):
        if pet.type == "cat":
            self.cat.enqueue(pet.name)
        elif pet.type == "dog":
            self.dog.enqueue(pet.name)
        else:
            return "only cats and dogs"


    def dequeue(self, pref):
        if pref == "cat":
            self.cat.dequeue()
        elif pref == "dog":
            self.dog.dequeue()
        else:
            return "only cats and dogs"

if __name__ == "__main__":
    dog1 = Dog("boby")
    dog2 = Dog("saso")
    dog3 = Dog("rex")
    dog4 = Dog("laly")

    cat1 = Cat("kitty")
    cat2 = Cat("lucy")
    cat3 = Cat("Mushmush")
    cat4 = Cat("roky")

    animal= AnimalShelter()
    animal.enqueue(dog2)
    animal.enqueue(cat1)
    animal.enqueue(cat2)
    animal.enqueue(cat3)
    
    print(animal.cat)
    print("#"*30)
    animal.dequeue("cat")
    print(animal.cat)
