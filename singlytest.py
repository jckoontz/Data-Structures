from linkedlist import LinkedList
from node import Node # Kim: In line 7, Node instance is created so Node must be imported from node.py 

class SinglyLinkedList(LinkedList):

    #TODO: Add a line such that you can return 1 for the class method defined in linkedlist.py. This is to try to pass the test cases under '#Test 1' in test_cases_sll.py.

    def insert(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def size(self):
        size = 0
        temp = self.head
        while temp is not None: 
            size += 1
            temp = temp.next
        #print("Size of LinkedList = ", size)
        return size # Kim: size variable is returned instead of being printed. It's good practice (more useful) to return instead of printing. Also, by returning we can pass the assert statements in the test cases since the assert statement compares two values.

    def search(self, data):
        current_node = self.head
        while current_node: 
            if current_node.getData() == data: 
                return True
                #Kim: Originally you had return data which is correct. But again in order to pass the assert statement I changed to return a boolean.
            else: 
             current_node = current_node.getNext()   
        return False # Kim: Same reason.

    def delete(self, data):
        current_node = self.head
        previous_node = None
        while current_node: 
            if current_node.getData() == data:
                if previous_node:
                #Kim: Originally you had if prev_node:. But I think it was a typo since prev_node was not initialized but previous_node was.
                    previous_node.setNext(current_node.getNext())
                    #Kim: Originally you had prev_node.setNext(current_node.getNext()). Same typo here.
                else: 
                    self.head = current_node
            previous_node = current_node
            current_node = current_node.getNext()

    def print_list_forward(self):
        print("Singly Linked List Data: ")
        current_node = self.head
        #Kim: Originally you had current_node - self.head. I think this was a typo as well.
        while current_node: 
            print(current_node.data),
            #Kim: Originally you had print(current_node.data). This is correct but I just added the above line for you to see printing with commas, which doesn't add a newline. I just wanted you to see that you can print this way :)
            current_node = current_node.next
            #Kim: Originally you had print("---" * 30) here.

        #TODO: It may be helpful to create a 'helper function' that you can recurse on. Try to implement this function below that recurses until the end of the list and then prints. This way you continuously call until you reach the end of the list, then print as you return back to the front of the list. 
    def print_backward(self, node):
        #TODO: Check if 'node' exists
        if node:
            self.print_backward(node.next)
            print(node.data)
        #TODO: Recurse on the next node
            
        #TODO: Print the data on that node
        #pass

    def print_list_backward(self):
        self.print_backward(self.head)
        #Kim: I added this line to get you started 
