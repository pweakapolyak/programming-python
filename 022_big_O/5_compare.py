

def f1(n):
    result = 0
    for i in range(0, 1e9):
        result += i

    for i in range(0, n):
        result += i

    return result


def f2(n):
    result = 0
    for i in range(n):
        for j in range(n):
            result += i * j

    return result