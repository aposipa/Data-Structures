# import sys
# sys.path.insert(1, '../queue/')
from linkedlist import LinkedList

class Queue(LinkedList):
    def __init__(self):
        self.storage = LinkedList()
        self.size = 0
        
    
    def len(self):
        return self.size

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size > 0:
            value = self.storage.head.get_value()
            self.storage.remove_head()
            self.size -= 1
            return value
        else: 
            return None
