'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
'''
from utils import build_ll
from utils import print_ll
from utils import Node


def remove_duplicates_II(head):
    if not head or not head.next:
        return head

    prev = dummy = Node(-1)
    curt = head
    is_dup = False
    while curt.next:
        if curt.val == curt.next.val:
            curt.next = curt.next.next
            is_dup = True
        else:
            if is_dup:
                prev.next = curt.next
            else:
                prev.next = curt
                prev = prev.next
            curt = curt.next
            is_dup = False
    if is_dup:
        prev.next = None
    return dummy.next


if __name__ == '__main__':
    head = build_ll([1, 1, 2, 3, 3])
    print_ll(remove_duplicates_II(head))