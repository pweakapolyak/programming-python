# --------------------- Найти сумму всех отрицательных чисел ---------------------

# Реализовать функцию negative_sum, на вход список из целых чисел.
# На выходе сумма всех отрицательных чисел.

# negative_sum([-5,-2, 15, 10, -3]) -> -10

# --------------------- Найти сумму всех отрицательных чисел ---------------------

def negative_sum(num_list):
    result_sum = 0
    for element in num_list:
        if element < 0:
            result_sum += element
    return result_sum


if __name__ == "__main__":
    print(negative_sum([-5, -2, 15, 10, -3]))
