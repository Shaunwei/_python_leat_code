'''
Problem: Trapping Rain Water
algorithm:
    min(max_left, max_right) - height
tags:
'''


class Solution:
    @classmethod
    # Time: O(n)
    # Space: O(n)
    def solve(self, problems):
        # Solution here
        arr = problems

        ml = [0] * len(arr)
        max_left = arr[0]
        for i in range(1, len(arr)):
            if arr[i] > max_left:
                max_left = arr[i]
            ml[i] = max_left

        mr = [0] * len(arr)
        max_right = arr[-1]
        for j in reversed(range(len(arr) - 1)):
            if arr[j] > max_right:
                max_right = arr[j]
            mr[j] = max_right

        result = 0
        for k in range(len(arr)):
            r = min(ml[k], mr[k]) - arr[k]
            if r > 0:
                result += r

        return result

# Think:

# ReThink:

# Summary:

    @classmethod
    # Time: O(n)
    # Space: O(n)
    def better_solve(self, problems):
        # Solution here
        arr = problems

        ml = [0] * len(arr)
        mr = [0] * len(arr)
        max_left = arr[0]
        max_right = arr[-1]
        for i in range(1, len(arr)):
            if arr[i] > max_left:
                max_left = arr[i]
            ml[i] = max_left
            if arr[len(arr) - i - 1] > max_right:
                max_right = arr[len(arr) - i - 1]
            mr[len(arr) - i - 1] = max_right

        result = 0
        for k in range(len(arr)):
            r = min(ml[k], mr[k]) - arr[k]
            if r > 0:
                result += r

        return result

    @classmethod
    def better_solve2(self, problems):
        arr = problems

        m = 0
        for i in range(len(arr)):
            if arr[i] > arr[m]:
                m = i

        water = 0
        peak = 0
        for w in range(len(arr)):
            if w == m:
                break
            if arr[w] > peak:
                peak = arr[w]
            else:
                water += peak - arr[w]
        peak = 0
        for w in reversed(range(len(arr))):
            if w == m:
                break
            if arr[w] > peak:
                peak = arr[w]
            else:
                water += peak - arr[w]
        return water


if __name__ == '__main__':
    problems = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]  # input
    result = Solution.solve(problems)

    print result
    assert result == 6, "Solution Error."  # output check

    print "problems solved."

    result = Solution.better_solve(problems)

    print result

    result = Solution.better_solve2(problems)

    print result
