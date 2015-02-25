from helpers import *


@timeit
def remove_white_spaces(s):
    '''
    replace?
    '''
    return s.replace(' ', '').replace('\t', '')


@timeit
def remove_white_spaces1(s):
    '''
    algorithm:
    read and write pointer
    '''
    res = ''
    if not len(s):
        return

    for character in s:
        if character == ' ' or character == '\t':
            pass
        else:
            res += character
    return res


if __name__ == '__main__':
    s = '\tQuick brown fox jumped over the lazy\tdog.\t'

    print remove_white_spaces(s)
    print remove_white_spaces1(s)
