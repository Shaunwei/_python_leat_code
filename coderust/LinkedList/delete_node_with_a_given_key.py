from helper import *


def delete_node(head, target):
    # node could be at top or anywhere
    # TOREAD: need to consider at edges!
    # TOREAD: !! what if more than one target
    # need to verify!!
    if not head:
        return

    if head.val == target:
        cur = head.next
        head.next = None
        return cur

    # top case processed
    pre = head
    cur = head.next
    while cur:
        if cur.val == target:
            pre.next = cur.next
            cur = cur.next
        else:
            # advance
            pre, cur = pre.next, cur.next
    return head


if __name__ == '__main__':
    # case 1
    array = [70, 10, 55, 22]
    final_array = [70, 10, 22]
    org_head = build_llist(array)
    final_head = build_llist(final_array)

    pro_head = delete_node(org_head, 55)

    print_llist(final_head)
    print_llist(pro_head)
    print(pro_head == final_head)

    # case 2
    array = [70, 10, 55, 22]
    final_array = [10, 55, 22]
    org_head = build_llist(array)
    final_head = build_llist(final_array)

    pro_head = delete_node(org_head, 70)

    print_llist(final_head)
    print_llist(pro_head)
    print(final_head == pro_head)
