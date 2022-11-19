# --------------------- Найти n самых частых значений в списке ---------------------

# Реализовать функцию find_n_most_common_values которая на вход принимает массив целых чисел
# и параметр n, целое число больше 0, которое означает сколько значений нужно вернуть из функции.
# Функция возвращает список из n самых частых значений, отсортированных от большего к меньшему.

# find_n_most_common_values([5,5,5,3,3,3,3,1,2,2], 3) -> [3, 5, 2]

# --------------------- Найти n самых частых значений в списке ---------------------

from collections import Counter


def count_of_value(num_list, value):
    counter = 0
    for element in num_list:
        if element == value:
            counter += 1
    return counter


def find_n_most_common_values(num_list, n):
    set_num = set(num_list)
    element_to_count_dict = {}
    for element in set_num:
        element_to_count_dict[element] = count_of_value(num_list, element)

    result = []

    for i in range(n):
        new_max = (0, 0)
        for key, value in element_to_count_dict.items():
            if key in result:
                continue
            if new_max[1] < value:
                new_max = (key, value)
        result.append(new_max[0])

    return result


def find_n_most_common_values_2(num_list, n):
    element_to_count_dict = Counter(num_list)
    sorted_result = sorted(element_to_count_dict.items(), key=lambda item: -item[1])
    return [x[0] for x in sorted_result[:n]]  # list comprehension


if __name__ == "__main__":
    print(find_n_most_common_values([5, 5, 5, 3, 3, 3, 3, 1, 2, 2], 3))
    print(find_n_most_common_values_2([5, 5, 5, 3, 3, 3, 3, 1, 2, 2], 3))
