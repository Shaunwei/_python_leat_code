'''
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
'''
from utils import *

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = self.right = None




def sorted_list_to_bst(head):
    pass



if __name__ == '__main__':
    head = build_ll([1, 2, 3, 4, 5])
    root = sorted_list_to_bst(head)
