# Problem: Search in Rotated Sorted Array


class Solution:
    @classmethod
    # Time: O(log(n))
    # Space: O(1)
    def solve(self, problems, target):
        # Solution here
        array = problems

        low = 0
        high = len(array) - 1

        index = -1

        while low < high:
            mid = (low + high) / 2
            if array[mid] != target:
                if array[low] < array[mid]:
                    if array[low] <= target < array[mid]:
                        high = mid - 1
                    else:
                        low = mid + 1
                # elif array[mid] < array[high]:  # WRONG
                # low < mid or low > mid
                # two cases
                elif array[low] > array[mid]:
                    if array[mid] < target <= array[high]:
                        low = mid + 1
                    else:
                        high = mid - 1
            else:
                index = mid
                break

        return index

#@ at least half of array is sorted

#@ One To Many(OTM):
#  use the known part to process
#  this case, it will always have at least half part sorted
#  which means, I could only process the sorted part,
# if it's not in the sorted part
# then it in the unsorted part. So that half eliminated.
# that's why we have the speed of log(n)
# Always Use and Process the Known part
# and decompose the unknown part to know


if __name__ == '__main__':
    problems = [4, 5, 6, 7, 0, 1, 2]  # input
    result = Solution.solve(problems, 5)

    print result
    assert result == 1, "Solution Error."   # output check

    result = Solution.solve(problems, 1)

    print result
    assert result == 5, "Solution Error."  # output check

    result = Solution.solve(problems, 3)

    print result
    assert result == -1, "Solution Error."  # output check

    print "problems solved."
