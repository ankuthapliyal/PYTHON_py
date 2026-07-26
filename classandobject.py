# class Student:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print("Name:",self.name)
#         print("Age:",self.age)

# s1 = Student("Anku",20)
# s1.display()


# class Atm:

#     def __init__(self):
#         self.pin = ""       ##instance variable:- It is kind of variable for which the value of the variable is diffrent for diffrent objects
#         self.balance = 0
    
#         # self.menu()
        
#     def menu(self):
#      while True:

#         user_input = input("""
# ====================================
#         SBI ATM
# ====================================
# 1. Create PIN
# 2. Deposit Money
# 3. Withdraw Money
# 4. Check Balance
# 5. Exit
# Enter your choice: """)
        
#         if user_input == "1":
#             self.create_pin()

#         elif user_input == "2":
#             self.deposit()

#         elif user_input == "3":
#             self.withdraw()

#         elif user_input == "4":
#             self.check_balance()

#         elif user_input == "5":
#             print("Thank You for using SBI ATM.")
#             break
        
#         else:
#              print("Invalid Choice! Please try again.")
    
#     def create_pin(self):
#          self.pin = input("Create your 4-digit PIN: ")
#          print("PIN created successfully!")
    
#     def deposit(self):
#         if self.pin == "":
#             print("Please create your PIN first:")
#             return
        
#         temp = input("Enter your PIN: ")

#         if temp == self.pin:
#             amount = int(input("Enter amount to deposit: "))
#             self.balance = self.balance + amount
#             print("Deposit successfully")
#         else:
#             print("Incorrect PIN ")

#     def withdraw(self):
#         if self.pin == "":
#             print("Please create your PIN first:")
#             return
        
#         temp = input("Enter your PIN: ")

#         if temp == self.pin:
#             amount = int(input("Enter amount to withdraw: "))
#             if amount <=  self.balance:
#                 self.balance = self.balance - amount
#                 print("Withdraw successfully")
#                 print("Remaining balance =",self.balance)
#             else:
#                 print("Insufficient Balance")
#         else:
#             print("Incorrect PIN")
    
#     def check_balance(self):
#          if self.pin == "":
#             print("Please create your PIN first:")
#             return
         
#          temp = input("Enter your PIN: ")

#          if temp == self.pin:
#              print("Current Balance =",self.balance)
#          else:
#              print("Incurrect PIN.")

# sbi = Atm()
# sbi.menu()


class Fraction:

    def __init__(self, n, d):
        self.num = n
        self.den = d

    def __str__(self):
        return "{}/{}".format(self.num,self.den)
    
    def __add__(self, other):
        temp_num = self.num * other.den + other.num * self.den
        temp_den = self.den * other.den
        return "{}/{}".format(temp_num, temp_den)
    
    def __sub__(self, other):
        temp_num = self.num * other.den - other.num * self.den
        temp_den = self.den * other.den
        return "{}/{}".format(temp_num, temp_den)
    
    def __mul__(self, other):
        temp_num = self.num * other.num 
        temp_den = self.den * other.den
        return "{}/{}".format(temp_num, temp_den)
    
    def __truediv__(self, other):
        temp_num = self.num * other.den
        temp_den = self.den * other.num
        return "{}/{}".format(temp_num, temp_den)

    def __mod__(self, other):
            return "{}/{}".format(self.num, other.den)


x = Fraction(2,4) 
print(x) 
y = Fraction(4,7)
print(y)
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(17%4)