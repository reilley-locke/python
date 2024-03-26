from Node import Node

class SortedNumberList:
    def __init__(self,):
        self.head = None
        self.tail = None    

    # Inserts the number into the list in the correct position such that the
    # list remains sorted in ascending order.
    def insert(self, number):
        new_node = Node(number)
        
        # If the list is empty, put new number as the tail and head
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        
        current = self.head
        # Traverse 
        # None is the end of the list
        while current.get_next() is not None and number < current.get_next().get_data():
            current = current.get_next()
        
        # Insert the new number once an inbetween is found
        new_node.set_next(current.get_next())
        if current.get_next() is not None: # If it is not the end/null
            #current.get_next().set_previous(new_node)
            current.set_next(new_node)
            new_node.set_previous(current)
        else:
            # If at the end, set the tail to the new number
            self.tail = new_node
        new_node.set_previous(current)
        current.set_next(new_node)
        

    # Removes the node with the specified number value from the list. Returns
    # True if the node is found and removed, False otherwise.
    def remove(self, number):
        # Type your code here.
        pass

    # Add any helper methods needed here
