# print(("anku thapliyal" + "\n") * 10)
# name = "anku"
# age = 30
# age2 = 40
# print("Actual age:", age2)
# age2 = age
# print("Change age:", age2)

# x = int(input("Enter the  of diameter: "))
# redius = x /2
# print("Radius of the circle is: ", redius)
# area = 3.13 * (x^2)
# print("Arera of circle is: ", area)
# print(type(age))


# x = input("Enter the value :-")
# convertvalue = float(x)

# print("Orignal value is = ",x, "Data Type :-",type(x))

# print("Converted value is = ", convertvalue,"Data type:-",type(convertvalue))

# celsius to Fahrenheit and kelvin
# a = float(input("Enter the celsius:- "))

# fahrenheit = (a * (9/5)) + 32
# print("celsius to fahrenheit :-",fahrenheit)

# kelvin = a + 273.15
# print("Celsius to kelvin :-", kelvin)

# WAP that  takes total bill amount and number of friends as input calcuate how much each person will pay

# bill = int(input("Enter the Total bill amount :- "))

# friends = int(input("Enter number of friends :- "))

# paybill = float(bill / friends)

# print("Each friends will pay bill :-", paybill)

# x = 5
# y = 2.8
# print(x // y)
# print(x ** y) 

# str1 = 'hello'
# str2  = "anku"
# str3 = '''thapliyal'''

# print(str2+ " "str3)  # concatinat
# print(len(str1))  # length of string
# print(str1[0],str1[2])  # indexing of string

# str4 = "Golabjamun" # string divide manye part call slicing
# print(str4[-5:-1]) #jamu
# print(str4[:6]) #gulabj
# print(str4[5:]) #jamun
# nm = "harry"
# print(nm[-4:-2])


# str = input("Enter the String: -")

# mid = len(str) // 2
# outout1 = str[mid - 1 : mid + 2]

# print( "Middle characters is :-",outout1)
# print(" last characters is :- ",str[-2:])


#String method

# str = "Anku Thapliyal"
# print(str.upper())
# print(str.lower())
# print(str.title())
# print(str.find("y"))
# print(str.replace("Anku ","madan mohan "))
# print(str.count("l"))

# str = input("Enter the string :- ")
# print(str.lower())
# print(str.replace(" ", "_"))

# name = "anku"
# age = 20
# print(f"My name is {name} and i am {age} year old")

# String methods

# Repetition String
# str = "yum!" *3
# print(str)

# x = input("Enter the string = ")
# print(len(x))
# print(x.upper())
# print(x.lower())
# print(x[0])
# print(x[0:])
# print(x[-1:])

# a = "anku!! !!!!"
# print(a)
# print(a.rstrip("!"))
# print(a.split(" "))

# hading = "introductIOn tO js"
# print(hading.capitalize())

# str = "Welcome to the console!!!"
# print(len(str))
# print(len(str.center(50)))
# print(str.endswith("!!!"))
# print(str.endswith("the", 4, 14))
# str1 = "Welcome1ToThe2Comsole"
# print(str1.isalnum())
# print(str1.isalpha())
st = "To Kill a Mocking Bird"
# print(st.istitle())
# print(st.startswith("a", 8, 14))
# print(st.startswith("o"))
print(st.endswith("d",21))
print(st.endswith("d"))
# print(st.swapcase())
# print(st.title())

print("Hello my name is {} and I am {} year old".format("anku thapliyal",20))
print("Hello my name is {1} and I am {0} year old".format("anku thapliyal",20))
print("Hello my name is {name} and I am {age} year old".format(name = "anku thapliyal",age = 20))
print("Who is pm of india".split())
print("Who is pm of india".split("i"))
print("-".join(['Who', 'is', 'pm', 'of', 'india']))
print("            anku thapliyal      ".split())