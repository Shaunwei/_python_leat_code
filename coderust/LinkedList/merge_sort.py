from helper import *
from find_middle import find_middle


def merge_sort(head):
    '''
    arg: head is linked list head
    return: sorted linked list
    algorithm:
        using merge sort
        divide and conquer
        1. recursively partition linked list into two parts,
            till it has one node each
        2. merge nodes in non-decreasing order
    '''
    def partition(head):
        if get_length(head) <= 1:
            return head, head
        # partition into 2 parts
        pre_mid = find_middle(head)
        mid = pre_mid.next
        pre_mid.next = None
        return head, mid

    def merge(head1, head2):
        # new_h = None
        # while head1 and head2:
        #     if head1.val < head2.val:
        #         if not new_h:
        #             new_h = head1
        #         else:
        #             new_h.next = head1
        #         head1 = head1.next
        #     else:
        #         if not new_h:
        #             new_h = head2
        #         else:
        #             new_h.next = head2
        #         head2 = head2.next

        # if head1:
        #     new_h.next = head1
        # if head2:
        #     new_h.next = head2
        # return new_h
        # TOREAD: THE DUMMY HEAD IS NOT RETURNED
        # JUST USE AS REFERENCE
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

    if not head or not head.next:
        return head

    head, mid = partition(head)
    return merge(merge_sort(head), merge_sort(mid))


if __name__ == '__main__':
    head = build_llist([29, 23, 82, 11])
    test_head = build_llist([11, 23, 29, 82])
    pro_head = merge_sort(head)

    print_llist(pro_head)

    print 'case 1'
    assert pro_head == test_head
    print 'test passed.'
