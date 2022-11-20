# --------------------- Найти всевозможные перестановки букв в слове ---------------------

# Реализовать функцию permutation(word).
# На вход слово, на выходе список из всех возможных перестановок букв в слове.

# permutation("tea") -> ["tea", "tae", "eta", "eat", "ate", "aet"]

# --------------------- Найти всевозможные перестановки букв в слове ---------------------


def permutation(word):
    if len(word) == 1 or len(word) == 0:
        return word

    result = []

    for index, char in enumerate(word):
        if index == 0:
            subsequence = word[1:]
        elif index == len(word) - 1:
            subsequence = word[:-1]
        else:
            subsequence = word[:index] + word[index+1:]

        list_sub_permutations = permutation(subsequence)
        result += [char + x for x in list_sub_permutations]

    return result



if __name__ == "__main__":
    print(permutation("tea"))