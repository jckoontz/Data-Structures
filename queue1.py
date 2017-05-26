from abc import ABCMeta, abstractmethod
from node import Node
from doublylinkedlist import DoublyLinkedList

class Queue(DoublyLinkedList):

    def __init__(self): 
        self.length = 0
        self.head = None
        self.tail = None

    def empty(self):
        pass

    #Push = enqueue
    def push(self, data):
        new_node = Node(data)
        new_node.next = None
        if self.head == None: 
            self.head == new_node
            self.tail == new_node
        else: 
            self.tail.next = new_node #add new node to the end of queue
            new_node.prev = self.tail #sets previous pointer to old tail
            self.tail = new_node #tail is now the new node
    
    #Pop = dequeue == remove and return the first item in queue 
    def pop(self):
        data = self.head.data #store data from head node 
        self.head = self.head.next #declare new head node
        return data
        
