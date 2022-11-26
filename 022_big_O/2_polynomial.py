import hashlib
import time

start_symbol = 97
end_symbol = 122+1

super_secret_password = "tests"
hash = hashlib.md5(super_secret_password.encode('utf-8')).hexdigest()
print(hash)

num_of_guess = 0

start = time.time()
for first_char in range(start_symbol, end_symbol):
    for second_char in range(start_symbol, end_symbol):
        for third_char in range(start_symbol, end_symbol):
            for fourth_char in range(start_symbol, end_symbol):
                for fifth_char in range(start_symbol, end_symbol):
                    guess = chr(first_char) + chr(second_char) + chr(third_char) + chr(fourth_char) + chr(fifth_char)
                    num_of_guess += 1
                    if hash == hashlib.md5(guess.encode('utf-8')).hexdigest():
                        print('The password: ', guess, '!!!!!!!!!')
                        print('Number of guesses: ', num_of_guess)
end = time.time()
print('Time: ', end - start)