'''
Problem: Plus One
algorithm:
    carry
tags: carry away value
'''


class Solution:
    @classmethod
    # Time: O(n)
    # Space: O(n)
    def solve(self, problems):
        # Solution here
        digits = problems
        carry = 1
        for d in range(len(digits)):
            s = digits[d] + carry
            carry = s/10
            s %= 10
            digits[d] = s
        # process last digit
        if carry:
            digits.insert(0, carry)
        return digits

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
    problems = [9, 9]  # input
    r = [1, 0, 0]
    result = Solution.solve(problems)

    print result
    assert result == r, "Solution Error."  # output check

    print "problems solved."
