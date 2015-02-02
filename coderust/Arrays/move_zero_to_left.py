def move_zero(array):
    # TOREAD: use two pointers to read and write
    # Do it backward, because in this way, don't need
    # to move elements again
    pread = pwrite = len(array) - 1

    while pread >= 0:
        # TOREAD: two case
        # is 0 or not
        if array[pread] != 0:
            array[pwrite] = array[pread]
            pwrite -= 1
        pread -= 1

    # empty 0
    # while pwrite >= 0:
    #     array[pwrite] = 0
    #     pwrite -= 1
    # TOREAD: [:2] == [0, 1] , len([:2]) = 2
    # pwrite + 1 is include pwrite
    array[:pwrite + 1] = [0] * (pwrite + 1)

    return array


if __name__ == '__main__':
    array = [1, 10, 20, 0, 59, 63, 0, 88, 0]

    res = [0, 0, 0, 1, 10, 20, 59, 63, 88]

    assert res == move_zero(array)

    print "test passed."
