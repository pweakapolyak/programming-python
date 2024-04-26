# --------------------- Накопления на дом #2  ---------------------

# Условия задачи на сайте.

# --------------------- Накопления на дом #2 ---------------------

def task():
    cost = int(input('Price: '))
    salary = int(input('Salary: '))
    procent = int(input('% от 1 до 100: '))
    procent_salary = int(input('% увелечения зп за полгода: '))
    price = cost / 4
    invest = 0.04 / 12
    month_salary = salary / 12
    nakoplenie = 0
    months = 0
    while nakoplenie < price:
        nakoplenie += nakoplenie * invest
        nakoplenie += month_salary * (procent / 100)
        months += 1
        if months % 6 == 0:
            month_salary += month_salary * (procent_salary /100)


    print('Number of months:', months)

if __name__ == "__main__":
    task()
