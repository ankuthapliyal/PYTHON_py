# class Employee:

#     def __init__(self, name, salary, password):

#         # Public Member
#         self.name = name

#         # Protected Member
#         self._salary = salary

#         # Private Member
#         self.__password = password

#     # Public Method
#     def show_details(self):
#         print("Name:", self.name)
#         print("Salary:", self._salary)
#         print("Password:", self.__password)


# class Manager(Employee):

#     def __init__(self, name, salary, password, department):
#         super().__init__(name, salary, password)
#         self.department = department

#     def manager_details(self):
#         print("Department:", self.department)

#         # Protected member access
#         print("Salary:", self._salary)

#         # Private member access (Directly nahi hoga)
#         # print(self.__password)   Error

#         # Getter method se ya Name Mangling se access kar sakte hain
#         print("Password:", self._Employee__password)


# emp = Manager("Anku", 50000, "abc@123", "CSE ER")

# print("----- Public -----")
# print(emp.name)

# print("\n----- Protected -----")
# print(emp._salary)      # Chalega, lekin recommended nahi

# print("\n----- Private -----")
# # print(emp.__password)   # ❌ Error

# print(emp._Employee__password)   #  Name Mangling

# print("\n----- Manager Details -----")
# emp.manager_details()
