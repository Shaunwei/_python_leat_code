'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
'''
from utils import print_ll
from utils import build_ll
from utils import Node


def partition(head, k):
    less_head = lcur = Node(-1)
    great_head = gcur = Node(-1)

    while head:
        if head.val < k:
            lcur.next = head
            lcur = lcur.next
        else:
            gcur.next = head
            gcur = gcur.next
        head = head.next

    gcur.next = None
    lcur.next = great_head.next
    return less_head.next


if __name__ == '__main__':
    head = build_ll([1, 4, 3, 2, 5, 2])
    print_ll(partition(head, 3))