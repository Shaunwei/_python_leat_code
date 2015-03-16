'''
Problem: Rotate Image
algorithm:
    1. rotate following diagonal
    2. rotate following horizontal
tags:
'''


class Solution:
    @classmethod
    # Time: O(n)
    # Space: O(n)
    def solve(self, problems):
        # Solution here
        image = problems
        length = len(image)
        # diagonal
        for x in range(length):
            for y in range(length - x):
                # swap
                image[x][y], image[length-y-1][length-x-1] = \
                    image[length-y-1][length-x-1], image[x][y]

        # horizontal
        for x in range(length/2):
            for y in range(length):
                image[x][y], image[length-x-1][y] = \
                    image[length-x-1][y], image[x][y]

        return image

# Think:

# ReThink:

# Summary:

    @classmethod
    # Time: O(n)
    # Space: O(n)
    def better_solve(self, problems):
        # Solution here
        # pythonic
        image = problems
        return zip(*reversed(image))

if __name__ == '__main__':
    '''
    1,2,3       7,4,1
    4,5,6   - > 8,5,2
    7,8,9       9,6,3
    '''
    problems = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # input
    r = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    result = Solution.solve(problems)

    print result
    assert result == r, "Solution Error."  # output check

    print "problems solved."

    print Solution.better_solve([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
