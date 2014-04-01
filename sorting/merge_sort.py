def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    left, right, result = [], [], []
    mid = len(arr) / 2
    left = merge_sort(arr[mid:])
    right = merge_sort(arr[:mid])
    return merge(left, right)

def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                result.append(left[0])
                left.pop(0)
            else:
                result.append(right[0])
                right.pop(0)
        else:
            if len(left) > 0:
                result.append(left[0])
                left.pop(0)
            else:
                result.append(right[0])
                right.pop(0)
    return result

if __name__ == '__main__':
    test_set = [7, 6, 2, 5, 4, 6, 1, 3, 10, 50, 3]
    print 'Sorting: {0}'.format(test_set)
    sorted_set = merge_sort(test_set)
    print 'Sorted: {0}'.format(sorted_set)