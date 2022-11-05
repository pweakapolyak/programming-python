# --------------------- Накопления на дом #2  ---------------------

# Условия задачи на сайте.

# --------------------- Накопления на дом #2 ---------------------

def task():
    portion_of_down_payment = 0.25
    annual_investment_rate = 0.04
    monthly_investment_rate = annual_investment_rate / 12
    current_savings = 0

    total_cost = int(input('Enter house total cost: '))
    annual_salary = int(input('Enter annual salary: '))
    portion_saved_percent = int(input('Enter portion saved each month %: '))
    semi_annual_raise_percent = int(input('Enter semi annual salary raise %: '))

    monthly_salary = annual_salary / 12
    cost_of_down_payment = total_cost * portion_of_down_payment

    num_of_months = 0

    while current_savings < cost_of_down_payment:

        if num_of_months > 0 and num_of_months % 6 == 0:
            annual_salary += annual_salary * (semi_annual_raise_percent / 100)
            monthly_salary = annual_salary / 12

        current_savings += current_savings * monthly_investment_rate
        current_savings += monthly_salary * (portion_saved_percent / 100)

        num_of_months += 1

    print('Number of months:', num_of_months)


if __name__ == "__main__":
    task()