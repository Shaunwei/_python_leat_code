from helper import build_tree
from helper import print_tree


class InorderIterator:
    def __init__(self, tree):
        self.stack = []
        self.root = None
        root = tree
        while root:
            # TOREAD: process current node
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        return len(self.stack) > 0

    def getNext(self):
        if not len(self.stack):
            return

        # TOREAD: process current node
        self.root = self.stack.pop()
        root = self.root.right
        while root:
            self.stack.append(root)
            root = root.left

        return self.root


if __name__ == '__main__':
    tree = build_tree([100, 50, 200, 25, 75, 125, 350])
    print_tree(tree)

    order = [25, 50, 75, 100, 125, 200, 350]

    iterator = InorderIterator(tree)

    while iterator.hasNext():
        print iterator.getNext().val
