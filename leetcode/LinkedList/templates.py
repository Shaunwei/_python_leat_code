import utils

def insert(head, val):
    '''
    Insert val in to linked list
    @params: val: int
    @params: head: Node
    @return: head: Node
    '''
    if not head or head.val >= val:
        new_head = utils.Node(val)
        new_head.next = head
        return new_head

    cur = head
    while cur.next and cur.next.val < val:
        cur = cur.next

    if not cur.next:
        # val is the last node
        cur.next = utils.Node(val)
    else:
        node = utils.Node(val)
        node.next = cur.next
        cur.next = node
    return head


def remove(head, target):
    '''
    Remove node if val is target
    @params: head: Node
    @params: target: int
    @return: head: Node
    '''
    cur = dummy = utils.Node(-1)
    dummy.next = head

    while cur.next:
        if cur.next.val == target:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return dummy.next


def reverse(head):
    dummy = utils.Node(-1)
    while head:
        temp = head.next
        head.next = dummy.next
        dummy.next = head
        head = temp
    return dummy.next


def merge(left, right):
    '''
    @params: head: Node
    @return: merged new linked list
    '''
    tail = dummy = utils.Node(-1)
    while left and right:
        if left.val <= right.val:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next
    if left:
        tail.next = left
    else:
        tail.next = right
    return dummy.next


def middle(head):
    '''
    return the middle node refernce of a linked list
    1, 2, 3, 4, 5
          s
    1, 2, 3, 4
       s
    @params: head: Node
    @return: middle: Node
    '''
    if not head or not head.next:
        return head

    slow, fast = head, head.next
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow


if __name__ == '__main__':
    print('insert')
    head = utils.build_ll([1, 2, 4, 5])
    head = insert(head, 3)
    utils.print_ll(head)
    head = insert(head, 0)
    utils.print_ll(head)
    head = insert(head, 6)
    utils.print_ll(head)
    print('=== ===')
    print('remove')
    head = remove(head, 3)
    utils.print_ll(head)
    head = remove(head, 0)
    utils.print_ll(head)
    head = remove(head, 6)
    utils.print_ll(head)
    utils.print_ll(
        remove(utils.build_ll([3, 3, 3, 2, 4]), 3)
    )
    print('=== ===')
    print('reverse')
    utils.print_ll(reverse(utils.build_ll(range(5))))
    print('=== ===')
    print('merge')
    left = utils.build_ll([1, 3, 4])
    right = utils.build_ll([2, 5, 6])
    utils.print_ll(merge(left, right))
    print('=== ===')
    print('middle')
    head = utils.build_ll([1, 2, 3, 4, 5])
    print(middle(head))
    head = utils.build_ll([1, 2, 3, 4])
    print(middle(head))

