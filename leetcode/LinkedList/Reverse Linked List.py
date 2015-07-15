'''
Reverse a singly linked list.
'''
from utils import *


def reverse_rec(head):
    if not head or not head.next:
        return head

    new_head = reverse_rec(head.next)

    tail = head.next
    head.next = tail.next
    tail.next = head
    return new_head

def reverse_iter(head):
    curt = dummy = Node(-1)
    while head:
        temp = head.next
        head.next = curt.next
        curt.next = head
        head = temp
    return dummy.next

if __name__ == '__main__':
    head = build_ll([1, 2, 3, 4])
    print_ll(reverse_rec(head))
    head = build_ll([1, 2, 3, 4])
    print_ll(reverse_iter(head))