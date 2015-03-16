'''
Problem: Four Sum
algorithm:
    sort items and find the middle point
    hashmap
tags: sort and find
'''


class Solution:
    @classmethod
    # Time: O(n^3)
    # Space: O(n)
    def solve(self, problems):
        # Solution here
        arr, target = problems

        arr.sort()
        result = []
        for i in range(len(arr) - 3):
            for j in range(i + 1, len(arr) - 2):
                k = j + 1
                h = len(arr) - 1
                while k < h:
                    r = [arr[i], arr[j], arr[k], arr[h]]
                    s = sum(r)
                    if s == target:
                        result.append(r)
                        h -= 1
                        k += 1
                    elif s > target:
                        h -= 1
                    else:
                        k += 1
        return result

# Think:

# ReThink:

# Summary:

    @classmethod
    # Time: O(n^2)
    # Space: O(n^2)
    def better_solve(self, problems):
        # Solution here
        arr, target = problems

        arr.sort()
        result = []
        cache = {}
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                s = arr[i] + arr[j]
                if cache.get(s):
                    cache[s].append((i, j))
                else:
                    cache[s] = [(i, j), ]

        for k in range(len(arr) - 1):
            for h in range(k + 1, len(arr)):
                t = target - arr[h] - arr[k]
                if t in cache:
                    for item in cache[t]:
                        # TOREAD
                        # continue if any item reuse!!!
                        if h == item[1] or k == item[0]:
                            continue
                        else:
                            r = sorted(
                                [arr[item[0]], arr[item[1]], arr[k], arr[h]])
                            if r not in result:
                                result.append(r)
        return result




if __name__ == '__main__':
    problems = [1, 0, -1, 0, -2, 2], 0  # input
    r = [[-1, 0, 0, 1], [-2, -1, 1, 2], [-2, 0, 0, 2]].sort()
    result = Solution.solve(problems)

    print result
    assert result.sort() == r, "Solution Error."  # output check

    print "problems solved."

    result = Solution.better_solve(problems)
    print result
