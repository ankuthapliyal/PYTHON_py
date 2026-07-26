class Customer:

    # def __init__(self,name,gender):
    #     self.name = name
    #     self.gender = gender

# def greet(customer):
#     if customer.gender == "Male":
#         print("hello",customer.name,"sir")
#     else:
#         print("Hello",customer.name,"ma'am'")
    
#     cust2 = Customer("Nitish","Male")

#     return cust2

# # Customer()  # address is loess then creat object cust reference varible
# cust = Customer("Ankita","Female")    # cust a is a reference variable 
# # print(id(cust))
# print(cust.name,cust.gender)
# new_cust = greet(cust)
# print(new_cust.name,new_cust.gender)
       
        def __init__(self,name):
                self.name = name

def greet(customer):
        print(id(customer))
        customer.name = "Nitish"
        # print(customer.name)
        # print(id(customer))


cust = Customer("ankita")   # cust a is a refrence variable 
print(id(cust))
greet(cust)
print(cust.name)      # class ke objects are alse mutable like list ,dict,and sets

#COLLECTION OF OBJECT
#         def __init__(self,name,age):
#                 self.name = name
#                 self.age = age

#         def inrto(self):
#                 # print("I am {} and I am {} year old".format("anku thapliyal",20))
#                 print("I am",self.name,"and I am",self.age,"year old")
# c1 = Customer("Rohit",23)
# c2 = Customer("Mohit",24)
# c3 = Customer("Neha",22)

# L = [c1,c2,c3]

# for i in L:
# #         print(i.name,i.age)
#           i.inrto()
# c1.inrto()
# c2.inrto()
# c3.inrto()