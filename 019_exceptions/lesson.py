
import traceback


str_input = input('Enter num:')


def super_function():
    super_function2()

def super_function2():
    raise Exception('Smth bad')

try:
    num = int(str_input)
    # if num == 5:
    #     raise Exception("We dont like number 5")
    super_function()
    print(num/num)
except ValueError:
    print('Sorry, you input is not a number: ', str_input)
except ZeroDivisionError:
    print('Sorry, zero is incorrect number')
except Exception as e:
    traceback.print_exc()
    print('Unhandled exception: ', e)