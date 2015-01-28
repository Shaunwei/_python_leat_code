# Quick Sort and pythonic


def quick_sort(array):
    less = []
    greater = []
    equal = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x > pivot:
                greater.append(x)
            else:
                equal.append(x)
        return quick_sort(less) + equal + quick_sort(greater)
    else:
        return array

if __name__ == '__main__':
    array = [1, 5, 7, 2, 3, 4, 8, 0, 7]
    print quick_sort(array)
