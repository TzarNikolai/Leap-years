def calc_leap_year(n):
    if n % 4  == 0 and n % 100 != 0 or n % 400 == 0:
        return True
    else: 
        return False

def calc_days(first_year, last_year):
    days = 0
    for n in range(first_year -1, last_year):
        if calc_leap_year(n) == True:
            days += 366
        else:
            days += 365
    return days

first_year = int(input("Year 1? "))
last_year = int(input("Year 2? "))

num_days = calc_days(first_year, last_year)

print(f"number of days: {num_days}")

