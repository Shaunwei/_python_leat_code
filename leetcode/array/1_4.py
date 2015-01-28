# Problem: Search In Rotated Sorted Array II
#   allow duplicates


class Solution:
    @classmethod
    # Time: O(n)
    # Space: O(1)
    def solve(self, problems, target):
        # Solution here
        array = problems
        low = 0
        high = len(array) - 1
        index = -1
        while low < high:
            mid = (low + high)/2
            if array[mid] == target:
                index = mid
                break
            elif array[low] < array[mid]:  # increasing the first half
                if array[low] < target < array[mid]:  # in sorted part
                    high = mid - 1
                else:  # not in increasing part
                    low = mid + 1
            elif array[low] > array[mid]:  # increasing the second half
                if array[mid] < target < array[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:  # array.low == array.mid
                # increase the last element
                # to make increasing or reduce duplicates
                low += 1

        return index

# Think:
# Allow Duplicates, Which means that half part non-decreasing is not guaranteed
# Need to find other way or make non-decreasing
# To make non-decreasing, when low == mid, make low ++
# also if non-decreasing exists, just use the previous solution.

# ReThink:
#  two cases is, low > mid or low < mid
# when low > mid, means the first part is unsorted
# in this case is not guaranteed the second part is sorted
# However, in the previous problem, the second part is sorted
# [7, 0, 1, 2, 3, 4, 5] -> second part [3, 4, 5]

# Summary:
#@ iterate bountry question
#@ OTM:
# if one FOLLOWUP question is hard to do,
# consider about the easy case, solve it and find partten
# Then find out the difference, and solve it on the spacial case
# Then merge it to the easy case(solve time may get worse, but it solved.)
# In this case, only need to solve it on the duplicates,
# with solution to increase the bountry


if __name__ == '__main__':

    problems = [1, 1, 1, 3, 1, 1]  # input
    result = Solution.solve(problems, 3)

    print result
    assert result == 3, "Solution Error."  # output check

    problems = [3, 4, 5, 6, 1, 2, 2, 2, 2]  # input
    result = Solution.solve(problems, 0)

    print result
    assert result == -1, "Solution Error."  # output check

    print "problems solved."
