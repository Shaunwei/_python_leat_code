from helper import *


def reverse_llist_rec(head):
    if not head.next:
        return head, None
    else:
        rev_head, tail = reverse_llist_rec(head.next)

    if not tail:
        rev_head.next = head
    else:
        tail.next = head
    head.next = None
    return rev_head, head


def reverse_llist_iter(head):
    rev_head = None
    cur = head
    while cur:
        cur = cur.next
        head.next = rev_head
        rev_head = head
        head = cur
    return rev_head

if __name__ == '__main__':
    # iter
    array = [7, 14, 21, 28]
    head = build_llist(array)
    final_head = build_llist(array[::-1])

    res_head = reverse_llist_iter(head)
    print_llist(res_head)
    print_llist(final_head)
    print(res_head == final_head)

    # rec
    array = [7, 14, 21, 28]
    head = build_llist(array)
    final_head = build_llist(array[::-1])

    res_head = reverse_llist_rec(head)[0]
    print_llist(res_head)
    print_llist(final_head)
    print(res_head == final_head)
