# a = input("Enter the number: ")
# print("Multiplicatioon table of {} is: ".format(a))

# try:
#     for i in range(1,11):
#         print("{} * {} = {}".format(int(a),i, int(a)*i))
# except Exception as e:
#     print("Invalid input!",e)

# print("Some imp lines of code")
# print("End of Program")

# try:
#     num = int(input("Enter a number: "))
#     print(10 / num)

# except ValueError:
#     print("Please enter a valid number.")
    
# except ZeroDivisionError:
#     print("Cannot divide by zero.")

# try:
#     arr = [2,3,4,6,8,9]
#     index = int(input("Enter the index:"))
#     print("Element = ",arr[index])

# except IndexError:
#     print("Index out of range.")

# except ValueError:
#     print("Please enter a valid number.")

# except Exception as e:
#     print("Error:", e)
    
# finally:
#     print("Program Ended")


#Coustm error

# a = int(input("Enter any vlaue between 5 and 9: "))

# if(a<5 or a>9):
#     raise ValueError("Value should be between 5 and 9: ")

# a = 305
# b = 5698

# print("A") if a>b else print("=") if a==b else print("B") # shorted code format

# c = print(9) if a<b else 0
# print(c)