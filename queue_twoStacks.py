from abc import ABCMeta, abstractmethod
from node import Node
from singlytest import SinglyLinkedList
from stack1 import Stack

class Queue_twoStacks(Stack):
    #construct two stacks 
    def __init__(self): 
        self.length = 0
        self.stack_1 = Stack()
        self.stack_2 = Stack()
    
    def empty(self):
        if self.size() == 0:                                               
            print("List is empty")
            return True
        else:
            print("List is not empty")
            return False

    def push(self, data): 
        self.stack_1.push(data)
        
    def pop(self): 
        if stack_1.empty() != True: 
            while stack_1.empty() != True: 
                self.stack_2.push(self.stack_1.pop())
            result = self.stack_2.pop()
            return result 

"""if stack1 is empty: 
currentstacl = stack2 
then recycle stack1 method 
"""


    
