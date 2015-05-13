'''
Write code to reverse a C-Style String (C-String means that “abcd” is 
    represented as five characters, including the null character )
'''

def reverse(s):
    '''
    \n only take one char space
    '''
    string, null = s[:-1], s[-1:]
    return string[::-1] + null

if __name__ == '__main__':
    inputs = 'abcd\n'
    outputs = 'dcba\n'
    assert outputs == reverse(inputs)