from helper import build_tree
from helper import print_tree

pre = -999


def is_binary_search_tree(root):
    # in order traversal should be increasing order
    # smaller than successor

    # TOREAD: YOU NEED GLOBAL LOW
    # AGAIN, THE VALUE KEEP CHANGING WHEN ITERATE
    #    pre = -999

    def is_bst_rec(root):
        if not root:
            return True

        # res = is_bst_rec(root.left, pre)
        # if root.val > pre:
        #     res = False
        # else:
        #     pre = root.val
        # res = is_bst_rec(root.right, pre)

        # return res
        global pre
        if not is_bst_rec(root.left):
            return False
        if root.val < pre and pre != -999:
            return False
        pre = root.val
        if not is_bst_rec(root.right):
            return False
        return True

    return is_bst_rec(root)


def is_binary_search_tree2(root):
    def is_bst_rec(root, max_v, min_v):
        if not root:
            return True

        if root.val < min_v or root.val > max_v:
            return False

        return is_bst_rec(root.left, root.val, min_v) and \
            is_bst_rec(root.right, max_v, root.val)
    return is_bst_rec(root, 9999, -9999)


if __name__ == '__main__':
    tree = build_tree([100, 50, 200, 25, 75, 125, 350])
    print_tree(tree)

    print
    print is_binary_search_tree(tree)

    print
    print is_binary_search_tree2(tree)
