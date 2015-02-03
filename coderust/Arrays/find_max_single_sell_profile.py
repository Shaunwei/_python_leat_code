def find_max_single_sell_profile(array):
    pass


if __name__ == '__main__':
    array = [8, 5, 12, 9, 19, 1]  # this is stock price
    # buy at 5 and sell at 19
    res = [5, 19]

    assert res == find_max_single_sell_profile(res)

    print 'test passed.'
