# --------------------- Мода ---------------------

# На вход дается список целых чисел.
# На выходе возвращается мода - это значение которое встречается большее количество раз,
# если два или более значения встречаются одинаковое количество раз и при этом больше всего, то можно вернуть любое

# moda([5,5,5,10,10,2,2,2,0,2]) -> 2

# Если список пустой, вернуть значение None

# --------------------- Мода ---------------------

def count_of_value(num_list, value):
    counter = 0
    for element in num_list:
        if element == value:
            counter += 1
    return counter


def moda(num_list):
    if not num_list:
        return None

    moda_value = num_list[0]
    moda_count = count_of_value(num_list, moda_value)

    for element in num_list:
        if element == moda_value:
            continue
        new_count_value = count_of_value(num_list, element)
        if new_count_value > moda_count:
            moda_value = element
            moda_count = new_count_value
    return moda_value


if __name__ == "__main__":
    print(moda([5, 5, 5, 10, 10, 2, 2, 2, 0, 2]))
    print(moda([-1, 1, 5, 5, 0, 0, 0, 5, 1, 5]))
    print(moda([]))
