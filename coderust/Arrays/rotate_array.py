def rotate_array(array, N):
    if N == 0:
        return

    if N > 0:
        while N > 0:
            # TOREAD: insert(position, value)
            # this is perpend
            array.insert(0, array.pop())
            N -= 1
        return

    if N < 0:
        while N < 0:
            array.append(array.pop(0))
            N += 1
        return


#@ working with distance!!
#
# what if N is larger than len(array)???
# N = len(array) % N
# if N<0, then N = len(array) + N
def rotate_array_rec(array, N):
    # TOREAD: reverse in place
    def reverse_inplace(array, start, end):
        while start < end:
            array[start], array[end] = array[end], array[start]
            start += 1
            end -= 1

    length = len(array)
    # TOREAD: % process negative value
    # do it, don't need to test
    # when do %, like -11 % 5 = 4
    # it already processed negative value
    N %= length

    reverse_inplace(array, 0, length - 1)
    reverse_inplace(array, 0, N - 1)
    reverse_inplace(array, N, length - 1)


if __name__ == '__main__':
    array = [1, 10, 20, 0, 59]

    res1 = [10, 20, 0, 59, 1]  # rotate -1
    res2 = [0, 59, 1, 10, 20]  # rotate 2

    rotate_array(array, -1)
    assert res1 == array

    array = [1, 10, 20, 0, 59]
    rotate_array(array, 2)
    assert res2 == array

    array = [1, 10, 20, 0, 59]
    rotate_array_rec(array, -1)
    print array
    print 'test passed.'
