# class ATM:

#     def __init__(self):
#         self.__balance = 0

#     def deposit(self, amount):
#         self.__balance += amount

#     def show_balance(self):
#         print("Balance =", self.__balance)


# sbi = ATM()

# sbi.deposit(5000)
# sbi.show_balance()

# sbi.__balance = "dbjjys"  #new varable are create
# sbi.deposit(90000)
# sbi.show_balance()
# print(sbi.__balance)   # Error
# print("Total balance is: ",sbi._ATM__balance)


#GETTER AND SETTER

# class Student:

#     def __init__(self):
#         self.__marks = 0

#     def set_marks(self, marks):
#         if 0 <= marks <= 100:
#             self.__marks = marks
#         else:
#             print("Invalid Marks")

#     def get_marks(self):
#         return self.__marks


# s = Student()

# s.set_marks(90)
# print(s.get_marks())
# print("Student marks is : ",s._Student__marks)

#GETTER AND SETTER

class Persion:

    def __init__(self):
        self.__age = 20    ##instance variable:- It is kind of variable for which the value of the variable is diffrent for diffrent objects

    def get_age(self):
        return self.__age

    def set_age(self, nwage):
        if(nwage > 17):
            self.__age = nwage
        else:
            print("Adult")

p = Persion()
p.set_age(25)
print("Age is: ",p.get_age())
print(p._Persion__age)

#GETTER AND SETTER

# class MyClass:
#     def __init__(self, value):
#         self.value = value

#     def show(self):
#         print("Value is: ",self.value)

#     @property  #getter
#     def ten_value(self):
#         return 10 * self.value

#     @ten_value.setter
#     def ten_value(self, new_value):
#         self.value = new_value
    


# obj = MyClass(10)
# obj.show()
# obj.ten_value = 20
# print("change vlaue: ",obj.ten_value)
# obj.show()

# class BankAccount:

#     def __init__(self):
#         self.__balance = 1000

#     def deposit(self, amount):
#         self.__balance += amount

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Insufficient Balance")

#     def get_balance(self):
#         return self.__balance


# sbi = BankAccount()

# sbi.deposit(500)
# sbi.withdraw(200)

# print(sbi.get_balance())
# print(sbi._BankAccount__balance)