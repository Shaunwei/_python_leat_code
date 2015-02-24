def find_all_palindrome_substrings(string):
    '''
    algorithm:
        1. for each substring in string
        2. check if it is palindrome
            if is, save in result
            else: pass
    '''
    def is_palindrome(s):
        if len(s) > 1:
            return s[0] == s[-1] and is_palindrome(s[1:-1])
        else:
            return True

    result = []
    l = len(string)
    for i in range(l):
        for j in range(i, l):
            x = string[i:j+1]
            # TOREAD: NEED TO LARGER THAN 1
            # AND NOT THE SAME!!
            if is_palindrome(x) and len(x) > 1 and x not in result:
                result.append(x)
    return result

if __name__ == '__main__':
    s = 'aabbbaa'
    res = ['aa', 'bb', 'bbb', 'abbba', 'aabbbaa']

    print 'case 1'
    r = find_all_palindrome_substrings(s)
    print r
    assert r.sort() == res.sort()
    print 'test 1 passed.'
