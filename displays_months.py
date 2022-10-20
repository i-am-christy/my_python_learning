print('''
This program accepts numbers from 1 to 12 and returns the corresponding
month given: 1 = "January"''')
months = {1: "January", 2: "February", 3:"March", 4:"April", 5:"May", 6:"June",
          7: "July", 8: "August", 9: "September", 10: "October", 11: "November",
          12: "December"}
number = int(input("Please enter the number of the month you would like to check: "))

if number in months:
    print(f"You entered {number} and its corresponding month is {months[number]}")
else:
    print("You have entered an invalid month number")

if number in [4, 6, 9, 11]:
    print(f"{months[number]} has 30 days")
elif number in [1, 3, 5, 7, 8, 10, 12]:
    print(f"{months[number]} has 31 days")
elif number == 2:
    print(f"{months[number]} has 28 days")
else:
    print("You have entered an invalid month number")

        
