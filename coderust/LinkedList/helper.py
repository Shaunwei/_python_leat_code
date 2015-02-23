class Node:
    def __init__(self, x=None):
        self.val = x
        self.next = None

    def link(self, x):
        if not isinstance(x, Node):
            x = Node(x)
        self.next = x

    def __repr__(self):
        return '[Node: %s]' % str(self.val)

    def __eq__(self, head):
        def compare_rec(head1, head2):
            if head1 is None or head2 is None:
                if head1 != head2:
                    return False
                else:
                    return True
            return head1.val == head2.val and \
                compare_rec(head1.next, head2.next)
        return compare_rec(self, head)


def build_llist(_list, node=Node):
    if not _list:
        return

    head = cur = node(_list[0])
    for val in _list[1:]:
        _node = node(val)
        cur.link(_node)
        cur = _node
    return head


def print_llist(head, func=None):
    while head:
        print head, '-->',
        if func:
            # add this to print arbitrary pointers
            print func(head)
        head = head.next
    print 'None'


if __name__ == '__main__':
    _list = [7, 14, 21, 28]
    head = build_llist(_list)

    print_llist(head)

    print(build_llist([7, 14, 21, 28]) == head)
    print(build_llist([7, 21, 14, 28]) == head)
