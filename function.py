# def calculategmean(a, b):
#     mean = (a*b)/(a+b)
#     print(mean)
    
# def isgreater(a, b):  
#     if a>b:
#         print("first number greater")
#     elif a == b:
#         print("number are equal")
#     else:
#         print("Second number is greater")
# a = 5
# b = 6
# isgreater(a, b)
# calculategmean(a, b)
# a = 9
# b = 8
# isgreater(a, b)
# calculategmean(a,b)
# isgreater(8, 7)
# calculategmean(8, 7)
# isgreater(4, 4)
# calculategmean(4, 4)
# print(ord('z'))

# def is_even(n):
#     if type(n) == int:
 
#         if(n%2==0):
#             print("number is even") 
#         else:
#             print("number is odd")
#     else:
#         print("not allowed")
        
# is_even(9.9)

# def flexi(*num):  # impement tupe *
#     product = 1
#     print(num)
#     print(type(num))
#     for i in num:
#         product = product * i
#     print(product)

# flexi(1,2,3,4,5)

# function are object
# def f(num):
#     return num**2

# print(f(2))
# x = f # function as a object 
# print(x(4)) 
# # del f     # python are delete function 
# # print(f(2))
# print(x(3))  # like call by value and refrence & data type
# l = [1,2,3,4,x]
# print(l)
# l1 = [1,2,3,4,x(5)]
# print(l)

#Docstring:- definition of funnction,method,class,or module
# def square(n):
#     """Takes in a number n, returns the square of n
#     """
#     print(n**2)

# square(5)
# print(square.__doc__)

#'IS' AND '==' comaprarison operator

a = [1, 2, 3]  
b = [1, 2, 3]

print(a is b)  # compare to exact location of object in memory
print(a==b)    # compare the value