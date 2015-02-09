class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        if self.left and self.right:
            msg = '<Tree Node: %s>'
        else:
            msg = '<Leaf Node: %s>'
        return msg % str(self.val)


def tree_serilize(root):
    # params: TreeNode
    # return: int list
    # algorithm: BFS print
    #   - append node.val
    #   - if None, append '#'
    unvisited = [root, ]
    _int_list = []
    while unvisited:
        node = unvisited.pop(0)
        if node is not None:
            _int_list.append(node.val)
        else:
            _int_list.append('#')
            continue

    # TOREAD: in this case None is processed above
    # We don't pass it, we process it then continue!!!
        unvisited.append(node.left)
        unvisited.append(node.right)

    # clean the tail '#'
    tail = len(_int_list) - 1
    while _int_list[tail] == '#':
    # TOREAD: please when do pointers, it's array[pointer]
    # is NOT pointer by itself!!!!!
        tail -= 1

    return _int_list[:tail + 1]


def tree_deserilize(int_list, has_parent=False):
    # params: int list
    # return: root
    # algorithm:
    #   for all tree node
    #   - left child is at position: 2n + 1
    #   - right child is at position: 2n + 2
    #   - parent node is at: (n - 1) / 2 if < 0 do None
    tree_list = [TreeNode(x) if isinstance(x, int) else None for x in int_list]
    length = len(int_list)
    for index, node in enumerate(tree_list):
        l_index = 2 * index + 1
        r_index = 2 * index + 2
        if l_index < length:
            node.left = tree_list[l_index]
        if r_index < length:
            node.right = tree_list[r_index]
        if has_parent:
            ind = (index - 1) / 2
            # TOREAD: position lager than 0 should be assigned
            node.parent = tree_list[ind] if ind >= 0 else None

    return tree_list[0]


def print_tree(root):
    # BFS
    # use x( a | b) represent
    # unvisited = [root, ]
    # while unvisited:
    #     node = unvisited.pop(0)
    #     print node.val,
    #     if node.left:
    #         unvisited.append(node.left)
    #     if node.right:
    #         unvisited.append(node.right)
    # in_order
    # TOREAD
    def in_order(node):
        if node is None:
            return '#'
        print node.val,
        if not node.left and not node.right:
            return ''
        print '( ',
        print in_order(node.left),
        print ' | ',
        print in_order(node.right),
        print ' )',
        return ''
    print
    return in_order(root)


def build_tree(array):
    if isinstance(array, list):
        return tree_deserilize(array)
    else:
        return


def build_tree_with_parent(array):
    if isinstance(array, list):
        return tree_deserilize(array, has_parent=True)
    else:
        return
