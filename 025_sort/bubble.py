


def bubble_sort(list):

    if not list or len(list) == 1:
        return list

    is_sorted = False
    while not is_sorted:
        is_sorted = True
        print('tmp: ', list)
        for j in range(1, len(list)):
            if list[j-1] > list[j]:
                is_sorted = False
                tmp = list[j]
                list[j] = list[j-1]
                list[j-1] = tmp


list = [5, 15, 0, -3, 1, 100]
bubble_sort(list)
print(list)