


def binary_search_2(list, element, low_index, high_index):
    if low_index == high_index:
        return list[low_index] == element
    else:
        middle_index = (low_index+high_index) // 2
        if list[middle_index] == element:
            return True

        if list[middle_index] > element:
            if middle_index == low_index:
                return False
            else:
                return binary_search_2(list, element, low_index, middle_index-1)
        else:
            return binary_search_2(list, element, middle_index+1, high_index)