# --------------------- Число или буква  ---------------------

# Пользователь вводит с клавиатуры символ(строка)
# Если символ 0,1,2,3,4,5,6,7,8,9, то печатается "digit"
# Если символ англиского алфавита a-z, A-Z, то печатается "alpha"
# Иначе печатается "incorrect character"

# --------------------- Число или буква ---------------------

def task():
    char = input('Enter char: ')
    char_code = ord(char)

    if 48 <= char_code <= 57:
        print('digit')
    elif 65 <= char_code <= 90 or 97 <= char_code <= 122:
        print('alpha')
    else:
        print('incorrect character')


if __name__ == "__main__":
    task()
