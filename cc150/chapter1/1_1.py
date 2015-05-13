'''
Implement an algorithm to determine if a string has all unique characters What 
if you can not use additional data structures?
'''
#import string
# string.ascii_letters [a-zA-Z]

def is_unique(s):
    '''
    O(n^2) with not extra space
    '''
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                return False
    return True

def is_unique2(s):
    '''
    O(n) with O(n) space
    '''
    string_dict = {}
    for char in s:
        if char in string_dict:
            return False
        else:
            string_dict[char] = True
    return True


if __name__ == '__main__':
    inputs = ['abca', 'abc']
    outputs = [False, True]
    assert outputs == list(map(is_unique, inputs))
    assert outputs == list(map(is_unique2, inputs))

