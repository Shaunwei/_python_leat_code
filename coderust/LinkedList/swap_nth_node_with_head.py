from helper import *


def swap_nth_node_with(head, n):
    '''
    algorithm:
        1. find nth node # move n-1 time
            (keep with pre node)
        2. swap with head
            keep head.next
            add head in position
            perpend nth node to head.next node
    '''
    if not head or not head.next:
        return head

    if n < 0:
        return head

    pre = head
    cur = head.next
    # moved once at cur == head.next
    #
    while cur is not None and n - 1 > 1:
        n -= 1
        cur = cur.next
        pre = pre.next

    if not cur:
        return None

    # swap with head
    head_next = head.next
    head.next = cur.next
    pre.next = head
    cur.next = head_next

    head = cur
    return head


if __name__ == '__main__':
    head = build_llist([7, 14, 21, 28, 9])
    test_head = build_llist([28, 14, 21, 7, 9])

    print 'case 1'
    pro_head = swap_nth_node_with(head, 4)  # 28 in this case
    assert pro_head == test_head
    print 'test case 1 passed.'
