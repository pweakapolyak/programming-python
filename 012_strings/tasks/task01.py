# --------------------- Посчитать количество букв 'a' ---------------------

# Реализовать функцию count_a_latter которая на вход принимает строку и
# булевский параметр is_ignore_case который означает, что при подсчете нужно
# игнорировать регистр буква, т.е. 'a' == 'A'
# Функция должна возвращать количество(целое число) букв 'a'(тут именно латинская 'a')

# Пример:
# count_a_latter("Apple invented IPhone") -> 0
# count_a_latter("Apple invented IPhone", True) -> 1

# --------------------- Посчитать количество букв 'a' ---------------------

def count_a_latter(str, is_ignore_case=False):

    target = 'a'

    target_counter = 0
    for char in str:
        processed_char = char.lower() if is_ignore_case else char
        if processed_char == target:
            target_counter += 1

    return target_counter


if __name__ == "__main__":
    print(count_a_latter("Today a perfect day"))
    print(count_a_latter("Apple invented IPhone"))
    print(count_a_latter("Apple invented IPhone", True))
