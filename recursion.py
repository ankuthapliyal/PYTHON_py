# def multiply(a,b):
#     if(b==1):
#         return a
#     else:
#         return a + multiply(a, b-1)
# print(multiply(5,5))

# def fact(n):

#     if(n == 1):
#         return 1
#     else:
#         return n * fact(n-1)
# print(fact(5))

# def palindrome(str):

#     if(len(str) <= 1):
#         print("palindrome")
#     else:
#         if(str[0] == str[-1]):
#             palindrome(str[1:-1])
#         else:
#             print("Not palindrome")
# palindrome("abbabba")

# import time
# def fibonacci(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# start = time.time()
# print(fibonacci(48))
# print(time.time() - start)

# time are reduses for fibonacci to use memory size for throw are dynamic and memorayzation programming
# import time
# def memory(m,d):   

#     if m in d:
#         return d[m]
#     else:
#         d[m] = memory(m-1,d) + memory(m-2,d)  # dictonary d[m]
#         return d[m]

# start = time.time()
# d = {0:1,1:1}
# print(memory(48,d))
# print(time.time() - start)
# print(d)


#Lambda Function:- without name using function it will be no return value
#return only one line
#not used for code reusability
# It is highey order function
# highyer order mens as function to input for one more function or funtion to return another function
# x = lambda x: x**2
# print(x(9))
# sum = lambda x,y: x+y
# print(sum(6,7))
# number = lambda x: "Even" if x%2==0 else "Odd"
# print(number(4))

#Highyer order function
# def return_sum(func,l):
#     result = 0

#     for i in l:
#         if func(i):
#             result += i
#     return result

# l = [11,14,21,23,56,78,45,29,28]

# x = lambda x:x%2 == 0
# y = lambda x: x%2 != 0
# z = lambda x: x%3 == 0

# print(return_sum(x,l))
# print(return_sum(y,l))
# print(return_sum(z,l))

# Map function high order function:- it will be perform list operation work on all elements in list
# l1 = [1,2,3,4,5,6,7]
# result = map(lambda x:x*2,l1)
# # print(list(map(lambda x:x*2,l1)))
# print(list(result))
# print(list(map(lambda x:x%2==0, l1)))

# students = [
#     {
#         "name": "mohit",
#         "rollno": 1232,
#         "branch": "civil",
#     },
#     {
#         "name": "rohit",
#         "rollno": 1232,
#         "branch": "ece",
#     },
#     {
#         "name": "sagar",
#         "rollno": 1232,
#         "branch": "ee",
#     }
# ]

# print(list(map(lambda students:students["name"],students)))

# Filter function:- use to condition of list
# l1 = [1,2,3,4,5,6,7]
# print(list(filter(lambda x:x>4,l1)))

# fruits = ["Apple", "Mango","Orange","Guava"]
# print(list(filter(lambda fruits:"e" in fruits, fruits))

# Reduce Function:- it will be reduce of the list
import functools
# l1 = [1,2,3,4,5,6,7]
# print(functools.reduce(lambda x,y:x+y,l1)) 

# l2 = [12,34,56,11,211,58]
# print(functools.reduce(lambda x,y: x if x>y else y , l2))

# l1 = [1,2,3,4,5,6,7]
# l2 = [item *2 for item in l1]  # list concurrency
# l3 = [i**2 for i in range(10) if i%2 == 0]
# print(l2)
# print(l3)

l = [1,2,3,4,5,6,7]
d = {"Name" : "Nitin", "Gender": "Male", "Age":21}
print(d.items())
d1 = {key : value for key, value in d.items() if len(key) > 3} #dictnory concurrency
d2 = {i: i**2 for i in l}
print(d2)