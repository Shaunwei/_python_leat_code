# Tree Traversal


def in_order(node):
    if node is None:
        return

    in_order(node.left)
    print node.val
    in_order(node.right)


def pre_order(node):
    if node is None:
        return

    print node.val
    pre_order(node.left)
    pre_order(node.right)


def post_order(node):
    if node is None:
        return

    post_order(node.left)
    post_order(node.right)
    print node.val
