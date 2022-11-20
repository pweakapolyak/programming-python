# --------------------- Найти всевозможные перестановки букв в слове ---------------------

# Реализовать функцию permutation(word).
# На вход слово, на выходе список из всех возможных перестановок букв в слове.

# permutation("tea") -> ["tea", "tae", "eta", "eat", "ate", "aet"]

# --------------------- Найти всевозможные перестановки букв в слове ---------------------

def remove_char_from_word_by_index(word, delete_index):
    if delete_index == 0:
        return word[1:]
    elif delete_index == len(word) - 1:
        return word[:-1]
    else:
        return word[:delete_index] + word[delete_index + 1:]

def permutation(word):
    if len(word) == 1 or len(word) == 0:
        return word

    result = []

    for index, char in enumerate(word):
        word_without_char = remove_char_from_word_by_index(word, index)
        list_sub_permutations = permutation(word_without_char)
        result += [char + x for x in list_sub_permutations]

    return result


if __name__ == "__main__":
    print(permutation("tea"))
