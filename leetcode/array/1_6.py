'''
Problem: Longest Consecutive Sequence
time: O(n)
algorithm:
    dict seqs,
    both ends expand
'''


class Solution:
    @classmethod
    # ONLY APLY TO CONSERCTIVE SEQUENCE
    # Time: O(n)
    # Space: O(n)
    def solve0(self, problems):
        # Solution here
        problems.sort()
        array = problems
        mseq = cseq = 1
        pre = array[0]
        for i in range(1, len(array)):
            pre += 1
            if pre == array[i]:
                cseq += 1
            else:
                mseq = max(mseq, cseq)
                cseq = 1
                pre = array[i]
        return mseq

#@ max flag and cur flag
#@ pre pointer to keep the increase value

    @classmethod
    # Time: O(n)
    # Space: O(n)
    def solve(self, problems):
        # Solution here
        used = {num: False for num in problems}
        longest = 0

        for i in used:
            length = 1  # TOREAD: careful, this is 1, I am already counted
            if used[i]:
                continue
            else:
                used[i] = True

            j = i + 1
            while j in used and not used[j]:
                used[j] = True
                length += 1
                j += 1

            k = i - 1
            while k in used and not used[k]:
                used[i] = True
                length += 1
                k -= 1

            longest = max(length, longest)

        return longest

# Think: time is O(n), so need to map to dict
#   set flag to true
#   keep longest value
#   local long and global long

# ReThink:

# Summary:

#@ local and global value
#@ map dict
#@ iterate all element, faster than array
#@ bi-direction
#   it's better to use a flag and then use while flag

    @classmethod
    # Time:
    # Space:
    # union and find
    # use set structure
    def better_solve(self, problems):
        pass

if __name__ == '__main__':
    problems = [100, 4, 200, 1, 3, 2]  # input
    result = Solution.solve0(problems)

    print result
    assert result == 4, "Solution Error."  # output check

    result = Solution.solve(problems)

    print result
    assert result == 4, "Solution Error."  # output check
    print "problems solved."
