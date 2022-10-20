print('''
This program accepts a year from a user and
checks whether it is a leap year or not''')

year = int(input("Please enter the year you'd like to check: "))

if year % 4 == 0:
    print(f"Year {year} is a leap year")
elif year % 100 and year % 400 == 0:
    print(f"Year {year} is a leap year")
else:
    print(f"Year {year} is not a leap year")
