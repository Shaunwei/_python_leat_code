import time


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


def timeit(func=None, loops=1, verbose=False):
    if func is not None:
        def inner(*args, **kwargs):
            sums = 0.0
            mins = 1.7976931348623157e+308
            maxs = 0.0
            print '====%s Timing====' % func.__name__
            for i in range(0, loops):
                t0 = time.time()
                result = func(*args, **kwargs)
                dt = time.time() - t0
                mins = dt if dt < mins else mins
                maxs = dt if dt > maxs else maxs
                sums += dt
                if verbose is True:
                    print '\t%r ran in %2.9f sec on run %s' % \
                        (func.__name__, dt, i)
            # print '%r min run time was %2.9f sec' % \
            #     (func.__name__, mins)
            # print '%r max run time was %2.9f sec' % \
            #     (func.__name__, maxs)
            # print '%r avg run time was %2.9f sec in %s runs' % \
            #     (func.__name__, sums / loops, loops)
            print '%r total run time was %2.9f sec in %s runs' % \
                (func.__name__, sums, loops)
            print '==== end ===='
            return result
        return inner
    else:
        def partial_inner(func):
            return timeit(func, loops, verbose)
        return partial_inner


def get_length(head, target=None):
    length = 0
    while head:
        if target and head.val == target.val:
            return length
        length += 1
        head = head.next
    return length


if __name__ == '__main__':
    _list = [7, 14, 21, 28]
    head = build_llist(_list)

    print_llist(head)

    print(build_llist([7, 14, 21, 28]) == head)
    print(build_llist([7, 21, 14, 28]) == head)
    print get_length(head)
