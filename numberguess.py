import random

# jackpot = random.randint(1,10)

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

# while True:
#     num = int(input("Enter a positive number: "))
#     print(num)
#     if(not num > 0):
#         break

#SNAKE WATHER GUN GAME

while True:

    print("\n===== Snake Water Gun Game =====")
    print("1. Snake")
    print("2. Water")
    print("3. Gun")

    computer = random.choice([1, 2, 3])

    user = int(input("Enter your choice: "))

    if user not in [1, 2, 3]:
        print("Invalid Choice! Please enter only 1, 2, or 3.")
    if user == computer:
        print("Match Draw!")

    elif (user == 1 and computer == 2):
        print("🎉 You Win!")

    elif(user == 2 and computer == 3):
         print("🎉 You Win!")

    elif(user == 3 and computer == 1):
        print("🎉 You Win!")


    else:
        print("💻 Computer Wins!")

    # Computer Choice Print
    if computer == 1:
        print("Computer chose Snake")
    elif computer == 2:
        print("Computer chose Water")
    else:
        print("Computer chose Gun")

    # print("Cumputer choice: ",computer)

    choice = input("Play Again? (yes/no): ")

    if choice.lower() != "yes":
        print("Thanks for Playing 😊")
        break