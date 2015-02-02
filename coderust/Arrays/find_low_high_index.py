def find_low_high_index(array, target):
    def find_low(array, target):
        # modified binary search
        low, high = 0, len(array) - 1
        # TOREAD: enable equal, so low will be finally larger than high
        while low <= high:
            mid = (low + high) / 2
            if target <= array[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            return low if array[low] == target else -1

    def find_high(array, target):
        low, high = 0, len(array) - 1
        # TOREAD: if not enable equals
        # the high will be -1, because, the last move is
        # low at 10, high at 11
        # mid is 10, and low + 1 is 11
        # low < high not valid, return array[11] which is 11
        while low <= high:
            mid = (low + high) / 2
            if target < array[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            return high if array[high] == target else -1

    res = []
    res.append(find_low(array, target))
    res.append(find_high(array, target))
    print res
    return res


if __name__ == '__main__':
    array = [1, 2, 2, 5, 5, 5, 5, 5, 5, 5, 5, 11]
    low_high = [3, 10]

    assert low_high == find_low_high_index(array, 5)

    print "test passed."
