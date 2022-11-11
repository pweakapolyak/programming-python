

def super_sqrt(number, epsilon=0.01, step=0.0001):
    """
    Calculate square root
    :param number:
    :param epsilon:
    :param step:
    :return: float
    """
    guess = 0.0

    while abs(guess*guess - number) > epsilon:

        if guess*guess > number:
            break

        guess += step

    if abs(guess*guess - number) <= epsilon:
        return guess
    else:
        return None

def negative_sqrt(number, epsilon=0.01, step=0.0001):
    return -1 * super_sqrt(number, epsilon, step)

result = negative_sqrt(2)
if result is None:
    print('Error')
else:
    print(result)