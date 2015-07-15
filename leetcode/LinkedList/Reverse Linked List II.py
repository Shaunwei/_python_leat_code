'''
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
'''
from utils import *

def reverse_btw(head, m, n):
    prev = dummy = Node(-1)
    dummy.next = head

    for _ in range(m - 1):
        prev = prev.next
    tail = curt = prev.next
    for _ in range(n - m + 1):
        tail = tail.next

    prev.next = tail
    while curt is not tail:
        temp = curt.next
        curt.next = prev.next
        prev.next = curt
        curt = temp
    return dummy.next


if __name__ == '__main__':
    head = build_ll([1, 2, 3, 4, 5])
    print_ll(reverse_btw(head, 2, 4))