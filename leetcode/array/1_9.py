'''
Problem: Three Sum Closest
algorithm:
    sort and find
    keep global closest value(abs value)
tags: sort and find
'''


class Solution:
    @classmethod
    # Time: O(n)
    # Space: O(n)
    def solve(self, problems):
        # Solution here
        arr, target = problems

        def quick_sort(array):
            def partition(array, low, high):
                pivot = array[low]
                i, j = low, high
                while i < j:
                    while array[i] <= pivot and i <= high:
                        i += 1
                    while array[j] > pivot and j >= low:
                        j -= 1
                    if i < j:
                        array[i], array[j] = array[j], array[i]
                array[low], array[j] = array[j], array[low]
                return j

            def qst_rec(array, low, high):
                if low < high:
                    pivot = partition(array, low, high)
                    qst_rec(array, low, pivot - 1)
                    qst_rec(array, pivot + 1, high)

            qst_rec(array, 0, len(array) - 1)
            return

        quick_sort(arr)
        print arr
        closest = 9999999  # large number
        result = None
        for i in range(len(arr) - 2):
            j = i + 1
            k = len(arr) - 1
            while j < k:
                res_list = [arr[i], arr[j], arr[k]]
                # closest is abs value
                s = abs(sum(res_list) - target)
                if s < closest:
                    closest = s
                    result = res_list
                    j += 1
                else:
                    k -= 1

        return result

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
    problems = [-1, 2, 1, -4], 1  # input
    r = [-1, 1, 2]
    result = Solution.solve(problems)

    print result
    assert result == r, "Solution Error."  # output check

    print "problems solved."
