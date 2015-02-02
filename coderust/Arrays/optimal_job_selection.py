class Interval:
    def __init__(self, st, en, j_id):
        self.start = st
        self.end = en
        self.job_id = j_id


# O(3n)
def optimal_job_sel(_list):
    # TOREAD: sort by end times
    sort_table = sorted(_list, key=lambda x: x.end)
    res = [sort_table[0]]

    for job in sort_table[1:]:
        if res[-1].end < job.start:
            res.append(job)

    return [x.job_id for x in res]


# O(2n)
def better_sel(_list):
    sort_table = sorted(_list, key=lambda x: x.end)
    res = []
    cur = Interval(0, 0, 'tmp')  # created an instance

    for job in sort_table:
        if cur.end < job.start:
            res.append(job.job_id)
            cur = job
    return res

if __name__ == '__main__':
    A = Interval(11, 14, 'A')
    B = Interval(3, 12, 'B')
    C = Interval(1, 4, 'C')
    D = Interval(7, 10, 'D')
    E = Interval(4, 10, 'E')
    table = [A, B, C, D, E]

    res = ['C', 'D', 'A']

    assert res == optimal_job_sel(table)

    assert res == better_sel(table)

    print "test passed."
