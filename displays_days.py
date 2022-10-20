print('''
This program accepts numbers from 1 to 7 from users and
displays the days of the week corresponding to those
numbers given: 1 = "Sunday" ...''')

days_of_the_week = {1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednessday", 5:"Thursday",
                    6: "Friday", 7: "Saturday"}

day_number = int(input("Enter the number you would like to check: "))

if day_number in days_of_the_week:
    print(days_of_the_week[day_number])
else:
    print("You have entered and invalid day number. A Week can only be 7 days")
