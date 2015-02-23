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

    p_two_step = head
    p_one_step = head
    # IT HAS NEXT BUT JUST NEXT IS NONE
    # while p_two_step:
    #     if getattr(p_two_step, 'next') is not None and \
    #             getattr(p_two_step.next, 'next') is not None:
    #         p_two_step = p_two_step.next.next
    #         p_one_step = p_one_step.next
    #     else:
    #         break
    # return p_one_step
    p_two_step = p_two_step.next.next
    while p_two_step:
        p_one_step = p_one_step.next
        try:
            p_two_step = p_two_step.next.next
        except:
            print 123
            return p_one_step
    return p_one_step


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
