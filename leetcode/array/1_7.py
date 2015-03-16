'''
Problem: Two Sum
algorithm:
    hashmap all index and items
    + 1

    if not Index
        could do sort and check low and high bound
tags: hashmap
'''


class Solution:
    @classmethod
    # Time: O(n)
    # Space: O(n)
    def solve(self, problems, target):
        # Solution here
        array = problems
        mapping = {num: index + 1 for index, num in enumerate(array)}
        result = []

        for num in mapping:
            # make sure the first index greater than the second
            if target - num in mapping and mapping[target-num] > mapping[num]:
                result.append(mapping[num])
                result.append(mapping[target-num])
            else:
                pass
        return result

# Think: two values, easy mapping

# ReThink:

# Summary:
#@ index, num in enumerate(list)
#@ mapping may need result list

    @classmethod
    # Time: O(n)
    # Space: O(n)
    def better_solve(self, problems):
        # Solution here
        pass

if __name__ == '__main__':
    problems = [2, 7, 11, 15]  # input
    result = Solution.solve(problems, 9)

    print result
    assert result == [1, 2], "Solution Error."  # output check

    print "problems solved."
