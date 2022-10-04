list1 = [] #declaring an empty list
print(list1)
list2 = ["Adewunmi", "Alex", "Kayode", "Christianah"] #declaring a list of strings
print(list2)
list3 = [1,3,5,3,6] #int list
print(list3)
list4 = [1.4, 3.5, 6.3, 5.6] #float list
print(list4)
list5 = [True, False] #bool list
print(list5)
list6 = [1, 2.0, True, "Engineer-D"] #heterogeneous list
print(list6)

#indexing
print(list2[0]) #first index using +ve indexing
print(list2[-4]) #first index using -ve indexing
print(list2[3]) #last index using +ve indexing
print(list2[-1]) #last index using -ve indexing

list7 = [1,2,3,[4,5,6,[7,8,[9]]], 10] #list of lists
print(list7)
print(list7[0]) #returns 1
print(list7[3]) #returns [4,5,6,[7,8,[9]]]
print(list7[4]) #returns 10
print(list7[3][3])#returns [7,8[9]]
print(list7[3][3][2]) #returns 9

#list conversion
list8 = [1,2,3,4]
print(type(list8))
list9 = list("Sabi Programmer") #converts a string to a list
print(list9)
list10 = list({1:"one", 2:"two"}) #converts a dictionary to a list
print(list10)
list11 = list((10,20,30)) #converts a tuple to a list
print(list11)
list12 = list({100,200,300}) #converts a set to a list
print(list12)

#iteration
for name in list2:
    print(name)

for ind in range(len(list2)):
    print(list2[ind])

#list operators
print(list2 + list3) #+ operator
print([1,2,3] *3) #* operator
print("Adewunmi" in list2) #in operator
print("Engineer-D" not in list2) #nor in operator

#slicing
print(list2[1:5]) #slicing

#update list
list2[0] = "Vera"
list2.append("Michael")
print(list2)

#remove item
print("list2: ", list2)
del list2[0]
print("After del list2[0]: ", list2)
list2.remove("Alex")
print("After removing Alex: ", list2)
print(list2.pop(0)) #remove the first item from the list
print("After popping first index: ", list2)
print(list2.pop()) #remove the last item
print("After popping the last item: ", list2)
list2.clear() #clears all the items in list2, making it an empty list
print(list2)
del list2 #deletes list2

#list methods
list13 = [2,4,6,8]
list14 = list13.copy() #copy function
print(list14)
list13.append(10) #append function
print("list13: ", list13)
print("list14: ", list14)
list13.append(4)
print(list13.count(4)) #count function
print(list13)
list14.extend([12,14,16]) #extend function
print(list14)
print(list14.index(14)) #index function
print(list13)
print(list13.index(4))
list13.insert(3, 7) #insert function
print(list13)
list13.insert(0, 1) #list.insert(index,value)
print(list13)
list13.pop(3) #remove the item at index3
print(list13)
list13.pop() #remove the last item
print(list13)
list13.remove(1) #remove 1 from list13
print(list13)
list13.reverse() #reverse function
print(list13)
list13.sort() #sort function
print(list13)
list13.sort(reverse=True)
print(list13)
