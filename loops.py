# i = 1
# x  = int(input("Enter the Range of Number: "))
# while(i <= x):

#     if(i % 2 == 0):
#      print(i)
#     #i = i + 1
#     i += 1

# print the sum of first n natural number

# n = int(input("Enter a Number: "))
# sum = 0

# while(n >= 1):
#     sum +=n
#     n = n-1
#     print(sum)

# print pattern using while loops

# n = 1
# while n<5:
#     print("*" * n)
#     n = n+1

# print table

# n = int(input("Enter a Number: "))
# i = 1
# while(i <= 10):
#     print(f"{n} * {i} = {n*i}")
#     i = i + 1

# foodlist = ["cake", "mango", "pizza"]
# for i in foodlist:
#     print(i)

# n = int(input("enter a number: "))
# i = 1
# for x in range(1,10):
#     print(f"{n} * {i} = {n*i}")
#     i = i + 1


# for i in range(1,11,1):
#     print(i*i)

# n = int(input("Enter a number: "))
# sum = 0
# for i in range(1,n+1):
#     sum +=i
#     print(sum)

# for i in range(1,10):
#     if(i == 5):
#         continue
#     print(i)

# Print countdown timer using for loops

import time
count = int(input("Enter the Counter Number: "))

print("\n Contdown Starts Now..")

for i in range(count, 0, -1):
    print(i)
    time.sleep(1)

print("\n 😍 Happy New Year..🎇🎆")