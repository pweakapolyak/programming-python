
def merge(left, right):
    result = []
    i, j = 0, 0
    while (i < len(left)) and (j < len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        elif right[j] < left[i]:
            result.append(right[j])
            j += 1
        else:
            result.append(right[j])
            result.append(left[i])
            i += 1
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def merge_sort(list):
    print('merge list', list)
    if not list or len(list) == 1:
        return list[:]
    else:
        middle = len(list) // 2
        left = merge_sort(list[:middle])
        right = merge_sort(list[middle:])
        return merge(left, right)


list = [5, 15, 0, -3, 1, 100]
sorted_list = merge_sort(list)
print(sorted_list)
