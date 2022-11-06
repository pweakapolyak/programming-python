

x = int(input('Enter x: '))
guess = 0.0

epsilon = 0.01
step = 0.0001

num_of_guesses = 0

while abs(guess*guess - x) > epsilon:

    if guess*guess > x:
        break

    guess += step
    num_of_guesses += 1

if abs(guess*guess - x) <= epsilon:
    print('Sqrt: ', guess)
else:
    print('Failed. Decrease step')

print('Num of guesses: ', num_of_guesses)

