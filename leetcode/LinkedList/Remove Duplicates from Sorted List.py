'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
'''
from utils import build_ll
from utils import print_ll

def delete_duplicates(head):
    if not head or not head.next:
        return head

    curt = head
    while curt.next:
        if curt.val == curt.next.val:
            curt.next = curt.next.next
        else:
            curt = curt.next
    return head



if __name__ == '__main__':
    head = build_ll([1, 1, 2, 3, 3])
    print_ll(delete_duplicates(head))