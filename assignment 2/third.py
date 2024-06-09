# 3) Try to use functions to output maximum days of one month in a year which are
# input by user. We need validate month and year(1970-2500), if not validated,
# let the user reinput.


def error_message(year, month):
    errors = []
    if year not in range(1970, 2501):
        errors.append("Please enter a correct year (1970-2500).")
    if month not in range(1, 13):
        errors.append("Please enter a correct month (1-12).")
    return errors


def leap_year_check(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def days_in_month(month, year):
    if month == 2:
        if leap_year_check(year):
            return 29 
        else: 
            return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31


def max_day():
    while True:
        try:
            month = int(input("Enter month (1-12): "))
            year = int(input("Enter year (1970-2500): "))
            break
        except ValueError:
            print("Invalid input. Please enter numerical values.")
    
    errors = error_message(year, month)
    while errors:
        for error in errors:
            print(error)
        try:
            month = int(input("Re-enter month (1-12): "))
            year = int(input("Re-enter year (1970-2500): "))
        except ValueError:
            print("Invalid input. Please enter numerical values.")
            continue
        errors = error_message(year, month)

    days = days_in_month(month, year)

    month_names = ["January", "February", "March", "April", "May", "June",
                   "July", "August", "September", "October", "November", "December"]

    month_name = month_names[month - 1]


    print(f"{month_name} {year} has {days} days.")



max_day()
