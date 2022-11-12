def is_vowel(char):
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'y':
        return True

    return False


str = input('Enter some str: ')

n = len(str)

# i = 0
# while i < n:
#     print('Index:', i, 'Char: ', str[i])
#     i += 1

# for i in range(n):
#     print('Index:', i, 'Char: ', str[i])

# for char in str:
#     print('Char:', char)
#
# for index, char in enumerate(str):
#     print('Index:', index, 'Char: ', char)

# result = ""
#
# for char in str:
#     if is_vowel(char):
#         continue
#     result += char
#
# print('Result: ', result)



result = ""

for char in str:
    if is_vowel(char):
        result += char.upper()
        continue

    result += char

print('Result: ', result)
