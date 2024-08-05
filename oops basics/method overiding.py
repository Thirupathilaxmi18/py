class encap:
    def __init__(self,price,brand):
        self._price=price
        self._brand=brand
    def call(self):
        # self._price=500000
        # self._brand="TOYOTA"
        print(f"{self._price} \n{self._brand} ")
class encap2(encap):
    def call(self):
        self._price = 500000
        self._brand="TOYOTA"
        print(f"{self._price} \n{self._brand} ")
    def call2(self):
        print(f"{self._price} \n{self._brand} ")
ob=encap(200000,"TATA")
ob.call()
ob1=encap2(300000,"HYUDAI")
ob1.call()
ob1.call2()
