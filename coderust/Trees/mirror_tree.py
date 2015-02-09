from helper import build_tree
from helper import print_tree


def mirror_tree(root):
    # post order swap
    def swap_node(root):
        if not root:
            return
        swap_node(root.left)
        swap_node(root.right)
        root.left, root.right = root.right, root.left
    return swap_node(root)


if __name__ == '__main__':
    tree = build_tree([20, 50, 200, 25, 75, '#', 300])
    print_tree(tree)

    print
    mirror_tree(tree)
    print_tree(tree)
