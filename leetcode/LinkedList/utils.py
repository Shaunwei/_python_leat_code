"""
Utilites
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return '[Node: %d]-> ' % self.val


def print_ll(head):
    while head:
        print(head, end='')
        head = head.next
    print('Null')

def build_ll(array):
    arr = list(map(Node, array))
    for i in range(len(arr) - 1):
        arr[i].next = arr[i + 1]
    return arr[0]


if __name__ == '__main__':
    head = build_ll(range(1, 11))
    print_ll(head)
