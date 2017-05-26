
from abc import ABCMeta, abstractmethod
from node import Node
from singlytest import SinglyLinkedList

class Stack(SinglyLinkedList):

    def empty(self):
        #self.size()
        if self.size() == 0: 
            #self.head is None:
            print("List is empty")
            return True
        else: 
            print("List is not empty")
            return False

    def push(self, data):
        self.insert(data)
       # oldhead = self.head
       # new_head = Node(data)
       # new_head.next = oldhead
       # self.head = new_head
        

    def pop(self):
        #self.head = self.head.next
        self.delete(self.head.data)
