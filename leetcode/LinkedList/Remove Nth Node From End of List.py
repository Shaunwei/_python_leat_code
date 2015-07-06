'''
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
'''
from utils import build_ll
from utils import print_ll
from utils import Node


def remove_nth_from_end(head, n):
    if not head:
        return head

    curt = prev = dummy = Node(-1)
    dummy.next = head

    for _ in range(n):
        curt = curt.next

    while curt.next:
        curt = curt.next
        prev = prev.next
    prev.next = prev.next.next
    return dummy.next


if __name__ == '__main__':
    head = build_ll([1, 2, 3, 4, 5])
    print_ll(remove_nth_from_end(head, 2))