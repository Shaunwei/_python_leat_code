'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
'''
from utils import print_ll
from utils import build_ll
from utils import Node


def reverse(prev, head, tail):
    curt = head
    while curt is not tail:
        temp = curt.next
        curt.next = prev.next
        prev.next = curt
        curt = temp
    head.next = tail


def reverse_k(head, k):
    prev = dummy = Node(-1)
    curt = dummy.next = head

    while True:
        tail = curt
        for _ in range(k):
            if not tail:
                return dummy.next
            tail = tail.next

        reverse(prev, curt, tail)
        curt.next = tail
        prev = curt
        curt = tail


if __name__ == '__main__':
    head = build_ll([1, 2, 3, 4, 5])
    print_ll(reverse_k(head, 2))
    head = build_ll([1, 2, 3, 4, 5])
    print_ll(reverse_k(head, 3))
