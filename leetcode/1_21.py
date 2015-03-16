'''
Problem: Gas Station
algorithm:
    scan all point
        check each point is valid
        sum all points
tags: DP, global guard
'''


class Solution:
    @classmethod
    # Time: O(n)
    # Space: O(n)
    def solve(self, problems):
        # Solution here
        gas, cost = problems

        total = 0
        s = 0
        j = -1
        for i in range(len(gas)):
            s += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if s < 0:
                s = 0
                j = i
        # TOREAD: total could be 0
        return j + 1 if total >= 0 else -1

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
    0, 1, 2, 3
    [6, 3, 4, 4], [5, 4, 6, 2] -> 17 return 3
    [6, 3, 4, 4], [6, 4, 6, 2] -> -1
    '''
    problems = [6, 3, 4, 4], [5, 4, 6, 2]  # input
    r = 3
    result = Solution.solve(problems)

    print result
    assert result == 3, "Solution Error."  # output check

    print "problems solved."

    problems = [6, 3, 4, 4], [6, 4, 6, 2]  # input
    r = -1
    result = Solution.solve(problems)

    print result
    assert result == r, "Solution Error."  # output check

    print "problems solved."
