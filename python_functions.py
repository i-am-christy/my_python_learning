def greet(): #funcion without parameter
    print("Good morning")

def greetname(name:int): #function with parameter
    print("Good morning", name)

def square(x):
    return x * x

square_number = lambda x: x * x
sum = lambda x,y,z: x + y+ z

'''def convert_binary(x):
    numbers = []
    remainder = x % 2
    quotient = x // 2
    numbers.append(str(remainder))
    if (quotient != 0) & (remainder!= 1):
        convert_binary(quotient)
    else:
        numbers.reverse()
    return "".join(numbers)'''

    


