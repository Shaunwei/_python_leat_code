def search_rotated_array(array, rotated_arr):
    # sorted!!
    # assume find the min number to rotate
    # assume it can be rotate left or right

    # binary search algorithm to find leftmost value
    # if cur_pos - pre_pos < len(array) /2, do right rotate
    # else do left rotate
    target = array[0]

    def binary_search(array, target):
        low = 0
        high = len(array) - 1
        # TOREAD: this is <=
        # Not <, because we need to check the last element
        # always do <=!!
        # while low < high:
        while low <= high:
            mid = (low + high) / 2
            if array[mid] == target:
                return mid
            if array[low] <= array[mid]:
                # first half increasing
                if array[low] <= target < array[mid]:
                    # in first half
                    high = mid - 1
                else:
                    # in second half
                    low = mid + 1
            else:  # second half increasing
                if array[mid] < target <= array[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1

    distance = binary_search(rotated_arr, target)
    if distance == -1:
        return "rotated_arr is not the same"

    # TOREAD: is not /2, I was thinking okay, compare distance
    # But, when round up, it's better to do length - distance
    # return min(distance, abs(len(array)/2 - distance))
    return min(distance, abs(len(array) - distance))


if __name__ == '__main__':
    array = [5, 6, 10, 11, 12, 13, 14]

    # rotate 5 times right or rotate 2 times left
    rotated_arr = [10, 11, 12, 13, 14, 5, 6]

    assert 2 == search_rotated_array(array, rotated_arr)

    # rotate 2 times right or rotate 5 times left
    rotated_arr = [13, 14, 5, 6, 10, 11, 12]
    assert 2 == search_rotated_array(array, rotated_arr)

    print 'test passed.'
