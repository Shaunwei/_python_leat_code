<<<<<<< Updated upstream
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
=======
def inorder1(root):
    if root.left:
        yield from inorder1(root.left)
    yield root.val
    if root.right:
        yield from inorder1(root.right)


def inorder2(root):
    if not root:
        return

    for node in inorder2(root.left):
        yield node
    yield root.val
    for node in inorder2(root.right):
        yield node


def preorder1(root):
    yield root.val
    if root.left:
        yield from preorder1(root.left)
    if root.right:
        yield from preorder1(root.right)


def preorder2(root):
    if not root:
        return

    yield root.val
    for node in preorder2(root.left):
        yield node
    for node in preorder2(root.right):
        yield node


def postorder1(root):
    if root.left:
        yield from postorder1(root.left)
    if root.right:
        yield from postorder1(root.right)
    yield root.val


def postorder2(root):
    if not root:
        return

    for node in postorder2(root.left):
        yield node
    for node in postorder2(root.right):
        yield node
    yield root.val


# Helpers
>>>>>>> Stashed changes
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


<<<<<<< Updated upstream
def build_tree(int_list):
=======
def tree_deserilize(int_list, has_parent=False):
>>>>>>> Stashed changes
    # params: int list
    # return: root
    # algorithm:
    #   for all tree node
    #   - left child is at position: 2n + 1
    #   - right child is at position: 2n + 2
<<<<<<< Updated upstream
=======
    #   - parent node is at: (n - 1) / 2 if < 0 do None
>>>>>>> Stashed changes
    tree_list = [TreeNode(x) if isinstance(x, int) else None for x in int_list]
    length = len(int_list)
    for index, node in enumerate(tree_list):
        l_index = 2 * index + 1
        r_index = 2 * index + 2
        if l_index < length:
            node.left = tree_list[l_index]
        if r_index < length:
            node.right = tree_list[r_index]
<<<<<<< Updated upstream
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
=======
        if has_parent:
            ind = (index - 1) / 2
            # TOREAD: position lager than 0 should be assigned
            node.parent = tree_list[ind] if ind >= 0 else None

    return tree_list[0]


def build_tree(array):
    if isinstance(array, list):
        return tree_deserilize(array)
    else:
        return

if __name__ == '__main__':
    tree = build_tree([20, 50, 200, 25, 75, '#', 300])
    print()
    print('inorder')
    for x in inorder1(tree):
        print(x, end=' ')
    print()
    print('inorder')
    for x in inorder2(tree):
        print(x, end=' ')
    print()
    print('preorder')
    for x in preorder1(tree):
        print(x, end=' ')
    print()
    print('preorder')
    for x in preorder2(tree):
        print(x, end=' ')
    print()
    print('postorder')
    for x in postorder1(tree):
        print(x, end=' ')
    print()
    print('postorder')
    for x in postorder2(tree):
        print(x, end=' ')
    print()
>>>>>>> Stashed changes
