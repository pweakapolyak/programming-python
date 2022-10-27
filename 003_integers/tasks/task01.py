# --------------------- Конвертер времени  ---------------------

# Пользователь вводит с клавиатуры количество секунд
# Напечатать в одну строчку через пробел:
# 1) (Кол-во дней в секундах)
# 2) (Кол-во часов в оставшихся секундах)
# 3) (Количество минут в оставшихся секундах)
# 4) (Количество оставшихся секунд)

# Пример, если ввести значение - 154_950 секунд
# То выведется: "1 19 2 30"

# --------------------- Конвертер времени ---------------------


def task():
    num_of_seconds_in_minute = 60
    num_of_minutes_in_hour = 60
    num_of_hour_in_day = 24

    num_of_seconds_in_day = num_of_hour_in_day * num_of_minutes_in_hour * num_of_seconds_in_minute
    num_of_seconds_in_hour = num_of_minutes_in_hour * num_of_seconds_in_minute

    full_seconds = int(input('Enter num of seconds: '))

    num_days = full_seconds // num_of_seconds_in_day
    remaining_seconds = full_seconds % num_of_seconds_in_day

    num_hours = remaining_seconds // num_of_seconds_in_hour
    remaining_seconds = remaining_seconds % num_of_seconds_in_hour

    num_minutes = remaining_seconds // num_of_seconds_in_minute
    remaining_seconds = remaining_seconds % num_of_seconds_in_minute

    print(num_days, num_hours, num_minutes, remaining_seconds)


if __name__ == "__main__":
    task()
