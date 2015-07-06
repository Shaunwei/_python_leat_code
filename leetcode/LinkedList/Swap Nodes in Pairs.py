'''
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in
 the list, only nodes itself can be changed.
'''
from utils import print_ll
from utils import build_ll
from utils import Node


def rotate(head):
    prev = dummy = Node(-1)
    curt = dummy.next = head
    while curt and curt.next:
        next = curt.next
        temp = next.next

        prev.next = next
        next.next = curt
        curt.next = temp

        prev = curt
        curt = temp

    return dummy.next

if __name__ == '__main__':
    head = build_ll([1, 2, 3, 4])
    print_ll(rotate(head))