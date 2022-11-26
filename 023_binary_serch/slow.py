

def binary_search_1(list, element):
    if not list:
        return False
    elif len(list) == 1:
        return list[0] == element
    else:
        middle = len(list) // 2
        if list[middle] > element:
            return binary_search_1(list[:middle], element)
        else:
            return binary_search_1(list[middle:], element)