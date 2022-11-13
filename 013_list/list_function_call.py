

def del_all_negative_numbers(list):

    for item in list[:]:
        if item < 0:
            list.remove(item)


list1 = [1,-2,-4,3]

print('Before: ', list1)

del_all_negative_numbers(list1)

print('After: ', list1)

