# Task 1: Leap Year Checker

year = int(input("Enter a year: "))

if ( year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")