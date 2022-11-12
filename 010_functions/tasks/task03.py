# --------------------- Найти месяц по номеру дня в году ---------------------

# Реализуйте функцию get_month_by_day_number
# На вход передается номер дня в году и параметр високосный ли год
# На выходе нужно вернуть название месяца

# В обычном году 365 дней, а в високосном 366
# Если номер дня будет меньше ил равен нулю или больше максимального количества дней,
# то нужно вывести "incorrect day number"

# Иначе вывести значение месяца с большой буквы.

# Таблица месяцев.

# January - 31 days
# February - 28 days in a common year and 29 days in leap years
# March - 31 days
# April - 30 days
# May - 31 days
# June - 30 days
# July - 31 days
# August - 31 days
# September - 30 days
# October - 31 days
# November - 30 days
# December - 31 days


# --------------------- Найти месяц по номеру дня в году ---------------------

def get_month_by_day_number(day_number, is_leap_year):
    pass


if __name__ == "__main__":
    print(get_month_by_day_number(60, is_leap_year=True))
    print(get_month_by_day_number(60, is_leap_year=False))
