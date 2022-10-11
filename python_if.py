price1 = 50

if price1 < 100: #check if price is < 100
    print("price is less than 100")

price2 = 50
quantity = 5
if price2 * quantity < 500: #checkes if price2 * quantity is < 500
    print("price * quantity is less than 500")
    print("price =", price2)
    print("quantity =", quantity)

price3 = 50
quantity = 5
if price3 * quantity < 100: #checks if price3 is < 100
    print("price is less than 500")
    print("price = ", price3)
    print("quantity = ", quantity)
print("No if block executed") #prints regardless of the if blcok above

price4 = 100
if price4 > 100: #checks if price4 is > 100
    print("price is greater than 100")
if price4 == 100: #checkes if price4 is == 100
    print("price is 100")
if price4 < 100: #checks if price4 is < 100
    print("price is less than 100")

price5 = 50
if price5 >= 100: #checks if price5 is > or = 100
    print("price is greater than 100")
else: #is run if the if blck above is False
    print("price is less than 100")

price6 = 100
if price6 > 100: #checks if price6 is > 100
    print("price is greater than 100")
elif price6 == 100: #checks if price6 is = 100
    print("price is 100")
elif price6 < 100: #checks if price6 is < 100
    print("price is less than 100")

price7 = 50
if price7 > 100: #checks if price7 is > 100
    print("price is greater than 100")
elif price7 == 100: #checks if price7 is = 100
    print("price is 100")
else: #runs if both conditions above are False
    print("price is less than 100")

price = 50
quantity = 5
amount = price * quantity
if amount > 100: #checks if amount is greater than 100
    if amount > 500: #checks if amount is greater than 500
        print("Amount is greater than 500")
    else: #runs if the above if block is False
        if amount < 500 and amount > 400: #checks if amount is less than 500 and greater 400 
            print("Amount is between 500 and 400")
        elif amount < 500 and amount > 300: #checks if amount is less than 500 and greater 300 
            print("Amount i between 500 and 300")
        else: #runs if both the if and elif blocks are False
            print("Amount is between 500 and 200")
elif amount == 100: #checks if amount is = 100
    print("Amount is 100")
else: #runs if the very first if and the immediate elif blocks are False
    print("Amount is less than 100")




