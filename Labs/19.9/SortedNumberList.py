from Node import Node

class SortedNumberList:
    def __init__(self,):
        self.head = None
        self.tail = None    

    # Inserts the number into the list in the correct position such that the
    # list remains sorted in ascending order.
    def insert(self, number):
        # Type your code here.
        new_node = Node(number)
        
        if self.head is None:
            new_node.set_next(self.head)
            self.head = new_node
 
        elif self.head.get_data() >= new_node.get_data():
            new_node.set_next(self.head)
            self.head = new_node
            
        else:
            current_node = self.head
            while current_node.get_next() is not None and current_node.get_next().get_data() < new_node.get_data():
                current_node = current_node.get_next()
             
            new_node.set_next(current_node.get_next())
            current_node.set_next(new_node)
        pass

    # Removes the node with the specified number value from the list. Returns
    # True if the node is found and removed, False otherwise.
    def remove(self, number):
        # Type your code here.
        current_node = self.head
        
        if current_node is not None:
            if current_node.get_data() == number:
                self.head = current_node.get_next()
                current_node = None
                return True
        while current_node is not None:
            if current_node.get_data() == number:
                break
            previous_node = current_node
            current_node = current_node.get_next()
            
        if current_node == None:
            return False
        previous_node.set_next(current_node.get_next())
        current_node = None
        return True
        pass

    # Add any helper methods needed here
