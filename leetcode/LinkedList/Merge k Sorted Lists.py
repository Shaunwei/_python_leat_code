'''
Merge k sorted linked lists and return it as one sorted list.
Analyze and describe its complexity.
'''
from utils import print_ll
from utils import build_ll
from utils import Node
import heapq


def merge(head_list):
    '''
    list of heads
    '''
    curt = dummy = Node(-1)
    heap = []
    for head in head_list:
        heapq.heappush(heap, [head.val, head])

    while heap:
        _, head = heapq.heappop(heap)
        curt.next = head
        curt = curt.next
        if head.next:
            heapq.heappush(heap, [head.next.val, head.next])
    return dummy.next


if __name__ == '__main__':
    lists = [
        [1, 3, 4, 6],
        [0, 2, 5, 8],
        [7, 9]
    ]
    lists = [build_ll(l) for l in lists]
    print_ll(merge(lists))