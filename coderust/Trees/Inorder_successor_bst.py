from helper import build_tree
from helper import print_tree


# space O(1) time O(n)
def inorder_success_bst(root, target):
    # do inorder and return the next value
    stack = []
    while len(stack) or root:
        if root:
            stack.append(root)
            root = root.left
            continue

        root = stack.pop()
        if root.val == target:
            if root.right:
                return root.right.val
            else:
                # this is the last case
                # TOREAD: edge case
                # target is the last element
                # does not have successor!!
                if not len(stack):
                    return
                return stack.pop().val
        else:
            root = root.right


# space O(n) time O(logn)
def inorder_success_bst2(root, target):
    # the successor means the next value
    # which is larger than the target
    # TOREAD: which is the leftmost element of its right branch
    parents = []
    while root is not None:
        if root.val == target:
            # find the successor
            # TOREAD: make it into two case
            # one tree node one leaf node
            if root.right:
                # right is not None
                # TREE NODE
                root = root.right
                while root.left:
                    root = root.left
                return root.val
            else:
                # LEAF NODE
                # two case
                # 1. last node
                # TOREAD: HOW TO SORT ANYTHING!
                parents.sort(key=lambda x: x.val)
                if root.val > parents[-1].val:
                    return
                else:
                    # 2. other leaf nodes
                    # TOREAD: RETURN first larger value
                    for node in parents:
                        if node.val > root.val:
                            return node.val

        elif root.val < target:
            # target in right branch
            parents.append(root)
            root = root.right
        else:
            # target in left branch
            parents.append(root)
            root = root.left
    else:
        return None


def inorder_success_bst3():
    pass


if __name__ == '__main__':
    tree = build_tree([100, 50, 200, 25, 75, 125, 350])
    print_tree(tree)

    print
    print inorder_success_bst(tree, 50)
    print inorder_success_bst2(tree, 75)
