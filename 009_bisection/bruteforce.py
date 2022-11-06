import hashlib
import time


super_secret_password = "tests"
hash = hashlib.md5(super_secret_password.encode('utf-8')).hexdigest()
print(hash)

num_of_guess = 0

# start = time.time()
# for first_char in range(97, 122+1):
#     for second_char in range(97, 122+1):
#         for third_char in range(97, 122+1):
#             for fourth_char in range(97, 122+1):
#                     guess = chr(first_char) + chr(second_char) + chr(third_char) + chr(fourth_char)
#                     num_of_guess += 1
#                     if hash == hashlib.md5(guess.encode('utf-8')).hexdigest():
#                         print('The password: ', guess, '!!!!!!!!!')
#                         print('Number of guesses: ', num_of_guess)
# end = time.time()
# print('Time: ', end - start)

start = time.time()
for first_char in range(97, 122+1):
    for second_char in range(97, 122+1):
        for third_char in range(97, 122+1):
            for fourth_char in range(97, 122+1):
                for fifth_char in range(97, 122+1):
                    guess = chr(first_char) + chr(second_char) + chr(third_char) + chr(fourth_char) + chr(fifth_char)
                    num_of_guess += 1
                    if hash == hashlib.md5(guess.encode('utf-8')).hexdigest():
                        print('The password: ', guess, '!!!!!!!!!')
                        print('Number of guesses: ', num_of_guess)
end = time.time()
print('Time: ', end - start)