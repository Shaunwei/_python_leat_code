def binary_search_rec(array, target):
    def bsr(array, low, high, target):
        if low > high:
            return -1

        mid = (low + high) / 2
        if array[mid] == target:
            return mid

        if target < array[mid]:
            return bsr(array, low, mid - 1, target)
        if array[mid] < target:
            return bsr(array, mid + 1, high, target)

    return bsr(array, 0, len(array) - 1, target)


def binary_search_iter(array, target):
    low = 0
    high = len(array) - 1

    while low < high:
        mid = (low + high) / 2

        if array[mid] == target:
            return mid

        if target < array[mid]:
            high = mid - 1
        else:
            low = mid + 1
    else:
        return -1


if __name__ == '__main__':
    array = [1, 10, 20, 47, 59, 63, 75, 88, 99]
    target = 20

    assert 2 == binary_search_rec(array, target), "Error."
    assert 2 == binary_search_iter(array, target), "Error."
    assert -1 == binary_search_iter(array, 58), "Error."

    print "test passed."
