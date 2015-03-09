'''
Problem: Median of Two Sorted Arrays (in O(log(m+n))time)
similar to find the kth elements of two arrays
algorithm:
    compare the mid point
    and git rid of half of array values

median: array[len(array)/2]
'''


class Solution:
    @classmethod
    # Time: O(m + n)
    # Space: O(n)
    def solve(self, problems):
        # Solution here
        A, B = problems
        k = (len(A) + len(B)) / 2  # is 5
        pa = pb = 0
        # if 11 elements, the median is 6th elements
        while (pa + pb) <= k - 2:
            # or (pa + pb) < k - 1:
            # pa, pb is 0 and 1 elements
            # then 1 2, 2 3, 3 4, 4 5
            # TOREAD: 6th elements, 0..5, already have 2 elements
            # which means only move 4 times, we get median
            if A[pa] > B[pb]:
                pb += 1
            else:
                pa += 1

        return max(A[pa], B[pb])

# Think: median is
# [0, 1, 2, 3, 4,   5,   6, 7, 8, 9, 10]
# if odd number like 11, then median = (11/2) + 1 = 6(6th element, array[5])
# [0, 1, 2, 3,   4, 5,   6, 7, 8, 9 ]
# if even number like 10, then median = 10/2 = 5(5th element, array[4])


def find_kth(A, m, B, n, k):
    if m > n:
        return find_kth(B, n, A, m, k)
    if m == 0:
        return B[k - 1]
    if k == 1:  # first element
        return min(A[0], B[0])

    # if a has less than k/2 elements, ia is m
    # elif a has more than k/2 elements, ia is k/2
    ia = min(k/2, m)
    ib = k - ia

    if A[ia - 1] < B[ib - 1]:
        # TOREAD: remove the less part and REMEMBER to reduce k
        return find_kth(A[ia:], m - ia, B, n, k - ia)
    elif A[ia - 1] > B[ib - 1]:
        return find_kth(A, m, B[ib:], n - ib, k - ib)
    else:  # if A[ia -1] == B[ib-1]
        return A[ia - 1]


# ReThink: get rid of k/2 elements in each computation
# base case: assume A always has less elements
#           A run out, then return B.k-1
#           if k is the first element return any
#  rec: imaging: a has k and b has k elements
# each time compare a[k/2 - 1] and b[k/2 - 1]
# remove the smaller part, because k is always in the larger part
# However, there will be elements less than k/2
# then choose the less value as piviot
# the other part use k - piviot as index
# so in real, we cannot always get rid of k/2 elements

# Summary:

if __name__ == '__main__':
    A = [1, 2, 3, 4, 5, 6]
    B = [1.1, 2.2, 3.3, 4.4, 5.5]
    problems = [A, B]  # input
    result = Solution.solve(problems)

    print result
    assert result == 3.3, "Solution Error."  # output check

    print find_kth(A, 6, B, 5, 6)

    print "problems solved."
