'''def sum(a,b,c):
    print(a+b+c)
    #return a+b+c
summer = sum(5,10,15)
print(summer * 5)

def sum(a,b,c):
    return a+b+c

summer = sum(5,10,15)
#print(summer)
print(summer * 5)'''

name = "Steve"
def greet():
    global name
    name = "Bill"
    print("Hello", name)

greet()
print(name)
#write a function to find which number is greater between two arguments
def greater(a,b):
    if a > b:
        return f"{a} is greater than {b}"
    else:
        return f"{b} is greater than {a}"
    
def greaterbool(a,b):
    if a > b:
        return True
    else:
        return False
