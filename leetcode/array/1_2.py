# Problem: remove duplicates from sorted array II
# allow at most twice duplicates


class Solution:
    @classmethod
    # Time: O(n)
    # Space: O(1)
    def solve(self, problems):
        # Solution here
        array = problems
        pre = repeat = 0
        for cur in range(len(array)):
            if array[pre] == array[cur]:
                if repeat == 1:
                    continue
                else:
                    repeat += 1
                    pre += 1         # TOREAD: when there is one more repeat
                    # the previous pointer need to move forward one more the make 
                    # the duplicate repeat twice
            else:
                pre += 1
                array[pre] = array[cur]
                repeat = 0

        return array[: pre + 1]

#@ two pointers
# add flag to record the repeat times
# REMEMBER: to move the previous pointer, or it will not keep the duplicates
# think about this, if you just check the repeat times, but not moving the pointer
# then nothing has been changed.

# To avoid this: missing important move
# do difficiate change
# differece from 1_1: 
# 1. add counts flag
# 2. after counts move, if counts less than requirement

# better understanding, that previous pointer creates a new array
# to keep dupilicates, the pre pointer needs to move

    # Time: O(n)
    # Space: O(1)
    @classmethod
    def better_solve(self, problems):
        array = problems
        # try to solve it with only one value 2
        pre = 2
        for cur in range(2, len(array)):
            if array[cur] != array[pre - 2]:
                array[pre] = array[cur]
                pre += 1
            else:
                pass

        return array[: pre]   # TOREAD: the last element is before pre
        # the pre element update the last

# thinking: duplicates, when cur pointer on it, pre pointer should not move
# when cur != pre , all move should happen and updates should happen
# when cur == pre , hold moves
# question is how?
# solution: 

#   when cur != pre - 2 (in this case, pre == pre-2, all same number in the ruler)
#               which is a way to extend one pointer
#        update pre <- cur, and pre += 1
#   when cur == pre - 2, cur just do + 1


#@ poniter ruler
# use pre-2 and pre as a ruler, to make sure I have twice the number(2 distance)
# which means, all numbers under ruler([pre-2 to pre]) are the same
# which also means [0, 1, 2], pre ruler has covered 3 numbers.
# the last number could be update any time( do array[pre] = array[cur])
# if we use pre-1 and pre, its [0, 1], that means we need to update the next number
# ( do array[pre+1] = array[cur])


#@ the corner case:
# if the value update the last, don't include it
# and array[: pre] means [: pre)
# range(5) == [0, 1, 2, 3, 4] == [0: 5)


if __name__ == '__main__':
    problems = [1, 1, 1, 2, 2, 3]# input
    result = Solution.solve(problems)

    print result

    assert result == [1, 1, 2, 2, 3], "Solution Error." # output check

    print "problems solved."

    problems = [1, 1, 1, 2, 2, 3]
    print Solution.better_solve(problems)