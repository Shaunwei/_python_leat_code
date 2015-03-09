'''
Remove Duplicates From Sorted Array
algorithm:
    keep update pointer
        if cur val == pointer:
            continue
        else:
            update and advance pointer
        return [0, pointer + 1]
tags: two pointers, +1 problem
'''


class Solution:
    @classmethod
    def solve(self, problems):
        # Solution here
        array = problems
        pre = 0
        for cur in range(len(array)):
            if array[pre] == array[cur]:
                continue
            else:
                pre += 1
                array[pre] = array[cur]

        return array[:pre+1]
        # TOREAD: return +1, because pre at the last element
        # if return pre, if its 1
        # then it only return array[0:1] this means [0:1)
        # so need to return [0:2) == [0, 1]
        # means array [: pre)

#@ + 1 problem
#@ two pointer, one check if duplicate, one refresh array

#@ range(len(array)) == [0, 1, 2]
# array = [1, 2, 3]


if __name__ == '__main__':
    problems = [1, 1, 2]
    result = Solution.solve(problems)

    print result
    assert result == [1, 2], "Solution Error."

    print "problems solved."
