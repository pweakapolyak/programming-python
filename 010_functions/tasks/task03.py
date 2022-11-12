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

def is_day_number_correct(day_number, extra_day):

    max_day = 365 + extra_day

    if day_number <= 0:
        return False
    if day_number > max_day:
        return False
    
    return True

def get_month_by_day_number(day_number, is_leap_year):

    extra_day = 1 if is_leap_year else 0

    # extra_day = 0
    # if is_leap_year:
    #     extra_day = 1
    
    if not is_day_number_correct(day_number, extra_day):
        return "incorrect day number"
    
    max_day_in_january = 31
    max_day_in_february = (28+extra_day) + max_day_in_january
    max_day_in_march = 31 + max_day_in_february
    max_day_in_april = 30 + max_day_in_march
    max_day_in_may = 31 + max_day_in_april
    max_day_in_june = 30 + max_day_in_may
    max_day_in_july = 31 + max_day_in_june
    max_day_in_august = 31 + max_day_in_july
    max_day_in_september = 30 + max_day_in_august
    max_day_in_october = 31 + max_day_in_september
    max_day_in_november = 30 + max_day_in_october
    max_day_in_december = 31 + max_day_in_november

    if day_number <= max_day_in_january:
        return "January"
    elif day_number <= max_day_in_february:
        return "February"
    elif day_number <= max_day_in_march:
        return "March"
    elif day_number <= max_day_in_april:
        return "April"
    elif day_number <= max_day_in_may:
        return "May"
    elif day_number <= max_day_in_june:
        return "June"
    elif day_number <= max_day_in_july:
        return "July"
    elif day_number <= max_day_in_august:
        return "August"
    elif day_number <= max_day_in_september:
        return "September"
    elif day_number <= max_day_in_october:
        return "October"
    elif day_number <= max_day_in_november:
        return "November"
    elif day_number <= max_day_in_december:
        return "December"


if __name__ == "__main__":
    print(get_month_by_day_number(60, is_leap_year=True))
    print(get_month_by_day_number(60, is_leap_year=False))
