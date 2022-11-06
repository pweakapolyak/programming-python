

x = int(input('Enter x: '))

epsilon = 0.01

num_of_guesses = 0

low = 0
high = x

guess = (low + high) / 2

while abs(guess*guess - x) > epsilon:

    if guess*guess > x:
        high = guess
    else:
        low = guess

    guess = (low + high) / 2
    num_of_guesses += 1

if abs(guess*guess - x) <= epsilon:
    print('Sqrt: ', guess)
else:
    print('Failed. Decrease step')

print('Num of guesses: ', num_of_guesses)

