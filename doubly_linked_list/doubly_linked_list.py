"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    # creates instance of ListNode with value
        # increment the DLL length attribute

        # if DLL is empty
            # set head and tail to the new node instance

        # if DLL is not empty
            # set new node's next to current head
            # set head's prev value to new node
            # set head to the new node

    def add_to_head(self, value):
        new_node = ListNode(value)
        self.length += 1

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node 
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    # store the value of the head
        # decrement the length of the DLL
        # delete the head
            # if head.next is not None
                # set head.next's prev to None
                # set head to head.next
            # else (if head.next is None)
                # set head to None
                # set tail to None

        # return the value
    def remove_from_head(self):
        prev_head = self.head.value
        self.delete(self.head)
        return prev_head
        # value = self.head.value
        # self.length -= 1
        # self.delete(self.head)

        # if self.head.next is not None:
        #     next.prev = None
        #     self.head.next = None
        #     self.head = self.head.next
        # else:
        #     self.head = None
        #     self.tail = None
        
        # return value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    # creates instance of ListNode with value
        # increment the DLL length attribute

        # if DLL is empty
            # set head and tail to the new node instance

        # if DLL is not empty
            # set new node's prev to current tail
            # set tails's next value to new node
            # set tail to the new node

    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    # store the value of the tail
        # decrement the length of the DLL
        # delete the tail
            # if tail.prev is not None
                # set tail.prev's next to None
                # set tail to tail.prev
            # else (if tail.prev is None)
                # set head to None
                # set tail to None

        # return the value

    def remove_from_tail(self):
        prev_tail = self.tail.value
        self.delete(self.tail)
        return prev_tail
        # value = self.tail.value
        # self.length -= 1
        # self.delete(self.tail)

        # if self.tail.prev is not None:
        #     self.tail.prev = None
        #     self.tail = self.tail.prev
        # else:
        #     self.head = None
        #     self.tail = None
        # return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if not self.head:
            return None
        self.length -= 1
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.head == node:
            self.head = self.head.next
            self.head.prev = None
        elif self.tail == node:
            self.tail = node.prev
            self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev


    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        current = self.head
        max_value = 0
        while current:
            if current.value >= max_value:
                max_value = current.value
            current = current.next
        return max_value