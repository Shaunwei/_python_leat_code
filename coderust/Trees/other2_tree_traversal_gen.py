#!/usr/bin/env python3
'''
Tree:
 100
|    \
50    200
| \     |  \
25 75  125  350
'''


# original way of in order traversal
def in_order(root):
    if not root:
        return

    print(root, end=', ')
    in_order(root.left)
    in_order(root.right)


# Pythonic way of doing tree traversal
def in_order_py2(root):
    '''
    python2 syntax
    Traverse node, then left child, then right child
    '''
    if not root:
        return

    yield root
    for node in in_order_py2(root.left):
        yield node

    for node in in_order_py2(root.right):
        yield node


def in_order_py3(root):
    '''
    python3 syntax
    Traverse node, then left child, then right child
    '''
    if not root:
        return

    yield root
    yield from in_order_py3(root.left)
    yield from in_order_py3(root.right)


# helper functions and class
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        if self.left and self.right:
            msg = '<Tree Node: %s>'
        else:
            msg = '<Leaf Node: %s>'
        return msg % str(self.val)


def build_tree(int_list):
    # params: int list
    # return: root
    # algorithm:
    #   for all tree node
    #   - left child is at position: 2n + 1
    #   - right child is at position: 2n + 2
    tree_list = [TreeNode(x) if isinstance(x, int) else None for x in int_list]
    length = len(int_list)
    for index, node in enumerate(tree_list):
        l_index = 2 * index + 1
        r_index = 2 * index + 2
        if l_index < length:
            node.left = tree_list[l_index]
        if r_index < length:
            node.right = tree_list[r_index]
    return tree_list[0]


if __name__ == '__main__':
    tree = build_tree([100, 50, 200, 25, 75, 125, 350])

    print('original way:')
    in_order(tree)
    print('')

    print('Pythonic ways:')
    for x in in_order_py3(tree):
        print(x, end=', ')
    print('')

    for x in in_order_py2(tree):
        print(x, end=', ')
    print('')
