'''
Problem: Remove Element
algorithm:
    read and write
tags:
'''


class Solution:
    @classmethod
    # Time: O(n)
    # Space: O(n)
    def solve(self, problems):
        # Solution here
        arr, target = problems
        write = 0
        for read in range(len(arr)):
            if arr[read] == target:
                continue
            else:
                arr[write] = arr[read]
                write += 1
        return arr[:write]

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
    problems = [1, 2, 3, 4, 2, 6], 2  # input
    result = Solution.solve(problems)
    r = [1, 3, 4, 6]
    print result
    assert result == r, "Solution Error."  # output check

    print "problems solved."
