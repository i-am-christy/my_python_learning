#input that takes c or f, if c convert to celsius and convert to farihient if f
converter = input("Enter 'c' to convert to celsius and 'f' to convert to fahrenheit: ").lower()

if converter == "c":
    temp = int(input("Enter the temperature to convert to celsius: "))
    c_temp = round((temp - 32) * (5/9))
    print(f"{temp}F is {c_temp}C")
elif converter == "f":
    temp = int(input("Enter the temperature to convert to fahrenheit: "))
    f_temp = round(((9 * temp) / 5) + 32)
    print(f"{temp}C is {f_temp}F")
else:
    print("Invalid value")
    
