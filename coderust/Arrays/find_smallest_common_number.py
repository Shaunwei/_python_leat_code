def find_smallest_common_number(a0, a1, a2):
    p0 = p1 = p2 = 0

    # TOREAD: no need to do len() - 1
    # the edge case is len()
    while p0 < len(a0) and p1 < len(a1) and p2 < len(a2):
        # move the smallest pointer forward
        if a0[p0] < a1[p1] and a0[p0] < a2[p2]:
            p0 += 1
        elif a1[p1] < a0[p0] and a1[p1] < a2[p2]:
            p1 += 1
        elif a2[p2] < a0[p0] and a2[p2] < a1[p1]:
            p2 += 1
        else:
            return a0[p0]
    return -1


if __name__ == '__main__':
    array0 = [6, 7, 10, 25, 30, 63, 64]
    array1 = [-1, 4, 5, 6, 7, 8, 50]
    array2 = [1, 6, 10, 14]

    assert 6 == find_smallest_common_number(array0, array1, array2)

    print "test passed."
