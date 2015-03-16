'''
Problem: Climbing Stairs
algorithm:
    f(n) = f(n-1) + f(n-2)
    Dynamic processing
tags:
'''


class Solution:
    @classmethod
    # Time: O(n)
    # Space: O(n)
    def solve(self, problems):
        # Solution here
        n = problems
        f1 = 1
        f2 = 2
        n -= 2
        while n > 0:
            f2, f1 = f1 + f2, f2
            n -= 1
        return f2

# Think:

# ReThink:

# Summary:

    @classmethod
    # Time: O(n)
    # Space: O(n)
    def better_solve(self, problems):
        # Solution here
        pass

if __name__ == '__main__':
    '''
    1, 2, 3, 5, 8, 13, 21 ...
    '''
    problems = 7  # input
    result = Solution.solve(problems)
    r = 21
    print result
    assert result == r, "Solution Error."  # output check

    print "problems solved."
