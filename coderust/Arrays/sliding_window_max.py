def sliding_window_max(array, wlen):
    # TOREAD:
    # a = [1, 2, 3, 4, 5, 6]
    # b = 3 # last three elements don't include!!
    # a[:-b] = [1,2,3],  a[:-b+1] = [1,2,3,4]
    window_max = []
    length = len(array)
    for x in range(length-wlen+1):
        window_max.append(max(array[x:x+3]))

    return window_max


if __name__ == '__main__':
    array = [-4, 2, -5, 3, 6]  # max -5, 3, 6 is 6
    window_length = 3

    assert [2, 3, 6] == sliding_window_max(array, window_length)

    print 'test passed.'
