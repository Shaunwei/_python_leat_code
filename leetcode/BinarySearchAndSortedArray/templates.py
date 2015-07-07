'''
1. start + 1 < end
2. start + (end - start) / 2
3. A[mid] ==, >, <
4. A[start], A[end], target

Search in range
1) first postion
2) last postion
'''

def binary_search_first(A, target):
    if not A:
        return

    start, end = 0, len(A) - 1
    # start == end
    # or
    # start + 1 == end
    while start + 1 < end:
        mid = start + (end - start) // 2
        if target == A[mid]:
            end = mid
        elif target < A[mid]:
            end = mid
        elif target > A[mid]:
            start = mid

    if A[start] == target:
        return start
    if A[end] == target:
        return end
    return -1


def binary_search_last(A, target):
    if not A:
        return

    start, end = 0, len(A) - 1
    while start + 1 < end:
        mid = (start + end) // 2
        if target == A[mid]:
            start = mid
        elif target > A[mid]:
            start = mid
        elif target < A[mid]:
            end = mid
    if A[end] == target:
        return end
    if A[start] == target:
        return start
    return -1



if __name__ == '__main__':
    A = [1, 2, 3, 4, 4, 4, 5, 6, 7]
    print(binary_search_first(A, 4))
    print(binary_search_last(A, 4))