# --------------------- trim ---------------------

# Реализовать функцию trim.
# На вход передается строка.
# На выходе строка без пробелов в начале и в конце.
# Пример trim("     Test  string     ") -> "Test  string"

# --------------------- trim ---------------------

def remove_whitespaces_from_begin(str):
    index_first_not_whitespace = 0
    for index, char in enumerate(str):
        if char != " ":
            index_first_not_whitespace = index
            break

    return str[index_first_not_whitespace:]

def trim(str):

    result = remove_whitespaces_from_begin(str)
    result = result[::-1]
    result = remove_whitespaces_from_begin(result)[::-1]

    return result


if __name__ == "__main__":
    print(trim("     Test  string     "))
