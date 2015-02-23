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
        mid = find_middle(head)
        if get_length(head, mid) > 1:
            head = partition(head)
        if get_length(mid.next) > 1:
            mid = partition(mid.next)
        return merge(head, mid)

    def merge(head1, head2):
        new_h = None
        while head1 and head2:
            if head1.val < head2.val:
                if not new_h:
                    new_h = head1
                else:
                    new_h.next = head1
                head1 = head1.next
            else:
                if not new_h:
                    new_h = head2
                else:
                    new_h.next = head2
                head2 = head2.next

        if head1:
            new_h.next = head1
        if head2:
            new_h.next = head2
        return new_h

    return partition(head)


if __name__ == '__main__':
    head = build_llist([29, 23, 82, 11])
    test_head = build_llist([11, 23, 29, 82])
    print_llist(head)
    print_llist(test_head)
    pro_head = merge_sort(head)

    print_llist(pro_head)
