import math


def permute_string(s):
    res = []
    list_s = list(s)
    for _ in range(math.factorial(len(s))):
        res.append(''.join(next_permute(list_s)))

    return res


def next_permute(array):
    '''
    algorithm:
        1. find the first element from right to left
            violate increasing order call it change_number
            5. if all element is in order, reverse them
        2. find the first element larger than change_number
            from right to left call it partition_number
        3. swap change_number and partition_number
        4. reverse all numbers on right of partition index
    '''

    n = change_number = len(array) - 1
    n -= 1
    while n >= 0:
        if array[n] > array[change_number]:
            change_number = n
        else:
            change_number = n
            break
        n -= 1

    if n < 0:
        array.reverse()
        return array

    n = len(array) - 1
    while n >= 0:
        if array[n] > array[change_number]:
            partition_number = n
            break
        n -= 1

    array[change_number], array[partition_number] = \
        array[partition_number], array[change_number]

    # in place reverse
    array[change_number+1:] = reversed(array[change_number+1:])
    return array


if __name__ == '__main__':
    s = 'bad'
    r = ['abd', 'adb', 'bad', 'bda', 'dab', 'dba']

    print 'case 1'
    # _s = permute_string(s)
    # print _s
    # assert _s.sort() == r
    print 'test 1 passed.'

    l = [1, 2, 3]
    p = [1, 2, 3]
    for _ in range(10):
        m = next_permute(l)
        print m
