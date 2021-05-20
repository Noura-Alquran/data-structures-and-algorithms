# Stacks and Queues
* **Stack** is a linear data structure that consists of Nodes. Each Node references the next Node in the stack, but does not reference its previous. It follows a particular order in which the operations are performed.The order may be **LIFO(Last In First Out)** or **FILO(First In Last Out)**.
* **A Queue** is a linear structure which follows a particular order in which the operations are performed. The order is First In First Out **(FIFO)**.
* The difference between stacks and queues is in removing. In a stack we remove the item the most recently added ; in a queue, we remove the item the least recently added.

## Challenge
* Implement a stack and queue using a linked list and test all them operations.

## Approach & Efficiency
### Big O :
* all methods >> O(1)
## Tasks checklist:
- [x] Top-level README “Table of Contents” is updated
- [x] Feature tasks for this challenge are completed
- [x] Unit tests written and passing
- [x] “Happy Path” - Expected outcome
- [x] Expected failure
- [x] Edge Case (if applicable/obvious)
- [x] README for this challenge is complete
- [x] Description, Approach & Efficiency, Solution
- [x] Link to code

## API
* **Stack**:
1. **push** takes any value as an argument and adds a new node with that value to the top of the stack with an O(1) Time performance.
2. **pop** does not take any argument, removes the node from the top of the stack, and returns the node’s value.
   - Should raise exception when called on empty stack
3. **peek** does not take an argument and returns the value of the node located on top of the stack, without removing it from the stack.
   - Should raise exception when called on empty stack
4. **isEmpty** takes no argument, and returns a boolean indicating whether or not the stack is empty.

* **Queue**:
1. **enqueue** takes any value as an argument and adds a new node with that value to the back of the queue with an O(1) Time performance.
2. **dequeue** does not take any argument, removes the node from the front of the queue, and returns the node’s value.
   - Should raise exception when called on empty queue
3. **peek** does not take an argument and returns the value of the node located in the front of the queue, without removing it from the queue.
   - Should raise exception when called on empty queue
4. **isEmpty** takes no argument, and returns a boolean indicating whether or not the queue is empty.


* **PR link** : https://github.com/Noura-Alquran/data-structures-and-algorithms/pull/23
