# Given functions
class Nut:
    def __init__(self, value):
        self.v = value


class Bolt:
    def __init__(self, value):
        self.v = value


def compare(first, second):
    if first.v == second.v:
        return 0

    if first.v < second.v:
        return -1
    else:
        return 1


# solution
def sort_nuts_and_bolts(blist, nlist):
    pass


if __name__ == '__main__':
    blist = [Bolt(15), Bolt(3), Bolt(9), Bolt(4), Bolt(5)]
    nlist = [Nut(5), Nut(3), Nut(15), Nut(9), Nut(4)]

    print 'test passed.'
