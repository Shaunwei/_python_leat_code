from helper import *


def reverse_even_nodes(head):
    '''
    return reversed head
    algorithm:
        1. pop even nodes into stack
        2. insert nodes back in even positions from stack
        (stack first in last out, reversed)
    '''
    cur = head
    _stack = []
    # process it when it has even number
    while cur and cur.next:
        _stack.append(cur.next)
        cur.next = cur.next.next
        # TOREAD: REMEMBER TO ADVANCE POINTER!!!!
        cur = cur.next

    cur = head
    while _stack:
        node = _stack.pop()
        node.next = cur.next
        cur.next = node
        cur = cur.next.next

    return head


if __name__ == '__main__':
    head = build_llist([7, 14, 21, 28, 9])
    test_head = build_llist([7, 28, 21, 14, 9])

    pro_head = reverse_even_nodes(head)
    print_llist(pro_head)

    assert pro_head == test_head
