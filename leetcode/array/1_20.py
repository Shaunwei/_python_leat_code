'''
Problem: Set Matrix Zero
algorithm:
        scan once, mark x and y
        scan again, set 0
tags:
'''

class Solution:
    @classmethod
    # Time: O(n)
    # Space: O(n)
    def solve(self, problems):
        # Solution here
        matrix = problems
        zero_index = {'x': [], 'y': []}

        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if matrix[x][y] == 0:
                    zero_index['x'].append(x)
                    zero_index['y'].append(y)

        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if x in zero_index['x'] or y in zero_index['y']:
                    matrix[x][y] = 0
        return matrix

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
    1, 1, 1, 1      0, 1, 0, 1
    0, 1, 1, 1      0, 0, 0, 0
    1, 1, 0, 1 ->   0, 0, 0, 0
    1, 1, 1, 1      0, 1, 0, 1
    '''
    problems = [[1, 1, 1, 1], [0, 1, 1, 1], [1, 1, 0, 1], [1, 1, 1, 1]]  # input
    r = [[0, 1, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 1]]
    result = Solution.solve(problems)

    print result
    assert result == r, "Solution Error."  # output check

    print "problems solved."
