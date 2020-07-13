class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node
    
    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value
    
    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_to_tail(self, value):
        new_node = Node(value)
        # if LinkedList is empty, head is None
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
    
    def remove_head(self):
        # return None if there is no head (i.e. the list is empty)
        if not self.head:
            return None
        # if head has no next, then we have a single element in our list
        if not self.head.get_next():  # get a reference to the head
            head = self.head # get a reference to the head
            self.head = None # delete the list's head reference
            self.tail = None # also make sure the tail reference doesn't refer to anything
            return head.get_value()  # return the value
        
        value = self.head.get_value() # otherwise we have more than one element in our list
        self.head = self.head.get_next() # set the head reference to the current head's next node in the list
        return value

    def remove_tail(self):
        # if linked list is empty
        if not self.head:
            return None

        if self.head is self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value
        
        current = self.head

        while current.get_next() is not self.tail:
            current = current.get_next()
        value = self.tail.get_value()
        self.tail = current
        return value

    def contains(self, value):
        if not self.head:
            return False

        # Recursive solution
        # def search(node):
        #   if node.get_value() == value:
        #     return True
        #   if not node.get_next():
        #     return False
        #   return search(node.get_next())
        # return search(self.head)

     # get a reference to the node we're currently at; update this as we traverse the list
        current = self.head

        while current:
        # return True if the current value we're looking at matches our target value
            if current.get_value() == value:
                return True
            current = current.get_next() # update our current node to the current node's next node
        return False # if we've gotten here, then the target node isn't in our list
    
    def get_max(self):
        if not self.head:
            return None
        # reference to the largest value we've seen so far
        max_value = self.head.get_value()
        # reference to our current node as we traverse the list
        current = self.head.get_next()
        # check to see if we're still at a valid list node
        while current:
            # check to see if the current value is greater than the max_value
            if current.get_value() > max_value:
                # if so, update our max_value variable
                max_value = current.get_value()
                # update the current node to the next node in the list
            current = current.get_next()
        return max_value
        
"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# Array as underlying storage structure
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.storage.append(value)
#         self.size += 1

#     def pop(self):
#         if self.size > 0:
#             self.size -= 1
#             return self.storage.pop()
#         else:
#             return None

# Link List implementation:
class Stack(LinkedList):
    def __init__(self):
        super().__init__()
        self.size = 0
        

    def __len__(self):
        return self.size

    def push(self, value):
        self.add_to_tail(value)
        self.size += 1

    def pop(self):
        if self.size > 0:
            self.size -=1
            return self.remove_tail()
        else:
            return None
