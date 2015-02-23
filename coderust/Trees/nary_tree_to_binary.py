class TreeNode:
    def __init__(self, value, x=None, y=None, z=None):
        self.val = value
        self.x = x
        self.y = y
        self.z = z


def convert_to_bianry(root):
    pass


if __name__ == '__main__':
    tree = TreeNode(1)
    tree.x = TreeNode(2)
    tree.y = TreeNode(3)
    tree.z = TreeNode(4)
    tree.y.x = TreeNode(5)
    tree.y.y = TreeNode(6)
