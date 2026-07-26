# class Atm:

#     __counter = 0

#     def __init__(self):
#         self.pin = ""
#         self.balance = 0
#         self.sno = Atm.__counter
#         Atm.counter += 1

#     @staticmethod
#     def get_counter():
#         return Atm.__counter
    
#     @staticmethod
#     def set_counter(new):
#         if(type(new) == int):
#             Atm.__counter = new
#         else:
#             print("Not Allowed")
    

# sbi = Atm()
# c1 = Atm()
# c2 = Atm()
# c3 = Atm()

# print(sbi.sno,c1.sno,c2.sno,c3.sno,c2.counter,c3.counter,Atm.counter)
# print("Counter",Atm.get_counter())
# Atm.set_counter(19)
# print("New Counter:",Atm.get_counter())

#STATIC METHOD

#     def __init__(self,num):
#         self.num = num

#     def addtonum(self, n):
#         self.num = self.num + n

#     @staticmethod
#     def add(a, b):
#         return a + b


# a = Atm(7)
# print(a.num)
# a.addtonum(5)
# print(a.num)

# print(a.add(3,5))
# print(Atm.add(4,4))


#STATIC/CLASS VARIABLE AND INSTANT VARIABLE

# class Employee:
#     __companyName = "Apple"
#     __noofEmployees = 0

#     def __init__(self,name):
#         self.name = name
#         self.raise_amount = 0.04
#         Employee.__noofEmployees += 1

#     def showDetails(self):
#         print(f"the name of the Employee is {self.name} and the raise amount in {self.__noofEmployees} sized {self.__companyName} is {self.raise_amount}")


# emp1 = Employee("Rohit")
# emp1.companyName = "Apple India"
# emp1.raise_amount = 0.05
# emp1.showDetails()
# emp2 = Employee("Anurag")
# emp2.companyName = "Google"
# emp2.showDetails()

#CLASS METHOD
class Employee:
    company = "Apple"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")

    @classmethod
    def changecompany(cls, newcompany):
        cls.company = newcompany


e1 = Employee()
e1.name = "Anku"
e1.show()
e1.changecompany("Google")
e1.show()
print(Employee.company)