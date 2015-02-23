from helper import *


def get_nth_from_last_node(head, n):
    n_node = head
    while n and head:
        n -= 1
        head = head.next
    if not head:
        return 0

    while head:
        head = head.next
        n_node = n_node.next
    return n_node.val


if __name__ == '__main__':
    head = build_llist([7, 14, 21, 28, 9])
    print 'case 1'
    assert 0 == get_nth_from_last_node(head, 10)
    print 'case 1 passed.'

    print 'case 2'
    assert 28 == get_nth_from_last_node(head, 2)
    print 'case 2 passed.'
