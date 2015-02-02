def quick_sort(array):
    def partition(arr, low, high):
        pivot = arr[low]
        i, j = low, high

        while i < j:
            # if arr[i] <= pivot and i <= high
            # i will out of index when access the last element
            # use high first it prevent it from out of index
            while i <= high and arr[i] <= pivot:
                i += 1
            while j >= low and arr[j] > pivot:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        # swap pivot
        # might out of index, when j is the last element
        # This is prevent from low<high in qs_rec
        arr[low], arr[j] = arr[j], arr[low]
        return j

    def qs_rec(array, low, high):
        if low < high:
            pivot = partition(array, low, high)
            # TOREAD: pivot is already sorted
            qs_rec(array, low, pivot - 1)
            qs_rec(array, pivot + 1, high)

    qs_rec(array, 0, len(array) - 1)
    return array


if __name__ == '__main__':
    array = [55, 23, 26, 2, 25]
    res = [2, 23, 25, 26, 55]

    print array
    assert res == quick_sort(array)

    print "test passed."
