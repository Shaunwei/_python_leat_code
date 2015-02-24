def get_all_substrings(string):
    '''
    algorithm: time O(n^2)
        1. for range(len(string)) as l
        2. get all l substring in string
    '''
    result = []
    # to reach last point.
    # NEED TO ADD 1
    for l in range(1, len(string) + 1):
        for start in range(0, len(string) + 1 - l):
            result.append(string[start: start + l])
    return result


def get_all_substrings_1(string):
    '''
    '''
    result = []
    length = len(string)
    for i in range(length):
        for j in range(i, length):
            result.append(string[i:j+1])
    return result


def get_all_substrings_2(string):
    l = len(string)
    return [string[i:j+1] for i in range(l) for j in range(i, l)]


if __name__ == '__main__':
    s = 'abc'
    r = ['a', 'b', 'c', 'ab', 'bc', 'abc']

    print 'case 1'
    res = get_all_substrings(s)
    print res
    assert res.sort() == r.sort()
    print 'test 1 passed.'

    print 'case 2'
    res = get_all_substrings_1(s)
    print res
    assert res.sort() == r.sort()
    print 'test 2 passed.'

    print 'case 3'
    res = get_all_substrings_2(s)
    print res
    assert res.sort() == r.sort()
    print 'test 3 passed.'
