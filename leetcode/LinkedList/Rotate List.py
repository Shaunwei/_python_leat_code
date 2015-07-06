'''
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
'''
from utils import print_ll
from utils import build_ll
from utils import Node


def rotate(head, k):
    if not head or not k:
        return head

    tail = prev = dummy = Node(-1)
    dummy.next = head

    for _ in range(k):
        if not tail:
            return head
        tail = tail.next

    while tail.next:
        prev = prev.next
        tail = tail.next

    new_head = prev.next
    prev.next = None
    tail.next = head
    return new_head




if __name__ == '__main__':
    head = build_ll([1, 2, 3, 4, 5])
    print_ll(rotate(head, 2))