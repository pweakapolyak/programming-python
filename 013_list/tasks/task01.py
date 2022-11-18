# --------------------- Максимальное и минимальное число в списке ---------------------

# Разработать функции по поиску максимального и минимального числа в списке по модулю(abs)
# На вход список из целых чисел, на выходе целое число или None.
# Пример:
# max_abs([-100, 15, 50]) -> -100
# max_abs([-100, 15, 50]) -> 15

# Если список пустой, то вернуть None

# --------------------- Максимальное и минимальное число в списке ---------------------

def max_abs(num_list):
    # if len(list) == 0
    if not num_list:
        return None
    max_value = num_list[0]

    for element in num_list:
        if abs(max_value) < abs(element):
            max_value = element
    return max_value


def min_abs(num_list):
    if not num_list:
        return None
    min_value = num_list[0]

    for element in num_list:
        if abs(min_value) > abs(element):
            min_value = element
    return min_value


if __name__ == "__main__":
    print(max_abs([-100, 15, 50]))
    print(min_abs([-100, 15, 50]))
    print(min_abs([]))
