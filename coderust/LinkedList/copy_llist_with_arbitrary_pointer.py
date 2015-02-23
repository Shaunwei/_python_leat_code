from helper import *


# time: O(2n), space: O(n)
def copy_llist_with_arbitrary_pointer(head):
    new_head = None

    cur_old = head
    cur_new = None

    index_dict = {}

    while cur_old:
#        index_dict[cur_old.val] = (cur_old, cur_old.arb_p)
        node = Node(cur_old.val)
        # save arb_p value to trace back
        if cur_old.arb_p:
            index_dict[node.val] = (node, cur_old.arb_p.val)
        else:
            # consider the arb_p is None
            index_dict[node.val] = (node, None)

        if not new_head:
            # first iteration
            new_head = cur_new = node
            cur_old = cur_old.next
            continue

        cur_new.link(node)
        cur_new = cur_new.next
        cur_old = cur_old.next

    # copy pointers
    for val, (cur_head, arb_p) in index_dict.iteritems():
        if arb_p:
            cur_head.arb_p = index_dict.get(arb_p, None)
        else:
            cur_head.arb_p = None
    return new_head


if __name__ == '__main__':
    head = build_llist([7, 14, 21])

    head.arb_p = head.next.next
    head.next.arb_p = None
    head.next.next.arb_p = head

    func = lambda x: str(x.arb_p) + ' is Arbitrary Pointer from ' + str(x)

    print_llist(head, func)

    pro_head = copy_llist_with_arbitrary_pointer(head)
    print_llist(head, func)
