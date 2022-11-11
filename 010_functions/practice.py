import math


def input_user_data():
    total_cost = int(input('Enter house total cost: '))
    annual_salary = int(input('Enter annual salary: '))
    goal_of_months = int(input('Enter num of months: '))
    return total_cost, annual_salary, goal_of_months

def model_investment(
    cost_of_down_payment,
    monthly_investment_rate,
    monthly_salary,
    portion_saved_percent
):
    month_guess = 0
    current_savings = 0
    while current_savings < cost_of_down_payment:
        current_savings += current_savings * monthly_investment_rate
        current_savings += monthly_salary * portion_saved_percent / 100

        month_guess += 1
    return month_guess

def bisection(
    cost_of_down_payment,
    monthly_investment_rate,
    monthly_salary
):
    low = 0
    high = 100

    portion_saved_percent = (low + high) / 2
    month_guess = model_investment(
        cost_of_down_payment,
        monthly_investment_rate,
        monthly_salary,
        portion_saved_percent
    )

    while month_guess != goal_of_months:

        if month_guess < goal_of_months:
            high = portion_saved_percent
        else:
            low = portion_saved_percent

        portion_saved_percent = (low + high) / 2

        month_guess = model_investment(
            cost_of_down_payment,
            monthly_investment_rate,
            monthly_salary,
            portion_saved_percent
        )

        if math.isclose(portion_saved_percent, 100) and month_guess > goal_of_months:
            return None

    return portion_saved_percent

portion_of_down_payment = 0.25
annual_investment_rate = 0.04
monthly_investment_rate = annual_investment_rate / 12

total_cost, annual_salary, goal_of_months = input_user_data()

monthly_salary = annual_salary / 12
cost_of_down_payment = total_cost * portion_of_down_payment

result = bisection(
    cost_of_down_payment,
    monthly_investment_rate,
    monthly_salary
)

if result is None:
    print('impossible')
else:
    print(result)