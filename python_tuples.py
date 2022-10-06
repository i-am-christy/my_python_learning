tpl1 = ("chris", "tianah", "kay", "Kate") #string tuple
print(tpl1)
tpl2 = (1,2,3, 4) #int tuple
print(tpl2)
tpl3 = (1.0, 2.0, 3.0) #float tuple
print(tpl3)
tpl4 = (True, False) #bool tuple
print(tpl4)
tpl5 = (1, "vera", False, 2.0) #heterogeneous tuple
print(tpl5)
tpl6 = () #empty tuple
print(tpl6)
print(type(tpl6))
tpl7 = "chris", "tianah", "kay" #string tuple
print(tpl7)
tpl8 = 1,2,3 #int tuple
print(tpl8)
tpl9 = 1.0, 2.0, 3.0 #float tuple
print(tpl9)
tpl10 = True, False #bool tuple
print(tpl10)
tpl11 = 1, "vera", False, 2.0 #heterogeneous tuple
print(tpl11)

#indexing
print(tpl1[0]) #1st index using +ve indexing
print(tpl1[-4]) #1st index using -ve indexing
print(tpl1[3]) #last index using +ve indexing
print(tpl1[-1]) #last index using -ve indexing
print(tpl1[1]) #2nd index using +ve indexing
print(tpl1[-3]) #2nd index using -ve indexing

#deleting
del tpl10 #delete tpl10

#conversion
tpl12 = tuple("Sabi Programmer") #converts str to tuple
print(tpl12)
tpl13 = tuple(["Sabi", "Programmer"]) #converts list to tuple
print(tpl13)
tpl14 = tuple({1,2,3,4}) #converts set to tuple
print(tpl14)
tpl15 = tuple({1:"one", 2:"two"}) #conevrts dict to tuple
print(tpl15)

#operators
print(tpl1 + tpl13) #+ operator
print(tpl4 * 4) # * operator
print(tpl2[1:3]) #slicing
print(2.4 in tpl3) # in operator
print(2.4 not in tpl3) # not in operator
