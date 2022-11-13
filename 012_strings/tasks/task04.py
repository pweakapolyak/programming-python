# --------------------- Шифр ---------------------

# Кодируем английский алфавит маленьких букв 'a'->'z'

# Функция encode - принимает на вход строку и шифрует ее.
# Шифр по правилу:
# каждую букву мы сдвигаем на 1. 'a'->'b', ... , 'c' -> 'd', ...., 'z'->'a'
# на выходе зашифрованная строка.

# Функция decode принимает на вход зашифровонную строку и раскодирует ее.

# Пример:
# encode("apple") -> "bqqmf"
# decode("bqqmf") -> "apple"

# --------------------- Шифр ---------------------


def encode(original_str):

    encoded_result = ""
    for char in original_str:
        if char == 'z':
            encoded_result += 'a'
        else:
            encoded_result += chr(ord(char)+1)

    return encoded_result

def decode(encoded_str):
    decoded_result = ""
    for char in encoded_str:
        if char == 'a':
            decoded_result += 'z'
        else:
            decoded_result += chr(ord(char) - 1)

    return decoded_result


if __name__ == "__main__":
    print(encode("apple"))
    print(decode("bqqmf"))
