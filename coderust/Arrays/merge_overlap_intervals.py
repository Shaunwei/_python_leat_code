def merge_overlap_intervals(_list):
    res = []

    clow, chigh = inputs[0]

    for low, high in inputs[1:]:
        print clow, chigh, low, high
        if low <= chigh:
            # overlap
            clow = min(low, clow)
            chigh = max(high, chigh)
        else:
            res.append((clow, chigh))
            # TOREAD: remember to update the local values
            clow, chigh = low, high
    else:
        # TOREAD: LAST Element, EDGE CASE
        res.append((clow, chigh))
    # TOREAD:!!!REMEBER TO RETURN VALUE
    return res

if __name__ == '__main__':
    inputs = [(1, 5), (3, 7), (4, 6), (6, 8), (10, 12), (11, 15)]
    output = [(1, 8), (10, 15)]

    res = merge_overlap_intervals(inputs)
    print res
    assert output == res, "error"

    print "test passed."
