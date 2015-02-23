from helper import *


class AddNode(Node):
    def __add__(self, head):
        head1 = self
        head2 = head
        res = None
        carry = 0
        if not head1 or not head2:
            if not head1:
                return head2
            else:
                return head1

        while head1 and head2:
            val = int(head1.val) + int(head2.val) + carry
            if val / 10:
                # TOREAD: carry is divide not mod!!
                carry = val / 10
                val = val % 10

            node = AddNode(val)
            if res is not None:
                res.link(node)
            else:
                head = node
            # TOREAD: always add advance!!!
            res = node
            head1 = head1.next
            head2 = head2.next
        else:
            # process mode digits
            if head1 and not head2:
                # head2 is None
                # TOREAD: need to carry result!!!
                # pass head, res not just head!!!
                # think: you are linking to res
                # not just head
                node_add_number(head1, res, carry)
            elif head2 and not head1:
                node_add_number(head2, res, carry)
            else:
                res.link(AddNode(carry))
        return head


def node_add_number(head, res, carry):
    while head:
        val = int(head.val) + carry
        if val / 10:
            carry = val / 10
            val = val % 10
        res.link(AddNode(val))
        res = res.next
        head = head.next

if __name__ == '__main__':
    # case 1
    print('case 1')
    value1 = 815
    value2 = 392
    head1 = build_llist(list(str(value1))[::-1], node=AddNode)
    head2 = build_llist(list(str(value2))[::-1], node=AddNode)
    print_llist(head1)
    print_llist(head2)
    print_llist(head1 + head2)

    # case 2
    print('case 2')
    value1 = 0
    value2 = 392
    head1 = build_llist(list(str(value1))[::-1], node=AddNode)
    head2 = build_llist(list(str(value2))[::-1], node=AddNode)
    print_llist(head1)
    print_llist(head2)
    print_llist(head1 + head2)
