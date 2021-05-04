def calc_total_money_earned(salary, salary_increase, months):
    result = salary

    for m in range(months - 1):
        salary += salary_increase
        result += salary

    return result

def calc_total_expenses(expenses, months):
    return expenses * months


def print_result(money_earned, expenses, car_price):

    if money_earned - expenses >= car_price:
        print("Have a nice ride!")
    else:
        print("Work harder!")


initial_salary = float(input())
monthly_expenses = float(input())
monthly_salary_increase = float(input())
dream_car_price = float(input())
saving_months = int(input())

total_money_earned = calc_total_money_earned(initial_salary, monthly_salary_increase, saving_months)
total_expenses = calc_total_expenses(monthly_expenses, saving_months)
print_result(total_money_earned, total_expenses, dream_car_price)