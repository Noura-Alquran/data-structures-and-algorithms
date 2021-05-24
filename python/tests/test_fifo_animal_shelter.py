from code_challenges.fifo_animal_shelter.fifo_animal_shelter import Cat,Dog,AnimalShelter,EmptyQueueException
import pytest


def test_cat_enqueue():
    expected = "kitty"
    cat1=Cat('kitty')
    animal_sh=AnimalShelter()
    animal_sh.enqueue(cat1)
    actual = f"{animal_sh.cat}"
    assert actual == expected

def test_dog_enqueue():
    expected = "Bobi"
    dog1=Dog('Bobi')
    animal_sh=AnimalShelter()
    animal_sh.enqueue(dog1)
    actual = f"{animal_sh.dog}"
    assert actual == expected

def test_queue_cat_multiple_enqueue(queue_cat_test):
    expected = "kitty lucy sabi radi"
    actual = f"{queue_cat_test}"
    assert actual == expected

def test_queue_dog_multiple_enqueue(queue_dog_test):
    expected = "bobi sasi soso lulu"
    actual = f"{queue_dog_test}"
    assert actual == expected

def test_queue_cat_dequeue(queue_cat_test):
    expected = 'kitty'
    actual = queue_cat_test.dequeue()
    assert actual == expected

def test_queue_dog_dequeue(queue_dog_test):
    expected = 'bobi'
    actual = queue_dog_test.dequeue()
    assert actual == expected

def test_queue_cat_multiple_dequeue(queue_cat_test):
    for num in range(4):
        queue_cat_test.dequeue()
    with pytest.raises(EmptyQueueException):
        queue_cat_test.dequeue()

def test_queue_dog_multiple_dequeue(queue_dog_test):
    for num in range(4):
        queue_dog_test.dequeue()
    with pytest.raises(EmptyQueueException):
        queue_dog_test.dequeue()


@pytest.fixture
def queue_cat_test():
    cat1=Cat('kitty')
    cat2=Cat('lucy')
    cat3=Cat('sabi')
    cat4=Cat('radi')

    cats=AnimalShelter()
    cats.enqueue(cat1)
    cats.enqueue(cat2)
    cats.enqueue(cat3)
    cats.enqueue(cat4)
    return cats.cat

@pytest.fixture
def queue_dog_test():
    dog1=Dog('bobi')
    dog2=Dog('sasi')
    dog3=Dog('soso')
    dog4=Dog('lulu')

    dogs=AnimalShelter()
    dogs.enqueue(dog1)
    dogs.enqueue(dog2)
    dogs.enqueue(dog3)
    dogs.enqueue(dog4)
    return dogs.dog
