# Problem: next permutation


def next_permutation(num):
    # TOREAD: compare the element and the element before
    # keep order flag to make sure the reverse case
    cur = len(num) - 2
    order = True
    while order and cur >= 0:
        # TOREAD: the element before should less than
        #  the later element
        # order means: 3, 2, 1 is decreasing
        if num[cur] < num[cur + 1]:
            order = False
        else:
            cur -= 1

    # order case
    if order:
        # reverse it in place!!
        num.reverse()
        return num

    part_val, part_num = num[cur], cur

    # TOREAD: find the first larger element
    cur = len(num) - 1
    swap_num = None
    while cur >= 0:
        if num[cur] > part_val:
            swap_num = cur
            break
        else:
            cur -= 1

    # swap elements
    num[swap_num], num[part_num] = num[part_num], num[swap_num]

    # num[part_num + 1:: -1]
    # TOREAD: idea is great to do partial reverse
    # But python doesn't support this
    # Do replace instead
    num[part_num+1:] = reversed(num[part_num+1:])
    return num


def next_permutation1(num):
    order = True
    cur = len(num) - 2  # the -2 element
    # find the first non order number
    while order and cur >= 0:
        # this order is decreasing order
        if num[cur] < num[cur + 1]:
            order = False
        else:
            cur -= 1

    # edge case
    if order:
        num.reverse()
        return num[:]

    part_num = cur
    cur = len(num) - 1  # the last element
    # find the first number larger than part_num
    while cur >= 0:
        if num[cur] > num[part_num]:
            break
        else:
            cur -= 1

    # swap
    num[cur], num[part_num] = num[part_num], num[cur]

    # reverse the elements after part_num in place
    num[part_num + 1:] = reversed(num[part_num + 1:])

    return num[:]

if __name__ == '__main__':
    a = [1, 2, 3]
    print next_permutation(a)
    print next_permutation(a)
    print next_permutation(a)
    print next_permutation(a)
    print next_permutation(a)
    print next_permutation(a)
    print next_permutation(a)


