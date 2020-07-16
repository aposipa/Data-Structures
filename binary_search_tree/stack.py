# import sys
# sys.path.insert(1, '../stack/')
from linkedlist import LinkedList


class Stack(LinkedList):
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def len(self):
        return self.size

    def push(self, value):
        self.size += 1
        self.storage.add_to_head(value)

    def pop(self):
        if self.size:
            self.size -= 1
            return self.storage.remove_head()