from helper import build_tree
from helper import print_tree


def level_order_traversal(root):
    level = 0
    cur_lvl = [root]
    next_lvl = []

    while len(cur_lvl):
        print 'level %s:' % str(level),
        for node in cur_lvl:
            if node.left:
                next_lvl.append(node.left)
            if node.right:
                next_lvl.append(node.right)

            print node.val,
        print
        cur_lvl, next_lvl = next_lvl, []
        level += 1


if __name__ == '__main__':
    tree = build_tree([100, 50, 200, 25, 75, 125, 350])
    print_tree(tree)

    print
    level_order_traversal(tree)
