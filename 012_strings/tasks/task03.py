# --------------------- Количество слов ---------------------

# Реализовать функцию word_count(str)
# На вход передается строка
# На выходе количество слов в строек - целое число
# Слова разделены пробелами, внимание между двумя словами может быть больше одного пробела.
# Знаков пунктуации не будет.

# "   Мишка косолапый    по   лесу идет     " -> 5

# --------------------- Количество слов ---------------------
import task02

def word_count(str):
    preprocessed_string = task02.trim(str)
    if preprocessed_string == "":
        return 0

    counter = 0
    is_in_word = False

    for char in preprocessed_string:
        if char != " " and not is_in_word:
            counter += 1
            is_in_word = True
        elif char == " ":
            is_in_word = False

    return counter


if __name__ == "__main__":
    print(word_count("   Мишка косолапый    по   лесу идет     "))
