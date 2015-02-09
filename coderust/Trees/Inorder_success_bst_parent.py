from helper import build_tree_with_parent
from helper import print_tree


def inorder_success_bst_with_parent(tree, target):
    # no need to keep parent
    root = tree
    # two case
    # 1. has right, successor is leftmost of right subtree
    # 2. no right, trace parent and get first larger val
    #    edge case: last right leaf node
    while root:
        if root.val == target:
            if root.right:
                # Tree Node
                # find leftmost
                root = root.right
                while root.left:
                    root = root.left
                return root.val
            else:
                # Leaf Node
                # smaller and has value
                # case 1
                parent = root.parent
                while parent and parent.val < root.val:
                    parent = parent.parent
                else:
                    # TOREAD
                    # parent may be None
                    if parent and parent.val > root.val:
                        return parent.val
                    else:
                        #case 2 last element
                        return None

        elif root.val < target:
            root = root.right
        else:
            root = root.left
    return None

if __name__ == '__main__':
    tree = build_tree_with_parent([100, 50, 200, 25, 75, 125, 350])
    print_tree(tree)

    print
    print inorder_success_bst_with_parent(tree, 350)
