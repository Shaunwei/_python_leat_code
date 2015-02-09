from helper import build_tree
from helper import print_tree


def transfer(root):
    tree = root
    visited = [root]
    while len(visited):
        root = visited.pop()
        if root.left:
            root.left.parent = root
            visited.append(root.left)

        # TOREAD: this is not elif
        # be careful, elif only when the first one is not right
        if root.right:
            root.right.parent = root
            visited.append(root.right)
    return tree


if __name__ == '__main__':
    tree = build_tree([100, 50, 200, 25, 75, 125, 350])
    print_tree(tree)

    root = transfer(tree)
    print_tree(root)
