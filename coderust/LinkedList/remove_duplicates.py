from helper import *


def remove_duplicates(head):
    '''
    algorithm: save node val in a hashmap
    1. iterate nodes
        if val not in hashmap, save it

        else next: delete the current(keep pre node)
    '''
    if not head or not head.next:
        return head

    pre = head
    cur = head.next
    visited = {head.val: True}

    while cur:
        if cur.val in visited:
            pre.next = cur.next
        else:
            visited[cur.val] = True

        cur = cur.next
        # TOREAD: DONT FORGET ABOUT ALL POINTER!!
        pre = pre.next

    return head


if __name__ == '__main__':
    head = build_llist([55, 10, 55, 22])
    test_head = build_llist([55, 10, 22])

    pro_head = remove_duplicates(head)
    print_llist(pro_head)
    assert pro_head == test_head
