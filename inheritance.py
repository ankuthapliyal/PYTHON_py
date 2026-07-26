# class Employee:
#     def __init__(self,name, id):
#         self.name = name
#         self.id = id

#     def showdetails(self):
#         print("The name of empolyee: ",self.id,"is",self.name)


# class Programmer(Employee):
#     def showlenguage(self):
#         print("The default lenguage is python")

# e = Employee("Anurag",321)
# e.showdetails()
# p = Programmer("Rohit",324)
# p.showdetails()

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     # def persondetails(self):
#     #     print("Name : {}".format(self.name),"\nAge: {}".format(self.age))


# class Student(Person):
#     def __init__(self, name, age, rollno):
#         super().__init__(name, age)  #Parent Constructor call
#         # self.name = name
#         # self.age = age
#         self.rollno = rollno

#     def studentdetails(self):
#         print("Name: ",self.name,"\nAge: ",self.age,"\nRoll no:",self.rollno)
    

# s1 = Student("Rohit",19,3432)
# # s1.persondetails()
# s1.studentdetails()
# print(s1.name)

class Phone:

    def __init__(self, price, brand, camera):
        print("Inside Phone Constructor")

        self.__price = price
        self.brand = brand
        self.camera = camera


class SmartPhone(Phone):

    def __init__(self, price, brand, camera, os, ram):
        print("First call")
        super().__init__(price, brand, camera)

        self.os = os
        self.ram = ram

        print("Inside Smartphone Constructor")

    def display(self):
        # print("Brand: ",self.brand,"\nPrice: ",self._Phone__price,"\nCamera: ",self.camera,"\nOS: ",self.os,"\nRAM: ",self.ram)
        print("Brand :", self.brand)
        print("Price :", self._Phone__price)
        print("Camera:", self.camera)
        print("OS    :", self.os)
        print("RAM   :", self.ram)


s = SmartPhone(25000, "Samsung", "30MP", "Android", "8GB")

s.display()
