set1 = {1,2,3,4,5}#int set
print(set1)
set2 = {"vera", "kate" "kaay", "paul"} #str set
print(set2)
set3 = {True, False} #bool set
print(set3)
set4 = set() #empty set
print(set4)
print(type(set4))
set5 = {1.0, 2.0 , 3.0, 4.0, 5.0} #float set
print(set5)
set6 = {1.0, 2, True, "vera"} #heterogenous set
print(set6)
set7 = {(12,57,43), 1,2.4, "great"} #set of hasables
print(set7)

#conversion
set8 = set("sabi programmers") #converts string to set
print(set8)
set9 = set(["sabi", "programmers"]) #converts list to set
print(set9)
set10 = set(("sabi", "programmers")) #converts tuple to set
print(set10)
set11 = set({1:"sabi", 2:"programmers"}) #converts dict to set
print(set11)

#set functions
set12 = set() #modifying a set
set12.add(20)
set12.add("christianah")
set12.add(True)
set12.add(40.123)
print("Befire uodate, set 12: ", set12)
set13 = {"vera", "Alex", "sola", "wunmi"}
set12.update(set13) #upadte function
print("After updating, set 12: ", set12)
set14 = {1, 2, 3, 4, 5}
set15 = {4, 5, 6, 7, 8}
print(set14 or set15, "using the or keyword") #or operator
print(set14 | set15, "using |") #or operator
print(set14 & set15, "using the & operator") #and ooperator
print(set14 and set15, "using the and keyword")
print(set14 - set15, "using set14 - set15") #difference
print(set15 - set14, "using set15 - set14")
print(set14 ^ set15, "using ^")
print(set14.union(set15), "using union")
print(set14.intersection(set15), "using interection")
print(set14.difference(set15), "using difference")
print(set15.difference(set14), "using difference")
print(set14.symmetric_difference(set15), "using symmetric difference")
print(set15.symmetric_difference(set14), "using symmetric difference")
set16 = set3.copy() #copy method
print("set 16:", set16)
set3.clear()
print("set 3:", set3) #clear method

#difference update
set14 = {1, 2, 3, 4, 5}
set15 = {4, 5, 6, 7, 8}
print("set 14 before difference_update", set14)
print("set 15 before difference_update", set15)
set14.difference_update(set15)
print("set 14 after differnce_upadte", set14)
print("set 14 after differnce_upadte", set15)

#intersection update
set14 = {1, 2, 3, 4, 5}
set15 = {4, 5, 6, 7, 8}
print("set 14 before intersection_update", set14)
print("set 15 before intersection_update", set15)
set15.intersection_update(set14)
print("set 14 after intersection_update", set14)
print("set 15 after intersection_update", set15)

#symmetric differnce update
set14 = {1, 2, 3, 4, 5}
set15 = {4, 5, 6, 7, 8}
print("set 14 before symmetric_difference_update", set14)
print("set 15 before symmetric_difference_update", set15)
set15.symmetric_difference_update(set14)
print("set 14 after symmetric_difference_update", set14)
print("set 15 after symmetric_difference_update", set15)
print(set14.discard(4)) #discard method
set17 = {1,2}
print(set15.remove(6)) #remove method
print("popped value:", set16.pop()) #pop method
print("new set:", set16)
print(set17.issubset(set14)) #issubset method
set18 = {20,30}
print(set18.isdisjoint(set14)) #isdisjoint method
