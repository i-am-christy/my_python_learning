dict1 = {"one":1, "two":2, "three":3, "four":4} #dict with string key
print(dict1)
dict2 = {1:"one", 2:"two", 3:"three", 4:"four"} #dcit with int key
print(dict2)
dict3 = {(1,2,3):"integers", ("a", "b", "c"):"letters", (1.1,2.1,3.1):"float"}#dict with tuple keys
print(dict3)
dict4 = { 1:["one", "two", "three"], 2:["kate", "vera", "ade"]} #dict with list values
print(dict4)
print(type(dict4))
dict5 = dict()
print(dict5)
dict6 = dict(I="one", II="two", III="three")
print(dict6)
print(dict6["I"])
print(dict6["II"])
print(dict6["III"])
print(dict6.get("I"))
print(dict6.get("IV"))

#iterattion
for key in dict6:
    print("key = "+key+ ", value = " +dict6[key])

dict6["I"] = "eleven"
dict6["II"] = "twenty-two"
dict6["III"] = "thirty-three"
dict6["IV"] = "four"
dict6["V"] = "five"
print(dict6)
del dict6["V"]
print(dict6)
del dict3
#print(dict3)
print(dict6.keys())
print(dict6.values())
print("IV" in dict6)
print("V" not in dict6)

dict7 = {"name":"vera", "age":25, "marks":40}
dict8 = {"name":"kate", "age":22, "marks":60}
dict9 = {"name":"alex", "age":50, "marks":80}
dict10 = {1:dict7, 2:dict8, 3:dict9}
print(dict10)
print(dict10[1]["age"])
dict1.clear()
print(dict1)
keys = {"mumbai", "bangalore", "chicago", "new york"}
values = "city"
dict11 = dict.fromkeys(keys, values)
print(dict11)
print(dict10.items())
print("dict 2 popped value:", dict2.pop(4))
print("dict 2 after popping:", dict2)
print(dict2.pop(4, "key not found"))
print(dict2.popitem()) #re,oves the last item from the dict
print(dict2)

dict12 = {"I":1, "II":2, "III":3}
dict13 = {"one":1, "two":2}
dict12.update(dict13)
print(dict12)
