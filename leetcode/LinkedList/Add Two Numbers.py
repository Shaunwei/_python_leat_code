'''
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''
from utils import build_ll
from utils import print_ll
from utils import Node

def add_two(l1, l2):
    curt = dummy = Node(-1)

    carry = 0
    while l1 or l2:
        v1 = v2 = 0
        if l1:
            v1 = l1.val
            l1 = l1.next
        if l2:
            v2 = l2.val
            l2 = l2.next
        val = (v1 + v2 + carry) % 10
        carry = (v1 + v2 + carry) // 10
        curt.next = Node(val)
        curt = curt.next

    if carry:
        curt.next = Node(carry)
    return dummy.next


if __name__ == '__main__':
    l1 = build_ll([2, 4, 3])
    l2 = build_ll([5, 6, 4])
    print_ll(add_two(l1, l2))