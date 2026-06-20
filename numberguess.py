# import random

# jackpot = random.randint(1,100)

# guess = int(input("Guess the number: "))
# counter = 1

# while(guess != jackpot):
#     if(guess < jackpot):
#         print(" You Guess low")
#     else:
#         print("You Guess high")

#     guess = int(input("Guess the number: "))
#     counter += 1

# print("Currect Number")
# print("You took", counter,"attempts")

# rows = int(input("Enter the number of rows: "))

# for i in range(1,rows+1):
#     for j in range(0, i):
#         print("*", end = " ")
#     print(" ")

# Do while loop 

while True:
    num = int(input("Enter a positive number: "))
    print(num)
    if(not num > 0):
        break