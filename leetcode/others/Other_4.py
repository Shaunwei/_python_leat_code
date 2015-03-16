def union_find(_list):
    items = map(set, _list)
    unions = []
    for item in items:
        tmp = []
        for u in unions:
            if u.isdisjoint(item):
                tmp.append(u)
            else:
                item = u.union(item)
        tmp.append(item)
        unions = tmp
    return unions


if __name__ == '__main__':
    l = [[1, 2], [3, 4], [5, 6], [2, 5]]
    print union_find(l)
