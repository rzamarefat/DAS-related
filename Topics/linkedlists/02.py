"""
Given a linked list, the task is to reverse the linked list by changing the links between nodes.

Examples: 

Input: Linked List = 1 -> 2 -> 3 -> 4 -> NULL 
Output: Reversed Linked List = 4 -> 3 -> 2 -> 1 -> NULL


Input: Linked List = 1 -> 2 -> 3 -> 4 -> 5 -> NULL 
Output: Reversed Linked List = 5 -> 4 -> 3 -> 2 -> 1 -> NULL


Input: Linked List = NULL 
Output: Reversed Linked List = NULL


Input: Linked List = 1->NULL 
Output: Reversed Linked List = 1->NULL 
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    

def reverse_list(head):
    curr_node = head
    prev_node = None

    while curr_node:
        next_node = curr_node.next
        curr_node.next = prev_node

        prev_node = curr_node
        curr_node = next_node
    return prev_node

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

if __name__ == "__main__":
    main()
