"""
Find Middle of the Linked List
Last Updated : 04 Sep, 2024
Given a singly linked list, the task is to find the middle of the linked list. If the number of nodes are even, then there would be two middle nodes, so return the second middle node.

https://www.geeksforgeeks.org/write-a-c-function-to-print-the-middle-of-the-linked-list/
"""

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


def get_length(head):
    length = 0

    while head:
        length += 1
        head = head.next

    return length


def get_middle(head):
    
    length = get_length(head)

    mid_index = length // 2
    while mid_index:
        head = head.next
        mid_index -= 1
    
    return head.value
    

def main():
    
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(50)
    head.next.next.next.next.next = Node(60)

    print(get_middle(head))



if __name__ == "__main__":
    main()