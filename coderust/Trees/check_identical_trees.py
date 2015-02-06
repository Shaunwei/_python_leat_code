from helper import build_tree
from helper import print_tree


def check_identical_trees(tree1, tree2):

    def dfs(root1, root2):
        if root1 is None and root2 is None:
            return True

        # if root1.val == root2.val:
        #     return dfs(root1.left, root2.left) and \
        #         dfs(root1.right, root2.right)
        # else:
        #     return False
        # TOREAD: better wrote
        if root1 is not None and root2 is not None:
            return (root1.val == root2.val) and \
                dfs(root1.left, root2.left) and \
                dfs(root1.right, root2.right)
        else:
            return False
    return dfs(tree1, tree2)


if __name__ == '__main__':
    tree1 = tree2 = build_tree([100, 50, 200, '#', 25, 125, 350])
    print_tree(tree1)
    assert True == check_identical_trees(tree1, tree2)

    tree1 = build_tree([100, 50, 200, '#', 25, 125, 350])
    tree2 = build_tree([100, 50, 200, '#', 25, 125, 250])
    print_tree(tree1)
    print_tree(tree2)

    assert False == check_identical_trees(tree1, tree2)
