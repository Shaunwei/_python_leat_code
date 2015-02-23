from helper import build_tree
from helper import print_tree

def connect_siblings(tree):
    # bfs and connect
    if not tree:
        return

    root = tree
    que = [root]
    pre = None

    while que:
        root = que.pop(0)
        if root.left:
            que.append(root.left)
        if root.right:
            que.append(root.right)
        if pre:
            pre.next = root
        pre = root

    root.next = None
    return tree



if __name__ == '__main__':
    tree = build_tree([100, 50, 200, 25, 75, 125, 350])
    print_tree(tree)

    tree = connect_siblings(tree)
    print
    while tree:
        print tree.val,
        tree = tree.next
