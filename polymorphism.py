#METHOD OVERRIDING

class Phone:
    def __init__(self,price, brand, camera):
        print("Inside Phone Constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone: ",self._Phone__price,"Rupes")

class SmartPhone(Phone):
    
    def buy(self):
        print("Buying a smartphone")
        super().buy()  #Perent method call

s = SmartPhone(25000,"Apple","30mp")
s.buy()