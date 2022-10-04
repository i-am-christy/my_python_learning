str1 = 'My name is Christianah' #str with single quotes
print(str1)
str2 = "My name is Christianah" #str with double quotes
print(str2)
str3 = '''My name is Christianah''' #str with triple single quotes
print(str3)
str4 = """My name is Christianah""" #str with triple double quotes
print(str4)
 #multiline string
str5 = '''This is My
own Multi-line string
using single quotes''' #a multi-line string using triple single quotes
print(str5)
str6 = """This is My
own Multi-line string
using single quotes""" #a multi-line string using triple double quotes
print(str6)

#quote in quote
str7 = 'Welcome to "Christianah`s" Class'#incuding double quotes in single quotes
print(str7)
str8 = "Welcome to 'Christinah`s' Class" #incuding single quotes in double quote
print(str8)

#string length and indexing
str9 = 'Sabi Programmer'
print(len(str9))# return the length of str9
print(str9[0]) #return first index using +ve indexing
print(str9[-15]) #return first index using -ve indexing
print(str9[14]) #return the last index using +ve indexing
print(str9[-1]) #return last index using -ve indexing
print(str9[7]) #return 8th index using +ve indexing
print(str9[-8]) #return 8th index using -ve indexing

#string conversion
print(str(100)) #converting int to str
print(str(12.2342)) #converting float to str
print(str(False)) #converting boolean to str

#Escape sequence
str10 = 'Welcome to \'Christianah\'s\' Class' #escaping single quotes in single quotes
print(str10)
str11 = "Welcome to \"Christianah\"s\" Class" #escaping single quotes in double quotes
print(str11)
str12 = r'Welcome to \'Christianah\'s\' Class' #ignoring escape sequence using single quotes
print(str12)
str13 = 'https:\\sabiprogrammers.org\\homes' #escaping backslash
print(str13)
str14 = 'Including\tDistance' #inclusing tab in text
print(str14)
str15 = 'Go to \nNext line' #include newline
print(str15)

#string operators
str16 = 'Catherine'
str17 = 'Welcome back'
print(str16 + str17)#concatenating two strings
print(str16 *3)
print(str16[0:4]) #slicing Catherine to return the first 4 characters
print(str16[5:9]) #slicng Catherine
print("Kate" in str16) #check membership
print("Back" in str17) #check membership
print("Kate" not in str16)#check membership
print("come" not in str17)

