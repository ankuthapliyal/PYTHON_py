class Customer:   # aggregation has a relationship of classes

    def __init__(self,name,gender,address):
        self.name = name
        self.gender = gender
        self.address = address

    def edit_profile(self,new_name,new_gender,new_city,new_pin,new_state):
        self.name = new_name
        self.gender = new_gender
        self.address.change_address(new_city,new_pin,new_state)

class Address:

    def __init__(self,city,pincode,state):
        self.city = city
        self.pincode = pincode
        self.state = state

    def change_address(self,new_city,new_pin,new_state):
        self.city = new_city
        self.pincode = new_pin
        self.state = new_state


add = Address("Chamoli",246481,"Uttarakhand")
cust = Customer("mohit","Male",add)
print(cust.name,cust.gender,cust.address.state)

cust.edit_profile("Ankita","Female",123445,"Gurgaon","Haryana")
print(cust.name,cust.gender,cust.address.state)