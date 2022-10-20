print('''
The following program accepts the price of bikes from users
and calculates the road tax of the bike based on the following conditions:
price > 100,000 pays 15% road tax,
price > 50,000 and < 100,000 pays 10% road tax and
price <= 50,000 pays 5% road tax''')

price = int(input("Enter the price of your bike: "))
tax15 = price * (15/100)
tax10 = price * (10/100)
tax5 = price * (5/100)

if price > 100000:
    print(f"The road tax for your bike is {round(tax15)} naira")
elif price < 100000 and price > 50000:
    print(f"The road tax for your bike is {round(tax10)} naira")
else:
    print(f"The road tax for your bike is {round(tax5)} naira")
        
