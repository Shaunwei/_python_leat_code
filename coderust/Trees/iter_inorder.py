from helper import build_tree
from helper import print_tree


def iter_inorder(tree):
    # visit == print
    # left, root, right
    root = tree
    stack = []
    nodes = []
    while len(stack) or root is not None:
        if root is not None:
            stack.append(root)
            root = root.left
            continue

        # TOREAD: process it and git rid of it at last
        nodes.append(stack[-1].val)
        root = stack[-1].right
        stack.pop()

    print
    print nodes


if __name__ == '__main__':
    tree = build_tree([100, 50, 200, 25, 75, 125, 350])
    print_tree(tree)

    order = [25, 50, 75, 100, 125, 200, 350]

    iter_inorder(tree)
