# --------------------- Интервалы  ---------------------

# C клавиатуры вводится целое число, вывести True/False, если
# число в интервале [100, 500) <- 100 включительно, 500 не включительно

# --------------------- Интервалы ---------------------

def task():
    num = int(input('Enter num:'))
    is_in_interval = 100 <= num < 500
    print(is_in_interval)


if __name__ == "__main__":
    task()
