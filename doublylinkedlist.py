from linkedlist import LinkedList
from node import Node

class DoublyLinkedList(LinkedList):

    head = None
    tail = None

    def insert(self, data):
        new_node = Node(data, self.head)
        if self.head is None: 
            self.head = self.tail = new_node
        else: 
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def size(self):
        size = 0
        temp = self.head
        while temp is not None: 
            size += 1
            temp = temp.next
        return size

    def search(self, data):
        current_node = self.head
        while current_node: 
            if current_node.getData() == data: 
                return True
            else: 
                current_node = current_node.getNext()
        return False

    def delete(self, data):
        current_node = self.head
        previous_node = None
        while current_node: 
            if current_node.getData() == data: 
                if prev_node: 
                    prev_node.setNext(current_node.getNext())
                    current_node.next.prev = previous_node
                else: 
                    self.head = self.head.getNext()
                    self.head.prev = None
                #break
            previous_node = current_node
            current_node = current_node.getNext()

    def print_list_forward(self):
        print("Doubly Linked List Data: ")
        current_node = self.head
        while current_node: 
            print(current_node.data)
            current_node = current_node.next
            print("---" * 30)

    def print_backward(self, node): 
        current_node = self.tail
        while current_node is not None: 
            print(current_node.data)
            current_node = current_node.prev
