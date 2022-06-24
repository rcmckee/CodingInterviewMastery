"""
Title: Linked List Solutions Part 1

This file contains the template for Linked List Exercise Set #1 in the DS &
Algos Primer. Fill in the exercises here and refer to
linked_list_solutions_part_1.py for the complete code samples.

Execution: python linked_lists_part_1.py
"""

"""
Exercise 1.1: Implement a singly-linked list
"""

"""
Singly linked list class
"""
class SinglyLinkedList:

    """
    A simple singly-linked node class
    """
    class _SinglyLinkedListNode:
        def __init__(self, val=0):
            # INSERT YOUR CODE HERE
            self.value = val
            self.next = None

    """
    Constructor

    Time Complexity:
    Space Complexity:
    """
    def __init__(self):
        # INSERT YOUR CODE HERE # this is different from the above lines 23 - 27 because that was just a node.
        # this is for the entire list.
        self.head = None
        self.length = 0

    """
    Insert new node at the head of the list

    Time Complexity:
    Space Complexity:
    """
    def insert(self, n: int):
        # INSERT YOUR CODE HERE
        # make a new node, then make it the head
        new_Node =  self._SinglyLinkedListNode(n)
        new_Node.next = self.head. # you need to point the new node to the current head before chaning the head
        self.head = new_head
        
        self.length = self.length + 1

    """
    Delete the first occurrence of n from the list

    Time Complexity:
    Space Complexity:
    """
    def delete(self, n: int) -> bool:
        # INSERT YOUR CODE HERE
        
        # find the node to delete
        
        # once it is found, connect the previous node to the node on the other side of the node I am deleting.
        # because this is a singly linked list without a pointer to the previous node, we need to create one and keep track of it.
        prev = None
        curr = self.head
        
        while curr:
            if not prev:
                #account for first node in the list
                if curr.value == prev:
                    self.head = curr.next
                else:
                    prev.next = curr.next
                    
                    self.length = self.length - 1
                    
                    return True
            
            prev = curr
            curr = curr.next
        return False
    """
    Return the number of items in the list

    Time Complexity:
    Space Complexity:
    """
    def size(self) -> int:
        # INSERT YOUR CODE HERE

    """
    Convert the list to a string

    Time Complexity:
    Space Complexity:
    """
    def __str__(self):
        # INSERT YOUR CODE HERE

"""
Exercise 1.2: Implement a doubly-linked list
"""

"""
Doubly linked list class
"""
class DoublyLinkedList:

    """
    A simple doubly-linked node class
    """
    class _DoublyLinkedListNode:
        def __init__(self, val=0):
            # INSERT YOUR CODE HERE

    """
    Constructor

    Time Complexity:
    Space Complexity:
    """
    def __init__(self):
        # INSERT YOUR CODE HERE

    """
    Insert node at the front of the list

    Time Complexity:
    Space Complexity:
    """
    def insert(self, n: int):
        # INSERT YOUR CODE HERE

    """
    Delete the first occurrence of n from the list

    Time Complexity:
    Space Complexity:
    """
    def delete(self, n: int) -> bool:
        # INSERT YOUR CODE HERE

    """
    Return the number of items in the list

    Time Complexity:
    Space Complexity:
    """
    def size(self) -> int:
        # INSERT YOUR CODE HERE

    """
    Convert the list to a string

    Time Complexity:
    Space Complexity:
    """
    def __str__(self):
        # INSERT YOUR CODE HERE

"""
Sample test cases
"""
if __name__ == '__main__':
    # ADD YOUR TEST CASES HERE
