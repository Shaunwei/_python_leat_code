from helpers import *


@timeit
def remove_duplicates(string):
    '''
    algorithm:
    1. store character in dict
    2. if in dict pass
        else append to res
    '''
    res = ''
    existed = {}
    for s in string:
        if s in existed:
            pass
        else:
            res += s
            existed[s] = True
    return res


@timeit
def remove_duplicates1(string):
    '''# ASK FOR VIRIFICATION
    algorithm:
    1. generate all character in dict
    2. if in dict, pass
        else append and set to True
    '''
    # TOREAD: BE CAREFUL WHEN YOU USE STRING
    import string as _s
    res = ''
    existed = {x: False for x in _s.ascii_lowercase}
    for s in string:
        if not existed[s]:
            existed[s] = True
            res += s
    return res


if __name__ == '__main__':
    s = 'abbabcddbabcdeedebc'
    r = 'abcde'

    print 'case 1'
    assert r == remove_duplicates(s)
    print 'test passed.'

    print 'case 2'
    assert r == remove_duplicates1(s)
    print 'test passed.'
