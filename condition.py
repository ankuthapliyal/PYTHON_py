# marks = int(input("Enter your marks = "))

# if(marks >= 90):
#     print("Your grade A")

# elif(marks >= 80):
#     print("Your grade is B")
# elif(marks >= 70):
#     print("Your grade is c")
# elif(marks >= 60):
#     print("Your grade is C")
# elif(marks >= 50):
#     print("you just pass")
# else:
#     print("You are fail")

# age = int(input("Enter your age:-"))

# if(age >= 18):
#     print("You are eligible to vote")
# else:
#     print("Your are not eligible to vote")

#practice1

# x = int(input("Enter the number:-"))

# if(x > 0):
#     print("Number are Positive...!")

# elif(x == 0):
#     print("Zero")

# else:
#     print("Number is a Nagative...!")


#List in python

# marks = [20, 40, 50, 60, 75, 85, 97]
# foods = ["samosa", "Pizza", "Burger", "Chole Bethure","Gulab jamun"]
# student = ["Anku thapliyal", 20, "Uttrakhand"]
# print(marks[6])
# marks[0] = 45 # list is a mutable modifying eage
# print(marks)
# print(marks[1:])
# print(max(marks))
# print(min(marks))
# print(foods[4])
# print(len(foods))
# print(student[1])
# num = [[[1,2,3][4,5][6,7]]] #3d list
# print(num)
# l1 = list("anku")
# print(l1)

#List method

# marks = [20, 40, 50, 60, 75, 85, 97]
# print(marks)
# marks.append(92)
# print(marks)
# marks.extend([99,100,105])
# print(marks)
# marks.extend('anku')
# print(marks)
# marks.insert(0,10)
# print(marks)
# l1 = [1,2,3,4]
# l2 = [5,6,7,8]
# print(l1 + l2)
# marks.sort() 
# print(marks)
# marks.copy()
# print(marks)
# marks.pop(0)
# print(marks)
# marks.remove(40)
# print(marks)
# marks.insert(0,20)
# print(marks)
# marks.clear()
# print(marks)

# sample = "how are you?"
# print(sample .split())
# list = []

# for i in sample.split():
#     print(i.capitalize())
#     list.append(i.capitalize())

# print(list)
# print(" ".join(list))

# sample = 'abc@gmail.com'
# print(sample[:sample.find("@")])

# l1 = [1,1,2,2,3,3,4,4] 
# l2 = [1,2,3,1]

# l = []
# for i in l1:
#     if i not in l:
#         l.append(i)
# print(l)
# take 3 food user input and store list

# food1 = input("Enter foos 1: ")
# food2 = input("Enter food 2: ")
# food3 = input('Enter food 3: ')

# foodList = [food1, food2, food3]
# print(foodList)
# print(len(foodList))

#Tuples in python

# marks = (20, 25, 30, 35, 45, 65, 75, 85, 95)
# tuple = ("anku", "Sonu", "Mohit", "Rohit", "Anil")
# emptytuple = () # empty tuple
# singletuple = (20) # integer tuple
# print(type(emptytuple))
# print(type(marks))
# print(type(singletuple))
# print(marks)
# print(marks[5])
# print(marks[:9])
# print(tuple)
# t1 = (1,2,3(4,5))
t1 = tuple("anku")
print(t1)
 
# method of tuple

# marks = (20, 25, 30, 35, 45, 65, 75, 85, 75, 95)
# print(marks)
# print(marks.index(65))
# print(marks.count(75))
# print(marks[1:])

# fruits = ("Mango", "Apple", "Banana", "Grapes", "Orange")
# print(len(fruits))

# import time

# timestemp = time.strftime('%H:%M:%S')
# print(timestemp)
# timestemp = time.strftime('%H')
# print(timestemp)
# timestemp = time.strftime("%M")
# print(timestemp)
# timestemp = time.strftime("%S")
# print(timestemp )
