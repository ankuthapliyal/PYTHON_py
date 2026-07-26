#1 SINGLE LEVEL
# class Phone:
#     def __init__(self, price, brand, camera):
#         self.price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print("Buying a phone")
#         print("Brand :", self.brand)
#         print("Price :", self.price)
#         print("Camera:", self.camera)

#     def return_phone(self):
#         print("Returning a phone")

# class Smartphone(Phone):
#    pass


# Smartphone(10000,"Apple", "15PX").buy()

# 2 #MULTILEVIL INHERITANCE

# class Product:
#     def review(self):
#         print("Product customer review")

# class Phone(Product):

#     def __init__(self,price, brand, camera):
#         print("Inside Phone cunstructor")
#         self.price = price
#         self.brand = brand
#         self.camera = camera
        
#     def buy(self):
#         print("Buying a phone...")
#         print("Brand :", self.brand)
#         print("Price :", self.price)
#         print("Camera:", self.camera)

# class SmartPhone(Phone):

#     def internet(self):
#         print("Browsing Internet...")


# class AndroidPhone(SmartPhone):

#     def apps(self):
#         print("Running Android Apps")


# a = AndroidPhone(25000,"Samsung", "50Px")
# s = SmartPhone(30000, "Nothing", "60Px")

# s.review()
# a.review()
# s.buy()
# s.brand = "Redmi"
# print(i.brand)
# a.buy()
# a.internet()
# a.apps()

#3 HIERARCHICAL INHERITANCE

# class Phone:

#     def __init__(self, price, brand):
#         self.price = price
#         self.brand = brand

#     def buy(self):
#         print("Buying a Phone")
#         print("Brand :", self.brand)
#         print("Price :", self.price)


# class AndroidPhone(Phone):

#     def apps(self):
#         print("Running Android Apps")


# class IPhone(Phone):

#     def facetime(self):
#         print("Using FaceTime")


# # Android Object
# a = AndroidPhone(25000, "Samsung")

# # iPhone Object
# i = IPhone(80000, "Apple")


# print("----- Android -----")
# a.buy()
# a.apps()

# print("\n----- iPhone -----")
# i.buy()
# i.facetime()

# 4 # MULTIPLE INHERITANCE

class Phone:

    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

    def call(self):
        print("Calling...")
        print("Brand:", self.brand)
        print("Price:", self.price)


class Camera:

    def click(self):
        print("Taking Photo...")


class SmartPhone(Phone, Camera):

    def internet(self):
        print("Browsing Internet")


s = SmartPhone(100000, "Apple")

s.call()       # Phone
s.click()      # Camera
s.internet()   # SmartPhone 