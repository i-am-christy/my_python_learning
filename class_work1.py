#collect user score
#enter user name
#return the grade
#>= 70 == A
#btw 60 and 69 = B
#btw 55 and 59 =C
#btw 54 and 50 = D
#btw 49 and 45 = E
#< 45 = F

name = input("Enter your name: ")
grade = int(input("Enter your grade: "))

#print(f"{name}'s score is {grade}")
if grade >= 70:
    print(f"{name}'s score is {grade}, hence {name}'s grade is A")
elif grade < 70 and grade > 59:
    print(f"{name}'s score is {grade}, hence {name}'s grade is B")
elif grade < 60 and grade > 54:
    print(f"{name}'s score is {grade}, hence {name}'s grade is C")
elif grade < 55 and grade > 49:
    print(f"{name}'s score is {grade}, hence {name}'s grade is D")
elif grade < 50 and grade > 44:
    print(f"{name}'s score is {grade}, hence {name}'s grade is E")
else:
    print(f"{name}'s score is {grade}, hence {name}'s grade is F")
