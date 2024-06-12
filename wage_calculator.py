def get_nonnegative_float(text, MUST_BE_LESS_THAN_24):
    user_input = 0
    while(True):
        try:
            user_input = float(input(text))
            if (user_input <= 0):
                print("Error: Enter a value greater than 0")
                continue
            if (user_input > 24 and MUST_BE_LESS_THAN_24):
                print("Error: Enter a value less than 24")
                continue
            break
        except ValueError:
            print("Error: Please enter a nonnegative numerical value.")
    return user_input



hours_worked_daily = get_nonnegative_float("Enter the number of hours worked daily: ", True)
hourly_wage = get_nonnegative_float("Enter the hourly wage: ", False)

total_income = hours_worked_daily * hourly_wage * 350 * 0.88

print("\nPay Advice\n-------------")
print(f"Hours Worked: {hours_worked_daily}")
print(f"Hourly Wage: ${hourly_wage}")
print(f"Wages Before Taxes: ${hours_worked_daily * hourly_wage * 350:.2f}")
print(f"Tax Amount: ${hours_worked_daily * hourly_wage * 350 * 0.12:.2f}")
print(f"Annual Wage After Taxes: ${total_income:.2f}")
