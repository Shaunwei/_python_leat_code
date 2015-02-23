from helper import *


@timeit
def find_intersection_point(head1, head2):
    '''
    args: head1, head2, the head of linked list
    return: Node, intersection point if find
            None, if not find
    algorithm:
        space O(1), time O(n + m)
        bf algorithm will spend n^2 time to find intersection
        1. spend n + m time to find same length node from this node
        to the last one, with comparison.
        2. then check each two nodes till the end. most O(n)

    @TOREAD: ALWAYS DO ITERATION FOR WHILE LOOP FIRST
    LIKE -= 1 OR += 1 OR A = A.NEXT
    '''
    intersection = None

    def get_length(head):
        res = 0
        while head:
            res += 1
            head = head.next
        return res

    length1 = get_length(head1)
    length2 = get_length(head2)

    if not length1 or not length2:
        return None

    # cur_h1 always point at shorter length ll
    len_diff = abs(length1 - length2)
    if length1 > length2:
        cur_h1 = head2
        cur_h2 = head1
    else:
        cur_h1 = head1
        cur_h2 = head2

    # move pointer at the same length till the end
    while len_diff > 0:
        if cur_h1.val == cur_h2.val:
            intersection = cur_h1
            break
        cur_h2 = cur_h2.next
        len_diff -= 1

    if intersection:
        return intersection

    # compare till end, they have the same length
    while cur_h1:
        if cur_h1.val == cur_h2.val:
            intersection = cur_h1
            break
        cur_h1, cur_h2 = cur_h1.next, cur_h2.next

    if intersection:
        return intersection
    else:
        return None


@timeit
def find_intersection_point_bf(head1, head2):
    '''
    brute force
    O(n^2)
    PLEASE DO:CENTROLIZED RETURN!!
    '''
    res = None
    cur_h1 = head1
    while cur_h1:
        cur_h2 = head2
        while cur_h2:
            if cur_h1.val == cur_h2.val:
                res = cur_h2
                break
            cur_h2 = cur_h2.next
        # this is needed. or the return will be the last
        # found value
        if res:
            break
        cur_h1 = cur_h1.next

    if cur_h1 is not None and res is None:
        res = cur_h1

    return res


if __name__ == '__main__':
    # case 1
    head1 = build_llist([29, 23, 82, 11])
    head2 = build_llist([13, 4, 18, 12])
    assert None == find_intersection_point_bf(head1, head2)

    # case 2
    head1 = build_llist([29, 23, 82, 12, 27])
    head2 = build_llist([13, 4, 12, 27])
    node = find_intersection_point_bf(head1, head2)
    assert node.val == 12

    # case 3
    head1 = build_llist([29, 23, 82, 11])
    head2 = build_llist([13, 4, 18, 12])
    assert None == find_intersection_point(head1, head2)

    # case 4
    head1 = build_llist([29, 23, 82, 12, 27])
    head2 = build_llist([13, 4, 12, 27])
    node = find_intersection_point(head1, head2)
    assert node.val == 12
