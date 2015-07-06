'''
Merge two sorted linked lists and return it as a new list. The new list should 
be made by splicing together the nodes of the first two lists.
'''

from utils import build_ll
from utils import print_ll
from utils import Node

def merge(l1, l2):
    curt = dummy = Node(-1)

    while l1 and l2:
        if l1.val <= l2.val:
            curt.next = l1
            l1 = l1.next
        else:
            curt.next = l2
            l2 = l2.next
        curt = curt.next

    if l1:
        curt.next = l1
    else:
        curt.next = l2
    return dummy.next


if __name__ == '__main__':
    l1 = build_ll([1, 3, 5])
    l2 = build_ll([2, 4, 6])
    print_ll(merge(l1, l2))