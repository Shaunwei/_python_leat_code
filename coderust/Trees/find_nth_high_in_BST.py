from helper import build_tree
from helper import print_tree


# space O(n), time O(2n)
def find_nth_highest(root, nth):
    # nth highest is len(bst) - nth + 1 lowest
    # 1 is (7 - 1 + 1) lowest
    # in order traversal len(bst) - nth + 1 times
    def count_nodes(root):
        def count_rec(root):
            if root is None:
                return 0
            return count_rec(root.left) + 1 + count_rec(root.right)
        return count_rec(root)

    def find_nth(root, nth_lowest):
        # in order
        nodes = []

        def find_rec(root):
            if root is None:
                return
            find_rec(root.left)
            nodes.append(root)
            find_rec(root.right)

        find_rec(root)
        # TOREAD: careful what's in nodes
        # it's tree node not val
        return nodes[nth_lowest - 1].val

    nth_lowest = count_nodes(root) - nth + 1
    print
    print 'n lowest', str(nth_lowest)
    return find_nth(root, nth_lowest)


# space O(n), time O(n)
def better_solve1(bst, nth):
    # could just do traversal once
    # use pointers
    # just do reverse in-order traversal
    root = bst
    nodes = []

    def rev_in_order(root):
        if root is None:
            return
        rev_in_order(root.right)
        nodes.append(root.val)
        rev_in_order(root.left)
    rev_in_order(root)
    return nodes[nth - 1]


# space O(1), time O(n)
# TOREAD: this is not working
# because I don;t have global count
# the branch right should count first
# And counts should add up
# That's why I need global variable
# In this case, n is always the current value
# def better_solve2(bst, nth):

#     def find_n_rec(root, n):
#         if root is None:
#             return

#         res = find_n_rec(root.right, n - 1)
#         if not res:
#             return res

#         if n == 1:
#             return root.val

#         res = find_n_rec(root.left, n - 1)
#         if not res:
#             return res
#         return
#     return find_n_rec(bst, nth)
cur_count = 0


def better_solve2(bst, nth):

    def find_n_rec(root, n):
        if root is None:
            return

        res = find_n_rec(root.right, n)
        if res:
            return res

        global cur_count
        cur_count += 1

        if n == cur_count:
            return root.val

        res = find_n_rec(root.left, n)
        if res:
            return res
        return
    return find_n_rec(bst, nth)


if __name__ == '__main__':
    binary_search_tree = \
        build_tree([100, 50, 200, 25, 75, 125, 350])

    print_tree(binary_search_tree)
    val = find_nth_highest(binary_search_tree, 3)
    print
    print 'nth highest is: ' + str(val)
    assert 125 == val

    print better_solve1(binary_search_tree, 3)
    print better_solve2(binary_search_tree, 3)
