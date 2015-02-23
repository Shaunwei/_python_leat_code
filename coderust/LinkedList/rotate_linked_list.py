from helper import *


def rotate(head, n):
    '''
    args: head is linked list
        n is integer + -
    return: head
    algorithm:
        1. normalize n in [0, length of linked list]
            4 % 5 == 4, -2 % 5 == 3, 3 % 5 == 3
        2. connect head to tail
        3. break at normalized n
        (step 2 and 3 exchange order could improve algorithm)
    '''
    length = get_length(head)

    if not head or not head.next:
        return head

    # rotate at the beginning counting
    # easier to calculate
    n = length - n % length
    # find rotation point and keep pre to break connection
    pre = head
    cur = head.next

    # already cur at next once
    while n > 1:
        cur = cur.next
        pre = pre.next
        n -= 1

    # get to tail node
    tail = cur
    # TOREAD:
    # this is wrong! I NEED THE LAST ELEMENT WITH VALUE
    # while tail:
    while tail.next is not None:
        tail = tail.next

    # connect head to tail and break old connection
    tail.next = head
    pre.next = None

    return cur


if __name__ == '__main__':
    print 'case 1'
    head = build_llist([1, 2, 3, 4, 5])
    test_head = build_llist([4, 5, 1, 2, 3])
    pro_head = rotate(head, 2)
    print_llist(pro_head)
    assert pro_head == test_head
    print 'case 1 passed.'

    print 'case 2'
    head = build_llist([1, 2, 3, 4, 5])
    test_head = build_llist([4, 5, 1, 2, 3])
    pro_head = rotate(head, 7)
    print_llist(pro_head)
    assert pro_head == test_head
    print 'case 2 passed.'

    print 'case 3'
    head = build_llist([1, 2, 3, 4, 5])
    pro_head = rotate(head, -2)
    test_head = build_llist([3, 4, 5, 1, 2])
    print_llist(pro_head)
    assert pro_head == test_head
    print 'case 3 passed.'
