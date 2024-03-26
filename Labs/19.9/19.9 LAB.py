    def insert(self, number):
        # Type your code here.
        new_node = Node(number)
        
        if self.head is None: # Empty list
            self.head = new_node
            self.tail = new_node
            pass
        
        if number < self.head.get_data():
            new_node.set_next(self.head)
            self.head.prev = new_node
            self.head = new_node
            pass
        
        # Traverse
        current_node = Node(self.head)
        #current_node = self.head # Beginning
        # While loop breaks when valid get_data() is found
        while current_node.get_next() is not None and current_node.get_next().get_data() < number: # None means end
            current_node = current_node.get_next() # Go to get_next() node
        
        new_node.set_next(current_node.get_next())
        # Insert new_node between current_node and current_node.get_next()
        if current_node.get_next() is not None: # Current position isnt at the end
            current_node.get_next().prev = new_node
        else: # If it is at the end, make it the tail
            self.tail = new_node
        new_node.prev = current_node
        current_node.get_next() = new_node
        pass