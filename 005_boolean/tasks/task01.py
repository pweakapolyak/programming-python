# --------------------- Интервалы  ---------------------

# C клавиатуры вводится целое число, вывести True/False, если
# число в интервале [100, 500) <- 100 включительно, 500 не включительно

# --------------------- Интервалы ---------------------

def task():
    с = int(input('ВВедите целое число: '))

    print(100 <= с < 500)


if __name__ == "__main__":
    task()
