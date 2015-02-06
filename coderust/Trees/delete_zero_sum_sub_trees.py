from helper import build_tree
from helper import print_tree


def delete_zero_sum_in(tree):
    def sub_sum_tree(root):
        if root is None:
            return 0

        # TOREAD: post order search
        left_sum = sub_sum_tree(root.left)
        right_sum = sub_sum_tree(root.right)

        # TOREAD: just some process different than tree sum
        if left_sum == 0:
            root.left = None
        elif right_sum == 0:
            root.right = None
        return root.val + left_sum + right_sum

    return sub_sum_tree(tree)

if __name__ == '__main__':
    tree = build_tree([7, 5, 6, -3, -2, '#', '#'])
    print_tree(tree)

    delete_zero_sum_in(tree)
    print_tree(tree)
