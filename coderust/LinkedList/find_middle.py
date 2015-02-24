from helper import *


def find_middle(head):
    '''
    arg: head is linked list node
    return: the middle node, if has one
        return None
    algorithm: two pointers
    1. two iterates two node at at time
        if two does not have the next (next)
        then the one pointer point at the middle
    2. one iterates one node at a time
    '''
    if not head or not head.next:
        return head

    # p_two_step = head
    # p_one_step = head
    # # IT HAS NEXT BUT JUST NEXT IS NONE
    # # while p_two_step:
    # #     if getattr(p_two_step, 'next') is not None and \
    # #             getattr(p_two_step.next, 'next') is not None:
    # #         p_two_step = p_two_step.next.next
    # #         p_one_step = p_one_step.next
    # #     else:
    # #         break
    # # return p_one_step
    # while p_two_step and p_two_step.next:
    #     p_one_step = p_one_step.next
    #     try:
    #         p_two_step = p_two_step.next.next
    #     except:
    #         return p_one_step
    # return p_one_step
    slow_head = fast_head = head
    while fast_head.next and fast_head.next.next:
        slow_head = slow_head.next
        fast_head = fast_head.next.next
    return slow_head


def merge(head1, head2):
    '''
    dummy_head is dummy at the top
    will not be returned at the end
    just for reference
    '''
    dummy_head = cur_head = Node(0)
    while head1 and head2:
        if head1.val < head2.val:
            cur_head.next = head1
            head1 = head1.next
        else:
            cur_head.next = head2
            head2 = head2.next
        cur_head = cur_head.next
    else:
        if head1:
            cur_head.next = head1
        if head2:
            cur_head.next = head2
    return dummy_head.next

if __name__ == '__main__':
    # case 1
    print 'case 1'
    head = build_llist([1, 2, 3, 4, 5])
    node = find_middle(head)
    assert node.val == 3

    # case 2
    print 'case 2'
    head = build_llist([1, 2, 3, 4, 5, 6])
    node = find_middle(head)
    assert node.val == 3

    head1 = build_llist([1, 3, 4])
    head2 = build_llist([2, 5, 6])
    print_llist(merge(head2, head1))
